#!/usr/bin/env python3
"""Brand-graphics plan validator (standard library only).

Two commands:

  prepare  Validate a plan.json and the reference files it names, then write a
           NEW receipt.json holding an immutable-by-convention SHA256 snapshot
           of the plan and each existing reference. Refuses to overwrite an
           existing receipt.

  check    Re-validate that the plan and references are unchanged since the
           receipt, that an execution record links back to the receipt hash,
           that the actual saved generation-tool argument JSON uses the planned
           reference paths, that declared output files exist, and that the
           review records every required criterion with a disposition and
           evidence (pass / fix / unverified). Release is blocked while any
           criterion is fix or unverified.

What this validator can and cannot do
-------------------------------------
It verifies STRUCTURAL records only: that files exist, that hashes match a
recorded snapshot, that references cross-link, and that a review is complete.
It CANNOT prove that a generation tool was truly executed, cannot prove
authorship order, and does not judge artistic quality. SHA256 snapshots and
timestamps are integrity/convenience records, NOT cryptographic proof that
planning preceded generation.
"""

import argparse
import hashlib
import json
import os
import sys

RECIPES_REL = os.path.join("..", "design-system", "recipes.json")
REVIEW_DISPOSITIONS = ("pass", "fix", "unverified")
RELEASE_BLOCKING = ("fix", "unverified")


class ValidationError(Exception):
    """Raised for any structural validation failure."""


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def _load_json(path):
    if not os.path.isfile(path):
        raise ValidationError("missing file: %s" % path)
    try:
        with open(path, "r", encoding="utf-8") as fh:
            return json.load(fh)
    except ValueError as exc:
        raise ValidationError("invalid JSON in %s: %s" % (path, exc))


def _sha256_file(path):
    if not os.path.isfile(path):
        raise ValidationError("missing file: %s" % path)
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _load_recipes(base_dir):
    """Load recipes.json relative to this validator's directory."""
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.normpath(os.path.join(here, RECIPES_REL))
    if not os.path.isfile(path):
        # fall back to a path relative to the plan's base dir
        path = os.path.normpath(os.path.join(base_dir, "..", "design-system", "recipes.json"))
    return _load_json(path)


def _resolve(base_dir, rel):
    return os.path.normpath(os.path.join(base_dir, rel))


# ---------------------------------------------------------------------------
# plan validation (shared by prepare and check)
# ---------------------------------------------------------------------------

def validate_plan(plan, recipes, base_dir):
    """Validate plan structure against the recipe routes/families. Returns the
    resolved (route, family, requires_evidence) tuple."""
    for key in ("plan_version", "source", "route", "recipe_family",
                "references", "purpose", "composition", "palette"):
        if key not in plan:
            raise ValidationError("plan missing required key: %s" % key)

    routes = recipes.get("routes", {})
    route = plan["route"]
    if route not in routes:
        raise ValidationError("unknown route: %s" % route)

    route_spec = routes[route]
    family = plan["recipe_family"]
    if family not in route_spec.get("valid_families", []):
        raise ValidationError(
            "recipe_family %r is not valid for route %r" % (family, route))

    fam_spec = None
    for f in recipes.get("families", []):
        if f["id"] == family:
            fam_spec = f
            break
    if fam_spec is None:
        raise ValidationError("recipe_family %r not defined in recipes" % family)

    references = plan["references"]
    if not isinstance(references, list):
        raise ValidationError("plan.references must be a list")

    requires_evidence = fam_spec.get("requires_evidence", False)

    # solid-field: no imagegen / reference attachment required; empty list ok.
    if route == "solid-field":
        # references optional; if present still validated for structure below.
        pass
    elif route_spec.get("requires_reference"):
        if len(references) < 1:
            raise ValidationError(
                "route %r family %r requires at least one reference" % (route, family))

    # per-reference structure + existence
    for i, ref in enumerate(references):
        for rk in ("path", "decision", "role"):
            if rk not in ref:
                raise ValidationError("reference[%d] missing %r" % (i, rk))
        if ref["decision"] not in ("preserve", "change", "free"):
            raise ValidationError(
                "reference[%d] decision must be preserve/change/free" % i)
        rp = _resolve(base_dir, ref["path"])
        if not os.path.isfile(rp):
            raise ValidationError("reference file does not exist: %s" % ref["path"])

    # evidence source rules
    source = plan.get("source", {})
    if requires_evidence:
        ev = source.get("source")
        if not ev or ev == "none":
            raise ValidationError(
                "route %r requires a real (non-none) source/evidence" % route)

    if plan["plan_version"] != 1 or not str(plan["purpose"]).strip():
        raise ValidationError("unsupported plan version or empty purpose")
    if not isinstance(source, dict) or any(not source.get(k) or source[k] == "none" for k in ("source", "ref")):
        raise ValidationError("authorized design source and ref are required for every route")
    if requires_evidence and plan.get("evidence_source", "none") == "none":
        raise ValidationError("product-proof requires a separate evidence_source")

    # composition dimensions
    comp = plan["composition"]
    for ck in ("width", "height"):
        if not isinstance(comp.get(ck), int) or comp[ck] <= 0:
            raise ValidationError("composition.%s must be a positive int" % ck)

    for key in ("copy_zones", "logo_zones"):
        if not isinstance(comp.get(key), list):
            raise ValidationError("composition must declare " + key + " (empty is allowed)")
        for zone in comp[key]:
            if any(not isinstance(zone.get(k), (int, float)) for k in ("x", "y", "w", "h")):
                raise ValidationError("zone coordinates must be numeric")
            if zone["x"] < 0 or zone["y"] < 0 or zone["w"] <= 0 or zone["h"] <= 0 or zone["x"] + zone["w"] > comp["width"] or zone["y"] + zone["h"] > comp["height"]:
                raise ValidationError("composition zone outside canvas")

    # palette roles + exclusions present
    pal = plan["palette"]
    if "roles" not in pal or not isinstance(pal["roles"], dict):
        raise ValidationError("palette.roles must be an object")
    if "exclusions" not in pal or not isinstance(pal["exclusions"], list):
        raise ValidationError("palette.exclusions must be a list")

    return route, family, requires_evidence


