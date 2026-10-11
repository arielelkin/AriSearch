#!/usr/bin/env python3
"""Exact placement certificate for the U/regular-W periodic counterexample."""
from pathlib import Path
import importlib.util
import json
from itertools import product
from sage.all import AA, QQbar
spec=importlib.util.spec_from_file_location("metric",Path(__file__).with_name("pentagrid-golden-metric.py"))
metric=importlib.util.module_from_spec(spec);spec.loader.exec_module(metric)
K,z,phi=metric.K,metric.z,metric.phi

def cross(a,b):
    return (a.conjugate()*b-a*b.conjugate())/(z-z.conjugate())
def aa(q):
    value=QQbar(q);assert value.imag()==0
    return AA(value.real())
def polygon_area(p):
    return sum(cross(p[j],p[(j+1)%len(p)]) for j in range(len(p)))/2

def separated(p,q):
    for a,b in ((p,q),(q,p)):
        for j in range(len(a)):
            e=a[(j+1)%len(a)]-a[j]
            if all(aa(cross(e,w-a[j]))<=0 for w in b):return True
    return False

def certificate():
    U=[K(0),phi**3,z+z**2+z**3,z**2+z**3,z**3]
    W=[K(0),K(1),1+z**2,z+z**3,z**3]
    p=[U,[-w+phi**3 for w in U],[z*w+z**2+z**3 for w in W],[z**2*w+z**3 for w in W]]
    u=z+z**2+z**3;v=4-z+z**2-5*z**3
    det=cross(u,v);assert aa(det)!=0
    assert sum(polygon_area(q) for q in p)==(det if aa(det)>0 else -det)
    boxes=[]
    for q in p:
        a=[aa(cross(w,v)/det) for w in q]
        b=[aa(cross(u,w)/det) for w in q]
        boxes.append((min(a),max(a),min(b),max(b)))
    tests=[]
    for i in range(4):
        for j in range(4):
            a,b=boxes[i],boxes[j]
            m_range=range(int((a[0]-b[1]).ceil()),int((a[1]-b[0]).floor())+1)
            n_range=range(int((a[2]-b[3]).ceil()),int((a[3]-b[2]).floor())+1)
            for m,n in product(m_range,n_range):
                if i==j and m==n==0:continue
                q=[w+m*u+n*v for w in p[j]]
                assert separated(p[i],q),(i,j,m,n)
                tests.append([i,j,m,n])
    return {"field":"Q(z), z^4-z^3+z^2-z+1=0, z=exp(pi*i/5)","phi":"z+z^(-1)","U_vertices":[metric.coefficients(w) for w in U],"W_vertices":[metric.coefficients(w) for w in W],"lattice":[metric.coefficients(u),metric.coefficients(v)],"placed_polygons":[[metric.coefficients(w) for w in q]for q in p],"normalized_lattice_determinant":metric.coefficients(det),"area_identity_exact":True,"exact_overlap_shift_tests":tests,"exact_overlap_shift_test_count":len(tests)}
if __name__=="__main__":
    import argparse
    parser=argparse.ArgumentParser();parser.add_argument("--output");args=parser.parse_args()
    result=certificate();payload=json.dumps(result,indent=2)+"\n"
    if args.output: Path(args.output).write_text(payload)
    else: print(payload,end="")
