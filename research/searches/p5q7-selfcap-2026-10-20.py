"""Exact changed-angle P5/Q7 self-cap reconnaissance; finite scope only."""
from sage.all import AA, NumberField, PolynomialRing, QQ, matrix, vector
import importlib.util
from pathlib import Path
from collections import Counter

R=PolynomialRing(QQ,'x');x=R.gen()
K=NumberField(x**4-10*x**2+1,'z',embedding=AA(2).sqrt()+AA(3).sqrt())
z=K.gen();r=(z-1/z)/2;s=(z+1/z)/2
assert r*r==2 and s*s==3 and r>0 and s>0
V=lambda a,b:vector(K,(a,b))
cross=lambda a,b:a[0]*b[1]-a[1]*b[0]
d=(s*r-r)/(-s*r+2+3*r) # (sqrt(6)-sqrt(2))/(2+3sqrt(2)-sqrt(6))
e=-d+s*d-1+s
assert d>0 and e>0
PL=(K(1),e,d,d,K(1))
QL=(d,K(1),K(1)+d/s,K(1),K(1)+2*d/s,K(1),K(1))
PD=[V(1,0),V(0,1),V(-(r*s+r)/4,(r*s-r)/4),V(-s/2,-1/2),V(-1/2,-s/2)]
QD=[V(1,0),V(s/2,1/2),V(0,1),V(-s/2,1/2),V(-s/2,-1/2),V(0,-1),V(s/2,-1/2)]
def poly(dirs,lens):
    out=[V(0,0)]
    for dr,le in zip(dirs[:-1],lens[:-1]):out.append(out[-1]+le*dr)
    assert out[-1]+lens[-1]*dirs[-1]==out[0]
    assert all(cross(out[(i+1)%len(out)]-out[i],out[(i+2)%len(out)]-out[(i+1)%len(out)])>0 for i in range(len(out)))
    return out
P=poly(PD,PL);Q=poly(QD,QL)
def overlap(a,b):
    for poly0 in (a,b):
        for i in range(len(poly0)):
            ed=poly0[(i+1)%len(poly0)]-poly0[i];no=V(-ed[1],ed[0])
            aa=[no*v for v in a];bb=[no*v for v in b]
            if max(aa)<=min(bb) or max(bb)<=min(aa):return False
    return True
def corner(poly,i,j,k,origin,jray,kray):
    X=matrix(K,[[*(poly[j]-poly[i])],[*(poly[k]-poly[i])]]).transpose()
    Y=matrix(K,[[*jray],[*kray]]).transpose();M=Y*X.inverse()
    assert M.transpose()*M==matrix.identity(K,2)
    return [origin+M*(v-poly[i]) for v in poly]

# Q/Q side-0 half-turn with P 60-degree caps at both endpoints.
Q0=Q;Q1=[Q[0]+Q[1]-v for v in Q]
O=Q[0];E=Q[1]
P0=corner(P,0,1,4,O,Q0[6]-O,Q1[2]-O)
P1=corner(P,0,1,4,E,Q1[6]-E,Q0[2]-E)
base=[Q0,Q1,P0,P1]
assert all(not overlap(base[i],base[j]) for i in range(4) for j in range(i+1,4))

def selfcap(host,slot,others,reflected=False):
    # Half-turn or reflected mate, then Q's (1,1) corner 6 at the 120+120 endpoints.
    a,b=host[slot],host[(slot+1)%7]
    if reflected:
        ed=b-a
        mate=[a+2*((v-a)*ed)/(ed*ed)*ed-(v-a) for v in host]
    else:
        mate=[a+b-v for v in host]
    if any(overlap(mate,p) for p in others):return 'mate overlaps'
    caps=[]
    for endpoint in (a,b):
        rays=[]
        for poly0 in (host,mate):
            ix=poly0.index(endpoint)
            for j in ((ix-1)%7,(ix+1)%7):
                ray=poly0[j]-endpoint
                if ray not in (b-a,a-b):rays.append(ray)
        assert len(rays)==2 and all(ray*ray==1 for ray in rays)
        cap=corner(Q,6,5,0,endpoint,rays[0],rays[1])
        if any(overlap(cap,p) for p in others+[host,mate]+caps):return 'cap overlaps'
        caps.append(cap)
    return 'legal'

for slot in (2,4):
    for refl in (False,True):
        print('Q private side',slot,'reflected',refl,'isolated',selfcap(Q0,slot,[],refl),'beside base',selfcap(Q0,slot,[Q1,P0,P1],refl))

