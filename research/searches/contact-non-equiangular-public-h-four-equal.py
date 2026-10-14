"""One exact public-H incidence change. Complete16 w-dimer/twoQ patch domain.
No H metric sweep and no finite patch asserted to extend to a plane.
"""
from sage.all import AA, QQ, vector, matrix
from itertools import product
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def J(a):return vector(AA,[-a[1],a[0]])
def area(P):return sum(cross(a,b) for a,b in zip(P,P[1:]+P[:1]))/2

def check(P):
 for i,a in enumerate(P):
  b=P[(i+1)%len(P)]
  for j,c in enumerate(P):
   if j not in(i,(i+1)%len(P)):assert cross(b-a,c-a)>0

def intersect(P,Q):
 P=P if area(P)>0 else P[::-1]
 Q=Q if area(Q)>0 else Q[::-1]
 out=list(P)
 for a,b in zip(Q,Q[1:]+Q[:1]):
  if not out:break
  prev=out[-1];dp=cross(b-a,prev-a);new=[]
  for cur in out:
   dc=cross(b-a,cur-a)
   if(dp<0)!=(dc<0):new.append(prev+(cur-prev)*dp/(dp-dc))
   if dc>=0:new.append(cur)
   prev=cur;dp=dc
  out=new
 return out

def canonical(P):return tuple(sorted(tuple(v) for v in P))
def placements(S,A,B):
 """Every full-side opposite placement, allowing all native slots/reflections."""
 seen={}
 for i,sa in enumerate(S):
  sb=S[(i+1)%len(S)];e=sb-sa
  if e.dot_product(e)!=(B-A).dot_product(B-A):continue
  e=e/e.norm(); E=matrix(AA,[list(e),list(J(e))]).transpose()
  for ta,tb in((A,B),(B,A)):
   f=(tb-ta)/(tb-ta).norm()
   for det in(-1,1):
    F=matrix(AA,[list(f),list(det*J(f))]).transpose()*E.transpose()
    T=[ta+F*(p-sa) for p in S]
    centre=sum(T,vector(AA,[0,0]))/len(T)
    if cross(B-A,centre-A)>=0:continue
    seen[canonical(T)]=T
 return list(seen.values())



r=AA(2).sqrt();c=((2+r)/4).sqrt();t=((2-r)/4).sqrt();w=r-2*t
P=[vector(AA,[0,0])]
for ell,d in zip([1,1,1,1,w],[(c,-t),(1/r,1/r),(-1/r,1/r),(-c,-t),(0,-1)]):P.append(P[-1]+ell*vector(AA,d))
assert P[-1]==P[0];P.pop()
Q=[vector(AA,[0,0])]
for d in[(c,t),(1/r,1/r),(0,1),(-1/r,1/r),(-c,-t),(-1/r,-1/r),(0,-1),(1/r,-1/r)]:Q.append(Q[-1]+vector(AA,d))
assert Q[-1]==Q[0];Q.pop();check(P);check(Q)
assert 0<w<1
assert [(P[(i+1)%5]-P[i]).norm() for i in range(5)]==[1,1,1,1,w]
assert all((Q[(i+1)%8]-Q[i]).norm()==1 for i in range(8))
Ph=[P[0]+P[4]-p for p in P]
Wmates=placements(P,P[4],P[0]);assert len(Wmates)==1 and canonical(Wmates[0])==canonical(Ph)
corneroptions={}
for at,A,B in[(P[0],P[1],Ph[3]),(P[4],P[3],Ph[1])]:
 opts=[]
 for T in placements(Q,at,A)+placements(Q,A,at):
  if at not in T or B not in T:continue
  j=T.index(at)
  if j not in[2,3,6,7]:continue
  if{tuple(T[j-1]),tuple(T[(j+1)%8])}!={tuple(A),tuple(B)}:continue
  if canonical(T) not in[canonical(S) for S in opts]:opts.append(T)
 assert len(opts)==4
 corneroptions[tuple(at)]=opts
print("PASS: unique actual whole-w P-dimer and four exact Q135 placements at each concave union endpoint")
patches=[]
for i,j in product(range(4),repeat=2):
 tiles=[P,Ph,corneroptions[tuple(P[0])][i],corneroptions[tuple(P[4])][j]]
 assert all(not(I:=intersect(F,G)) or area(I)==0 for a,F in enumerate(tiles) for G in tiles[a+1:])
 patches.append((i,j))
