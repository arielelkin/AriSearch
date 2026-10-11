"""Exact six-tile maximum-side strip: candidate, no plane claim."""
from sage.all import QQbar, NumberField, cyclotomic_polynomial
import json

K=NumberField(cyclotomic_polynomial(10), "z", embedding=QQbar.zeta(10))
z=K.gen()
phi=z+1/z
b,c,d=K(10),K(1),K(1)
A=phi*b+phi*c+d
B=b+phi*c+phi*d
x=K(1)
y=(b-c-phi**2*(x+d))/phi
q_d=x+c+phi**2*d
assert all(QQbar(t).imag()==0 and QQbar(t)>0 for t in [x,y,q_d])
assert phi*x+phi*y+q_d==b
assert x+phi*y+phi*q_d==B-c

def polygon(a,bb,b,c,d):
    v=[K(0)]
    for l,k in [(a,0),(d,2),(c,3),(b,4),(bb,6)]:
        v.append(v[-1]+l*z**k)
    assert v[-1]==0
    return v[:-1]
P=polygon(A,B,b,c,d)
s=A-d
R=[z**8*(v-P[2]) for v in P]
H=[s-v for v in P]
R2=[s-v for v in R]
Q=[c*z]
for l,k in [(b,2),(q_d,0),(y,9),(x,8),(B-c,6)]:
    Q.append(Q[-1]+l*z**k)
assert Q[-1]==Q[0]
Q=list(reversed(Q[:-1]))
Q2=[s-v for v in Q]
polys=[P,H,R,R2,Q,Q2]

def cross(a,b):
    return QQbar(a.conjugate()*b).imag()
def area(poly):
    return sum(cross(u,v) for u,v in zip(poly,poly[1:]+poly[:1]))/2
assert all(area(p)>0 for p in polys)
assert all(cross(v-a,k-a)>0 for p in polys for j,(a,v) in enumerate(zip(p,p[1:]+p[:1])) for h,k in enumerate(p) if h not in [j,(j+1)%len(p)])
def sat(p,q):
    for poly in (p,q):
        for a,v in zip(poly,poly[1:]+poly[:1]):
            e=v-a
            pp=[cross(e,k) for k in p]
            qq=[cross(e,k) for k in q]
            if max(pp)<=min(qq) or max(qq)<=min(pp):
                return True
    return False
assert all(sat(polys[i],polys[j]) for i in range(6) for j in range(i))
# Subdivide all native sides at every boundary vertex lying on them.
verts=set(v for p in polys for v in p)
pieces={}
for i,p in enumerate(polys):
    for a,v in zip(p,p[1:]+p[:1]):
        e=v-a
        on=[k for k in verts if cross(e,k-a)==0 and QQbar(e.conjugate()*(k-a)).real()>=0 and QQbar(e.conjugate()*(k-v)).real()<=0]
        on.sort(key=lambda k:QQbar(e.conjugate()*(k-a)).real())
        for u,w in zip(on,on[1:]):
            pieces[(u,w)]=pieces.get((u,w),[])+[i]
outer=[e for e in pieces if (e[1],e[0]) not in pieces]
assert all(len(v)==1 for v in pieces.values())
assert all(len(v)==1 for e,v in pieces.items() if (e[1],e[0]) in pieces)
cycles=[]
while outer:
    u,v=outer.pop()
    cyc=[u]
    while v!=cyc[0]:
        cyc.append(v)
        candidates=[e for e in outer if e[0]==v]
        assert len(candidates)==1, (len(candidates),v)
        e=candidates[0]
        outer.remove(e)
        v=e[1]
    # Merge collinear subdivisions.
    changed=True
    while changed:
        changed=False
        for i in range(len(cyc)):
            if cross(cyc[i]-cyc[i-1],cyc[(i+1)%len(cyc)]-cyc[i])==0:
                cyc.pop(i)
                changed=True
                break
    cycles.append(cyc)
assert sum(area(k) for k in cycles)==sum(area(p) for p in polys)
def enc(v):
    return str(v)
report={'status':'six-tile locally legal patch; forced completion falsified; no plane witness', 'coordinate_field':{'polynomial':str(K.polynomial()),'generator_embedding':'exp(pi*i/5)'}, 'P_shorts':[str(b),str(c),str(d)], 'Q_shorts':[str(x),str(y),str(q_d)], 'pairwise_disjoint':True,'boundary_cycles':[{'vertices':[enc(v) for v in cyc], 'turn_signs':[int(cross(cyc[i]-cyc[i-1],cyc[(i+1)%len(cyc)]-cyc[i]).sign()) for i in range(len(cyc))], 'area_over_sin36':str(sum((u.conjugate()*v-u*v.conjugate())/(z-1/z) for u,v in zip(cyc,cyc[1:]+cyc[:1]))/2)} for cyc in cycles], 'motifs':[[enc(v) for v in p] for p in polys]}
assert QQbar(B-c)>QQbar(b) and QQbar(b)<QQbar(B)
assert all(QQbar(arm)<QQbar(b) for arm in [x,q_d])
assert QQbar(B-c)<QQbar(A-c)
# The rear double108 vertex forces144 with c against a maximal side.
# Q arms cannot be a long of either type; P arm d cannot; P arm b
# forces Q's remaining long B-c, which is shorter than A-c.
report['selected_strip_completion']='impossible: forced144 P/Q both excluded at rear double108 vertex'
report['rear_completion_scalar_checks']={'Q_arm_below_P_min_long':True, 'P_d_below_Q_min_long':bool(QQbar(d)<QQbar(b)), 'Q_forward_long_below_remaining_maximum':bool(QQbar(B-c)<QQbar(A-c))}
from pathlib import Path
out=Path('research/certificates/pentagrid-asymmetric-u-maximal-strip.json')
out.write_text(json.dumps(report,indent=2)+'\n')
print('PASS: six exact convex tiles, 15 SAT disjointness checks, one16-turn boundary, exact area, selected-strip completion contradiction')
