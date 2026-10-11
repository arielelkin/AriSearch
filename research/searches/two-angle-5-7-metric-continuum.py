#!/usr/bin/env python3
"""Exact full metric cone for the retained(5,7) gluing, plus formal torus identities.

Eight homogeneous inequalities in four real parameters. Enumerate all56
triples of active inequalities, retain nine exact extreme rays, verify all
facet interiors. Symbolic coordinates over Q(zeta28)[a,b,c,d]; no numerical
branches or parameter sampling used for universal identities. --output only
writes a requested certificate; default is nondestructive JSON output.
"""
import argparse
from itertools import combinations
import json
from pathlib import Path
from sage.all import AA, CyclotomicField, NumberField, PolynomialRing, QQ, RIF, matrix, vector

R=PolynomialRing(QQ,"x");x=R.gen()
f=x**3-x**2-2*x+1
F=NumberField(f,"t",embedding=AA.polynomial_root(f,RIF(QQ(18)/10,QQ(181)/100)))
t=F.gen()
labels=("a=H1","b=H2","c=H4","d=H6","H0","H3","H5","Pprivate")
e=lambda j:vector(F,[int(k==j) for k in range(4)])
a,b,c,d=(e(j) for j in range(4))
L3=t*d-(t*t-1)*b/2+c/2
L5=(t-1)*a+b/2+(-t*t+t+1)*c/2
L0=(-t*t+t+1)*a+(t*t/2-t-F(1)/2)*b+(t-F(1)/2)*c+d
p=(t*t-t-1)*a-(t*t-1)*b/2+c/2+d
normals=(a,b,c,d,L0,L3,L5,p)
lengths=(L0,a,b,L3,c,L5,d)
enc=lambda q:[str(x) for x in F(q).list()]

def cone():
    rays=set()
    for indices in combinations(range(8),3):
        M=matrix(F,[normals[j] for j in indices])
        if M.rank()!=3:continue
        r=M.right_kernel().basis()[0]
        pivot=next(q for q in r if q)
        r=r/pivot
        if any(n.dot_product(r)<0 for n in normals):continue
        rays.add(tuple(r))
    rays=sorted(rays,key=lambda r:tuple(tuple(q.list()) for q in r))
    assert len(rays)==9
    facets=[]
    for j,n in enumerate(normals):
        on=[vector(F,r) for r in rays if n.dot_product(vector(F,r))==0]
        assert matrix(F,on).rank()==3
        witness=sum(on,vector(F,[0]*4))
        assert n.dot_product(witness)==0
        assert all(normals[k].dot_product(witness)>0 for k in range(8) if k!=j)
        facets.append({"label":labels[j],"facet_relative_interior_witness":[enc(q) for q in witness]})
    generic=vector(F,[1,QQ(11)/10,QQ(6)/5,QQ(9)/10])
    values=[n.dot_product(generic) for n in normals]
    assert all(q>0 for q in values) and len(set(values))==8
    return {
        "dimension":4,"scale_quotient_dimension":3,"inequality_labels":labels,
        "strict_inequality_normals":[[enc(q) for q in n] for n in normals],
        "extreme_rays":[{"parameters":[enc(q) for q in r],
            "zero_lengths":[labels[j] for j,n in enumerate(normals) if n.dot_product(vector(F,r))==0]} for r in rays],
        "irredundant_facets":facets,"generic_fixture_parameters":["1","11/10","6/5","9/10"],
        "generic_fixture_eight_lengths":[enc(q) for q in values]}

