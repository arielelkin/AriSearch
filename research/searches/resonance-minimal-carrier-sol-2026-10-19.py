"""Exhaustive oriented 2P+2Q saturated torus combinatorial/direction gate."""
import itertools,json
from pathlib import Path

def pairings(xs):
 if not xs:
  yield [];return
 a=xs[0]
 for j in range(1,len(xs)):
  for rest in pairings(xs[1:j]+xs[j+1:]):yield [(a,xs[j])]+rest

out=[]
for reflected in (False,True):
 angles=[[9]*5,[9]*5,[12,12,10,10,10,10,11], [12,12,11,10,10,10,10] if reflected else [12,12,10,10,10,10,11]]
 offsets=[0,5,10,17];sizes=[5,5,7,7]
 face={offsets[f]+i:f for f,n in enumerate(sizes) for i in range(n)}
 local={offsets[f]+i:i for f,n in enumerate(sizes) for i in range(n)}
 prev={offsets[f]+i:offsets[f]+(i-1)%n for f,n in enumerate(sizes) for i in range(n)}
 aa=sum(angles,[])
 dirs=[]
 for row in angles:
  ds=[0]
  for i in range(1,len(row)):ds.append((ds[-1]+15-row[i])%30)
  dirs+=ds
 pp=[1,4,6,9];pq=[0,2,3,5,7,8];qp=[10,11,16,17,18,23];qq=[12,13,14,15,19,20,21,22]
 counts=dict(all=0,vertex=0,direction=0);survivors=[]
 for ppairs in pairings(pp):
  for perm in itertools.permutations(qp):
   cross=list(zip(pq,perm))
   # AA side must face designated P side0.
   if {dict(cross)[0],dict(cross)[5]}!={10,17}:continue
   for qpairs in pairings(qq):
    counts['all']+=1
    pairs=ppairs+cross+qpairs
    alpha={a:b for a,b in pairs}|{b:a for a,b in pairs}
    unseen=set(range(24));cycles=[]
    while unseen:
     d=min(unseen);cy=[]
     while d in unseen:
      unseen.remove(d);cy.append(d);d=alpha[prev[d]]
     cycles.append(cy)
    if any(len(c)!=3 or sum(aa[d] for d in c)!=30 for c in cycles):continue
    counts['vertex']+=1
    rot={0:0};changed=True;bad=False
    while changed:
     changed=False
     for a,b in pairs:
      f,g=face[a],face[b];delta=(dirs[a]+15-dirs[b])%30
      if f in rot and g not in rot:rot[g]=(rot[f]+delta)%30;changed=True
      if g in rot and f not in rot:rot[f]=(rot[g]-delta)%30;changed=True
      if f in rot and g in rot and (rot[g]-rot[f]-delta)%30:bad=True;break
     if bad:break
    if bad or len(rot)!=4:continue
    counts['direction']+=1
    survivors.append(dict(pairs=pairs,rotations=rot,vertices=cycles))
 out.append(dict(second_Q_reflected=reflected,counts=counts,survivors=survivors))
p=Path(__file__).with_suffix('.json');p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