# ---------------------------------------------------------------------------
# prepare
# ---------------------------------------------------------------------------

def cmd_prepare(plan_path, receipt_path):
    base_dir = os.path.dirname(os.path.abspath(plan_path))
    plan = _load_json(plan_path)
    recipes = _load_recipes(base_dir)
    validate_plan(plan, recipes, base_dir)

    if os.path.exists(receipt_path):
        raise ValidationError(
            "receipt already exists (immutable by convention, refusing to "
            "overwrite): %s" % receipt_path)

    ref_hashes = {}
    for ref in plan["references"]:
        rp = _resolve(base_dir, ref["path"])
        ref_hashes[ref["path"]] = _sha256_file(rp)

    receipt = {
        "receipt_version": 1,
        "note": ("Immutable by convention. Structural snapshot only. Not proof "
                 "of tool execution, authorship order, or quality."),
        "plan_path": os.path.basename(plan_path),
        "plan_sha256": _sha256_file(plan_path),
        "reference_sha256": ref_hashes,
    }
    with open(receipt_path, "x", encoding="utf-8") as fh:
        json.dump(receipt, fh, indent=2, sort_keys=True)
        fh.write("\n")
    return receipt


# ---------------------------------------------------------------------------
# check
# ---------------------------------------------------------------------------

def _receipt_sha256(receipt_path):
    return _sha256_file(receipt_path)