def geometry():
    K=CyclotomicField(28);w=K.gen();ii=w**7;z=w**4
    embedding=F.hom([w**2+w**(-2)],K)
    S=PolynomialRing(K,names=("a","b","c","d"));parameters=S.gens()
    lin=lambda n:sum(embedding(q)*v for q,v in zip(n,parameters))
    l=[lin(n) for n in lengths];private=lin(p)
    C=lambda q:(q+q**(-1))/2
    T=lambda q:(q-q**(-1))/(2*ii)
    add=lambda p,q:tuple(a+b for a,b in zip(p,q))
    sub=lambda p,q:tuple(a-b for a,b in zip(p,q))
    H=[(S(0),S(0))]
    for j in range(7):H.append(add(H[-1],(l[j]*C(z**j),l[j]*T(z**j))))
    assert H[-1]==(0,0);H.pop()
    ds={j:add(H[j],H[j+1]) for j in (0,2,4)}
    u,v=sub(ds[2],ds[0]),sub(ds[4],ds[0]);cs=add(sub(ds[0],ds[2]),ds[4])
    P=[H[6],H[0],sub(ds[0],H[2]),add(sub(ds[0],ds[2]),H[4]),sub(cs,H[6])]
    assert sub(P[0],P[-1])==(private,0)
    polys=(H,[sub(ds[0],q) for q in H],P,[sub(cs,q) for q in P])
    # (tile,side,tile,side,u_shift,v_shift,reversed_endpoint_order)
    seams=[(0,j,1,j,int(j==2),int(j==4),True) for j in (0,2,4)]
    seams += [(0,6,2,0,0,0,False),(0,1,3,1,1,-1,False),
              (0,3,2,2,1,0,False),(0,5,3,3,0,0,False),
              (1,6,3,0,1,-1,False),(1,1,2,1,0,0,False),
              (1,3,3,2,0,-1,False),(1,5,2,3,1,-1,False),
              (2,4,3,4,0,0,True)]
    nodes=[(i,j) for i,poly in enumerate(polys) for j in range(len(poly))]
    parent={n:n for n in nodes}
    def root(n):
        while parent[n]!=n:n=parent[n]
        return n
    def union(a,b):parent[root(a)]=root(b)
    used=set()
    for i,j,k,h,m,n,reverse in seams:
        assert (i,j) not in used and (k,h) not in used
        used.update(((i,j),(k,h)))
        shift=tuple(m*a+n*b for a,b in zip(u,v))
        aa=[polys[i][j],polys[i][(j+1)%len(polys[i])]]
        bb=[add(polys[k][h],shift),add(polys[k][(h+1)%len(polys[k])],shift)]
        if reverse:bb.reverse()
        assert aa==bb
        union((i,j),(k,(h+int(reverse))%len(polys[k])))
        union((i,(j+1)%len(polys[i])),(k,(h+int(not reverse))%len(polys[k])))
    assert used==set(nodes)
    classes=[]
    for rt in set(map(root,nodes)):
        corners=sorted(n for n in nodes if root(n)==rt)
        assert len(corners)==3
        angles=[5 if i<2 or j==0 else 4 for i,j in corners]
        assert sorted(angles)==[4,5,5]
        classes.append(corners)
    assert len(classes)==8
    cross=lambda a,b:a[0]*b[1]-a[1]*b[0]
    twice=lambda poly:sum(cross(p,q) for p,q in zip(poly,poly[1:]+poly[:1]))
    det=cross(u,v)
    assert det==twice(H)-twice(P) # 2areaH+2areaP, P is clockwise
    return {"seam_table":[list(row) for row in seams],"vertex_links":sorted(classes),
            "area_identity":"det(u,v)=2*area(H)+2*area(P)>0",
            "whole_plane_proof":"connected flat torus, positive polygon areas, area/covolume degree1"}

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--output",type=Path);args=ap.parse_args()
    data={"scope":"full4D positive metric cone of retained(5,7) gluing; generic8-distinct-length metrics force this periodic source",
          "field":{"polynomial_coefficients":[str(q) for q in f.list()],"root_interval":["18/10","181/100"]},
          "cone":cone(),"formal_geometry":geometry()}
    text=json.dumps(data,indent=2,sort_keys=True)+"\n"
    if args.output:args.output.write_text(text)
    else:print(text,end="")

if __name__=="__main__":
    if not __debug__:raise RuntimeError("Assertions required")
    main()
