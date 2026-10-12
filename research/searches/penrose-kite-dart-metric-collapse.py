#!/usr/bin/env python3
"""Arbitrary-rotation necessary congruence gate for P2 positive-dimensional families.

Full pairwise squared-distance equations, all cyclic shifts/reversals.
Real coordinates z_j=s_j+t_j*w; equations over Q(sqrt(5)), exact Groebner
bases. NO vertex deletions. A complex algebraic positive-dimensional locus
is necessary, not sufficient, for a real angle-varying family.

A pair option is rejected if the ideal is unit, zero-dimensional, forces a
zero final edge/equal interior nodes, or fixes a source node outside its
source polygon. Only complete pair-option lists create incompatibility
edges. An odd cycle of incompatible face classes forbids <=2 shape classes
on a positive-dimensional family in this bounded no-deletion domain.

Checkpoint after EVERY option; exclusive flock prevents duplicate jobs.
The wall limit is checked between Groebner calls, not inside Singular.
"""
import argparse, collections, fcntl, hashlib, importlib.util, itertools, json, time
from pathlib import Path
from sage.all import PolynomialRing, matrix

HERE=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('linear',HERE/'penrose-kite-dart-linear-collapse.py');lin=importlib.util.module_from_spec(s);s.loader.exec_module(lin)
F,w,phi=lin.F,lin.w,lin.phi

def polynomials(classes):
    active=sorted({int(k) for c in classes for f in c['forms'] for k in f if k!='c'})
    names=[f'{prefix}{j}' for j in active for prefix in ('s','t')]
    R=PolynomialRing(F,names,order='degrevlex');X=R.gens();polys=[]
    for c in classes:
        V=[]
        for form in c['forms']:
            L=lin.lin(form,active);parts=[lin.split(v) for v in L]
            a=sum((aa*X[i] for i,(aa,bb) in enumerate(parts[:-1])),R(parts[-1][0]))
            b=sum((bb*X[i] for i,(aa,bb) in enumerate(parts[:-1])),R(parts[-1][1]))
            V.append((a,b))
        polys.append(V)
    def norm(a,b):return a*a+phi*a*b+b*b
    distances=[];edge_norms=[]
    for V in polys:
        distances.append([[norm(a-c,b-d) for c,d in V] for a,b in V])
        edge_norms.extend(norm(V[i][0]-V[(i+1)%len(V)][0],V[i][1]-V[(i+1)%len(V)][1]) for i in range(len(V)))
    for p,q in ((0,1),(2,3)):
        if p in active and q in active:
            i,j=active.index(p),active.index(q)
            edge_norms.append(norm(X[2*i]-X[2*j],X[2*i+1]-X[2*j+1]))
    return R,active,distances,edge_norms

def option(R,active,D,i,j,orientation,shift,norms):
    n=len(D[i]);seq=[(shift+orientation*k)%n for k in range(n)]
    eq=[D[i][a][b]-D[j][seq[a]][seq[b]] for a in range(n) for b in range(a+1,n)]
    I=R.ideal(eq);G=I.groebner_basis();J=R.ideal(G)
    result={'basis':[str(g) for g in G]}
    if G==[R(1)] or list(G)==[R(1)]:result.update(status='unit',dimension=-1);return result
    dim=int(J.dimension());result['dimension']=dim
    if dim==0:result['status']='zero-dimensional';return result
    for p in norms:
        if J.reduce(p)==0:
            result.update(status='forced-degeneracy',degenerate_polynomial=str(p));return result
    for k,p in enumerate(active):
        a=J.reduce(R.gen(2*k));b=J.reduce(R.gen(2*k+1))
        if a.is_constant() and b.is_constant():
            q=lin.f_to_k(F(a))+lin.f_to_k(F(b))*w
            if not lin.inside(q,'kite' if p<2 else 'dart'):
                result.update(status='fixed-exterior-node',node=p,coordinates=[str(a),str(b)]);return result
    result['status']='positive-dimensional-necessary-survivor';return result

