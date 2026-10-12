#!/usr/bin/env python3
"""Exact necessary strict/weak turn feasibility for retained P2 survivor faces.

All source point coordinates are free real variables over Q(sqrt(5)).
Strict turns are necessary for the NO vertex-deletion domain; weak turns
also admit straight-vertex specializations. No planar embedding, source-node
containment or periodicity follows from SAT. UNSAT excludes the encoded
necessary conditions only; no independent UNSAT proof certificate supplied.
"""
import argparse, importlib.util, json, time
from pathlib import Path
import z3
from sage.all import PolynomialRing
HERE=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('metric',HERE/'penrose-kite-dart-metric-collapse.py');met=importlib.util.module_from_spec(s);s.loader.exec_module(met)
F,phi=met.F,met.phi

def coordinates(classes):
    R,active,D,norms=met.polynomials(classes);V=[]
    for c in classes:
        seq=[]
        for f in c['forms']:
            parts=[met.lin.split(v) for v in met.lin.lin(f,active)]
            a=sum((q*R.gen(i) for i,(q,t) in enumerate(parts[:-1])),R(parts[-1][0]))
            b=sum((t*R.gen(i) for i,(q,t) in enumerate(parts[:-1])),R(parts[-1][1]))
            seq.append((a,b))
        V.append(seq)
    return R,active,V

def check(row,weak,timeout,interior=False,min_corners=0):
    R,active,V=coordinates(row['classes']);X=[z3.Real(str(v)) for v in R.gens()];root=z3.Real('positive_sqrt5')
    def convert(p):
        terms=[]
        for powers,c in R(p).dict().items():
            a,b=F(c).vector();v=z3.RealVal(str(a))+z3.RealVal(str(b))*root
            for x,k in zip(X,powers):
                if k:v*=x**int(k)
            terms.append(v)
        return z3.Sum(terms) if terms else z3.RealVal(0)
    solver=z3.SolverFor('QF_NRA');solver.set(timeout=timeout)
    solver.add(root*root==5,root>2,root<3)
    for P in V:
        turns=[]
        for i in range(len(P)):
            prev,here,nxt=P[i-1],P[i],P[(i+1)%len(P)]
            a,b=here[0]-prev[0],here[1]-prev[1];c,d=nxt[0]-here[0],nxt[1]-here[1]
            turn=convert(a*d-b*c);turns.append(turn);solver.add(turn>=0 if weak else turn>0)
        if min_corners:
            solver.add(z3.Sum([z3.If(t>0,z3.RealVal(1),z3.RealVal(0)) for t in turns])>=min_corners)
        # Positive normalized signed area is necessary, also for weak turns.
        area=sum(P[i][0]*P[(i+1)%len(P)][1]-P[i][1]*P[(i+1)%len(P)][0] for i in range(len(P)))
        solver.add(convert(area)>0)
    if interior:
        # Nonzero original edges allow genuine straight-vertex deletions.
        for P in V:
            for i in range(len(P)):
                da=P[(i+1)%len(P)][0]-P[i][0];db=P[(i+1)%len(P)][1]-P[i][1]
                solver.add(convert(da*da+phi*da*db+db*db)>0)
        for k,p in enumerate(active):
            a,b=R.gen(2*k),R.gen(2*k+1)
            ref=[(R(0),R(0)),(R(1),R(0)),(R(0),R(1) if p<2 else R(1/phi)),(R(-1),R(phi))]
            def turn(A,B):return convert((B[0]-A[0])*(b-A[1])-(B[1]-A[1])*(a-A[0]))
            if p<2:solver.add(*[turn(ref[i],ref[(i+1)%4])>0 for i in range(4)])
            else:
                A,B,C,D=ref
                solver.add(z3.Or(z3.And(turn(A,B)>0,turn(B,C)>0,turn(C,A)>=0),
                                 z3.And(turn(A,C)>=0,turn(C,D)>0,turn(D,A)>0)))
        for p,q in ((0,1),(2,3)):
            if p in active and q in active:
                i,j=active.index(p),active.index(q);da=R.gen(2*i)-R.gen(2*j);db=R.gen(2*i+1)-R.gen(2*j+1)
                solver.add(convert(da*da+phi*da*db+db*db)>0)
    t=time.monotonic();answer=solver.check()
    result={'kite':row['kite'],'dart':row['dart'],'weak_turns':weak,'timeout_ms':timeout,
            'status':str(answer),'elapsed_seconds':round(time.monotonic()-t,3),
            'active_parameters':active,'necessary_conditions_only':True,'interior_and_nonzero_edges':interior,'minimum_genuine_corners':min_corners}
    if answer==z3.sat:result['model']={str(v):solver.model().eval(v,model_completion=True).sexpr() for v in X}
    if answer==z3.unknown:result['reason_unknown']=solver.reason_unknown()
    return result,solver.sexpr()

if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--checkpoint',required=True);a.add_argument('--output',required=True)
    a.add_argument('--timeout-ms',type=int,default=10000);a.add_argument('--interior',action='store_true');a.add_argument('--min-corners',type=int,default=0);args=a.parse_args();out=Path(args.output)
    results=json.loads(out.read_text()) if out.exists() else [];assert all(r.get('interior_and_nonzero_edges',False)==args.interior and r.get('minimum_genuine_corners',0)==args.min_corners for r in results);done={(r['kite'],r['dart'],r['weak_turns']) for r in results}
    rows=[json.loads(s) for s in Path(args.checkpoint).read_text().splitlines()]
    rows=[r for r in rows if r['dead'] is None and r['interior_faces']]
    rows.sort(key=lambda r:(len({c['corners'] for c in r['classes']})!=1,r['kite'],r['dart']))
    for r in rows:
        for weak in (False,True):
            if (r['kite'],r['dart'],weak) in done:continue
            result,smt=check(r,weak,args.timeout_ms,args.interior,args.min_corners);results.append(result)
            Path(str(out)+f'.{r["kite"]}-{r["dart"]}-'+('weak' if weak else 'strict')+'.smt2').write_text(smt+'\n(check-sat)\n')
            met.lin.p2.atomic_json(out,results);print(json.dumps(result),flush=True)