# Complete prescribed full-edge seam audit: Q's side 0 has length d; its
# only potential mates are another Q side 0 or P sides 2,3. The latter fail
# at a 135-degree endpoint. For both Q/Q side-0 orientations, enumerate the
# two P(60) arm assignments at each endpoint and both Q/Q side-2 orientations.
def outer_rays(poly0,endpoint,other_endpoint):
    ix=poly0.index(endpoint)
    return [poly0[j]-endpoint for j in ((ix-1)%7,(ix+1)%7)
            if poly0[j]!=other_endpoint]

audit=[]
torus_necessary=[]
for seam_reflected in (False,True):
    if seam_reflected:
        qm=[V(v[0],-v[1]) for v in Q0]
    else:
        qm=[O+E-v for v in Q0]
    assert not overlap(Q0,qm)
    end_caps=[]
    for endpoint,other in ((O,E),(E,O)):
        rays=outer_rays(Q0,endpoint,other)+outer_rays(qm,endpoint,other)
        assert len(rays)==2 and all(ray*ray==1 for ray in rays)
        end_caps.append([corner(P,0,1,4,endpoint,*assignment)
                         for assignment in (rays,rays[::-1])])
    for i,ca in enumerate(end_caps[0]):
        for j,cb in enumerate(end_caps[1]):
            bset=[Q0,qm,ca,cb]
            if any(overlap(bset[k],bset[m]) for k in range(4) for m in range(k+1,4)):
                audit.append((seam_reflected,i,j,'base overlap'))
                continue
            def oriented_edge(poly0,slot):
                signed=sum(cross(poly0[k],poly0[(k+1)%len(poly0)])
                           for k in range(len(poly0)))
                sg=1 if signed>0 else -1
                return sg*(poly0[(slot+1)%len(poly0)]-poly0[slot])
            q_u=oriented_edge(Q0,2)+oriented_edge(qm,2)
            q_w=oriented_edge(Q0,4)+oriented_edge(qm,4)
            p_e=oriented_edge(ca,1)+oriented_edge(cb,1)
            # A two-Q translation torus must pair the two unique u and w
            # sides; a two-P torus must pair the two unique e sides.
            torus_necessary.append((seam_reflected,i,j,q_u==0,q_w==0,p_e==0))
            def edge_balance(tiles):
                edges=Counter(tuple(oriented_edge(poly0,k))
                              for poly0 in tiles for k in range(len(poly0)))
                return all(edges[v]==edges[tuple(-x for x in v)] for v in edges)
            print('all-edge vector balance',seam_reflected,i,j,edge_balance(bset))
            if not seam_reflected and i==1 and j==0:
                Tu=Q0[2]-qm[3];Tw=Q0[4]-qm[5];Te=ca[1]-cb[2]
                area=sum(abs(sum(cross(poly0[k],poly0[(k+1)%len(poly0)])
                                 for k in range(len(poly0)))/2) for poly0 in bset)
                print('torus vectors Tu,Tw,Te=',Tu,Tw,Te)
                ratio=cross(Tu,Tw)/area
                assert 1<ratio<2
                print('det(Tu,Tw)/patch area=',ratio,'strictly between 1 and 2')
            for private_reflected in (False,True):
                a,b=Q0[2],Q0[3]
                if private_reflected:
                    ed=b-a
                    private=[a+2*((v-a)*ed)/(ed*ed)*ed-(v-a) for v in Q0]
                else:
                    private=[a+b-v for v in Q0]
                bad=[k for k,v in enumerate(bset) if overlap(private,v)]
                audit.append((seam_reflected,i,j,private_reflected,tuple(bad)))
print('side-2 seam audit:',audit)
print('2P+2Q translation-torus necessary edge-vector test:',torus_necessary)

spec=importlib.util.spec_from_file_location('rao',Path(__file__).with_name('convex-substitution-shapes.py'))
rao=importlib.util.module_from_spec(spec);spec.loader.exec_module(rao)
PA=(60,90,105,135,150);hits=[]
for typ,(ae,le) in rao.RAO.items():
    for sign in (1,-1):
        for off in range(5):
            am=[(off+sign*i)%5 for i in range(5)]
            if not all(sum(a*b for a,b in zip(row,[PA[j] for j in am]))==target*36 for row,target in ae):continue
            sm=([(off+i)%5 for i in range(5)] if sign==1 else [(off-i-1)%5 for i in range(5)])
            if all(sum((coef*PL[j] for coef,j in zip(row,sm)),K(0))==0 for row in le):hits.append((typ,sign,off))
print('P lengths',PL,'Q lengths',QL,'Rao hits',hits)
print('P',P,'Q',Q)
print('base P/Q/Q/P legal')
