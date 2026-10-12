#!/usr/bin/env python3
"""Straight-vertex cells for the two one-point P2 hexagon survivors.

Enumerates realizable zero-turn Boolean patterns in retained necessary
weak-convexity SMT domains (strict source interior, nonzero edges, >=5 real
corners). For each cell, imposes zero-turn equations, deletes exactly those
vertices, then checks arbitrary-rotation congruence partitions over
Q(sqrt(5)). A surviving complex locus is only a candidate; solver SAT does
not establish the actual source embedding or positive real dimension.
"""
import fcntl
import argparse, importlib.util, itertools, json, time
from pathlib import Path
import z3
HERE=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('conv',HERE/'penrose-kite-dart-convexity.py');conv=importlib.util.module_from_spec(s);s.loader.exec_module(conv)
met=conv.met
s=importlib.util.spec_from_file_location('joint',HERE/'penrose-kite-dart-joint-collapse.py');joint=importlib.util.module_from_spec(s);s.loader.exec_module(joint)

def run(row,smt_path,timeout,max_cells,max_seconds):
    start=time.monotonic();R,active,V=conv.coordinates(row['classes']);N=len(V)
    X=[z3.Real(str(v)) for v in R.gens()];root=z3.Real('positive_sqrt5')
    def convert(p):
        terms=[]
        for exponents,c in R(p).dict().items():
            a,b=met.F(c).vector();v=z3.RealVal(str(a))+z3.RealVal(str(b))*root
            for x,k in zip(X,exponents):
                if k:v*=x**int(k)
            terms.append(v)
        return z3.Sum(terms) if terms else z3.RealVal(0)
    turn=[];indices=[]
    for ci,P in enumerate(V):
        for i in range(len(P)):
            A,B,C=P[i-1],P[i],P[(i+1)%len(P)]
            turn.append((B[0]-A[0])*(C[1]-B[1])-(B[1]-A[1])*(C[0]-B[0]));indices.append((ci,i))
    zero=[convert(p)==0 for p in turn]
    solver=z3.SolverFor('QF_NRA');solver.set(timeout=timeout);solver.from_string(Path(smt_path).read_text())
    cells=[];complete=False;reason='cell-limit'
    while len(cells)<max_cells and time.monotonic()-start<max_seconds:
        answer=solver.check()
        if answer==z3.unsat:complete=True;reason='exhausted-zero-turn-patterns';break
        if answer==z3.unknown:reason=solver.reason_unknown();break
        M=solver.model();pattern=[z3.is_true(M.eval(p,model_completion=True)) for p in zero]
        assert any(pattern),'Strict turn system was UNSAT'
        deleted=[[] for _ in range(N)]
        for yes,(ci,i) in zip(pattern,indices):
            if yes:deleted[ci].append(i)
        classes=[dict(c,forms=[f for i,f in enumerate(c['forms']) if i not in deleted[ci]],
                      corners=len(c['forms'])-len(deleted[ci])) for ci,c in enumerate(row['classes'])]
        R2,active2,D,norms=met.polynomials(classes);assert R2==R and active==active2
        Q=tuple(R.ideal([p for p,b in zip(turn,pattern) if b]).groebner_basis())
        options={}
        for i in range(N):
            for j in range(i+1,N):
                if classes[i]['corners']!=classes[j]['corners']:continue
                bases=set();n=classes[i]['corners']
                for o in (1,-1):
                    for shift in range(n):
                        seq=[(shift+o*k)%n for k in range(n)]
                        eq=[D[i][a][b]-D[j][seq[a]][seq[b]] for a in range(n) for b in range(a+1,n)]
                        G=tuple(R.ideal(list(Q)+eq).groebner_basis());valid,dim=joint.admissible(G,R,active,norms)
                        if valid:bases.add(G)
                options[i,j]=sorted(bases,key=str)
        loci={};cache={};nodes=0
        for mask in range(1<<(N-1)):
            blocks=[[0]+[i for i in range(1,N) if not(mask>>(i-1)&1)],
                    [i for i in range(1,N) if mask>>(i-1)&1]]
            if any(len({classes[i]['corners'] for i in b})>1 for b in blocks):continue
            links=[tuple(sorted((b[0],i))) for b in blocks if b for i in b[1:]]
            if any(not options.get(link) for link in links):continue
            links.sort(key=lambda x:len(options[x]));seen=set()
            def dfs(level,G):
                nonlocal nodes
                key=(level,G)
                if key in seen:return
                seen.add(key);nodes+=1
                if level==len(links):
                    valid,dim=joint.admissible(G,R,active,norms)
                    if valid:loci[G]={'dimension':dim,'basis':[str(g) for g in G],'blocks':blocks}
                    return
                for H in options[links[level]]:
                    combined=tuple(sorted(set(G+H),key=str))
                    if combined not in cache:
                        GG=tuple(R.ideal(combined).groebner_basis());valid,dim=joint.admissible(GG,R,active,norms)
                        cache[combined]=(GG,valid)
                    GG,valid=cache[combined]
                    if valid:dfs(level+1,GG)
            dfs(0,Q)
        cell={'deleted_vertices':deleted,'side_counts':[c['corners'] for c in classes],
              'zero_turn_basis':[str(g) for g in Q],'nodes':nodes,'loci':list(loci.values()),
              'necessary_condition_model':{str(x):M.eval(x,model_completion=True).sexpr() for x in X}}
        cells.append(cell)
        print(json.dumps({'pair':[row['kite'],row['dart']],'cell':len(cells),'deleted':deleted,'loci':len(loci)}),flush=True)
        solver.add(z3.Or([z3.Not(p) if yes else p for p,yes in zip(zero,pattern)]))
    if time.monotonic()-start>=max_seconds:reason='wall-limit-between-cells'
    return {'kite':row['kite'],'dart':row['dart'],'complete':complete,'reason':reason,'cells':cells,
            'retained_loci':sum(len(c['loci']) for c in cells),'elapsed_seconds':round(time.monotonic()-start,3)}

if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--checkpoint',required=True);a.add_argument('--convexity',required=True)
    a.add_argument('--output',required=True);a.add_argument('--timeout-ms',type=int,default=10000)
    a.add_argument('--max-cells',type=int,default=100);a.add_argument('--max-seconds-per-pair',type=float,default=120)
    args=a.parse_args();out=Path(args.output);results=json.loads(out.read_text()) if out.exists() else []
    lock=out.with_suffix(out.suffix+'.lock').open('a+')
    try:fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
    except BlockingIOError:raise SystemExit('Flat checkpoint already has a running search.')
    done={(r['kite'],r['dart']) for r in results if r['complete']}
    rows=[json.loads(s) for s in Path(args.checkpoint).read_text().splitlines()]
    for row in rows:
        pair=(row['kite'],row['dart'])
        if pair not in ((1,3),(3,1)) or pair in done:continue
        smt=args.convexity+f'.{pair[0]}-{pair[1]}-weak.smt2'
        r=run(row,smt,args.timeout_ms,args.max_cells,args.max_seconds_per_pair)
        results=[v for v in results if (v['kite'],v['dart'])!=pair]+[r]
        met.lin.p2.atomic_json(out,results);print(json.dumps({k:v for k,v in r.items() if k!='cells'}),flush=True)
