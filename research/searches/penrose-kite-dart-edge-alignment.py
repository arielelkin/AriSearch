#!/usr/bin/env python3
"""Matched edge endpoints for one-centre P2 star recompositions.

Domain: one distinct strictly interior centre per kite/dart, repeated in
its marked reference frame. Chosen edge-role orbits carry one matched
endpoint, at a common directed fraction or its complement. All source
edges erased. Each owner contributes at most one centre--endpoint segment.
At a used endpoint convex final faces force the two segments to be straight
and forward. These necessary equations do not depend on corner spokes.

Source patch edge-role graph has two bipartite orbits (long, short). The
three nonempty activation subsets are checked. A retained finite patch
provides necessary constraints; completeness of the plane-wide P2 edge
atlas is not assumed. Positive dimension/SAT alone is not a construction.
"""
import argparse, fcntl, hashlib, importlib.util, json, time
from collections import defaultdict
from pathlib import Path
import z3
from sage.all import PolynomialRing

HERE=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('linear',HERE/'penrose-kite-dart-linear-collapse.py');lin=importlib.util.module_from_spec(s);s.loader.exec_module(lin)
K,F,w,phi=lin.K,lin.F,lin.w,lin.phi

def source(path):
    P=json.loads(Path(path).read_text());V=[K(v) for v in P['verts']];owners=defaultdict(list);g=defaultdict(set)
    for ri,(kind,gv,a) in enumerate(P['tiles']):
        for i in range(4):owners[frozenset((gv[i],gv[(i+1)%4]))].append((ri,i))
    role_pairs=set()
    for os_ in owners.values():
        if len(os_)!=2:continue
        (ri,i),(rj,j)=os_;A=P['tiles'][ri];B=P['tiles'][rj]
        assert A[1][i]==B[1][(j+1)%4] and A[1][(i+1)%4]==B[1][j]
        a,b=(A[0],i),(B[0],j);g[a].add(b);g[b].add(a);role_pairs.add(tuple(sorted((a,b))))
    components=[];seen=set();roles={}
    for start in sorted(g):
        if start in seen:continue
        parity={start:0};todo=[start];odd=False
        while todo:
            u=todo.pop();seen.add(u)
            for v in g[u]:
                if v in parity:
                    if parity[v]!=1-parity[u]:odd=True
                else:parity[v]=1-parity[u];todo.append(v)
        label='long' if any(i in (0,3) for kind,i in parity) else 'short'
        assert all((i in (0,3))==(label=='long') for kind,i in parity)
        assert not odd,'Endpoint orbit forced to midpoint; outside this initial domain'
        ci=len(components);components.append({'name':label,'roles':[[k,i,p] for (k,i),p in sorted(parity.items())]})
        for role,p in parity.items():roles[role]=(ci,p)
    assert len(components)==2
    return P,V,owners,components,roles,sorted(role_pairs)

def geometry(path,active):
    P,V,owners,components,roles,pairs=source(path)
    names=['sK','tK','sD','tD']+['r_'+components[i]['name'] for i in active]
    R=PolynomialRing(F,names,order='degrevlex');X=R.gens();fraction={ci:X[4+k] for k,ci in enumerate(active)}
    def constant(z):a,b=lin.split(z);return R(a),R(b)
    def point(kind,c=K(0),u=K(1)):
        offset=0 if kind=='kite' else 2;a,b=constant(c)
        us,ut=constant(u),constant(u*w)
        return a+us[0]*X[offset]+ut[0]*X[offset+1],b+us[1]*X[offset]+ut[1]*X[offset+1]
    def edgepoint(ri,i,origin,orientation):
        kind,gv,a=P['tiles'][ri];ci,parity=roles[kind,i]
        r=fraction[ci] if parity==0 else 1-fraction[ci]
        start=constant((V[gv[i]]-origin)*w**(-orientation));delta=constant((V[gv[(i+1)%4]]-V[gv[i]])*w**(-orientation))
        return start[0]+r*delta[0],start[1]+r*delta[1]
    crosses=set();dots=set();records=[]
    for edge,os_ in owners.items():
        if len(os_)!=2:continue
        (ri,i),(rj,j)=os_;kind,gv,a=P['tiles'][ri];ci,_=roles[kind,i]
        if ci not in active:continue
        kind2,gv2,b=P['tiles'][rj];origin=V[gv[0]]
        PA=point(kind);PB=point(kind2,(V[gv2[0]]-origin)*w**(-a),w**(b-a));E=edgepoint(ri,i,origin,a)
        E2=edgepoint(rj,j,origin,a);assert E==E2,'Matched endpoints disagree'
        A=(PA[0]-E[0],PA[1]-E[1]);B=(PB[0]-E[0],PB[1]-E[1])
        cross=A[0]*B[1]-A[1]*B[0]
        dot=A[0]*B[0]+A[1]*B[1]+phi/2*(A[0]*B[1]+A[1]*B[0])
        if cross:crosses.add(cross/cross.leading_coefficient())
        dots.add(dot);records.append({'source_tiles':[ri,rj],'source_sides':[i,j],'orbit':ci})
    return R,tuple(sorted(crosses,key=str)),tuple(sorted(dots,key=str)),components,roles,records,pairs

