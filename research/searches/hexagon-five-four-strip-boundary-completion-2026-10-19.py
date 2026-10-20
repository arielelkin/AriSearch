#!/usr/bin/env python3
"""Exact same-strip boundary-isometry gate; eight edge orbits only."""
from sage.all import QuadraticField, vector, matrix, floor, ZZ
from pathlib import Path
import json
K=QuadraticField(3,"r");r=K.gen();root=Path(__file__).resolve().parents[1]
src=json.loads((root/"certificates/hexagon-five-four-39-omissions-2026-10-19.json").read_text())
cor=json.loads((root/"certificates/hexagon-five-four-five-residual-coronas-2026-10-19.json").read_text())
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def pt(x):return vector(K,[K(z) for z in x])
def ser(x):return [str(z) for z in x]
def pkey(p):return tuple(sorted(tuple(x) for x in p))
results=[]
for ent in cor["rows"]:
 idx=ent["row_index"];row=src["rows"][idx]
 A=[vector(K,[K(z[0])+K(z[1])*r for z in x]) for x in row["vertices"][0]]
 v=A[3]+A[4]-A[5]-A[0];norm=v*v
 def canon(x):return x-int(floor((x*v)/norm))*v
 def ek(a,b):
  sh=int(floor(min(a*v,b*v)/norm));return tuple(sorted((tuple(a-sh*v),tuple(b-sh*v))))
 patch=[[pt(x) for x in p] for p in ent["results"][6]["patch"]]
 reps={}
 for p in patch:
  sh=int(floor(min(x*v for x in p)/norm));q=[x-sh*v for x in p];reps[pkey(q)]=q
 edges={}
 for f,p in enumerate(reps.values()):
  orient=1 if cross(p[1]-p[0],p[2]-p[1])>0 else -1
  for side in range(6):
   a,b=p[side],p[(side+1)%6]
   if orient<0:a,b=b,a
   edges.setdefault(ek(a,b),[]).append((a,b,f,side))
 exposed=[es[0] for es in edges.values() if len(es)==1];assert len(exposed)==8
 # Lift each directed boundary cycle from quotient vertices to an actual chain.
 chains=[];unused=set(range(8))
 while unused:
  start=min(unused);order=[];verts=[exposed[start][0]];i=start
  while True:
   unused.remove(i);a,b,f,s=exposed[i];shift=verts[-1]-a
   assert cross(shift,v)==0 and (shift*v)/norm in ZZ
   order.append((f,s));verts.append(b+shift)
   candidates=[j for j in range(8) if canon(exposed[j][0])==canon(verts[-1])]
   assert len(candidates)==1;i=candidates[0]
   if i==start:break
   assert i in unused
  period=verts[-1]-verts[0];assert period==v or period==-v
  chains.append((verts,order,period))
 assert len(chains)==2 and all(len(c[1])==4 for c in chains)
 assert chains[0][2]==-chains[1][2]
 for k in range(4):assert chains[0][0][k+1]-chains[0][0][k]==-(chains[1][0][k+1]-chains[1][0][k])
 lengths=[(chains[0][0][k+1]-chains[0][0][k]).dot_product(chains[0][0][k+1]-chains[0][0][k]) for k in range(4)]
 assert len(set(lengths))==4 and all(z>0 for z in lengths)
 directions=[chains[0][0][k+1]-chains[0][0][k] for k in range(4)]
 assert all(cross(directions[k],directions[(k+1)%4])!=0 for k in range(4))
 assert cross(chains[0][0][1]-chains[0][0][0],chains[0][0][2]-chains[0][0][1])!=0
 assert all([s for f,s in c[1]]==[2,0,5,4] for c in chains)
 # All exposed representatives are B: compare native vertex order with a certified B isometry.
 B=[vector(K,[K(z[0])+K(z[1])*r for z in x]) for x in row["vertices"][1]]
 for a,b,f,s in exposed:
  p=list(reps.values())[f]
  assert any(all(p[k]-p[0]==matrix(K,iso["matrix"])*(B[k]-B[0]) for k in range(6)) for iso in ent["results"][6]["isometries"] if iso["species"]==1)

 # All orthogonal maps preserving the period line, including halfturn for completeness.
 J=matrix(K,[[0,-1],[1,0]]);w=J*v
 basis=matrix(K,[[v[0],w[0]],[v[1],w[1]]])
 maps=[(name,basis*matrix(K,[[a,0],[0,b]])*basis.inverse()) for name,a,b in [("translation",1,1),("halfturn",-1,-1),("parallel_reflection",1,-1),("perpendicular_reflection",-1,1)]]
 tests=[]
 for ti,(tv,to,tp) in enumerate(chains):
  target={ek(tv[k],tv[k+1]) for k in range(4)}
  for si,(sv,so,sp) in enumerate(chains):
   for name,M in maps:
    # Opposite tile-side orientation at the seam: det(M)*M(sp)=-tp.
    if M.det()*(M*sp)!=-tp:continue
    for j in range(4):
     # Map source vertex zero to each target vertex modulo v.
     t=tv[j]-M*sv[0]
     image={ek(M*sv[k]+t,M*sv[k+1]+t) for k in range(4)}
     match=image==target
     tests.append(dict(target=ti,source=si,kind=name,anchor=j,translation=ser(t),match=match,matched_edges=len(image & target)))
 result=dict(row_index=idx,period=ser(v),chains=[dict(vertices=[ser(x) for x in vv],native_incidence=[dict(species="B",quotient_face=f,native_side=s) for f,s in oo],period=ser(pp),edge_vectors=[ser(vv[k+1]-vv[k]) for k in range(4)],squared_lengths=[str((vv[k+1]-vv[k])*(vv[k+1]-vv[k])) for k in range(4)]) for vv,oo,pp in chains],tests=tests,matches=[t for t in tests if t["match"]])
 results.append(result);print(idx,[[z[1] for z in c[1]] for c in chains],"matches",result["matches"])
