"""SUPERSEDED historical symmetric-P four-ring control; not a proof gate.
Canonical producer: contact-symmetric-two-private-symbolic-carrier.py.
A necessary local census only, not plane existence or all-family search.
Run sage through the locked mise/conda wrapper.
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
 # Normalize local copies; native corner indices elsewhere remain unchanged.
 if area(P)<0:P=list(reversed(P))
 if area(Q)<0:Q=list(reversed(Q))
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

r=AA(2).sqrt();u=AA(1);w=AA(QQ(5)/4)
bx=(3-r)/8;by=-QQ(5)/8-r/2
P=[vector(AA,[0,-w]),vector(AA,[bx,by]),vector(AA,[bx+r/2,-w/2]),vector(AA,[bx,-QQ(5)/8+r/2]),vector(AA,[0,0])]
H=(5+r)/4
lengths=[H,u,u,H,u,w,w,u]
dirs=[(1,0),(1/r,1/r),(0,1),(-1/r,1/r),(-1,0),(-1/r,-1/r),(0,-1),(1/r,-1/r)]
Q=[vector(AA,[0,0])]
for ell,d in zip(lengths,dirs):Q.append(Q[-1]+ell*vector(AA,d))
assert Q[-1]==Q[0];Q.pop()
check(P);check(Q)
acute=P[2]
assert(P[2]-P[1]).norm()==u==(P[3]-P[2]).norm()
p_lengths=[(P[(i+1)%5]-P[i]).norm() for i in range(5)]
assert all(H!=ell for ell in p_lengths)
assert p_lengths[0]==p_lengths[3] and p_lengths[4]==w
assert all(p_lengths[i]!=2*u for i in(0,3,4))
private={0,3};options=[]
for k,A in enumerate(Q):
 B=Q[(k+1)%8]
 opts=placements(Q if k in private else P,A,B)
 if k not in private:
  opts=[T for T in opts if (T[2]==A)==((k-1)%8 in private) and (T[2]==B)==((k+1)%8 in private)]
 options.append(opts)
assert [len(o) for o in options]==[2,1,1,2,1,1,1,1]

def violation(tiles,kinds):
 for i,F in enumerate(tiles):
  for j,G in enumerate(tiles[i+1:],i+1):
   I=intersect(F,G)
   if I and area(I)>0:return("overlap",i,j)
   for A in F:
    for B,C in zip(G,G[1:]+G[:1]):
     if cross(C-B,A-B)==0 and(A-B).dot_product(A-C)<0:return("partial",i,j)
   for A in G:
    for B,C in zip(F,F[1:]+F[:1]):
     if cross(C-B,A-B)==0 and(A-B).dot_product(A-C)<0:return("partial",i,j)
 corners={}
 for F,kind in zip(tiles,kinds):
  for i,v in enumerate(F):
   label="q" if kind=="Q" else("a" if i==2 else"p")
   corners.setdefault(tuple(v),{"q":0,"a":0,"p":0})[label]+=1
 for c in corners.values():
  if not(c["a"]==0 and c["p"]<=2 and c["q"]<=1) and not(c["p"]==0 and c["a"]<=1 and c["q"]<=2):return("badstar",c)
 return None
survivors=[]
for choices in product(*(range(len(o)) for o in options)):
 tiles=[Q]+[options[k][choice] for k,choice in enumerate(choices)]
 bad=violation(tiles,["Q"]+["Q" if k in private else"P" for k in range(8)])
 print("ring",choices,"=>",bad if bad else"necessary local survivor")
 if not bad:survivors.append(choices)
print("one exact symmetric-P pair; four rings; survivors",survivors)
