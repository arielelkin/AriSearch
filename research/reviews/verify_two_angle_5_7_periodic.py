"""Independent exact checker of the retained periodic placement certificate.
No imports from the generator. Convexity, congruence, all possible overlaps,
and exact area density prove the whole-plane periodic tiling.
"""
from pathlib import Path
from sage.all import QQ, QQbar, AA, NumberField, PolynomialRing
import json
root = Path(__file__).resolve().parents[2]
c = json.loads((root/'research/certificates/two_angle_5_7_periodic.json').read_text())
R=PolynomialRing(QQ,'x'); x=R.gen()
f=R([QQ(t) for t in c['field']['polynomial_coefficients']])
assert f == x**12-x**10+x**8-x**6+x**4-x**2+1
lo,hi=map(QQ,c['field']['root_real_interval']); ilo,ihi=map(QQ,c['field']['root_imag_interval'])
roots=[r for r in f.roots(QQbar,multiplicities=False) if lo<r.real()<hi and ilo<r.imag()<ihi]
assert len(roots)==1
omega=roots[0]; K=NumberField(f,'w'); w=K.gen()
embed=K.hom([omega],QQbar)
def value(a):
    t=embed(a)
    assert t.imag()==0
    return AA(t.real())
def sign(a):
    if a==0: return 0
    return 1 if value(a)>0 else -1
unpack=lambda a: K([QQ(t) for t in a])
pt=lambda a: (unpack(a[0]),unpack(a[1]))
add=lambda a,b:(a[0]+b[0],a[1]+b[1])
sub=lambda a,b:(a[0]-b[0],a[1]-b[1])
cross=lambda a,b:a[0]*b[1]-a[1]*b[0]
u,v=map(pt,c['lattice']); det=cross(u,v)
assert det!=0
polys=[list(map(pt,t['vertices'])) for t in c['tiles']]
assert [len(p) for p in polys]==[7,7,5,5]
for coordinate in [t for point in [u,v]+[q for poly in polys for q in poly] for t in point]:
    value(coordinate)
assert all(value(unpack(t))>0 for t in c['lengths'])
areas=[]
for poly in polys:
    turns=[sign(cross(sub(poly[(i+1)%len(poly)],poly[i]),sub(poly[(i+2)%len(poly)],poly[(i+1)%len(poly)]))) for i in range(len(poly))]
    assert set(turns) in ({1},{-1})
    orientation=turns[0]
    # Strict supporting-side inequalities certify global convexity and simplicity.
    for j in range(len(poly)):
        e=sub(poly[(j+1)%len(poly)],poly[j])
        for k in range(len(poly)):
            if k not in (j,(j+1)%len(poly)):
                assert sign(cross(e,sub(poly[k],poly[j])))==orientation
    twice=sum(cross(poly[i],poly[(i+1)%len(poly)]) for i in range(len(poly)))
    areas.append(twice if sign(twice)>0 else -twice)
assert sum(areas)==(2*det if sign(det)>0 else -2*det)
# Verify same-type tile congruence by explicit half-turn, independent of generator formulas.
for a,b in [(polys[0],polys[1]),(polys[2],polys[3])]:
    center_sum=add(a[0],b[0])
    assert all(add(pa,pb)==center_sum for pa,pb in zip(a,b))
# H edges rotate by 2pi/7. P exterior angles are three or two pi/7.
iunit=w**7
squared=lambda a:a[0]**2+a[1]**2
cos=lambda z:(z+z**(-1))/2
sin=lambda z:(z-z**(-1))/(2*iunit)
for poly,exponents in [(polys[0],[4]*7),(polys[2],[4,6,6,6,6])]:
    for j,e in enumerate(exponents):
        a=sub(poly[j],poly[j-1]); b=sub(poly[(j+1)%len(poly)],poly[j])
        dot=a[0]*b[0]+a[1]*b[1]; turn=cross(a,b)
        # Match positive exterior turn magnitude without taking square roots.
        ce,se=cos(w**e),sin(w**e)
        assert dot*se == (turn if sign(turn)>0 else -turn)*ce
        assert sign(dot)==sign(ce)
# Bound possible shifts by exact coordinates in the lattice basis.
boxes=[]
for poly in polys:
    xy=[(cross(p,v)/det,cross(u,p)/det) for p in poly]
    boxes.append([(min(value(t[j]) for t in xy),max(value(t[j]) for t in xy)) for j in (0,1)])
def no_interior_overlap(a,b):
    for poly in (a,b):
        for j in range(len(poly)):
            e=sub(poly[(j+1)%len(poly)],poly[j])
            aa=[value(cross(e,t)) for t in a]; bb=[value(cross(e,t)) for t in b]
            if max(aa)<=min(bb) or max(bb)<=min(aa): return True
    return False
checks=0; ranges=[]
for i,a in enumerate(polys):
    for j,b in enumerate(polys):
        # If translated boxes overlap, m is in [amin-bmax,amax-bmin].
        bounds=[(int((boxes[i][q][0]-boxes[j][q][1]).ceil()),int((boxes[i][q][1]-boxes[j][q][0]).floor())) for q in (0,1)]
        ranges.append({"i":i,"j":j,"m":list(bounds[0]),"n":list(bounds[1])})
        for m in range(bounds[0][0],bounds[0][1]+1):
            for n in range(bounds[1][0],bounds[1][1]+1):
                if i==j and m==n==0: continue
                shift=(m*u[0]+n*v[0],m*u[1]+n*v[1])
                assert no_interior_overlap(a,[add(t,shift) for t in b]),(i,j,m,n)
                checks+=1
# Areas differ, so P and H are distinct congruence classes.
assert areas[0]!=areas[2]
print(json.dumps({"verdict":"PASS","overlap_checks":checks,"pair_shift_domains":ranges,
    "plane_coverage":"disjoint periodic interiors + exact area density + closed union",
    "angle_signature":"P: four 4pi/7, one 5pi/7; H: seven 5pi/7"},indent=2,sort_keys=True))
