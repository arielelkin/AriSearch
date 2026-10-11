"""Fresh raw-slot and convex-clipping audit of the two extra-sharing Cairo roots.
No producer imports, no author overlap point, no solver.
"""
from itertools import combinations_with_replacement
from sage.all import QuadraticField, PolynomialRing, vector, matrix
K=QuadraticField(3, 's'); s=K.gen(); half=K(1)/2
r=(2*s-1)/(s+2); t=2-r
shapes=((K(1),r,(3*s-r)/2,(s*r-1)/2,K(2)),
        ((s*t-1)/2,(3*s-t)/2,t,K(1),K(2)))
assert s/3<r<1<t<2-s/3
for a,b,c,d,e in shapes:
    assert all(x>0 for x in (a,b,c,d,e))
    assert b-c==s*(d-a) and e==s*c+d-2*a
    assert len({a,b,c,d})==4
# Native slots are keyed by species and arm, never collapsed by equal length.
length={(z,i):shapes[z][i] for z in range(2) for i in range(4)}
perp=lambda key:(key[0],key[1]^1)
slots=tuple(length)
assert {(i,j) for i in range(4) for j in range(4)
        if shapes[0][i]==shapes[1][j]}=={(0,3),(1,0)}
# A right-corner event records the two native bank slots. Their perpendicular
# arms must coincide. Every self event is retained.
ledger={}
for x,y in combinations_with_replacement(slots,2):
    if length[perp(x)]==length[perp(y)]:
        ledger[(x,y)]=length[x]+length[y]
assert len(ledger)==10 and len(set(ledger.values()))==7
sums={x:{v for pair,v in ledger.items() if x in pair} for x in slots}
allowed=lambda x,y:length[x]==length[y] or bool(sums[x]&sums[y])
q_b=(1,1)
assert {y for y in slots if allowed(q_b,y)}=={(0,0),(1,1)}
hostable={x for pair,total in ledger.items() if total==2 for x in pair}
assert hostable=={(0,0),(0,1),(1,2),(1,3)}
# The e ray is a separate native120-to120 slot. No B-facing e bank exists.
corners=tuple((x,y) for z in range(2) for x,y in
              (((z,0),(z,4)),((z,1),(z,2)),((z,3),(z,4))))
assert not any(x in slots and y in slots and allowed(q_b,x) and allowed(q_b,y)
               for x,y in corners)
assert [(x,y) for x,y in corners if (x in hostable or x[1]==4)
        and (y in hostable or y[1]==4)]==[
            ((0,0),(0,4)),((1,3),(1,4))]
# P private core has singleton bank totals, e-incompatible; Qc full seam
# only has its own physical native mate.
for key in ((0,2),(0,3)):
    assert {y for y in slots if length[key]==length[y]}=={key}
    assert sums[key]=={2*length[key]}
    assert sum(v==2*length[key] for v in ledger.values())==1
    assert 2 not in sums[key]
assert {y for y in slots if length[y]==length[(1,2)]}=={(1,2)}
# P filler breakpoint: perpendicular Pb may equal Qa, but that event's
# bank total is 1+Qb, not2. Exhaust all same-length perpendicular mates.
perpendicular=(0,1)
breakpoint_mates=[]
for y in slots:
    if length[y]==length[perpendicular]:
        banks=(perp(perpendicular),perp(y))
        if length[banks[0]]+length[banks[1]]==2:
            breakpoint_mates.append(y)
assert breakpoint_mates==[(0,1)]
# Native reflection followed by species swap identifies the other root.
rev=lambda L:(L[3],L[2],L[1],L[0],L[4])
other_shapes=((K(1),t,(3*s-t)/2,(s*t-1)/2,K(2)),
              ((s*r-1)/2,(3*s-r)/2,r,K(1),K(2)))
assert tuple(map(rev,shapes))==other_shapes[::-1]
# Reconstruct the actual forced P quadrant and reflected mate. Clip their
# convex interiors instead of substituting the author's point W.
V=lambda x,y:vector(K,(x,y))
quarter=[V(0,0),V(shapes[0][3],0),V(shapes[0][3]+1,-s),
         V(shapes[0][3]+half,-3*s/2),V(0,-shapes[0][2])]
cross=lambda u,v:u[0]*v[1]-u[1]*v[0]
assert all(cross(quarter[(i+1)%5]-quarter[i],quarter[j]-quarter[i])<0
           for i in range(5) for j in range(5) if j not in (i,(i+1)%5))
# Derive the seam line from the quadrant's unit tip and axis notch.
x=V(-quarter[3][0],quarter[3][1]); axis=V(0,-shapes[0][2]); seam=axis-x
assert seam.dot_product(seam)==r*r
unit=seam/r
F=2*matrix(K,[[unit[0]*unit[0],unit[0]*unit[1]],
              [unit[1]*unit[0],unit[1]*unit[1]]])-matrix.identity(K,2)
reflected=[x+F*(v-x) for v in quarter]
assert x-F*x!=V(0,0)
# Clockwise source; reflected clipping polygon is counterclockwise.
poly=list(quarter)
for i in range(5):
    a,b=reflected[i],reflected[(i+1)%5]; edge=b-a
    value=lambda point:cross(edge,point-a)
    result=[]
    for j,u in enumerate(poly):
        v=poly[(j+1)%len(poly)]; fu,fv=value(u),value(v)
        if fu>=0: result.append(u)
        if (fu<0 and fv>0) or (fu>0 and fv<0):
            result.append(u+fu/(fu-fv)*(v-u))
    poly=result
    assert poly
area=abs(sum(cross(poly[i],poly[(i+1)%len(poly)]) for i in range(len(poly))))/2
assert area>0
# Fresh audit of the interval proof's repaired center formula, from the
# raw lower-left quadrant tip and the lower axis notch.
R=PolynomialRing(K,'z'); z=R.gen()
pt=vector(R,(-s*z/2,-3*s/2)); notch=vector(R,(0,-(3*s-z)/2))
u=(notch-pt)/z
reflection=2*matrix(R,[[u[0]*u[0],u[0]*u[1]],[u[1]*u[0],u[1]*u[1]]])-matrix.identity(R,2)
center=pt-reflection*pt
assert center==vector(R,((9-s*z)/4,(3*z-9*s)/4))
assert center==(3*s-z)*vector(R,(s/4,-K(3)/4))
assert 2-s/3<2<3*s
print('PASS: raw native-slot root ledger, only two notch types, Qc full-seam contradiction, P-only mate, reflected-root equivalence; strict actual overlap area='+str(area))
