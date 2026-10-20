"""Exact first gate for q=1/2 resonant P5/H6 metric."""
from importlib.util import spec_from_file_location, module_from_spec
from sage.all import AA, CyclotomicField

K=CyclotomicField(36); z=K.gen(); I=z**9
u=lambda d:z**(d//10)
re=lambda w:(w+w.conjugate())/2
im=lambda w:(w-w.conjugate())/(2*I)
cr=lambda a,b:re(a)*im(b)-im(a)*re(b)

def solve(a,b,w):
    determinant=cr(a,b)
    assert determinant!=0
    return cr(w,b)/determinant,cr(a,w)/determinant

def polygon(dirs,lens):
    pts=[K(0)]
    for d,l in zip(dirs,lens):pts.append(pts[-1]+l*u(d))
    assert pts[-1]==0
    pts=tuple(pts[:-1]); n=len(pts)
    assert all(AA(x)>0 for x in lens)
    assert all(AA(cr(pts[(i+1)%n]-pts[i],pts[(i+2)%n]-pts[(i+1)%n]))>0 for i in range(n))
    return pts

q=K(1)/2
p,s=solve(u(0),u(200),-u(50)-q*u(150)-u(280)/2)
L=p+q
c,e=solve(u(180),u(280),-L-u(50)-u(100)-u(230)/2)
PL=(p,K(1),q,s,K(1)/2)
HL=(L,K(1),K(1),c,K(1)/2,e)
P=polygon((0,50,150,200,280),PL)
H=polygon((0,50,100,180,230,280),HL)

# Enumerate all 15 reviewed Rao family rows and 10 dihedral relabelings.
spec=spec_from_file_location('rao','research/searches/convex-substitution-shapes.py')
mod=module_from_spec(spec); spec.loader.exec_module(mod)
angles=(100,130,80,130,100)
hits=[]
for typ,(angle_equations,length_equations) in mod.RAO.items():
    for sign in (1,-1):
        for offset in range(5):
            amap=[(offset+sign*i)%5 for i in range(5)]
            if not all(sum(coef*angles[j] for coef,j in zip(row,amap))==36*target
                       for row,target in angle_equations):continue
            smap=[(offset+i)%5 if sign==1 else (offset-i-1)%5 for i in range(5)]
            if all(sum((coef*PL[j] for coef,j in zip(row,smap)),K(0))==0
                   for row in length_equations):hits.append((typ,sign,offset))
assert hits==[(2,1,0)]
assert angles[0]+angles[1]+angles[3]==360
assert PL[2]==PL[4]==K(1)/2

print('p,q,s,L,c,e:',[AA(x) for x in (p,q,s,L,c,e)])
print('Exact closure, positive sides, strict convexity: PASS')
print('Rao hits over 15 families x 10 dihedral relabelings:',hits)
print('Type 2: A+B+D=360, c=e=P2=P4=1/2')
print('STOP: periodic P-only omission before mixed geometry gate')