assert len(patches)==16
print("PASS: complete4x4 native endpoint domain has16 disjoint P-dimer/twoQ patches")
# Two complete palette potentials, used analytically to select clean disks.
units=[4,5,5,6,7];score1=[4,1,1,-2,-5];score2=[1,0,0,0,-1]
full=[C for C in product(range(5),repeat=5) if sum(a*b for a,b in zip(C,units))==16]
flat=[C for C in product(range(5),repeat=5) if sum(a*b for a,b in zip(C,units))==8]
assert flat==[(2,0,0,0,0)]
assert all(sum(a*b for a,b in zip(C,score1))>=0 and sum(a*b for a,b in zip(C,score2))>=0 for C in full+flat)
assert sum(score1[i] for i in[0,1,1,1,1])==8
assert sum(score1[i] for i in[2,4,3,3,2,4,3,3])==-16
assert sum(score2[i] for i in[0,1,1,1,1])==1
assert sum(score2[i] for i in[2,4,3,3,2,4,3,3])==-2
print("PASS: both full/flat native score enumerations and per-tile totals(8,-16),(1,-2)")
print("Parea",area(P),"Qarea",area(Q),"w",w)


# Canonical periodic plane certificate; no radius/partner search at replay.
R=matrix(AA,[[t,-c],[c,t]])
assert R.transpose()*R==matrix.identity(AA,2) and R.det()==1
S=Q[1]-R*P[2];S1=Q[1]+R*P[1]
reps=[Q,[R*p+S for p in P],[-R*p+S1 for p in P]]
L=Q[3];U=Q[4]-S-S1
assert S1-S-R*(P[0]+P[4])==L
pairs=[((0,0),(1,2),(0,0)),((0,1),(2,0),(0,0)),((0,2),(1,3),(1,0)),((0,3),(0,7),(1,0)),((0,4),(2,2),(0,1)),((0,5),(1,0),(0,1)),((0,6),(2,3),(-1,1)),((1,1),(2,1),(0,0)),((1,4),(2,4),(-1,0))]
seen=[]
for(f,i),(g,j),(m,n) in pairs:
 seen.extend([(f,i),(g,j)]);shift=m*L+n*U
 assert reps[f][i]==reps[g][(j+1)%len(reps[g])]+shift
 assert reps[f][(i+1)%len(reps[f])]==reps[g][j]+shift
assert len(set(seen))==18 and set(seen)=={(f,i)for f,F in enumerate(reps)for i in range(len(F))}
assert area(reps[1])==area(reps[2])==area(P)
assert cross(L,U)>0 and cross(L,U)==sum(area(F) for F in reps)
print("PASS: explicit publicH1 Q/twoP carrier;9 reversed pairs/18edges/36 exact coordinates;positive area/covolume identity")
# Optional retained clean-layer local reconnaissance, not needed by carrier.
import sys
if "--rings" in sys.argv:
 # Clean-field next layer: everyP90 has oneQ157. Complete4x4 high-corner
 # alternatives are checked against every w-dimer/twoQ patch, using exactSAT.
 def overlaps(F,G):
  for A in[F,G]:
   for a,b in zip(A,A[1:]+A[:1]):
    edge=b-a;I=[cross(edge,p) for p in F];J=[cross(edge,p) for p in G]
    if max(I)<=min(J) or max(J)<=min(I):return False
  return True
 high=[]
 for F in[P,Ph]:
  O=[]
  for i in[1,2]:
   for T in placements(Q,F[i],F[i+1]):
    if F[2] not in T:continue
    if T.index(F[2]) not in[1,5]:continue
    if canonical(T) not in[canonical(S) for S in O]:O.append(T)
  assert len(O)==4
  high.append(O)
 layer_survivors=[]
 for i,j in patches:
  base=[P,Ph,corneroptions[tuple(P[0])][i],corneroptions[tuple(P[4])][j]]
  for a,b in product(range(4),repeat=2):
   tiles=base+[high[0][a],high[1][b]]
   if all(not overlaps(F,G) for k,F in enumerate(tiles) for G in tiles[k+1:]):layer_survivors.append((i,j,a,b))
 print("clean high-corner layer survivors",layer_survivors)
 print("complete16x16 domain size256; surviving disjoint six-tile patches",len(layer_survivors))

 assert len(layer_survivors)==64
