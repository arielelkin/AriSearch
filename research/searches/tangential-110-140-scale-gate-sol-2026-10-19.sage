# Exact finite arithmetic checks; analytic global proof is in adjacent md.
from itertools import product
K=CyclotomicField(36); zz=K.gen(); ii=zz**9
AAz=AA(2*AA.cos(AA.pi()/18)) if False else None
# AA embedding through QQbar is exact, including trigonometric constants.
def cot_half(a):
    q=QQ(a)/360
    z=QQbar.zeta(q.denominator())**q.numerator()
    return AA(((z+1)/(z-1))*QQbar.gen())
# cot(theta/2)=i*(exp(i theta)+1)/(exp(i theta)-1)
u,v,w,z=[cot_half(a) for a in (110,120,100,140)]
a,b,c,h=1+u,2*u,u+v,1+v
f,d,e=2*w,w+z,2*z
assert 0<c<b<a and c<b<h and 0<e<d<f
angles=(90,100,110,120,140,180)
stars=[]
for n in product(range(5),repeat=6):
    if sum(x*y for x,y in zip(n,angles))==360:
        stars.append(tuple(x for x,y in zip(angles,n) for _ in range(y)))
# 180+180 is two flat sectors along a generic seam, not a vertex.
assert set(stars)=={(90,90,90,90),(90,90,180),(110,110,140),(100,120,140),(120,120,120),(180,180)}
print('PASS: exact inequalities and complete angle-star list')
