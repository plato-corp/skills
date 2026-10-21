/* Horizontal ribbons sampled from the original material field, not 42 vertical ribbons.
 * Fixed Y carriers, 112 paired vertices, per-object X support: topology stays morphable.
 */
window.HorizontalWave=(()=>{
 const cache=new Map();
 function fieldFor(key){
  if(!cache.has(key)){const f=window.HorizontalFields;const raw=atob(f.fields[key]);cache.set(key,{...f,data:Uint8Array.from(raw,c=>c.charCodeAt(0))});}
  return cache.get(key);
 }
 return (_rows,count,thickness=1,key=0)=>{
  const f=fieldFor(key),points=112,pitch=356/(count-1);
  function sample(x,y){
   const u=x-f.x,v=y-f.y;if(u<0||v<0||u>f.w-1||v>f.h-1)return 0;
   const a=Math.floor(u),b=Math.floor(v),aa=Math.min(a+1,f.w-1),bb=Math.min(b+1,f.h-1),dx=u-a,dy=v-b;
   return ((f.data[b*f.w+a]*(1-dx)+f.data[b*f.w+aa]*dx)*(1-dy)+(f.data[bb*f.w+a]*(1-dx)+f.data[bb*f.w+aa]*dx)*dy)/255;
  }
  return Array.from({length:count},(_,i)=>{
   const y=12+i*pitch,upper=[],lower=[];let start=Infinity,end=-Infinity;
   for(let x=12;x<=378;x+=.5)if(sample(x,y)>.015){start=Math.min(start,x);end=x;}
   const empty=!Number.isFinite(start);if(empty)start=end=195;
   else{start=Math.max(12,start-.5);end=Math.min(378,end+.5);}
   for(let j=0;j<points;j++){
    const x=start+(end-start)*j/(points-1),h=empty?0:sample(x,y)*pitch*.41*thickness;
    upper.push(x,y-h);lower.unshift(x,y+h);
   }
   return upper.concat(lower);
  });
 };
})();
