from sage.all import *
from itertools import permutations
import json
K=CyclotomicField(20); w=K.gen()
t=2*(w+w.conjugate())/2
# t=2 cos18.
P=[sum((w**(4*j) for j in range(i)),K(0)) for i in range(5)]
Q=[sum(((t if j%2 else 1)*w**(3*j) for j in range(i)),K(0)) for i in range(7)]
assert sum(((t if j%2 else 1)*w**(3*j) for j in range(7)),K(0))==0
assert {w**8*z.conjugate() for z in Q}==set(Q)
polys=[P,P,Q,Q]; n=[5,5,7,7]; off=[0,5,10,17]
D=[(f,i) for f in range(4) for i in range(n[f])]
idx={d:k for k,d in enumerate(D)}
nextd=[idx[(f,(i+1)%n[f])] for f,i in D]
labels=[('P' if f<2 else ('A' if i==0 else 'B')) for f,i in D]
def matchings(xs):
 if not xs:
  yield []
 else:
  a=xs[0]
  for j in range(1,len(xs)):
   b=xs[j]
   for rest in matchings(xs[1:j]+xs[j+1:]): yield [(a,b)]+rest
# Fixed unique PP edge. AB endpoints constrain cross gluing.
pa=[idx[(f,1)] for f in (0,1)]; pb=[idx[(f,4)] for f in (0,1)]
qa=[idx[(f,6)] for f in (2,3)]; qb=[idx[(f,0)] for f in (2,3)]
pbb=[idx[(f,i)] for f in (0,1) for i in (2,3)]
qbb=[idx[(f,i)] for f in (2,3) for i in (2,4)]
qq=[idx[(f,i)] for f in (2,3) for i in (1,3,5)]
counts=dict(pairings=0,vertex_stars=0,connected=0,translation_holonomy=0)
records=[]
for aa in permutations(qa):
 for bb in permutations(qb):
  for cc in permutations(qbb):
   for mm in matchings(qq):
    pairs=[(0,5)]+list(zip(pa,aa))+list(zip(pb,bb))+list(zip(pbb,cc))+mm
    counts['pairings']+=1
    alpha=[None]*24
    for a,b in pairs: alpha[a]=b; alpha[b]=a
    perm=[nextd[alpha[d]] for d in range(24)]
    cycles=[]; unseen=set(range(24))
    while unseen:
     start=min(unseen); cyc=[]; d=start
     while d not in cyc:
      cyc.append(d); unseen.remove(d); d=perm[d]
     assert d==start
     cycles.append(cyc)
    if any(sorted(labels[d] for d in c) not in [['A','P','P'],['B','B','P']] for c in cycles): continue
    counts['vertex_stars']+=1
    # Develop a spanning tree of faces. All rotations must agree along every edge
    # for a translational (rather than rotational) quotient.
    rot={0:K(1)}; trans={0:K(0)}
    changed=True
    while changed:
     changed=False
     for a,b in pairs:
      for x,y in ((a,b),(b,a)):
       f,i=D[x]; g,j=D[y]
       if f in rot and g not in rot:
        vf=polys[f][(i+1)%n[f]]-polys[f][i]
        vg=polys[g][(j+1)%n[g]]-polys[g][j]
        rot[g]=-rot[f]*vf/vg
        trans[g]=rot[f]*polys[f][(i+1)%n[f]]+trans[f]-rot[g]*polys[g][j]
        changed=True
    if len(rot)<4: continue
    counts['connected']+=1
    if any(rot[D[a][0]]*(polys[D[a][0]][(D[a][1]+1)%n[D[a][0]]]-polys[D[a][0]][D[a][1]]) != -rot[D[b][0]]*(polys[D[b][0]][(D[b][1]+1)%n[D[b][0]]]-polys[D[b][0]][D[b][1]]) for a,b in pairs): continue
    counts['translation_holonomy']+=1
    records.append(dict(pairs=pairs,cycles=cycles,rotations={str(f):str(v) for f,v in rot.items()},translations={str(f):str(v) for f,v in trans.items()}))
# Verify one surviving carrier, including all translates that could overlap.
verification=None
if records:
 rec=records[0]
 rr={int(f):K(v) for f,v in rec['rotations'].items()}
 tt={int(f):K(v) for f,v in rec['translations'].items()}
 tiles=[[rr[f]*v+tt[f] for v in polys[f]] for f in range(4)]
 delta=[]
 for a,b in rec['pairs']:
  f,i=D[a]; g,j=D[b]
  z=tiles[f][i]-tiles[g][(j+1)%n[g]]
  assert z==tiles[f][(i+1)%n[f]]-tiles[g][j]
  delta.append(z)
 re=lambda z:AA((z+z.conjugate())/2)
 im=lambda z:AA((z-z.conjugate())/(2*w**5))
 cross=lambda a,b:re((a.conjugate()*b-a*b.conjugate())/(2*w**5))
 nz=[z for z in delta if z]
 L1=nz[0]; L2=next(z for z in nz if cross(L1,z))
 det=cross(L1,L2)
 lc=lambda z:(cross(z,L2)/det,cross(L1,z)/det)
 coeff=[lc(z) for z in delta]
 assert all(x in ZZ and y in ZZ for x,y in coeff)
 area=lambda poly:sum(cross(poly[i],poly[(i+1)%len(poly)]) for i in range(len(poly)))/2
 assert abs(det)==sum(area(T) for T in tiles)
 def overlap(A,B):
  for C in (A,B):
   for j,a in enumerate(C):
    d=C[(j+1)%len(C)]-a
    va=[cross(d,x-a) for x in A]; vb=[cross(d,x-a) for x in B]
    if max(va)<=min(vb) or max(vb)<=min(va):return False
  return True
 bounds=[]
 for T in tiles:
  xy=[lc(z) for z in T]
  bounds.append([(min(v[k] for v in xy),max(v[k] for v in xy)) for k in (0,1)])
 checked=0
 for f in range(4):
  for g in range(4):
   ranges=[range(ceil(bounds[f][k][0]-bounds[g][k][1]),floor(bounds[f][k][1]-bounds[g][k][0])+1) for k in (0,1)]
   for a in ranges[0]:
    for b in ranges[1]:
     if f==g and a==b==0:continue
     assert not overlap(tiles[f],[z+a*L1+b*L2 for z in tiles[g]])
     checked+=1
 verification=dict(lattice=[str(L1),str(L2)],edge_shift_coefficients=[[int(ZZ(x)),int(ZZ(y))] for x,y in coeff],polygons=[[str(z) for z in T] for T in tiles],covolume=str((L1.conjugate()*L2-L1*L2.conjugate())/(2*w**5)),total_tile_area=str(sum(sum((T[i].conjugate()*T[(i+1)%len(T)]-T[i]*T[(i+1)%len(T)].conjugate())/(4*w**5) for i in range(len(T))) for T in tiles)),finite_translate_pairs_checked=checked,nonoverlap=True,coverage_by_equal_area=True)
print(json.dumps(dict(status=('UNSAT_2P_2Q' if not records else 'EXACT_PERIODIC_WITNESS'),counts=counts,verification=verification,candidates=records,complete=True,software=version()),indent=2,default=lambda x:int(x)))
