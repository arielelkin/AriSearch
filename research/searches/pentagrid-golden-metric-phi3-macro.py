#!/usr/bin/env python3
"""One exact 5U+8V dissection of phi^3 U, with a fixed timeout."""
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
from time import monotonic
from itertools import combinations
from sage.all import AA, QQ, QQbar
import z3

spec=importlib.util.spec_from_file_location("metric",Path(__file__).with_name("pentagrid-golden-metric.py"))
metric=importlib.util.module_from_spec(spec);spec.loader.exec_module(metric)
K,z,phi=metric.K,metric.z,metric.phi

def real(q):
    value=QQbar(q);assert value.imag()==0
    return AA(value.real())
def cross(a,b):return (a.conjugate()*b-a*b.conjugate())/(z-z.conjugate())
def f_coeff(q):
    q=K(q);c=list(q)
    c += [QQ(0)]*(4-len(c))
    assert c[1]==0 and c[2]==-c[3]
    return QQ(c[0]-c[2]),QQ(c[2])
def basis(q):
    y=(q-q.conjugate())/(z-z.conjugate());x=q-y*z
    assert real(x)==real(x) and real(y)==real(y)
    assert x+y*z==q
    return x,y

def shapes():
    U=[K(0),phi**3,z+z**2+z**3,z**2+z**3,z**3]
    directions=[z**j for j in(0,3,6,7,9)]
    lengths=[K(1),3*phi+1,K(1),2*phi,2*phi]
    V=[K(0)]
    for a,b in zip(directions,lengths):V.append(V[-1]+a*b)
    assert V[-1]==0;V=V[:-1]
    # Exact intrinsic reflections: r*conjugate(w)+t.
    ru=z**9;tu=U[1]-ru*U[1].conjugate()
    rv=z;tv=V[4]-rv*V[4].conjugate()
    assert all(ru*U[j].conjugate()+tu==U[(2-j)%5]for j in range(5))
    assert all(rv*V[j].conjugate()+tv==V[(3-j)%5]for j in range(5))
    for q in(U,V):
        for i in range(5):
            for j in range(5):
                if j not in(i,(i+1)%5):assert real(cross(q[(i+1)%5]-q[i],q[j]-q[i]))>0
    return U,V,{"U":{"rotation_factor":metric.coefficients(ru),"translation":metric.coefficients(tu),"vertex_index_map":"j -> (2-j) mod5"},"V":{"rotation_factor":metric.coefficients(rv),"translation":metric.coefficients(tv),"vertex_index_map":"j -> (3-j) mod5"}}

