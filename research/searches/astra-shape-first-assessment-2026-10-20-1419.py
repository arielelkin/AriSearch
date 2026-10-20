"""Exact coordinates and omission triage for P5/H6 complementary seam proposal."""
from sage.all import AA, CyclotomicField
from importlib.util import spec_from_file_location,module_from_spec
K=CyclotomicField(36); z=K.gen(); I=z**9

def u(d):
    assert d%10==0
    return z**(d//10)
def re(w):return (w+w.conjugate())/2
def im(w):return (w-w.conjugate())/(2*I)
def cr(a,b):return re(a)*im(b)-im(a)*re(b)
a=u(0); b=u(140)+u(200); w=-u(60)-u(200)-u(260)
p=cr(w,b)/cr(a,b); q=cr(a,w)/cr(a,b); t=1+q; L=p+q
PL=(p,K(1),q,t,K(1)); HL=(L,K(1),L,t,p,t)
def polygon(dirs,lens):
    pts=[K(0)]
    for d,l in zip(dirs,lens):pts.append(pts[-1]+l*u(d))
    assert pts[-1]==0
    pts=tuple(pts[:-1]); n=len(pts)
    assert all(AA(l)>0 for l in lens)
    assert all(AA(cr(pts[(i+1)%n]-pts[i],pts[(i+2)%n]-pts[(i+1)%n]))>0 for i in range(n))
    return pts
P=polygon((0,60,140,200,260),PL)
H=polygon((0,60,120,180,240,300),HL)
assert len(set((K(1),p,q,t,L)))==5
spec=spec_from_file_location('rao','research/searches/convex-substitution-shapes.py')
mod=module_from_spec(spec);spec.loader.exec_module(mod)
angles=(80,120,100,120,120);hits=[]
for typ,(aeqs,leqs) in mod.RAO.items():
    for sign in (1,-1):
        for off in range(5):
            aa=[angles[(off+sign*i)%5] for i in range(5)]
            if not all(sum(c*x for c,x in zip(row,aa))==36*target for row,target in aeqs):continue
            smap=[(off+i)%5 if sign==1 else (off-i-1)%5 for i in range(5)]
            if all(sum((c*PL[i] for c,i in zip(row,smap)),K(0))==0 for row in leqs):hits.append((typ,sign,off))
print('p,q,t,L:',[AA(x) for x in (p,q,t,L)])
print('P monohedral classification hits:',hits)
print('P exact vertices:',P)
print('H exact vertices:',H)
assert hits == [(2,-1,4)]

# Replacement with a forced offset corner, not an equal-length closed seam.
w=-u(50)-3*u(200)/2-u(280)/2
p=cr(w,u(150))/cr(u(0),u(150));q=cr(u(0),w)/cr(u(0),u(150));L=p+q
w=-L*u(0)-u(50)-u(100)-u(230)/2
c=cr(w,u(280))/cr(u(180),u(280));e=cr(u(180),w)/cr(u(180),u(280))
PL=(p,K(1),q,K(3)/2,K(1)/2);HL=(L,K(1),K(1),c,K(1)/2,e)
P=polygon((0,50,150,200,280),PL)
H=polygon((0,50,100,180,230,280),HL)
angles=(100,130,80,130,100);hits=[]
for typ,(aeqs,leqs) in mod.RAO.items():
    for sign in (1,-1):
        for off in range(5):
            aa=[angles[(off+sign*i)%5] for i in range(5)]
            if not all(sum(cc*x for cc,x in zip(row,aa))==36*target for row,target in aeqs):continue
            smap=[(off+i)%5 if sign==1 else (off-i-1)%5 for i in range(5)]
            if all(sum((cc*PL[i] for cc,i in zip(row,smap)),K(0))==0 for row in leqs):hits.append((typ,sign,off))
print('REPLACEMENT p,q,L,c,e:',[AA(x) for x in (p,q,L,c,e)])
print('Replacement P monohedral classification hits:',hits)
assert not hits
from itertools import combinations_with_replacement
for total in (180,360):
    print('angle partitions of',total,[a for n in range(1,5) for a in combinations_with_replacement((80,100,130),n) if sum(a)==total])

# H alone is edge-to-edge (all angles >90). Its corner0 is100 and
# needs two130 corners. Their numerical side pairs must connect e to L.
HC=[(HL[(i-1)%6],HL[i]) for i in (1,2,4,5)]
bridges=[]
for a,b in HC:
    for x,y in ((a,b),(b,a)):
        for cc,dd in HC:
            for v,w in ((cc,dd),(dd,cc)):
                if x==e and y==v and w==L:bridges.append((x,y,w))
print('H-only completion of corner0:',bridges)
assert not bridges
assert len(set((p,q,L,c,e,K(1),K(1)/2,K(3)/2)))==8
