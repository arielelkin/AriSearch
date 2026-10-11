#!/usr/bin/env python3
"""Exact positive golden metric family with area ratio phi."""
from pathlib import Path
import importlib.util
import json
import argparse
from sage.all import QQ, QQbar, AA, matrix
spec=importlib.util.spec_from_file_location("metric",Path(__file__).with_name("pentagrid-golden-metric.py"))
metric=importlib.util.module_from_spec(spec);spec.loader.exec_module(metric)
K,z,phi=metric.K,metric.z,metric.phi

def cross(a,b):return (a.conjugate()*b-a*b.conjugate())/(z-z.conjugate())
def sign(a):
    q=QQbar(a);assert q.imag()==0
    return AA(q.real())
def area(p):return sum(cross(p[j],p[(j+1)%5]) for j in range(5))/2

def record(directions,lb,lc):
    vb=[K(0)];vc=[K(0)]
    for d,b,c in zip(directions,lb,lc):
        assert sign(b)>=0 and sign(c)>=0 and sign(b+c)>0
        vb.append(vb[-1]+d*b);vc.append(vc[-1]+d*c)
    assert vb[-1]==0 and vc[-1]==0
    supports=[]
    for i in range(5):
        for j in range(5):
            if j in(i,(i+1)%5):continue
            b=cross(directions[i],vb[j]-vb[i]);c=cross(directions[i],vc[j]-vc[i])
            assert sign(b)>=0 and sign(c)>=0 and sign(b+c)>0
            supports.append({"side":i,"vertex":j,"b_coefficient":metric.coefficients(b),"c_coefficient":metric.coefficients(c)})
    a0=area(vb[:-1]);a2=area(vc[:-1]);a1=area([vb[j]+vc[j] for j in range(5)])-a0-a2
    return {"vertex_b_coefficients":[metric.coefficients(q)for q in vb[:-1]],"vertex_c_coefficients":[metric.coefficients(q)for q in vc[:-1]],"supporting_side_linear_coefficients":supports,"normalized_area_b_squared_bc_c_squared":[metric.coefficients(q)for q in (a0,a1,a2)]},(a0,a1,a2)

def certificate():
    U,au=record([z**j for j in(0,4,6,7,8)],[phi**2,phi**2,1,0,1],[phi,phi,0,1,0])
    V,av=record([z**j for j in(0,3,6,7,9)],[1,2*phi,1,phi,phi],[0,phi**2,0,phi,phi])
    assert au==(phi**3,2*phi**2,phi**2/2)
    assert av==tuple(phi*q for q in au)
    M=matrix(QQ,[[1,1],[1,2]])
    assert matrix(K,[[1,phi]])*M==phi**2*matrix(K,[[1,phi]])
    return {"field":"Q(z), z^4-z^3+z^2-z+1=0, z=exp(pi*i/5), phi=z+z^(-1)","parameter_domain":"b>0,c>0 arbitraryreal; proof by linearpositive supporting-side coefficients","U_side_lengths":["phi^2*b+phi*c","phi^2*b+phi*c","b","c","b"],"V_side_lengths":["b","2*phi*b+phi^2*c","b","phi*(b+c)","phi*(b+c)"],"U":U,"V":V,"area_V_over_area_U":"phi","inflation_area_count_matrices":{str(k):[[int(q)for q in row]for row in M**k]for k in(1,2,3)}}
if __name__=="__main__":
    parser=argparse.ArgumentParser();parser.add_argument("--output");args=parser.parse_args();payload=json.dumps(certificate(),indent=2)+"\n"
    if args.output:Path(args.output).write_text(payload)
    else:print(payload,end="")