def cmd_check(plan_path, receipt_path, execution_path, review_path):
    base_dir = os.path.dirname(os.path.abspath(plan_path))
    plan = _load_json(plan_path)
    recipes = _load_recipes(base_dir)
    route, family, requires_evidence = validate_plan(plan, recipes, base_dir)

    receipt = _load_json(receipt_path)

    # 1. plan unchanged since receipt
    if _sha256_file(plan_path) != receipt.get("plan_sha256"):
        raise ValidationError("plan hash differs from receipt (plan changed after prepare)")

    # 2. references unchanged since receipt
    recorded = receipt.get("reference_sha256", {})
    current_refs = {r["path"] for r in plan["references"]}
    if set(recorded) != current_refs:
        raise ValidationError(
            "reference set differs from receipt (references added/removed after prepare)")
    for ref in plan["references"]:
        rp = _resolve(base_dir, ref["path"])
        if _sha256_file(rp) != recorded.get(ref["path"]):
            raise ValidationError("reference changed after prepare: %s" % ref["path"])

    # 3. execution record links to receipt hash
    execution = _load_json(execution_path)
    expect = _receipt_sha256(receipt_path)
    if execution.get("receipt_sha256") != expect:
        raise ValidationError(
            "execution record receipt_sha256 does not match actual receipt hash")

    method = execution.get("method", "reuse" if "reuse" in execution else "direct" if route == "solid-field" else "generation")
    if method not in ("generation", "direct", "reuse"):
        raise ValidationError("unknown execution method")
    is_generation = method == "generation"
    if method == "direct":
        source_file = execution.get("source_artifact")
        if not source_file or not os.path.isfile(_resolve(base_dir, source_file)):
            raise ValidationError("direct composition needs its editable source_artifact")

    if is_generation:
        # 4. actual saved generation-tool argument JSON uses planned reference paths
        args_ref = execution.get("tool_args_path")
        if not args_ref:
            raise ValidationError("execution record missing tool_args_path for generation route")
        args_path = _resolve(base_dir, args_ref)
        tool_args = _load_json(args_path)
        actual_refs = tool_args.get("referenced_image_paths") or tool_args.get("reference_images") or tool_args.get("references") or []
        actual_set = {os.path.realpath(_resolve(base_dir, p)) for p in actual_refs}
        planned_set = {os.path.realpath(_resolve(base_dir, r["path"])) for r in plan["references"]}
        if not planned_set:
            raise ValidationError("generation route has no planned references")
        if actual_set != planned_set:
            raise ValidationError(
                "actual tool reference paths %s do not match planned %s"
                % (sorted(actual_set), sorted(planned_set)))
    else:
        # solid-field: must NOT require imagegen/reference attachment.
        if execution.get("tool_args_path"):
            # allowed to be absent; if present it's fine but not required
            pass

    # non-generation reuse: explicit source artifact check
    if method == "reuse":
        reuse = execution.get("reuse", {})
        src_art = reuse.get("source_artifact")
        if not src_art:
            raise ValidationError("non-generation reuse must name a source_artifact")
        if not os.path.isfile(_resolve(base_dir, src_art)):
            raise ValidationError("reuse source_artifact does not exist: %s" % src_art)

    # 5. output files exist
    outputs = execution.get("outputs", [])
    if not outputs:
        raise ValidationError("execution record lists no outputs")
    for out in outputs:
        op = _resolve(base_dir, out)
        if not os.path.isfile(op):
            raise ValidationError("declared output file missing: %s" % out)

    # 6. review: each required criterion has a disposition + evidence
    review = _load_json(review_path)
    criteria = review.get("criteria")
    if not isinstance(criteria, list) or not criteria:
        raise ValidationError("review must list criteria")
    required = {"hierarchy", "craft"} | {
        r["decision"] + ":" + r["role"] for r in plan["references"] if r["decision"] != "free"
    }
    if not required.issubset({c.get("name") for c in criteria}):
        raise ValidationError("review missing required hierarchy/craft/reference criteria")
    blocking = []
    for i, crit in enumerate(criteria):
        name = crit.get("name")
        disp = crit.get("disposition")
        evidence = crit.get("evidence")
        if not name:
            raise ValidationError("review criterion[%d] missing name" % i)
        if disp not in REVIEW_DISPOSITIONS:
            raise ValidationError(
                "review criterion %r disposition must be one of %s"
                % (name, REVIEW_DISPOSITIONS))
        if not isinstance(evidence, str) or not evidence.strip():
            raise ValidationError("review criterion %r missing evidence" % name)
        if disp in RELEASE_BLOCKING:
            blocking.append((name, disp))

    result = {
        "ok": not blocking,
        "route": route,
        "recipe_family": family,
        "blocking": blocking,
        "note": ("Structural verification only. Cannot prove tool execution, "
                 "authorship order, or artistic quality."),
    }
    if blocking:
        raise ValidationError(
            "release blocked by unresolved review criteria: %s"
            % ", ".join("%s=%s" % (n, d) for n, d in blocking))
    return result


# ---------------------------------------------------------------------------
# cli
# ---------------------------------------------------------------------------

def main(argv=None):
    parser = argparse.ArgumentParser(description="Brand-graphics plan validator")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("prepare", help="validate plan + references, write new receipt")
    p.add_argument("--plan", required=True)
    p.add_argument("--receipt", required=True)

    c = sub.add_parser("check", help="verify hashes, execution link, outputs, review")
    c.add_argument("--plan", required=True)
    c.add_argument("--receipt", required=True)
    c.add_argument("--execution", required=True)
    c.add_argument("--review", required=True)

    args = parser.parse_args(argv)
    try:
        if args.command == "prepare":
            cmd_prepare(args.plan, args.receipt)
            print("prepare OK: receipt written to %s" % args.receipt)
        elif args.command == "check":
            result = cmd_check(args.plan, args.receipt, args.execution, args.review)
            print("check OK: %s" % json.dumps(result, sort_keys=True))
    except ValidationError as exc:
        print("VALIDATION FAILED: %s" % exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
