from sage.all import *
from itertools import permutations, product
from pathlib import Path
import json
K=CyclotomicField(20); w=K.gen()
word='AAABBABB'; native=[0,2,4,7,10,12,15,18]; private=[3,6]
P=[sum((w**(4*j) for j in range(i)),K(0)) for i in range(5)]
L=-w**7+w**5-w**3+2*w
Q=[K(0)]
for i in range(7):Q.append(Q[-1]+(L if i in private else 1)*w**native[i])
assert Q[-1]+w**native[7]==0
cross=lambda a,b:(a.conjugate()*b-a*b.conjugate())/(2*w**5)
assert QQbar(L).real()>0
for poly in [P,Q]:
 for i in range(len(poly)):
  for j in range(len(poly)):
   if j not in [i,(i+1)%len(poly)]:assert QQbar(cross(poly[(i+1)%len(poly)]-poly[i],poly[j]-poly[i])).real()>0

def match(xs):
 if not xs:yield [];return
 for j in range(1,len(xs)):
  for r in match(xs[1:j]+xs[j+1:]):yield [(xs[0],xs[j])]+r
D=[(f,i) for f in range(6) for i in range(5 if f<4 else 8)]
ix={d:k for k,d in enumerate(D)}; n=[5]*4+[8]*2
nxt=[ix[(f,(i+1)%n[f])] for f,i in D]
counts=dict(qq_tests=0,qq_consistent=0,pq_bijections=0,pq_rotational=0,pp_matchings=0,pp_rotational=0,correct_stars=0)
qq_records=[]; records=[]
for reflected in [False,True]:
 polys=[P]*4+[Q,([Q[(-i)%8].conjugate() for i in range(8)] if reflected else Q)]
 labels=[['A','A','A','A','B']]*4+[list(word),[word[(-i)%8] for i in range(8)] if reflected else list(word)]
 qe=[private,[( -i-1)%8 for i in private] if reflected else private]
 exps=[native,[(10-native[(-i-1)%8])%20 for i in range(8)] if reflected else native]
 for perm in permutations(qe[1]):
  counts['qq_tests']+=1
  rp=[(10+exps[0][i]-exps[1][j])%20 for i,j in zip(qe[0],perm)]
  ok=rp[0]==rp[1]
  qq_records.append(dict(reflected=reflected,source=qe[0],target=perm,relative_rotation=rp,consistent=ok))
  if not ok:continue
  counts['qq_consistent']+=1
  qrot=[0,rp[0]]
  public=[(f,i) for f in [4,5] for i in range(8) if i not in qe[f-4]]
  typ=lambda d:labels[d[0]][d[1]]+labels[d[0]][(d[1]+1)%n[d[0]]]
  aa=[d for d in public if typ(d)=='AA']; ab=[d for d in public if typ(d)=='AB'];ba=[d for d in public if typ(d)=='BA']
  assert len(aa)==len(ab)==len(ba)==4
  # P labels fixed by lexicographic order of their unique AA-facing Q dart.
  for bs,cs in product(permutations(ba),permutations(ab)):
   counts['pq_bijections']+=1
   assignments=[[(1,aa[f]),(3,bs[f]),(4,cs[f])] for f in range(4)]
   pro=[]
   for ass in assignments:
    rr=[(10+qrot[g-4]+exps[g-4][j]-4*i)%20 for i,(g,j) in ass]
    if len(set(rr))!=1:break
    pro.append(rr[0])
   if len(pro)!=4:continue
   counts['pq_rotational']+=1
   rot=pro+qrot
   pq=[(ix[(f,i)],ix[d]) for f,ass in enumerate(assignments) for i,d in ass]
   qq=[(ix[(4,i)],ix[(5,j)]) for i,j in zip(qe[0],perm)]
   for pp in match([ix[(f,i)] for f in range(4) for i in [0,2]]):
    counts['pp_matchings']+=1
    if any((rot[D[a][0]]+4*D[a][1]-rot[D[b][0]]-4*D[b][1])%20!=10 for a,b in pp):continue
    counts['pp_rotational']+=1
    pairs=pp+pq+qq
    alpha={a:b for a,b in pairs};alpha.update({b:a for a,b in pairs})
    unseen=set(range(len(D)));cycles=[]
    while unseen:
     d=min(unseen);c=[]
     while d not in c:c.append(d);unseen.remove(d);d=nxt[alpha[d]]
     cycles.append(c)
    if any(sorted('P' if D[d][0]<4 else labels[D[d][0]][D[d][1]] for d in c) not in [['A','P','P'],['B','B','P']] for c in cycles):continue
    counts['correct_stars']+=1
    records.append(dict(reflected=reflected,pairs=pairs,cycles=cycles,rotations=rot))
print(counts,flush=True)
for rec in records:
 polys=[P]*4+[Q,([Q[(-i)%8].conjugate() for i in range(8)] if rec['reflected'] else Q)]
 rotations=[w**k for k in rec['rotations']];trans={0:K(0)}
 pairs=rec['pairs']
 while len(trans)<6:
  old=len(trans)
  for a,b in pairs:
   for x,y in [(a,b),(b,a)]:
    f,i=D[x];g,j=D[y]
    if f in trans and g not in trans:trans[g]=trans[f]+rotations[f]*polys[f][(i+1)%n[f]]-rotations[g]*polys[g][j]
  assert len(trans)>old
 tiles=[[rotations[f]*z+trans[f] for z in polys[f]] for f in range(6)]
 delta=[]
 for a,b in pairs:
  f,i=D[a];g,j=D[b]
  z=tiles[f][i]-tiles[g][(j+1)%n[g]]
  assert z==tiles[f][(i+1)%n[f]]-tiles[g][j]
  delta.append(z)
 area=sum(sum(cross(T[i],T[(i+1)%len(T)]) for i in range(len(T)))/2 for T in tiles)
 assert QQbar(area).real()>0
 cert=None
 for L1 in delta:
  for L2 in delta:
   det=cross(L1,L2)
   if not det:continue
   coeff=[(cross(z,L2)/det,cross(L1,z)/det) for z in delta]
   if all(x in ZZ and y in ZZ for x,y in coeff) and det in [area,-area]:
    assert len(rec['cycles'])==12 and all(len(c)==3 for c in rec['cycles'])
    cert=dict(lattice=[str(L1),str(L2)],determinant=str(det),total_area=str(area),shift_coefficients=[[int(x),int(y)] for x,y in coeff],polygons=[[str(z) for z in T] for T in tiles],translations=[str(trans[f]) for f in range(6)])
    break
  if cert:break
 rec['certificate']=cert
assert set(records[0]['certificate']['polygons'][5])==set(records[1]['certificate']['polygons'][5])
print('certificates',sum(r['certificate'] is not None for r in records),flush=True)
assert all(r['certificate'] for r in records)
out=dict(software=version(),counts=counts,qq_tests=qq_records,records=records,scope='All oriented full-edge translation quotients with exactly four P and two Q faces, up to face relabeling and global reflection. Each recorded certificate proves a periodic plane tiling; no claim about all larger inventories or the unrestricted two-convex-polygon problem.')
Path('research/searches/regular-pentagon-octagon-qdimer-carrier-sol-2026-10-19.json').write_text(json.dumps(out,indent=2,default=int))
