from sage.all import *
# One exact algebraic witness; no enumeration or solver.
r=AA(5).sqrt()
c=(1+r)/4; d=(r-1)/4
s=(10-2*r).sqrt()/4; t=(10+2*r).sqrt()/4
e=vector(AA,[1,0]); zero=vector(AA,[0,0])
v1=vector(AA,[c,s]);v2=vector(AA,[d,t]);v3=vector(AA,[-d,t])
P=[zero,e,v1,v2,v3]
H=[v1,v2,v3,e-v1,e-v2,e-v3]
def cross(u,v): return u[0]*v[1]-u[1]*v[0]
def area(p): return sum(cross(p[i],p[(i+1)%len(p)]) for i in range(len(p)))/2
def strict(p): return all(cross(p[(i+1)%len(p)]-p[i],p[(i+2)%len(p)]-p[(i+1)%len(p)])>0 for i in range(len(p)))
assert strict(P) and strict(H)
assert all(H[i]+H[i+3]==e for i in range(3))
assert area(H)==2*area(P)>0
L1=H[0]+H[1]-e;L2=H[1]+H[2]-e
assert abs(cross(L1,L2))==area(H)
assert H[3]+L1==H[1] and H[4]+L1==H[0]
assert H[4]+L2==H[2] and H[5]+L2==H[1]
assert H[5]+(L2-L1)==H[3] and H[0]+(L2-L1)==H[2]
assert v1.norm()==v2.norm()==v3.norm()==1
assert (v1-e).norm()==(v2-v1).norm()==(v3-v2).norm()==(r-1)/2
print('PASS: strict pentagon, half-turn hexagon, edge-pair lattice, exact area equality')
