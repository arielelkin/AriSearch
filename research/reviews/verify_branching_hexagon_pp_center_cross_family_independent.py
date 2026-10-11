"""Independent native-reflection, full-phase and raw8face carrier audit. No author imports.
Replay: conda run --no-capture-output -n arisearch python research/reviews/verify_branching_hexagon_pp_center_cross_family_independent.py
"""
from pathlib import Path
from collections import Counter,defaultdict
import json
from sage.all import QQ,QQbar,AA,PolynomialRing,matrix,ZZ,lcm,CyclotomicField
root=Path(__file__).parents[1]
raw=json.loads((root/'certificates/branching-hexagon-two-run-pp-center-cross-eight-face.json').read_text())
assert raw['status']=='positive_witness'
raw=raw['witness'];faces=raw['faces'];pairs=raw['paired_edges']
cert=json.loads((root/'certificates/branching-hexagon-two-run-pp-center-cross-periodic-family.json').read_text())
assert [f['species'] for f in faces]==['A']*4+['B']*4
assert [f['mirror'] for f in faces]==[False,False,True,True]*2
native_words=[list('pqpqpq'),list('pppqqq')]
rows=[[(120,1,0,0) if i%2==0 else (120,-1,0,0) for i in range(6)],
 [(240,1,-1,0),(120,0,0,0),(120,0,0,0),(240,-1,0,-1),(0,0,1,0),(0,0,0,1)]]
face_rows=[]
for face in faces:
    sp=0 if face['species']=='A' else 1
    # Directly derive the mirrored side and corner maps from reflected vertices
    # v'_j=conjugate(v_{-j}); labels use5-j, corners use-j.
    sides=[(5-j)%6 if face['mirror'] else j for j in range(6)]
    corners=[(-j)%6 if face['mirror'] else j for j in range(6)]
    assert face['labels']==[native_words[sp][j] for j in sides]
    rr=[rows[sp][j] for j in corners]
    assert [tuple(r) for r in face['angle_rows']]==rr
    face_rows.append(rr)
used=Counter();links=defaultdict(list);dual=defaultdict(set)
for (u,i),(v,j) in pairs:
    used[u,i]+=1;used[v,j]+=1
    assert faces[u]['labels'][i]==faces[v]['labels'][j]
    dual[u].add(v);dual[v].add(u)
    for x,y in (((u,i),(v,(j+1)%6)),((u,(i+1)%6),(v,j))):
        links[x].append(y);links[y].append(x)
assert len(pairs)==24 and used==Counter({(u,j):1 for u in range(8) for j in range(6)})
def component(start,graph):
    todo=[start];seen=set()
    while todo:
        x=todo.pop()
        if x not in seen:seen.add(x);todo.extend(graph[x])
    return seen
assert component(0,dual)==set(range(8))
remaining=set(used);classes=[]
while remaining:
    cls=component(min(remaining),links);remaining-=cls;classes.append(cls)
assert len(classes)==16 and all(len(c)==3 for c in classes)
assert all(len(links[x])==2 for x in used)
assert {frozenset(c) for c in classes}=={frozenset(map(tuple,c)) for c in raw['vertex_classes']}
for cls in classes:
    assert tuple(sum(face_rows[u][j][k] for u,j in cls) for k in range(4))==(360,0,0,0)
assert 8-24+len(classes)==0
# Symbolic cleared reconstruction norm for the entire cross family.
R=PolynomialRing(QQ,['cd','sd','cx','sx','cy','sy','p']);cd,sd,cx,sx,cy,sy,p=R.gens()
unit=R.ideal([cd*cd+sd*sd-1,cx*cx+sx*sx-1,cy*cy+sy*sy-1])
Nre,Nim=-2*p*cd-cx,2*p*sd+sx
Dre,Dim=1-cx,sx
norm=Nre*Nre+Nim*Nim-Dre*Dre-Dim*Dim
assert norm-(4*p*p+4*(cd*cx+sd*sx)*p+2*cx-1) in unit
# exp(ipsi)*(1-exp(-ichi))= -2p exp(-idelta)-exp(-ichi).
pre, pim=cy*Dre-sy*Dim-Nre,sy*Dre+cy*Dim-Nim
phase=unit+R.ideal([pre,pim])
# Multiply out the family's three-unit q chain to verify closure directly.
qre=cy-(cy*cx+sy*sx)+cx
qim=sy-(sy*cx-cy*sx)-sx
assert cd*qre-sd*qim+2*p in phase
assert sd*qre+cd*qim in phase
# Fresh QQbar embedding of delta15,chi90 geometry.
z=QQbar.zeta(24);ii=z**6
C=(z+z**-1)/2;S=(z-z**-1)/(2*ii)
k=(1+S*S).sqrt();assert k.imag()==0 and k.real()>0
P=(k-S)/2;assert P.imag()==0 and 0<P.real()<QQ(1)/2
Z=(-2*P/z+ii)/(1+ii)
assert Z*Z.conjugate()==1
assert Z.real()>0 and Z.imag()>Z.real()
assert Z.real()==QQ(1)/2+P*(S-C)
assert Z.imag()==QQ(1)/2+P*(S+C)
assert z*(Z-Z/ii+1/ii)==-2*P
NF=CyclotomicField(24);nz=NF.gen();ns=(nz-nz**-1)/(2*nz**6)
assert not (1+ns*ns).is_square()
def decode(row):
    assert len(row)==16
    return sum(QQ(v)*z**j for j,v in enumerate(row[:8]))+k*sum(QQ(v)*z**j for j,v in enumerate(row[8:]))