def odd_cycle(N,edges):
    E={tuple(sorted(e)) for e in edges}
    # Domains here have <=7 classes; enumerate simple odd cycles exactly.
    for length in range(3,N+1,2):
        for vertices in itertools.combinations(range(N),length):
            start=vertices[0]
            for rest in itertools.permutations(vertices[1:]):
                cyc=(start,)+rest
                if cyc[1]>cyc[-1]:continue
                if all(tuple(sorted((cyc[k],cyc[(k+1)%length]))) in E for k in range(length)):
                    return list(cyc)
    return None

def main():
    a=argparse.ArgumentParser();a.add_argument('--checkpoint',required=True);a.add_argument('--output',required=True)
    a.add_argument('--summary',required=True);a.add_argument('--max-seconds',type=float,default=180)
    args=a.parse_args();start=time.monotonic();out=Path(args.output)
    lock=out.with_suffix(out.suffix+'.lock').open('a+')
    try:fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
    except BlockingIOError:raise SystemExit('Metric checkpoint already has a running search.')
    raw=Path(args.checkpoint).read_bytes();h=hashlib.sha256(raw).hexdigest()
    rows=[json.loads(s) for s in raw.splitlines()]
    sources=[r for r in rows if r['dead'] is None and r['interior_faces'] and len({c['corners'] for c in r['classes']})==1]
    previous=lin.p2.checkpoint(out)
    assert all(r['source_sha256']==h for r in previous)
    done={(r['kite'],r['dart'],r['i'],r['j'],r['orientation'],r['shift']):r for r in previous}
    total=0;stop=False
    with out.open('a') as f:
        for row in sources:
            classes=row['classes'];R,active,D,norms=polynomials(classes)
            tasks=[(i,j,o,k) for i in range(len(classes)) for j in range(i+1,len(classes)) for o in (1,-1) for k in range(classes[i]['corners'])]
            total+=len(tasks)
            for i,j,o,k in tasks:
                key=(row['kite'],row['dart'],i,j,o,k)
                if key in done:continue
                if time.monotonic()-start>=args.max_seconds:stop=True;break
                t=time.monotonic();r=option(R,active,D,i,j,o,k,norms)
                r.update(kite=row['kite'],dart=row['dart'],i=i,j=j,orientation=o,shift=k,
                         source_sha256=h,active_parameters=active,elapsed_seconds=round(time.monotonic()-t,4))
                f.write(json.dumps(r,separators=(',',':'))+'\n');f.flush();done[key]=r
                if len(done)%20==0:print(json.dumps({'processed_options':len(done),'last_pair':[row['kite'],row['dart']],
                                                  'elapsed_seconds':round(time.monotonic()-start,2)}),flush=True)
            if stop:break
    summaries=[];total=0
    for row in sources:
        classes=row['classes'];N=len(classes);edges=[];pair_summaries=[]
        for i in range(N):
            for j in range(i+1,N):
                opts=[done.get((row['kite'],row['dart'],i,j,o,k)) for o in (1,-1) for k in range(classes[i]['corners'])]
                total+=len(opts);complete=all(r is not None for r in opts)
                statuses=collections.Counter(r['status'] for r in opts if r is not None)
                if complete and not statuses['positive-dimensional-necessary-survivor']:edges.append([i,j])
                pair_summaries.append({'i':i,'j':j,'complete':complete,'status_counts':dict(statuses)})
        cycle=odd_cycle(N,edges)
        summaries.append({'kite':row['kite'],'dart':row['dart'],'incompatibility_edges':edges,'odd_cycle':cycle,
                          'positive_dimensional_two_class_family_excluded_without_vertex_deletions':cycle is not None,
                          'pair_option_summaries':pair_summaries})
    result={'source_checkpoint':args.checkpoint,'source_sha256':h,'metric_options_total':total,
            'metric_options_completed':len(done),'complete':len(done)==total,
            'vertex_deletions':False,'arbitrary_rotations_and_reflections':True,
            'source_pairs':summaries,'elapsed_seconds_this_run':round(time.monotonic()-start,3)}
    lin.p2.atomic_json(Path(args.summary),result)
    print(json.dumps({k:v for k,v in result.items() if k!='source_pairs'}),flush=True)
    for r in summaries:print(json.dumps({k:v for k,v in r.items() if k!='pair_option_summaries'}),flush=True)

if __name__=='__main__':main()
