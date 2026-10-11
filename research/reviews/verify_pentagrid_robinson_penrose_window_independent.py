#!/usr/bin/env python3
"""Independent exact Penrose window exclusion of full/mandatory-only objects.

No producer imports, Polyhedron or LP backend. Reconstruct native rho heights,
derive zonotope facets by generator cross products, clip shifted2D windows,
and check the explicit Farkas inequalities and closed-window witnesses.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations
import importlib.util
import json
from pathlib import Path
from sage.all import QuadraticField, QQ

_spec=importlib.util.spec_from_file_location("independent_residual",Path(__file__).with_name(
    "verify_pentagrid_robinson_residual_independent.py"))
r=importlib.util.module_from_spec(_spec);_spec.loader.exec_module(r)
g=r.g;K,z=g.K,g.z
F=QuadraticField(5,"rt5")
phi=(1+F.gen())/2
COS=(F(1),-phi/2,(phi-1)/2,(phi-1)/2,-phi/2)
SIN=(F(0),F(1),-phi,phi,F(-1))
GENERATORS=tuple((F(1),COS[j],SIN[j]) for j in range(5))


def sign(v):
    a,b=F(v).list()
    if b==0:return (a>0)-(a<0)
    if a>=0 and b>0:return 1
    if a<=0 and b<0:return -1
    diff=a*a-5*b*b if a>0 else 5*b*b-a*a
    assert diff!=0
    return (diff>0)-(diff<0)


def dot(a,b):return sum(x*y for x,y in zip(a,b))

def cross3(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])


def derive_facets():
    out=[]
    for a,b in combinations(GENERATORS,2):
        n=cross3(a,b)
        assert n!=(0,0,0)
        for orientation in (-1,1):
            normal=tuple(orientation*x for x in n)
            lower=sum((dot(normal,v) for v in GENERATORS if sign(dot(normal,v))<0),F(0))
            out.append((-lower,)+normal)
    return tuple(out)


def equal_ray(a,b):
    pivot=next(i for i,v in enumerate(a) if v)
    scale=b[pivot]/a[pivot]
    return sign(scale)>0 and all(y==scale*x for x,y in zip(a,b))


def projected(N):
    return F(sum(N)),sum(F(N[j])*COS[j] for j in range(5)),sum(F(N[j])*SIN[j] for j in range(5))


# Determine the native rho-basis unit lifts directly by physical field equality.
RHO_UNIT={sgn*z**(2*j):tuple(sgn if i==j else 0 for i in range(5))
          for j in range(5) for sgn in (-1,1)}


def lifts(label,words,residual=None):
    _,completed,_=g.construct(label,words)
    parents=list(completed)
    if residual is not None:parents += [r.decode_poly(p) for p in residual]
    edges=[(a,b) for p in parents for a,b in zip(p,p[1:]+p[:1])]
    edges += r.unit_segments(label,words)
    adj=defaultdict(list)
    for a,b in edges:
        nh=RHO_UNIT[b-a]
        zh=g.height.basis(r.UNIT[b-a])
        adj[a].append((b,nh,zh))
        adj[b].append((a,tuple(-x for x in nh),tuple(-x for x in zh)))
    N={K(0):(0,)*5};H={K(0):(0,)*5};queue=deque([K(0)])
    while queue:
        a=queue.popleft()
        for b,nh,zh in adj[a]:
            n=tuple(x+y for x,y in zip(N[a],nh));h=tuple(x+y for x,y in zip(H[a],zh))
            if b in N:assert N[b]==n and H[b]==h
            else:N[b]=n;H[b]=h;queue.append(b)
    assert len(N)==len(adj)
    for p,n in N.items():
        h=H[p]
        assert sum(n[j]*z**(2*j) for j in range(5))==p
        assert sum(h[j]*z**j for j in range(5))==p
        assert all(n[3*i%5]==(-1)**i*h[i] for i in range(5))
    return H,N


def cleaned(vertices):
    out=[]
    for p in vertices:
        if not out or out[-1]!=p:out.append(p)
    if len(out)>1 and out[-1]==out[0]:out.pop()
    return tuple(out)


def intersect(rows):
    # Zero is a required source vertex. Every shift lies in this bounded box.
    polygon=((-phi,-phi**2),(phi,-phi**2),(phi,phi**2),(-phi,phi**2))
    for c,a,b in rows:
        if not polygon:break
        out=[]
        for p,q in zip(polygon,polygon[1:]+polygon[:1]):
            fp=c+a*p[0]+b*p[1];fq=c+a*q[0]+b*q[1]
            ip,iq=sign(fp)>=0,sign(fq)>=0
            if ip!=iq:
                t=fp/(fp-fq)
                out.append(tuple(p[j]+t*(q[j]-p[j]) for j in range(2)))
            if iq:out.append(q)
        polygon=cleaned(out)
    assert all(sign(c+a*p[0]+b*p[1])>=0 for p in polygon for c,a,b in rows)
    area=sum((p[0]*q[1]-p[1]*q[0] for p,q in zip(polygon,polygon[1:]+polygon[:1])),F(0)) if polygon else F(0)
    assert sign(area)>=0
    return polygon,area


def check_gate(row,N,facets):
    layers=[sum(n) for n in N.values()];lo,hi=min(layers),max(layers)
    assert row["layer_interval"]==[lo,hi] and row["layer_span"]==hi-lo
    assert row["vertex_count"]==len(N)
    if "lifted_vertices" in row:
        seen=set()
        for v in row["lifted_vertices"]:
            p=g.decode(v["physical_coefficients"]);seen.add(p)
            assert list(N[p])==v["N_rho_basis"]
        assert seen==set(N)
    if hi-lo>3:
        assert row["window_gate"]["verdict"]=="fails Penrose four-layer necessity"
        return "layers"
    cases=row["window_gate"]["cases"]
    assert {c["integer_intercept_sum"] for c in cases}==set(range(hi-4,lo))
    verdicts=[]
    for case in cases:
        m=case["integer_intercept_sum"]
        rows=[(c+k*(layer-m)+a*x+b*y,-a,-b)
              for layer,x,y in map(projected,N.values()) for c,k,a,b in facets]
        poly,area=intersect(rows)
        assert area==0                   # strict intersection would have positive2D area
        dual=case["dual_obstruction"]
        selected=[tuple(F(x) for x in t) for t in dual["selected_rows"]]
        weights=[F(w) for w in dual["positive_weights"]]
        assert len(selected)==len(weights) in (2,3)
        assert all(sign(w)>=0 for w in weights) and any(sign(w)>0 for w in weights)
        assert all(t in rows for t in selected)
        assert sum(w*t[1] for w,t in zip(weights,selected))==0
        assert sum(w*t[2] for w,t in zip(weights,selected))==0
        constant=sum(w*t[0] for w,t in zip(weights,selected))
        assert constant==F(dual["constant_sum"]) and sign(constant)<=0
        assert [F(v) for v in dual["normal_sum"]]==[0,0]
        if not poly:
            assert case["verdict"]=="closed-window intersection empty"
            verdicts.append("empty")
        else:
            assert case["verdict"]=="only boundary-window feasibility"
            assert F(case["margin"])==0
            A,T=map(F,case["star_shift"])
            assert all(sign(c+a*A+b*T)>=0 for c,a,b in rows)
            assert any(c+a*A+b*T==0 for c,a,b in rows)
            verdicts.append("boundary")
    assert row["window_gate"]["verdict"]=="no strict shifted-window witness"
    return ",".join(verdicts)


def main():
    root=Path(__file__).parents[1]/"certificates"
    certificate=json.loads((root/"pentagrid-robinson-penrose-window.json").read_text())
    residual=json.loads((root/"pentagrid-robinson-residual-rhombs.json").read_text())
    completion=json.loads((root/"pentagrid-robinson-boundary-completion.json").read_text())
    facets=tuple(tuple(F(t) for t in row) for row in certificate["window_facets"])
    derived=derive_facets()
    assert len(facets)==len(derived)==20
    assert all(sum(equal_ray(a,b) for a in derived)==1 for b in facets)
    assert all(sum(equal_ray(a,b) for b in facets)==1 for a in derived)
    assert all(a!=0 or b!=0 for c,k,a,b in facets)
    for domain in ("fixtures","boundary_only"):
        for label,record in certificate[domain].items():
            expected=(residual["fixtures"][label]["results"] if domain=="fixtures" else
                      completion["fixtures"][label]["surviving_boundary_words"])
            histogram=Counter();gates=Counter();seen=set()
            for row in record["results"]:
                ix=row["source_row_index"] if domain=="fixtures" else row["source_boundary_index"]
                assert ix not in seen;seen.add(ix)
                words=expected[ix]["side_words"] if domain=="fixtures" else expected[ix]
                assert row["side_words"]==words
                whole=expected[ix]["whole_rhombs"] if domain=="fixtures" else None
                assert domain!="fixtures" or whole is not None
                H,N=lifts(label,words,whole)
                if "lifted_vertices" in row:
                    for v in row["lifted_vertices"]:
                        assert list(H[g.decode(v["physical_coefficients"])])==v["H_z_basis"]
                histogram[row["layer_span"]]+=1
                gates[check_gate(row,N,facets)]+=1
            required=({i for i,row in enumerate(expected) if row["whole_rhombs"] is not None}
                      if domain=="fixtures" else set(range(len(expected))))
            assert seen==required
            field="full_cluster_layer_span_histogram" if domain=="fixtures" else "layer_span_histogram"
            assert {str(k):v for k,v in sorted(histogram.items())}==record[field]
            assert record["strict_window_pass_count"]==0
            print(domain,label,"layer spans",dict(sorted(histogram.items())),"gates",dict(gates),flush=True)
    print("Independent native-lift/zonotope/clipping/Farkas window exclusion passed; proper Penrose source scope only.",flush=True)


if __name__=="__main__":
    if not __debug__:raise RuntimeError("Run without optimization")
    main()
