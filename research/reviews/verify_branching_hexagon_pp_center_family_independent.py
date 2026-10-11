"""Fresh pp-center family audit; raw geometry and indexed carrier, no author imports.
Replay: conda run --no-capture-output -n arisearch python research/reviews/verify_branching_hexagon_pp_center_family_independent.py
"""
from pathlib import Path
import json
from collections import Counter, defaultdict
from sage.all import QQ, QQbar, AA, PolynomialRing, matrix, ZZ, lcm, CyclotomicField
root=Path(__file__).parents[1]
raw=json.loads((root/'certificates/branching-hexagon-new-two-run-four-face-periodic.json').read_text())
cert=json.loads((root/'certificates/branching-hexagon-two-run-pp-center-periodic-family.json').read_text())
faces=raw['faces']; pairs=raw['paired_edges']
assert [f['species'] for f in faces]==['A','A','B','B']
assert all(f['mirror'] is False for f in faces)
words=[list('pqpqpq'),list('pppqqq')]
assert all(f['labels']==words[0 if f['species']=='A' else 1] for f in faces)
used=Counter();links=defaultdict(list);dual=defaultdict(set)
for (u,a),(v,b) in pairs:
    used[u,a]+=1;used[v,b]+=1
    assert faces[u]['labels'][a]==faces[v]['labels'][b]
    dual[u].add(v);dual[v].add(u)
    for x,y in (((u,a),(v,(b+1)%6)),((u,(a+1)%6),(v,b))):
        links[x].append(y);links[y].append(x)
assert len(pairs)==12 and used==Counter({(f,i):1 for f in range(4) for i in range(6)})
def component(start,graph):
    seen=set();todo=[start]
    while todo:
        x=todo.pop()
        if x not in seen:seen.add(x);todo.extend(graph[x])
    return seen
assert component(0,dual)==set(range(4))
remaining=set(used);classes=[]
while remaining:
    cls=component(min(remaining),links);remaining-=cls;classes.append(cls)
assert len(classes)==8 and all(len(c)==3 for c in classes)
assert all(len(links[v])==2 for v in used)
assert {frozenset(c) for c in classes}=={frozenset(map(tuple,c)) for c in raw['vertex_classes']}
angle_rows=[[(120,1,0,0) if i%2==0 else (120,-1,0,0) for i in range(6)],
 [(240,1,0,-1),(120,0,0,0),(120,0,0,0),(240,-1,-1,0),(0,0,1,0),(0,0,0,1)]]
for cls in classes:
    row=tuple(sum(angle_rows[0 if faces[f]['species']=='A' else 1][i][k] for f,i in cls) for k in range(4))
    assert row==(360,0,0,0)
assert 4-12+len(classes)==0
# Independent polynomial reconstruction of the phase norm, all unit directions,
# and native angle units. The full convexity bounds are reviewed analytically.
R=PolynomialRing(QQ,['cd','sd','cx','sx','cy','sy','p']);cd,sd,cx,sx,cy,sy,p=R.gens()
unit=R.ideal([cd*cd+sd*sd-1,cx*cx+sx*sx-1,cy*cy+sy*sy-1])
K=cd-cd*cx+sd*sx
norm=(1-cx-2*p*cd)**2+(-sx+2*p*sd)**2-1
assert norm-(4*p*p-4*K*p+1-2*cx) in unit
# Phase: exp(idelta)*(exp(ichi)-1+exp(-ipsi))=-2p.
re=cd*(cx-1+cy)-sd*(sx-sy)
im=sd*(cx-1+cy)+cd*(sx-sy)
phase=unit+R.ideal([re+2*p,im])
assert (cy-(1-cx-2*p*cd)) in phase
assert (-sy-(-sx+2*p*sd)) in phase
# Exact degree16 fixture, embedded directly in QQbar, independently of producer.
z=QQbar.zeta(24);ii=z**6;w=z**2+z**-2
C=(z+z**-1)/2;S=(z-z**-1)/(2*ii)
r=w/2-S;k=(1-r*r).sqrt()
assert k.imag()==0 and k.real()>0
P=(QQ(1)/2+C+k)/2
assert QQ(1)/2<r.real()<AA(2).sqrt()/2
assert P.real()>1 and P.imag()==0
assert z**8-z-k-ii*r==-2*P
# Degree claim: quadratic radicand is not square in Q(zeta24).
NF=CyclotomicField(24);nz=NF.gen();ni=nz**6;nr=(nz**2+nz**-2)/2-(nz-nz**-1)/(2*ni)
assert not (1-nr*nr).is_square()
def decode(row):
    assert len(row)==16
    return sum(QQ(v)*z**j for j,v in enumerate(row[:8]))+k*sum(QQ(v)*z**j for j,v in enumerate(row[8:]))