def cross(a,b):
    value=(a.conjugate()*b-a*b.conjugate())/(2*ii)
    assert value.imag()==0
    return value.real()
native_dirs=[[z**j for j in (0,5,8,13,16,21)],
 [QQbar(1),z**4,z**8,z**5*Z,z**11*Z,z**23]]
native_angles=[[z**9 if j%2==0 else z**7 for j in range(6)],
 [z**11,z**8,z**8,z**15/Z,ii,Z]]
native_pts=[]
for s in range(2):
    pp=[];cur=QQbar(0)
    for lab,d in zip(native_words[s],native_dirs[s]):
        pp.append(cur);cur+=(P if lab=='p' else 1)*d
    assert cur==0
    native_pts.append(pp)
pts=[];edges=[];areas=[]
for u,face in enumerate(faces):
    s=0 if face['species']=='A' else 1;mir=face['mirror']
    dirs=[-native_dirs[s][(5-j)%6].conjugate() if mir else native_dirs[s][j] for j in range(6)]
    es=[(P if lab=='p' else 1)*d for lab,d in zip(face['labels'],dirs)]
    pp=[];cur=QQbar(0)
    for e in es:pp.append(cur);cur+=e
    assert cur==0
    # Exact reflected congruence at every original native vertex.
    expected=[native_pts[s][(-j)%6].conjugate() if mir else native_pts[s][j] for j in range(6)]
    assert pp==expected
    for j,e in enumerate(es):
        oldj=(-j)%6 if mir else j
        assert dirs[j]*dirs[j].conjugate()==1
        assert -(dirs[j]/dirs[j-1]).conjugate()==native_angles[s][oldj]
        assert all(cross(e,pp[h]-pp[j])>0 for h in range(6) if h not in(j,(j+1)%6))
    area=sum(cross(pp[j],pp[(j+1)%6]) for j in range(6))/2
    assert area>0
    assert pp==[decode(v) for v in cert['reference_vertices'][u]]
    assert area==decode(cert['tile_areas'][u])
    pts.append(pp);edges.append(es);areas.append(area)
assert decode(cert['p'])==P
trans=[(decode(f['rotation']),decode(f['translation'])) for f in cert['face_transforms']]
assert trans[0]==(1,0)
assert all(a*a.conjugate()==1 for a,t in trans)
for n,((u,i),(v,j)) in enumerate(pairs):
    au,tu=trans[u];av,tv=trans[v]
    assert au*edges[u][i]==-av*edges[v][j]
    h=au*pts[u][i]+tu-av*pts[v][(j+1)%6]-tv
    assert h==decode(cert['seam_holonomies'][n])
    assert au*pts[u][(i+1)%6]+tu-av*pts[v][j]-tv==h
lattice=[decode(v) for v in cert['primitive_period_lattice']]
assert len(lattice)==2
covol=abs(cross(*lattice))
assert covol>0 and covol==sum(areas)==decode(cert['covolume'])
rs=[list(map(QQ,row)) for row in cert['seam_holonomies']]
ls=[list(map(QQ,row)) for row in cert['primitive_period_lattice']]
den=lcm([x.denominator() for row in rs+ls for x in row])
H=matrix(ZZ,[[den*x for x in row] for row in rs]).hermite_form(include_zero_rows=False)
L=matrix(ZZ,[[den*x for x in row] for row in ls]).hermite_form(include_zero_rows=False)
assert H.nrows()==2 and H==L
print('PASS full cross phase/quadratic identities; all48 displayed sides24 reversedpairs16 newly derived circularlinks360; both native reflection index maps; degree16 new fixture/unitangles/192 strict supports,24 translation holonomies and primitive integral lattice covolume=8face area.')