def solve(R,equations,dots,timeout):
    I=R.ideal(equations);G=I.groebner_basis();dim=int(I.dimension())
    X=[z3.Real(str(x)) for x in R.gens()];root=z3.Real('positive_sqrt5')
    def convert(p):
        terms=[]
        for powers,c in R(p).dict().items():
            a,b=F(c).vector();v=z3.RealVal(str(a))+z3.RealVal(str(b))*root
            for x,k in zip(X,powers):
                if k:v*=x**int(k)
            terms.append(v)
        return z3.Sum(terms) if terms else z3.RealVal(0)
    solver=z3.SolverFor('QF_NRA');solver.set(timeout=timeout);solver.add(root*root==5,root>2,root<3)
    solver.add(*[convert(g)==0 for g in G]);solver.add(*[convert(d)<0 for d in dots])
    for x in X[4:]:solver.add(x>0,x<1)
    for offset,kind in [(0,'kite'),(2,'dart')]:
        a,b=R.gen(offset),R.gen(offset+1)
        ref=[(R(0),R(0)),(R(1),R(0)),(R(0),R(1) if kind=='kite' else R(1/phi)),(R(-1),R(phi))]
        def turn(A,B):return convert((B[0]-A[0])*(b-A[1])-(B[1]-A[1])*(a-A[0]))
        if kind=='kite':solver.add(*[turn(ref[i],ref[(i+1)%4])>0 for i in range(4)])
        else:
            A,B,C,D=ref
            solver.add(z3.Or(z3.And(turn(A,B)>0,turn(B,C)>0,turn(C,A)>=0),
                             z3.And(turn(A,C)>=0,turn(C,D)>0,turn(D,A)>0)))
    t=time.monotonic();ans=solver.check()
    result={'basis':[str(g) for g in G],'complex_dimension':dim,'status':str(ans),
            'solver_seconds':round(time.monotonic()-t,4),'source_centres_not_fixed_constants':any(not I.reduce(x).is_constant() for x in R.gens()[:4]),
            'necessary_conditions_only':True}
    if ans==z3.sat:result['model']={str(x):solver.model().eval(x,model_completion=True).sexpr() for x in X}
    if ans==z3.unknown:result['reason_unknown']=solver.reason_unknown()
    return result,solver.sexpr()

if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--patch',required=True);a.add_argument('--output',required=True)
    a.add_argument('--timeout-ms',type=int,default=20000);args=a.parse_args();out=Path(args.output)
    lock=out.with_suffix(out.suffix+'.lock').open('a+')
    try:fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
    except BlockingIOError:raise SystemExit('Edge alignment checkpoint already running')
    h=hashlib.sha256(Path(args.patch).read_bytes()).hexdigest();results=json.loads(out.read_text()) if out.exists() else []
    assert all(r['patch_sha256']==h for r in results)
    done={tuple(r['active_orbits']) for r in results}
    for active in [(0,),(1,),(0,1)]:
        if active in done:continue
        start=time.monotonic();R,eq,dots,components,roles,records,pairs=geometry(args.patch,active)
        r,smt=solve(R,eq,dots,args.timeout_ms)
        r.update(active_orbits=list(active),orbit_definitions=components,variables=list(R.variable_names()),
                 equations=[str(e) for e in eq],dots=[str(d) for d in dots],source_edge_instances=len(records),
                 source_role_pairs=pairs,patch=args.patch,patch_sha256=h,elapsed_seconds=round(time.monotonic()-start,3))
        results.append(r);lin.p2.atomic_json(out,results)
        Path(str(out)+'.'+''.join(map(str,active))+'.smt2').write_text(smt+'\n(check-sat)\n')
        print(json.dumps({k:v for k,v in r.items() if k not in ('equations','dots','source_role_pairs','orbit_definitions')}),flush=True)
