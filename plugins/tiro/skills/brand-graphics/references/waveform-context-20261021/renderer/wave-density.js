/* Optical ink-density calibration, anchored to the unchanged globe.
 * Canonical 42-carrier source quantiles weighted by vertical support length.
 * Changes paired X half-widths only: Y support, centers and voids stay intact.
 */
(function(root){
 const calibration={"target":[1.26,2.51,4.61,6.21,7.2],"sources":[[2.5,3.32,4.73,5.95,6.6],[1.53,2.73,5.8,6.66,7.01],[2.46,2.77,3.93,5.6,5.91],[1.68,1.72,1.84,1.94,3.03],[2.3,2.71,3.5,4.66,5.73],[1.26,2.51,4.61,6.21,7.2],[2.22,2.92,4.14,5.98,7.0]]};
 function balance(row,object,sourceQuantiles){
  if(object===5)return row.slice();
  const anchors=[[0,0],[.15,.15],...(sourceQuantiles||calibration.sources[object]).map((x,i)=>[x,calibration.target[i]]),[7.5,7.5]];
  const result=row.slice(),n=row.length/4;
  for(let j=0;j<n;j++){
   const a=j*2,b=row.length-2-j*2,w=Math.max(0,row[b]-row[a]);let mapped=w;
   for(let k=0;k<anchors.length-1;k++){
    const [x,y]=anchors[k],[xx,yy]=anchors[k+1];
    if(w>=x&&w<=xx){mapped=y+(yy-y)*(w-x)/Math.max(.00001,xx-x);break;}
   }
   const u=Math.max(0,Math.min(1,(w-.15)/.85)),gate=u*u*(3-2*u);
   const width=w+.82*gate*(mapped-w),center=(row[a]+row[b])/2;
   result[a]=center-width/2;result[b]=center+width/2;
  }
  return result;
 }
 const api={balance,calibration,version:'globe-44-v1'};
 if(typeof module==='object'&&module.exports)module.exports=api;else root.WaveDensity=api;
})(typeof window==='object'?window:globalThis);