def build():
    U,V,mirrors=shapes();rho=phi**3
    assert 5*sum(cross(U[j],U[(j+1)%5])for j in range(5))+8*sum(cross(V[j],V[(j+1)%5])for j in range(5)) == rho**2*sum(cross(U[j],U[(j+1)%5])for j in range(5))
    solver=z3.SolverFor("QF_NRA");solver.set(timeout=120000,random_seed=0)
    f=z3.Real("phi");solver.add(f*f-f-1==0,f>z3.RealVal("3/2"),f<z3.RealVal("5/3"))
    def val(q):
        a,b=f_coeff(q)
        return z3.RealVal(str(a))+z3.RealVal(str(b))*f
    # Intervals of rotated reference polygons along each global normal.
    intervals={}
    for name,poly in (("U",U),("V",V)):
        table=[]
        for k in range(10):
            p=[z**k*w for w in poly];row=[]
            for j in range(10):
                values=[cross(z**j,w)for w in p]
                lo=min(values,key=real);hi=max(values,key=real)
                row.append((lo,hi))
            table.append(row)
        intervals[name]=table
    X=[z3.Real("x_%d"%i)for i in range(13)]
    Y=[z3.Real("y_%d"%i)for i in range(13)]
    choices=[[z3.Bool("orientation_%d_%d"%(i,k))for k in range(10)]for i in range(13)]
    for b in choices:solver.add(z3.Or(b),z3.AtMost(*b,1))
    solver.add(choices[0][0],X[0]==val((rho-1)*phi**3),Y[0]==0)
    for group in (range(1,5),range(5,13)):
        for i,j in zip(group,list(group)[1:]):solver.add(X[i]<=X[j])
    names=["U"]*5+["V"]*8
    def choose(i,values):
        out=val(values[-1])
        for k in range(8,-1,-1):out=z3.If(choices[i][k],val(values[k]),out)
        return out
    projection={}
    for j in range(10):
        dx,dy=basis(z**j)
        for i in range(13):
            shift=val(dx)*Y[i]-val(dy)*X[i]
            lo=choose(i,[intervals[names[i]][k][j][0]for k in range(10)])
            hi=choose(i,[intervals[names[i]][k][j][1]for k in range(10)])
            projection[i,j]=(shift+lo,shift+hi)
    # Containment is equivalent to all five parent supporting half-planes.
    parent_directions=(0,4,6,7,8)
    for i in range(13):
        for side,j in enumerate(parent_directions):
            solver.add(projection[i,j][0]>=val(cross(z**j,rho*U[side])))
    # Every child edge is parallel to one of these five unoriented axes.
    for i,j in combinations(range(13),2):
        separated=[]
        for a in range(5):
            separated.extend((projection[i,a][1]<=projection[j,a][0],projection[j,a][1]<=projection[i,a][0]))
        solver.add(z3.Or(separated))
    metadata={"question":"Partition one phi^3 U parent into five U and eight V at b=c=1","arithmetic":"exact QF_NRA; phi^2-phi-1=0,3/2<phi<5/3; coordinates in basis(1,z), z=exp(pi*i/5)","child_count":13,"child_types":names,"orientation_domain":"10 reference rotations z^k, k0..9; reflections covered by certified intrinsic symmetries","raw_remaining_orientation_assignments":10**12,"translation_domain":"arbitrary real coordinates in basis(1,z); no grid, rational denominator, or edge-to-edge assumption","anchor":"child0 U orientation0, x=(phi^3-1)*phi^3, y=0, its unique36 corner at parent36 corner","symmetry_reductions":"sort x translations of unanchored U copies and of V copies; no physical placements excluded","constraints":{"containment_halfplanes":65,"unordered_polygon_pairs":78,"separation_axes_per_pair":5},"intrinsic_reflections":mirrors,"area_identity_exact":True,"solver_timeout_ms":120000,"random_seed":0,"z3_version":z3.get_version_string()}
    return solver,X,Y,choices,metadata

if __name__=="__main__":
    if not __debug__:raise RuntimeError("Exact assertions require Python without -O")
    parser=argparse.ArgumentParser();parser.add_argument("--output");parser.add_argument("--formula-output");args=parser.parse_args()
    start=monotonic();solver,X,Y,choices,metadata=build();formula=solver.to_smt2()
    formula="(set-option :timeout 120000)\n(set-option :random-seed 0)\n"+formula
    metadata["formula_sha256"]=hashlib.sha256(formula.encode()).hexdigest()
    metadata["formula_bytes"]=len(formula.encode())
    metadata["build_seconds"]=monotonic()-start
    if args.formula_output:Path(args.formula_output).write_text(formula)
    print("Exact fixed-macro formula built; starting one 120000ms solver check",flush=True,file=__import__("sys").stderr)
    tick=monotonic();result=solver.check();metadata["solver_seconds"]=monotonic()-tick
    metadata["solver_result"]=str(result)
    metadata["solver_statistics"]=str(solver.statistics())
    if result==z3.unknown:
        metadata["completion_status"]="unknown";metadata["reason_unknown"]=solver.reason_unknown()
    elif result==z3.unsat:
        metadata["completion_status"]="solver_unsat_fixed_macro_domain_unreviewed"
    else:
        model=solver.model();metadata["completion_status"]="sat_model_pending_independent_geometry_verification"
        metadata["placements"]=[{"type":metadata["child_types"][i],"orientation":[k for k in range(10)if z3.is_true(model.eval(choices[i][k]))][0],"x_exact_z3":model.eval(X[i]).sexpr(),"y_exact_z3":model.eval(Y[i]).sexpr()}for i in range(13)]
        metadata["model_exact_z3"]=model.sexpr()
    payload=json.dumps(metadata,indent=2)+"\n"
    if args.output:Path(args.output).write_text(payload)
    else:print(payload,end="")
    print("Fixed-macro solver result:",result,flush=True,file=__import__("sys").stderr)
