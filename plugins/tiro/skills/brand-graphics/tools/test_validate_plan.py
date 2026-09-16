#!/usr/bin/env python3
"""Tests for the brand-graphics plan validator.

Run:  python3 -m unittest discover -s tools -p 'test_*.py'
   or  python3 tools/test_validate_plan.py

These tests build fixtures in a temp directory. The validator loads recipes.json
from its own directory (../design-system/recipes.json), so tests use the real
recipe route/family definitions shipped with the skill.
"""

import json
import os
import shutil
import tempfile
import unittest

import validate_plan as vp


def _write(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        if isinstance(obj, (dict, list)):
            json.dump(obj, fh, indent=2)
        else:
            fh.write(obj)


class Base(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.dir)
        self.plan_path = os.path.join(self.dir, "plan.json")
        self.receipt_path = os.path.join(self.dir, "receipt.json")
        self.exec_path = os.path.join(self.dir, "execution.json")
        self.review_path = os.path.join(self.dir, "review.json")
        self.args_path = os.path.join(self.dir, "tool_args.json")
        # a reference image file
        self.ref_rel = "ref.png"
        _write(os.path.join(self.dir, self.ref_rel), "PNGDATA-A")

    # ---- plan builders -------------------------------------------------
    def proof_plan(self):
        return {
            "plan_version": 1,
            "source": {"source": "handoff-x", "ref": "abc123"},
            "route": "product-proof",
            "evidence_source": "verified fixture screenshot",
            "recipe_family": "product-proof-field",
            "references": [
                {"path": self.ref_rel, "decision": "preserve", "role": "product crop"}
            ],
            "purpose": "make the viewer trust the capture",
            "composition": {
                "width": 1600, "height": 900,
                "copy_zones": [{"name": "c", "x": 0, "y": 0, "w": 400, "h": 200}],
                "logo_zones": [{"name": "l", "x": 20, "y": 20, "w": 120, "h": 40}],
            },
            "palette": {"roles": {"bg": "stone"}, "exclusions": ["neon"]},
        }

    def solid_plan(self):
        return {
            "plan_version": 1,
            "source": {"source": "authorized-guide", "ref": "abc123"},
            "route": "solid-field",
            "recipe_family": "solid-brand-field",
            "references": [],
            "purpose": "let the logo and title carry the message",
            "composition": {
                "width": 1600, "height": 900,
                "copy_zones": [{"name": "c", "x": 0, "y": 0, "w": 400, "h": 200}],
                "logo_zones": [{"name": "l", "x": 20, "y": 20, "w": 120, "h": 40}],
            },
            "palette": {"roles": {"field": "brand-primary"}, "exclusions": ["gradient"]},
        }

    def ambient_plan(self):
        return {
            "plan_version": 1,
            "source": {"source": "authorized-guide", "ref": "abc123"},
            "route": "brand-graphic",
            "recipe_family": "ambient-atmosphere",
            "references": [
                {"path": self.ref_rel, "decision": "preserve", "role": "mood field"}
            ],
            "purpose": "set a calm mood behind a section",
            "composition": {
                "width": 1600, "height": 900,
                "copy_zones": [{"name": "c", "x": 0, "y": 0, "w": 400, "h": 200}],
                "logo_zones": [],
            },
            "palette": {"roles": {"field": "brand-primary"}, "exclusions": ["neon"]},
        }

    # ---- record builders ----------------------------------------------
    def good_review(self):
        with open(self.plan_path) as f:
            refs = json.load(f)["references"]
        base = {"criteria": [
            {"name": "preserve:product crop", "disposition": "pass",
             "evidence": "crop present unchanged in output at master and thumb"},
            {"name": "hierarchy", "disposition": "pass",
             "evidence": "focal event reads first; release zone usable"},
            {"name": "craft", "disposition": "pass",
             "evidence": "edges hold at thumbnail"},
        ]}

        base["criteria"] = [c for c in base["criteria"] if c["name"] in ("hierarchy", "craft")]
        base["criteria"] += [{"name": r["decision"]+":"+r["role"], "disposition":"pass", "evidence":"reference and output compared at master and thumbnail"} for r in refs if r["decision"] != "free"]
        return base

    def execution_record(self, receipt_hash, **extra):
        rec = {
            "receipt_sha256": receipt_hash,
            "outputs": ["out.png"],
            "source_artifact": "composition.svg",
        }
        _write(os.path.join(self.dir, "composition.svg"), "<svg/>")
        rec.update(extra)
        return rec

    def prepare_ok(self, plan):
        _write(self.plan_path, plan)
        return vp.cmd_prepare(self.plan_path, self.receipt_path)


class PrepareTests(Base):
    def test_prepare_invented_recipe_fails(self):
        plan = self.proof_plan()
        plan["recipe_family"] = "totally-made-up"
        _write(self.plan_path, plan)
        with self.assertRaises(vp.ValidationError):
            vp.cmd_prepare(self.plan_path, self.receipt_path)

    def test_prepare_missing_reference_fails(self):
        plan = self.proof_plan()
        plan["references"][0]["path"] = "does-not-exist.png"
        _write(self.plan_path, plan)
        with self.assertRaises(vp.ValidationError):
            vp.cmd_prepare(self.plan_path, self.receipt_path)

    def test_prepare_proof_without_evidence_fails(self):
        plan = self.proof_plan()
        plan["source"] = {"source": "none", "ref": "none"}
        _write(self.plan_path, plan)
        with self.assertRaises(vp.ValidationError):
            vp.cmd_prepare(self.plan_path, self.receipt_path)

    def test_prepare_refuses_overwrite(self):
        self.prepare_ok(self.proof_plan())
        with self.assertRaises(vp.ValidationError):
            vp.cmd_prepare(self.plan_path, self.receipt_path)


class CheckPositiveTests(Base):
    def test_proof_flow_passes(self):
        plan = self.proof_plan()
        receipt = self.prepare_ok(plan)
        rhash = vp._sha256_file(self.receipt_path)
        _write(self.args_path, {"reference_images": [self.ref_rel]})
        _write(os.path.join(self.dir, "out.png"), "OUT")
        _write(self.exec_path, self.execution_record(
            rhash, tool_args_path="tool_args.json"))
        _write(self.review_path, self.good_review())
        result = vp.cmd_check(self.plan_path, self.receipt_path,
                              self.exec_path, self.review_path)
        self.assertTrue(result["ok"])

    def test_solid_flow_passes_without_imagegen(self):
        plan = self.solid_plan()
        self.prepare_ok(plan)
        rhash = vp._sha256_file(self.receipt_path)
        _write(os.path.join(self.dir, "out.png"), "OUT")
        _write(self.exec_path, self.execution_record(rhash))  # no tool_args_path
        _write(self.review_path, {"criteria": [
            {"name": "hierarchy", "disposition": "pass",
             "evidence": "logo+title carry message; whitespace usable"},
            {"name": "craft", "disposition": "pass", "evidence": "clean field"},
        ]})
        result = vp.cmd_check(self.plan_path, self.receipt_path,
                              self.exec_path, self.review_path)
        self.assertTrue(result["ok"])

    def test_ambient_flow_passes(self):
        plan = self.ambient_plan()
        self.prepare_ok(plan)
        rhash = vp._sha256_file(self.receipt_path)
        _write(self.args_path, {"reference_images": [self.ref_rel]})
        _write(os.path.join(self.dir, "out.png"), "OUT")
        _write(self.exec_path, self.execution_record(
            rhash, tool_args_path="tool_args.json"))
        _write(self.review_path, self.good_review())
        result = vp.cmd_check(self.plan_path, self.receipt_path,
                              self.exec_path, self.review_path)
        self.assertTrue(result["ok"])


class CheckNegativeTests(Base):
    def _base_generation_setup(self):
        plan = self.proof_plan()
        self.prepare_ok(plan)
        rhash = vp._sha256_file(self.receipt_path)
        _write(self.args_path, {"reference_images": [self.ref_rel]})
        _write(os.path.join(self.dir, "out.png"), "OUT")
        _write(self.exec_path, self.execution_record(
            rhash, tool_args_path="tool_args.json"))
        _write(self.review_path, self.good_review())
        return rhash

    def test_changed_plan_after_prepare_fails(self):
        self._base_generation_setup()
        # mutate the plan on disk after prepare
        plan = self.proof_plan()
        plan["purpose"] = "different purpose"
        _write(self.plan_path, plan)
        with self.assertRaises(vp.ValidationError):
            vp.cmd_check(self.plan_path, self.receipt_path,
                         self.exec_path, self.review_path)

    def test_changed_reference_after_prepare_fails(self):
        self._base_generation_setup()
        _write(os.path.join(self.dir, self.ref_rel), "PNGDATA-MUTATED")
        with self.assertRaises(vp.ValidationError):
            vp.cmd_check(self.plan_path, self.receipt_path,
                         self.exec_path, self.review_path)

    def test_wrong_actual_reference_inputs_fails(self):
        self._base_generation_setup()
        # actual tool args reference a different (unplanned) path
        _write(os.path.join(self.dir, "other.png"), "OTHER")
        _write(self.args_path, {"reference_images": ["other.png"]})
        with self.assertRaises(vp.ValidationError):
            vp.cmd_check(self.plan_path, self.receipt_path,
                         self.exec_path, self.review_path)

    def test_missing_actual_reference_inputs_fails(self):
        self._base_generation_setup()
        _write(self.args_path, {"reference_images": []})
        with self.assertRaises(vp.ValidationError):
            vp.cmd_check(self.plan_path, self.receipt_path,
                         self.exec_path, self.review_path)

    def test_unresolved_review_fix_blocks_release(self):
        self._base_generation_setup()
        review = self.good_review()
        review["criteria"][0]["disposition"] = "fix"
        _write(self.review_path, review)
        with self.assertRaises(vp.ValidationError):
            vp.cmd_check(self.plan_path, self.receipt_path,
                         self.exec_path, self.review_path)

    def test_unverified_review_blocks_release(self):
        self._base_generation_setup()
        review = self.good_review()
        review["criteria"][1]["disposition"] = "unverified"
        _write(self.review_path, review)
        with self.assertRaises(vp.ValidationError):
            vp.cmd_check(self.plan_path, self.receipt_path,
                         self.exec_path, self.review_path)

    def test_review_criterion_missing_evidence_fails(self):
        self._base_generation_setup()
        review = self.good_review()
        del review["criteria"][0]["evidence"]
        _write(self.review_path, review)
        with self.assertRaises(vp.ValidationError):
            vp.cmd_check(self.plan_path, self.receipt_path,
                         self.exec_path, self.review_path)

    def test_missing_output_fails(self):
        self._base_generation_setup()
        os.remove(os.path.join(self.dir, "out.png"))
        with self.assertRaises(vp.ValidationError):
            vp.cmd_check(self.plan_path, self.receipt_path,
                         self.exec_path, self.review_path)

    def test_execution_receipt_hash_mismatch_fails(self):
        self._base_generation_setup()
        _write(self.exec_path, self.execution_record(
            "deadbeef", tool_args_path="tool_args.json"))
        with self.assertRaises(vp.ValidationError):
            vp.cmd_check(self.plan_path, self.receipt_path,
                         self.exec_path, self.review_path)

    def test_reuse_without_source_artifact_fails(self):
        self._base_generation_setup()
        rhash = vp._sha256_file(self.receipt_path)
        _write(self.exec_path, self.execution_record(
            rhash, tool_args_path="tool_args.json", reuse={}))
        with self.assertRaises(vp.ValidationError):
            vp.cmd_check(self.plan_path, self.receipt_path,
                         self.exec_path, self.review_path)

    def test_reuse_with_valid_source_artifact_passes(self):
        self._base_generation_setup()
        rhash = vp._sha256_file(self.receipt_path)
        _write(os.path.join(self.dir, "prior.png"), "PRIOR")
        _write(self.exec_path, self.execution_record(
            rhash, tool_args_path="tool_args.json",
            reuse={"source_artifact": "prior.png"}))
        result = vp.cmd_check(self.plan_path, self.receipt_path,
                              self.exec_path, self.review_path)
        self.assertTrue(result["ok"])


class RegressionTests(Base):
    def test_copy_zone_outside_canvas_rejected(self):
        plan=self.ambient_plan();plan["composition"]["copy_zones"][0]["w"]=9999
        with self.assertRaises(vp.ValidationError):self.prepare_ok(plan)

    def test_missing_ambient_reference_rejected_before_production(self):
        plan=self.ambient_plan();plan["references"]=[]
        with self.assertRaises(vp.ValidationError):self.prepare_ok(plan)

    def run_flow(self, method="generation", missing_criterion=False):
        plan=self.ambient_plan()
        plan["references"].append({"path":self.ref_rel,"decision":"change","role":"remove depth"})
        self.prepare_ok(plan)
        _write(os.path.join(self.dir,"out.png"),"OUT")
        _write(self.args_path,{"referenced_image_paths":[os.path.join(self.dir,self.ref_rel)]})
        record=self.execution_record(vp._sha256_file(self.receipt_path),method=method)
        if method=="generation":record["tool_args_path"]="tool_args.json"
        if method=="reuse":record["reuse"]={"source_artifact":self.ref_rel}
        _write(self.exec_path,record)
        review=self.good_review()
        if missing_criterion:review["criteria"]=[c for c in review["criteria"] if c["name"]!="change:remove depth"]
        _write(self.review_path,review)
        return vp.cmd_check(self.plan_path,self.receipt_path,self.exec_path,self.review_path)

    def test_native_imagegen_absolute_paths_and_multiple_traits(self):
        self.assertTrue(self.run_flow()["ok"])

    def test_unreviewed_change_trait_rejected(self):
        with self.assertRaises(vp.ValidationError):self.run_flow(missing_criterion=True)

    def test_ambient_reuse_without_imagegen(self):
        self.assertTrue(self.run_flow(method="reuse")["ok"])

    def test_ambient_direct_composition_without_imagegen(self):
        self.assertTrue(self.run_flow(method="direct")["ok"])

if __name__ == "__main__":
    unittest.main()
