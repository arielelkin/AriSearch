from sage.all import *
from itertools import permutations
import json
from pathlib import Path
K=CyclotomicField(20); w=K.gen(); R=PolynomialRing(K,'h'); h=R.gen()
conj=lambda x:R([a.conjugate() for a in R(x)])
cross=lambda a,b:(conj(a)*b-a*conj(b))/(2*w**5)
P=[R(sum((w**(4*j) for j in range(i)),K(0))) for i in range(5)]
D=[(f,i) for f,n in enumerate([5,5,8]) for i in range(n)]; ix={d:k for k,d in enumerate(D)}
n=[5,5,8]; nxt=[ix[(f,(i+1)%n[f])] for f,i in D]
def match(xs):
 if not xs: yield []; return
 a=xs[0]
 for j in range(1,len(xs)):
  for r in match(xs[1:j]+xs[j+1:]):yield [(a,xs[j])]+r
out={}
for word,qq in [('AAABBABB',[3,6]),('AABBAABB',[2,6])]:
 ds=[K(1)]
 for i in range(1,8):ds.append(ds[-1]*w**(2 if word[i]=='A' else 3))
 ell=R(-w**7+w**5-w**3+2*w) if word=='AAABBABB' else h
 Q=[R(0)]
 for i in range(7):Q.append(Q[-1]+(ell if i in qq else 1)*ds[i])
 assert Q[-1]+(ell if 7 in qq else 1)*ds[7]==0
 # Strict supporting half-planes for all h>0; coefficients embed in R.
 for i in range(8):
  for j in range(8):
   if j in [i,(i+1)%8]:continue
   c=cross(ds[i],Q[j]-Q[i])
   assert all(QQbar(a).real()>=0 for a in c.list()) and QQbar(c(1)).real()>0
 counts=dict(pairings=0,endpoint_compatible=0,stars=0,holonomy=0); records=[]
 for refl in [False,True]:
  polys=[P,P,([conj(Q[(-i)%8]) for i in range(8)] if refl else Q)]
  labels=['A' if i<4 else 'B' for f,i in D[:10]]+[word[(-i)%8] if refl else word[i] for i in range(8)]
  qe=[i for i in range(8) if (-(i+1))%8 in qq] if refl else qq
  pp=[ix[(f,i)] for f in [0,1] for i in [0,2]]
  pq=[ix[(f,i)] for f in [0,1] for i in [1,3,4]]
  qp=[ix[(2,i)] for i in range(8) if i not in qe]
  for m in match(pp):
   for perm in permutations(qp):
    counts['pairings']+=1
    pairs=m+list(zip(pq,perm))+[(ix[(2,qe[0])],ix[(2,qe[1])])]
    if any(labels[a]!=labels[nxt[b]] or labels[nxt[a]]!=labels[b] for a,b in pairs):continue
    counts['endpoint_compatible']+=1
    alpha={a:b for a,b in pairs};alpha.update({b:a for a,b in pairs})
    unseen=set(range(18)); cycles=[]
    while unseen:
     d=min(unseen);c=[]
     while d not in c:c.append(d);unseen.remove(d);d=nxt[alpha[d]]
     cycles.append(c)
    if any(sorted(('P' if D[d][0]<2 else labels[d]) for d in c) not in [['A','P','P'],['B','B','P']] for c in cycles):continue
    counts['stars']+=1
    rot={0:K(1)};trans={0:R(0)}
    edges=[polys[f][(i+1)%n[f]]-polys[f][i] for f,i in D]
    change=True
    while change:
     change=False
     for a,b in pairs:
      for x,y in [(a,b),(b,a)]:
       f,i=D[x];g,j=D[y]
       if f in rot and g not in rot:
        ratio=-edges[x]/edges[y];assert ratio in K
        rot[g]=rot[f]*K(ratio);trans[g]=rot[f]*polys[f][(i+1)%n[f]]+trans[f]-rot[g]*polys[g][j];change=True
    if len(rot)<3 or any(rot[D[a][0]]*edges[a]!=-rot[D[b][0]]*edges[b] for a,b in pairs):continue
    counts['holonomy']+=1
    tiles=[[rot[f]*z+trans[f] for z in polys[f]] for f in range(3)]
    delta=[]
    for a,b in pairs:
     f,i=D[a];g,j=D[b];z=tiles[f][i]-tiles[g][(j+1)%n[g]]
     assert z==tiles[f][(i+1)%n[f]]-tiles[g][j];delta.append(z)
    rec=dict(reflected=refl,pairs=pairs,cycles=cycles,rotations=[str(rot[f]) for f in range(3)],translations=[str(trans[f]) for f in range(3)],deltas=[str(z) for z in delta])
    # A certificate with integral shift coordinates and covolume equal total area
    nz=[z for z in delta if z];cert=None
    for L1 in nz:
     for L2 in nz:
      det=cross(L1,L2)
      if not det:continue
      coeff=[(cross(z,L2)/det,cross(L1,z)/det) for z in delta]
      if not all(x in ZZ and y in ZZ for x,y in coeff):continue
      area=sum(sum(cross(T[i],T[(i+1)%len(T)]) for i in range(len(T)))/2 for T in tiles)
      if det not in [area,-area]:continue
      assert all(QQbar(a).real()>=0 for a in area.list()) and QQbar(area(0)).real()>0
      assert len(cycles)==6
      assert all(len(c)==3 for c in cycles)
      cert=dict(lattice=[str(L1),str(L2)],determinant=str(det),total_area=str(area),shift_coefficients=[[int(x),int(y)] for x,y in coeff],polygons=[[str(z) for z in T] for T in tiles]);break
     if cert:break
    rec['certificate']=cert;records.append(rec)
 out[word]=dict(counts=counts,records=records)
 print(word,counts,'certificates',sum(r['certificate'] is not None for r in records),flush=True)
Path('research/searches/regular-pentagon-octagon-minimal-carrier-sol-2026-10-19.json').write_text(json.dumps(dict(software=version(),results=out),indent=2,default=lambda x:int(x)))
