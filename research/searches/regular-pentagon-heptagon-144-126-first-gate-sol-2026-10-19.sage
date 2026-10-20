from sage.all import *
import json
K=CyclotomicField(20); w=K.gen(); I=w**5
R=AA
re=lambda z: R((z+z.conjugate())/2)
im=lambda z: R((z-z.conjugate())/(2*I))
cross=lambda a,b: re((a.conjugate()*b-a*b.conjugate())/(2*I))
u=[w**(3*i) for i in range(7)]
S=sum(u[::2]); t=-S/sum(u[1::2]); assert t==t.conjugate() and re(t)>0
# x=t+h, y=t+k*h, z=t+h; kernel follows by symmetry.
k=-(u[1]+u[5])/u[3]; assert k==k.conjugate() and re(k)>0
assert u[1]+k*u[3]+u[5]==0
length=[K(1),t,K(1),t,K(1),t,K(1)]
Q=[K(0)]
for l,d in zip(length,u): Q.append(Q[-1]+l*d)
assert Q[-1]==0; Q=Q[:-1]
P=[K(0)]
for j in range(5): P.append(P[-1]+w**(4*j))
assert P[-1]==0; P=P[:-1]
def place(poly,j,a,b,reflect):
    c,d=poly[j],poly[(j+1)%len(poly)]
    if reflect:
        f=(b-a)/(d-c).conjugate()
        return [a+f*(v-c).conjugate() for v in poly]
    f=(a-b)/(d-c)
    return [b+f*(v-c) for v in poly]
def overlap(A,B):
    for C in (A,B):
        for j,a in enumerate(C):
            d=C[(j+1)%len(C)]-a
            va=[cross(d,x-a) for x in A]; vb=[cross(d,x-a) for x in B]
            if max(va)<=min(vb) or max(vb)<=min(va): return False
    return True
Ps=[place(P,0,Q[j],Q[(j+1)%7],True) for j in (0,2,4,6)]
base=[Q]+Ps
pairs=[[i,j] for i in range(5) for j in range(i) if overlap(base[i],base[j])]
joins=[]
for j in (1,3,5):
    for k0 in (1,3,5):
        for reflect in (False,True):
            N=place(Q,k0,Q[j],Q[(j+1)%7],reflect)
            hits=[i for i,T in enumerate(base) if overlap(N,T)]
            joins.append(dict(target=j,source=k0,reflect=reflect,overlaps=hits))
from itertools import product
options={j:[place(Q,k0,Q[j],Q[(j+1)%7],r) for k0 in (1,3,5) for r in (False,True)] for j in (1,3,5)}
compat={}
for a,b in ((1,3),(1,5),(3,5)):
 compat[(a,b)]={(i,j):not overlap(options[a][i],options[b][j]) for i in range(6) for j in range(6)}
stars=[list(c) for c in product(range(6),repeat=3) if compat[(1,3)][(c[0],c[1])] and compat[(1,5)][(c[0],c[2])] and compat[(3,5)][(c[1],c[2])]]
# Exact boundary contacts of representative tuple (0,0,0).
star=base+[options[j][0] for j in (1,3,5)]
def contacts(A,B):
    pts=set()
    for C,D in ((A,B),(B,A)):
      for v in C:
       for j,a in enumerate(D):
        b=D[(j+1)%len(D)]; q=(v-a)/(b-a)
        if q==q.conjugate() and 0<=re(q)<=1: pts.add(v)
    return sorted(str(v) for v in pts)
contact_record=[dict(a=i,b=j,points=contacts(star[i],star[j])) for i in range(8) for j in range(i)]
angles=[]
for p in range(5):
 for a in range(4):
  for b in range(4):
   if 108*p+144*a+126*b==360: angles.append([p,a,b])
assert angles==[[1,0,2],[2,1,0]]
assert not pairs
out=dict(field='CyclotomicField(20), w=exp(2*pi*i/20)',equal_QQ_length=str(t),kernel_coefficient=str(k),parameter_domain='h > max(-t,-t/k)',Q=[str(v) for v in Q],angle_solutions=angles,base_overlap_pairs=pairs,joins=joins,simultaneous_stars=stars,representative_star=dict(tuple=[0,0,0],polygons=[[str(v) for v in T] for T in star],contacts=contact_record),versions=dict(sage=version()),scope='one Q, four forced P, three immediate adjacent Q; 216 tuples; no patch growth')
print(json.dumps(out,indent=2,default=lambda x:int(x)))
