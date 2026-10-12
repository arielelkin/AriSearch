#!/usr/bin/env python3
"""Joint arbitrary-rotation congruence gate, positive-dimensional P2 families.

Consumes metric option bases. Enumerates all 2-block partitions, retaining
only common congruence ideals of positive complex dimension which do not
force zero edges, equal source points or fixed exterior source points.
This is necessary only: real strict-convexity and actual source embedding
must still be checked. No vertex deletions. Checkpoint each partition.
"""
import fcntl
import argparse, hashlib, importlib.util, itertools, json, time
from pathlib import Path
HERE=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('metric',HERE/'penrose-kite-dart-metric-collapse.py');met=importlib.util.module_from_spec(s);s.loader.exec_module(met)

def admissible(G,R,active,norms):
    if list(G)==[R(1)]:return False,-1
    I=R.ideal(G);dim=int(I.dimension())
    if dim<=0:return False,dim
    if any(I.reduce(p)==0 for p in norms):return False,dim
    for k,p in enumerate(active):
        a=I.reduce(R.gen(2*k));b=I.reduce(R.gen(2*k+1))
        if a.is_constant() and b.is_constant():
            q=met.lin.f_to_k(met.F(a))+met.lin.f_to_k(met.F(b))*met.w
            if not met.lin.inside(q,'kite' if p<2 else 'dart'):return False,dim
    return True,dim

def main():
    a=argparse.ArgumentParser();a.add_argument('--source',required=True);a.add_argument('--metric',required=True)
    a.add_argument('--output',required=True);a.add_argument('--summary',required=True)
    a.add_argument('--max-seconds',type=float,default=180);a.add_argument('--max-nodes-per-partition',type=int,default=10000)
    args=a.parse_args();start=time.monotonic();out=Path(args.output)
    lock=out.with_suffix(out.suffix+'.lock').open('a+')
    try:fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
    except BlockingIOError:raise SystemExit('Joint checkpoint already has a running search.')
    source_bytes=Path(args.source).read_bytes();metric_bytes=Path(args.metric).read_bytes()
    h=hashlib.sha256(source_bytes+metric_bytes).hexdigest()
    previous=met.lin.p2.checkpoint(out);assert all(r['domain_hash']==h for r in previous)
    done={(r['kite'],r['dart'],r['mask']) for r in previous if r['complete']}
    opts=[json.loads(s) for s in metric_bytes.splitlines()]
    rows=[json.loads(s) for s in source_bytes.splitlines()]
    rows=[r for r in rows if r['dead'] is None and r['interior_faces'] and
          len({c['corners'] for c in r['classes']})==1 and r['classes'][0]['corners']==5]
    total=sum(1<<(len(r['classes'])-1) for r in rows);all_results=list(previous);stop=False
    with out.open('a') as f:
        for row in rows:
            C=row['classes'];N=len(C);R,active,D,norms=met.polynomials(C)
            options={}
            for i in range(N):
                for j in range(i+1,N):
                    available=[r for r in opts if r['kite']==row['kite'] and r['dart']==row['dart'] and r['i']==i and r['j']==j]
                    assert len(available)==2*C[i]['corners'],'Incomplete metric pair options'
                    bases={tuple(R(g) for g in r['basis']) for r in available if r['status']=='positive-dimensional-necessary-survivor'}
                    options[i,j]=sorted(bases,key=str)
            print(json.dumps({'pair':[row['kite'],row['dart']],'distinct_option_counts':{str(k):len(v) for k,v in options.items()}}),flush=True)
            cache={}
            for mask in range(1<<(N-1)):
                if (row['kite'],row['dart'],mask) in done:continue
                if time.monotonic()-start>=args.max_seconds:stop=True;break
                blocks=[[0]+[i for i in range(1,N) if not(mask>>(i-1)&1)],
                        [i for i in range(1,N) if mask>>(i-1)&1]]
                links=[tuple(sorted((b[0],i))) for b in blocks if b for i in b[1:]]
                links.sort(key=lambda x:len(options[x]));seen=set();loci={};nodes=0;complete=True
                def dfs(level,G):
                    nonlocal nodes,complete
                    if nodes>=args.max_nodes_per_partition or time.monotonic()-start>=args.max_seconds:
                        complete=False;return
                    key=(level,G)
                    if key in seen:return
                    seen.add(key);nodes+=1
                    if level==len(links):
                        valid,dim=admissible(G,R,active,norms)
                        if valid:loci[G]={'dimension':dim,'basis':[str(g) for g in G]}
                        return
                    for H in options[links[level]]:
                        combined=tuple(sorted(set(G+H),key=str))
                        if combined not in cache:
                            GG=tuple(R.ideal(combined).groebner_basis());valid,dim=admissible(GG,R,active,norms)
                            cache[combined]=(GG,valid)
                        GG,valid=cache[combined]
                        if valid:dfs(level+1,GG)
                        if not complete:return
                dfs(0,())
                result={'kite':row['kite'],'dart':row['dart'],'mask':mask,'blocks':blocks,
                        'domain_hash':h,'complete':complete,'nodes':nodes,
                        'active_parameters':active,'loci':list(loci.values())}
                f.write(json.dumps(result,separators=(',',':'))+'\n');f.flush();all_results.append(result)
                print(json.dumps({k:v for k,v in result.items() if k not in ('loci','domain_hash','blocks')}|{'loci_count':len(loci)}),flush=True)
                if not complete:stop=True;break
            if stop:break
    complete_rows={(r['kite'],r['dart'],r['mask']):r for r in all_results if r['complete']}
    result={'domain_hash':h,'partitions_total':total,'partitions_completed':len(complete_rows),
            'complete':len(complete_rows)==total,'vertex_deletions':False,
            'arbitrary_rotations_and_reflections':True,
            'retained_loci':sum(len(r['loci']) for r in complete_rows.values()),
            'elapsed_seconds_this_run':round(time.monotonic()-start,3)}
    met.lin.p2.atomic_json(Path(args.summary),result);print(json.dumps(result),flush=True)

if __name__=='__main__':main()