def cross(a,b):
    v=(a.conjugate()*b-a*b.conjugate())/(2*ii)
    assert v.imag()==0
    return v.real()
directions=[[z**j for j in (0,5,8,13,16,21)],
 [QQbar(1),z**4,z**8,z**4*z*z**7,z**16*z,z**4*(-k-ii*r)]]
assert directions[1][3]==z**12 # q3=60+15+105=180
angle_units=[[z**9 if i%2==0 else z**7 for i in range(6)],
 [z**4*(k+ii*r),z**8,z**8,z**8,z**7,z**13*(k-ii*r)]]
polygons=[];edges=[];areas=[]
for species in range(2):
    es=[(P if label=='p' else 1)*d for label,d in zip(words[species],directions[species])]
    assert all((d*d.conjugate())==1 for d in directions[species])
    vs=[];cur=QQbar(0)
    for e in es:vs.append(cur);cur+=e
    assert cur==0
    for i,e in enumerate(es):
        assert -(directions[species][i]/directions[species][i-1]).conjugate()==angle_units[species][i]
        assert all(cross(e,vs[j]-vs[i])>0 for j in range(6) if j not in (i,(i+1)%6))
    area=sum(cross(vs[i],vs[(i+1)%6]) for i in range(6))/2
    assert area>0
    polygons.append(vs);edges.append(es);areas.append(area)
assert decode(cert['p'])==P
for f in range(4):
    s=0 if faces[f]['species']=='A' else 1
    assert [decode(v) for v in cert['reference_vertices'][f]]==polygons[s]
    assert decode(cert['tile_areas'][f])==areas[s]
trans=[(decode(t['rotation']),decode(t['translation'])) for t in cert['face_transforms']]
assert trans[0]==(1,0)
assert all(a*a.conjugate()==1 for a,t in trans)
for n,((u,i),(v,j)) in enumerate(pairs):
    su=0 if faces[u]['species']=='A' else 1;sv=0 if faces[v]['species']=='A' else 1
    au,tu=trans[u];av,tv=trans[v]
    assert au*edges[su][i]==-av*edges[sv][j]
    h=au*polygons[su][i]+tu-av*polygons[sv][(j+1)%6]-tv
    assert h==decode(cert['seam_holonomies'][n])
    assert au*polygons[su][(i+1)%6]+tu-av*polygons[sv][j]-tv==h
lattice=[decode(row) for row in cert['primitive_period_lattice']]
assert len(lattice)==2
covol=abs(cross(*lattice))
assert covol>0 and covol==2*sum(areas)==decode(cert['covolume'])
# In the proven independent degree16 basis compare actual integral spans, not
# just rational rank: the advertised lattice is exactly all cycle holonomies.
rows=[list(map(QQ,row)) for row in cert['seam_holonomies']]
lrows=[list(map(QQ,row)) for row in cert['primitive_period_lattice']]
den=lcm([x.denominator() for row in rows+lrows for x in row])
H=matrix(ZZ,[[den*x for x in row] for row in rows]).hermite_form(include_zero_rows=False)
L=matrix(ZZ,[[den*x for x in row] for row in lrows]).hermite_form(include_zero_rows=False)
assert H.nrows()==2 and H==L
# Complete fixture polygons modulo lattice also have reverse boundary pairing;
# the complete flat-torus proof establishes injectivity/coverage in all domains.
print('PASS full phase/quadratic identities; all24 native sides,12 reverse pairs,8 independently derived connected circular links360; exact degree16 fixture,48 strict supports,12 pure translation holonomies, primitive integral period span and positive covolume=motifarea.')
