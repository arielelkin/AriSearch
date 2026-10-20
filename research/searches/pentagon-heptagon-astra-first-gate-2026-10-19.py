"""Finite exact first gate; no plane-extension claim. Runtime cap: 120 seconds.
Domain: 7 angle multiplicities, total <=6, sums 180 or 360; indexed
stars are all assignments of equal-angle indices to those occurrences.
Metric: one unit-incircle realization per cyclic angle word in QQ(zeta_72).
Motif: exactly three tiles, centered at star (P0,Q0,Q0).
"""
import itertools, json, time
from pathlib import Path
import sympy as s
started=time.monotonic()
x=s.Symbol('x'); mod=s.Poly(s.cyclotomic_poly(72,x),x,domain=s.QQ)
def r(a): return s.rem(s.Poly(a,x,domain=s.QQ),mod).as_expr()
def add(a,b): return r(a+b)
def mul(a,b): return r(a*b)
def div(a,b): return mul(a,s.invert(b,mod.as_expr(),x))
def z(k): return r(x**(k%72))
def co(k): return r((z(k)+z(-k))/2)
def si(k): return div(r((z(k)-z(-k))/2),z(18))
def dot(a,b): return add(mul(a[0],b[0]),mul(a[1],b[1]))
def cross(a,b): return add(mul(a[0],b[1]),-mul(a[1],b[0]))
def coeff(a): return [str(s.Poly(a,x).nth(i)) for i in range(24)]
def metric(angles):
    dirs=[0]
    for a in angles[1:]: dirs.append((dirs[-1]+180-a)%360)
    normals=[(-si(d//5),co(d//5)) for d in dirs]
    vertices=[]
    for i,b in enumerate(normals):
        a=normals[i-1]; det=cross(a,b)
        vertices.append((div(a[1]-b[1],det),div(b[0]-a[0],det)))
    lengths=[]
    for i,d in enumerate(dirs):
        u=vertices[i]; v=vertices[(i+1)%len(angles)]
        e=(r(v[0]-u[0]),r(v[1]-u[1])); direction=(co(d//5),si(d//5))
        length=dot(e,direction)
        assert all(r(e[j]-mul(length,direction[j]))==0 for j in range(2))
        # Unit incircle formula proves positivity without floating arithmetic.
        k=(180-angles[i])//5; h=(180-angles[(i+1)%len(angles)])//5
        assert r(length-add(div(si(k),1+co(k)),div(si(h),1+co(h))))==0
        lengths.append(length)
    assert all(add(sum((mul(lengths[i],(co(dirs[i]//5),si(dirs[i]//5))[j]) for i in range(len(angles))),s.Integer(0)),0)==0 for j in range(2))
    return vertices,lengths
angles=[60,105,115,125,135,120,150]
stars=[]
for c in itertools.product(range(7),repeat=7):
    if sum(c)>6: continue
    total=sum(a*n for a,n in zip(angles,c))
    if total in (180,360): stars.append({'multiplicities':list(c),'flat_host':total==180})
index={'60':['P0'],'105':['P1'],'115':['P2'],'125':['P3'],'135':['P4'],
       '120':['Q2','Q3','Q4','Q5','Q6'],'150':['Q0','Q1']}
polys={}
raw={}
for name,word in [('P',[60,105,115,125,135]),('Q',[150,150,120,120,120,120,120])]:
    v,l=metric(word); raw[name]=v
    polys[name]={'angles':word,'vertices':[[coeff(t) for t in p] for p in v], 'edge_lengths':[coeff(t) for t in l]}
# Translate corner zero to origin and rotate its outgoing ray to 0,60,210.
# Its interior occupies [ray,ray+angle0]; these three intervals partition 360.
motif=[]
for name,deg in [('P',0),('Q',60),('Q',210)]:
    v=raw[name]; c=co(deg//5); t=si(deg//5)
    pts=[]
    for p in v:
        u=(r(p[0]-v[0][0]),r(p[1]-v[0][1]))
        pts.append((r(mul(c,u[0])-mul(t,u[1])),r(mul(t,u[0])+mul(c,u[1]))))
    motif.append({'tile':name,'rotation_degrees':deg,'vertices':[[coeff(t) for t in p] for p in pts]})
# Complete labeled orientation-preserving 12-halfedge pairings (11!!).
def pairings(items):
    if not items:
        yield []; return
    a=items[0]
    for b in items[1:]:
        for rest in pairings([v for v in items[1:] if v!=b]): yield [(a,b)]+rest
dirs=[0,15,28,39,48,0,6,18,30,42,54,66]
counts={"pairings":0,"direction_survivors":0,"reflected_direction_survivors":0}
for pairs in pairings(list(range(12))):
    counts["pairings"]+=1
    for reflection,label in [(1,"direction_survivors"),(-1,"reflected_direction_survivors")]:
        phase=None; good=True
        for a,b in pairs:
            if (a<5)==(b<5):
                if (dirs[a]-dirs[b])%72!=36: good=False; break
            else:
                if a>=5: a,b=b,a
                value=(dirs[a]+36-reflection*dirs[b])%72
                if phase is None: phase=value
                elif phase!=value: good=False; break
        counts[label]+=int(good)
assert counts=={"pairings":10395,"direction_survivors":0,"reflected_direction_survivors":0}
assert time.monotonic()-started<120
out={'field':{'polynomial':str(mod.as_expr()),'root':'exp(2*pi*i/72)','basis':'1,z,...,z^23'},
     'angle_order':angles,'index_expansion':index,'stars':stars,'polygons':polys,'three_tile_motif':motif,
     'one_P_one_Q_native_torus':counts,
     'scope':'Exact finite local feasibility only; plane tilability unresolved.'}
path=Path('research/certificates/pentagon-heptagon-astra-first-gate-2026-10-19.json')
path.write_text(json.dumps(out,indent=2)+'\n')
print('verified',len(stars),'angle multisets; exact metrics and three-tile motif; seconds',round(time.monotonic()-started,3))
