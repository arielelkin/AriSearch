"""Independent exact hosted periodic-carrier checker; no producer imports.
Checks a frozen coordinate certificate, not the necessary ring enumeration.
"""
from pathlib import Path
import json
from itertools import product
from sage.all import QQ, AA, NumberField, PolynomialRing, vector, matrix

root=Path(__file__).resolve().parents[2]
cert=json.loads((root/"research/certificates/hosted-oneprivate-x2u-periodic-carrier.json").read_text())
assert cert["field_polynomial_coefficients"]==[1,0,-8,0,8]
assert cert["field_isolating_interval"]==["9/10","1"]
Z=PolynomialRing(QQ,"z");z=Z.gen()
K=NumberField(8*z**4-8*z**2+1,"c",embedding=((2+AA(2).sqrt())/4).sqrt())
c=K.gen();r=4*c*c-2;t=r/(4*c)
def point(row):return vector(K,[K(a) for a in row])
def edges(F):return list(zip(F,F[1:]+F[:1]))
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def area(F):return sum(cross(a,b) for a,b in edges(F))/2
x=K(1);u=K(1)/2
y=(r+2*c-t-1)/(2*c+t+1/r)
v=u+r*c*(x-y);w=(u+v)/r-t*(x+y)
H=y-(u+v-y-x)/r
lens={"x":x,"y":y,"u":u,"v":v,"w":w,"H":H}
assert all(AA(a)>0 for a in lens.values()) and len(set(lens.values()))==6
assert {name:K(value) for name,value in cert["native_lengths"].items()}==lens
P=[vector(K,[0,-w])]
for length,direction in zip((x,u,v,y,w),((c,-t),(1/r,1/r),(-1/r,1/r),(-c,-t),(0,-1))):
 P.append(P[-1]+length*vector(K,direction))
assert P[-1]==P[0];P.pop();P=tuple(P)
Q=[vector(K,[0,0])]
word=(H,u,x,y,y,x,w,v)
directions=((1,0),(1/r,1/r),(0,1),(-1/r,1/r),(-1,0),(-1/r,-1/r),(0,-1),(1/r,-1/r))
for length,direction in zip(word,directions):Q.append(Q[-1]+length*vector(K,direction))
assert Q[-1]==Q[0];Q.pop();Q=tuple(Q)
for name,F in (("P",P),("Q",Q)):
 assert F==tuple(point(row) for row in cert["canonical_polygons"][name])
 assert AA(area(F))>0
 for i,(a,b) in enumerate(edges(F)):
  assert all(AA(cross(b-a,p-a))>0 for j,p in enumerate(F) if j not in(i,(i+1)%len(F)))
  incoming=F[i-1]-a;outgoing=b-a;dot=incoming.dot_product(outgoing)
  if name=="P" and i==2:assert dot==0
  else:
   assert AA(dot)<0
   ratio=(2-r)/4 if name=="P" else QQ(1)/2
   assert dot**2==ratio*incoming.dot_product(incoming)*outgoing.dot_product(outgoing)
assert sum(length not in (x,u,v,y,w) for length in word)==1
reps=[];species=[]
for entry in cert["representatives"]:
 F=tuple(point(row) for row in entry["vertices"]);kind=entry["species"];base=P if kind=="P" else Q
 assert kind in("P","Q") and len(F)==len(base)
 n=len(F)
 assert any(all((F[i]-F[j]).dot_product(F[i]-F[j])==(base[(shift+sign*i)%n]-base[(shift+sign*j)%n]).dot_product(base[(shift+sign*i)%n]-base[(shift+sign*j)%n]) for i,j in product(range(n),repeat=2)) for shift,sign in product(range(n),(-1,1)))
 if AA(area(F))<0:F=tuple(reversed(F))
 assert AA(area(F))>0
 reps.append(F);species.append(kind)
assert species.count("P")==6 and species.count("Q")==2
U=point(cert["U"]);V=point(cert["V"])
L=matrix(K,[[U[0],V[0]],[U[1],V[1]]]);det=L.det();assert AA(det)!=0
assert det==K(cert["signed_covolume"])
segments={}
for f,F in enumerate(reps):
 number=0
 for p,q in edges(F):
  split=(p,(p+q)/2,q) if (q-p).dot_product(q-p)==x*x else(p,q)
  for a,b in zip(split,split[1:]):
   assert a!=b;segments[(f,number)]=(a,b);number+=1
assert len(segments)==cert["atomic_segment_count"]==56
inverse=L.inverse();regenerated={}
for name,(p,q) in segments.items():
 matches=[]
 for other,(a,b) in segments.items():
  shift=p-b
  if q-a!=shift:continue
  coefficients=inverse*shift
  if all(value in QQ and QQ(value).denominator()==1 for value in coefficients):
   matches.append((other,tuple(int(value) for value in coefficients)))
 assert len(matches)==1,(name,matches)
 regenerated[name]=matches[0]
assert len(set(name for name in regenerated))==56
for name,(other,shift) in regenerated.items():assert regenerated[other]==(name,tuple(-value for value in shift))
saved={tuple(entry["segment"]):(tuple(entry["partner"]),tuple(entry["lattice_shift"])) for entry in cert["segment_pairs"]}
assert saved==regenerated
assert sum(area(F) for F in reps)==abs(det) and K(cert["area_difference"])==0
print(json.dumps({"status":"PASS","P_representatives":6,"Q_representatives":2,"atomic_segments":56,"undirected_pairs":28,"entire_plane_certificate":"positive convex polygons, complete reversed atomic boundaries, exact area/covolume one","producer_imports":False}))
