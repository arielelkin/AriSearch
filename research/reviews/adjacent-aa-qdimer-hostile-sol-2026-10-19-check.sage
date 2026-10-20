from sage.all import *
import json
from pathlib import Path
K=CyclotomicField(40); zeta40=K.gen()
j=json.loads(Path("research/searches/adjacent-aa-qdimer-carrier-sol-2026-10-19-witness.json").read_text())
r=j["records"][0]; c=r["certificate"]
parse=lambda s: K(sage_eval(s,locals={"zeta40":zeta40}))
polys=[[parse(s) for s in T] for T in c["polygons"]]
cross=lambda a,b: (a.conjugate()*b-a*b.conjugate())/(2*zeta40**10)
pos=lambda a: QQbar(a).real()>0
# Native polygons reconstructed without reading the search implementation.
angles=[0,36,72,135,180,216,279,324]
v=[zeta40**(a//9) for a in angles]
public=sum([v[i] for i in [0,1,2,4,5,7]],K(0))
x=-cross(public,v[6])/cross(v[3],v[6]); y=-cross(v[3],public)/cross(v[3],v[6])
assert pos(x) and pos(y)
q=[K(0)]
for i in range(8): q.append(q[-1]+([x if i==3 else y if i==6 else K(1)][0])*v[i])
assert q[-1]==0
p=[sum([zeta40**(8*k) for k in range(i)],K(0)) for i in range(5)]
for f,T in enumerate(polys):
 base=p if f<4 else q[:-1]
 assert len(T)==len(base)
 assert all(T[i]-T[0]==zeta40**r["rotations"][f]*base[i] for i in range(len(T)))
 assert all(pos(cross(T[(i+1)%len(T)]-T[i],T[k]-T[i])) for i in range(len(T)) for k in range(len(T)) if k not in [i,(i+1)%len(T)])
D=[(f,i) for f,T in enumerate(polys) for i in range(len(T))]; index={d:k for k,d in enumerate(D)}
succ=[index[(f,(i+1)%len(polys[f]))] for f,i in D]
mate={}; lattice=[parse(s) for s in c["lattice"]]
for (a,b),(m,n) in zip(r["pairs"],c["shift_coefficients"]):
 assert a!=b and a not in mate and b not in mate
 mate[a]=b; mate[b]=a
 f,i=D[a];g,k=D[b];T=polys[f];U=polys[g]
 shift=m*lattice[0]+n*lattice[1]
 assert T[i]-U[(k+1)%len(U)]==shift==T[(i+1)%len(T)]-U[k]
assert len(mate)==36
cycles=[]; todo=set(mate)
while todo:
 a=min(todo); cyc=[]
 while a not in cyc:
  cyc.append(a);todo.remove(a);a=succ[mate[a]]
 assert a==cyc[0];cycles.append(cyc)
assert cycles==r["cycles"] and len(cycles)==12
for cyc in cycles:
 types=["P" if D[a][0]<4 else "AAABCABC"[D[a][1]] for a in cyc]
 assert sorted(types) in [sorted("PPA"),sorted("PBC")]
areas=[sum([cross(T[i],T[(i+1)%len(T)]) for i in range(len(T))],K(0))/2 for T in polys]
assert all(pos(a) for a in areas)
det=cross(*lattice);assert det!=0 and abs(QQbar(det).real())==QQbar(sum(areas)).real()
assert det==parse(c["determinant"]) and sum(areas)==parse(c["total_area"])
# Connected face adjacency, so the smooth quotient is a connected genus-one surface.
seen={0}
while True:
 old=set(seen)
 for a,b in r["pairs"]:
  f,g=D[a][0],D[b][0]
  if f in seen or g in seen: seen.update([f,g])
 if old==seen:break
assert len(seen)==6
print("PASS: independent exact native reconstruction, convexity, 18 edge mates, 12 stars, connected torus, signed areas and lattice degree one")