out=dict(schema="SAME_STRIP_BOUNDARY_COMPLETION_V1",domain="five rows; two four-edge boundary cycles; four period-line orthogonal maps; four vertex correspondences; opposite interior sides",rows=results)
(root/"certificates/hexagon-five-four-strip-boundary-completion-2026-10-19.json").write_text(json.dumps(out,indent=2)+"\n")

# Diagnostic only: float conversion occurs solely when rendering certified exact vertices.
xrow=results[0];vv=[[pt(x) for x in c["vertices"]] for c in xrow["chains"]];period=pt(xrow["period"])
segments=[([x+n*period for x in c],ci) for ci,c in enumerate(vv) for n in range(-1,2)]
points=[p for c,ci in segments for p in c];lo=[min(float(p[k]) for p in points) for k in range(2)];hi=[max(float(p[k]) for p in points) for k in range(2)]
scale=85
svg=["<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"1000\" height=\"650\" viewBox=\"0 0 1000 650\"><rect width=\"1000\" height=\"650\" fill=\"white\"/><text x=\"20\" y=\"28\">Row15: two exposed chains; diagnostic only, not plane coverage proof</text>"]
for c,ci in segments:
 coords=[(40+scale*(float(p[0])-lo[0]),600-scale*(float(p[1])-lo[1])) for p in c]
 svg.append("<polyline fill=\"none\" stroke=\"%s\" stroke-width=\"3\" points=\"%s\"/>"%(["#165a9a","#b83a32"][ci]," ".join("%g,%g"%xy for xy in coords)))
 for k in range(4):
  x,y=coords[k];xx,yy=coords[k+1];svg.append("<text x=\"%g\" y=\"%g\" font-size=\"13\">B%d</text>"%((x+xx)/2,(y+yy)/2-5,[2,0,5,4][k]))
svg.append("</svg>");(root/"figures/hexagon-five-four-strip-boundaries-row15-2026-10-19.svg").write_text("\n".join(svg)+"\n")
