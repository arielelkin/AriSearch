#!/usr/bin/env python3
"""Bounded exact two-class congruence loci for P2 survivor faces.

Every cyclic shift and reflection, rotation restricted to w^k (k=0..9),
NO straight-vertex deletion. Coordinates z_j=s_j+t_j*w with real s_j,t_j.
Thus congruence equations are linear over Q(sqrt(5)). All partitions into
at most two classes are tested by exact RREF with consistency pruning.
Forced zero edges, equal interior nodes and fixed exterior nodes are killed.
Positive-dimensional loci still require feasibility, changing angles, and
monohedral/mixed periodic-escape checks. Arbitrary and parameter-dependent
rotations and straight-angle subfamilies remain outside this bounded stage.
"""
import argparse, importlib.util, itertools, json, time
from pathlib import Path
from sage.all import CyclotomicField, QuadraticField, matrix, AA

HERE=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('p2',HERE/'penrose-kite-dart-recomposition.py');p2=importlib.util.module_from_spec(s);s.loader.exec_module(p2)
K=CyclotomicField(10);w=K.gen();F=QuadraticField(5,'sqrt5',embedding=AA(5).sqrt());phi=(1+F.gen())/2
kwphi=w+w**-1;f_to_k=F.hom([2*kwphi-1],K)

def split(v):
    a=list(K(v).vector());return F(a[0]-a[2])-phi*a[3],F(a[1])+phi*(a[2]+a[3])

def normalize(rows,n):
    if not rows:return ()
    M=matrix(F,rows).echelon_form();out=[]
    for row in M.rows():
        r=tuple(row)
        if not any(r):continue
        if not any(r[:n]):return None
        out.append(r)
    return tuple(out)

def lin(form,active,mirror=False):
    v=[K(0)]*(2*len(active)+1)
    for key,coeff in form.items():
        c=K(coeff)
        if mirror:c=c.conjugate()
        if key=='c':v[-1]+=c
        else:
            i=active.index(int(key));v[2*i]+=c;v[2*i+1]+=c*(w.conjugate() if mirror else w)
    return v

def edges(poly,active,mirror=False):
    if mirror:poly=list(reversed(poly))
    V=[lin(f,active,mirror) for f in poly]
    return [[b-a for a,b in zip(V[i],V[(i+1)%len(V)])] for i in range(len(V))]

def implied_zero(v,sys,n):
    vv=list(v)
    for r in sys:
        pivot=next(i for i,x in enumerate(r[:n]) if x)
        a=vv[pivot]
        if a:vv=[x-a*y for x,y in zip(vv,r)]
    return not any(vv)

def forced(var,sys,n):
    for r in sys:
        pivot=next(i for i,x in enumerate(r[:n]) if x)
        if pivot==var and not any(r[i] for i in range(n) if i!=var):return -r[-1]
    return None

def cross(a,b):
    return F(split(a.conjugate()*b)[1]) # Im()/Im(w)

def inside(q,kind):
    ref=[K(0),K(1),w if kind=='kite' else w/kwphi,w**2]
    if kind=='kite':return all(cross(ref[(i+1)%4]-ref[i],q-ref[i])>0 for i in range(4))
    a,b,c,d=ref
    return ((cross(b-a,q-a)>0 and cross(c-b,q-b)>0 and cross(a-c,q-c)>=0) or
            (cross(c-a,q-a)>=0 and cross(d-c,q-c)>0 and cross(a-d,q-d)>0))

def admissible(sys,active,es):
    n=2*len(active)
    for i,p in enumerate(active):
        x=forced(2*i,sys,n);y=forced(2*i+1,sys,n)
        if x is not None and y is not None:
            q=f_to_k(x)+f_to_k(y)*w
            if not inside(q,'kite' if p<2 else 'dart'):return False
    for p,q in ((0,1),(2,3)):
        if p in active and q in active:
            i,j=active.index(p),active.index(q)
            v=[F(0)]*(n+1);v[2*i]=1;v[2*j]=-1
            u=[F(0)]*(n+1);u[2*i+1]=1;u[2*j+1]=-1
            if implied_zero(v,sys,n) and implied_zero(u,sys,n):return False
    for e in es:
        a,b=zip(*(split(v) for v in e))
        if implied_zero(a,sys,n) and implied_zero(b,sys,n):return False
    return True

def options(P,Q,active,es):
    n=2*len(active);E=edges(P,active);out={}
    for mirror in (False,True):
        H=edges(Q,active,mirror)
        for k in range(10):
            for shift in range(len(E)):
                rows=[];u=w**k
                for i,e in enumerate(E):
                    v=[a-u*b for a,b in zip(e,H[(i+shift)%len(H)])]
                    ab=[split(x) for x in v];rows.extend([tuple(a for a,b in ab),tuple(b for a,b in ab)])
                sys=normalize(rows,n)
                if sys is not None and admissible(sys,active,es):out.setdefault(sys,(mirror,k,shift))
    return sorted(out, key=lambda x:(len(x),str(x)))

def encode(sys):return [[str(x) for x in r] for r in sys]

def run(row,max_seconds,max_nodes):
    start=time.monotonic();C=row['classes'];N=len(C)
    active=sorted({int(k) for c in C for f in c['forms'] for k in f if k!='c'});n=2*len(active)
    es=[e for c in C for e in edges(c['forms'],active)]
    ops={};op_counts={}
    for i in range(N):
        for j in range(i+1,N):
            if C[i]['corners']!=C[j]['corners']:continue
            ops[i,j]=options(C[i]['forms'],C[j]['forms'],active,es)
            op_counts[f'{i},{j}']=len(ops[i,j])
    loci={};nodes=0;complete=True;partitions=0
    for mask in range(1<<(N-1)):
        blocks=[[0]+[i for i in range(1,N) if not (mask>>(i-1)&1)],
                [i for i in range(1,N) if mask>>(i-1)&1]]
        if any(len({C[i]['corners'] for i in b})>1 for b in blocks):continue
        links=[tuple(sorted((b[0],i))) for b in blocks if b for i in b[1:]]
        if any(not ops.get(link) for link in links):continue
        partitions+=1;links.sort(key=lambda x:len(ops[x]));seen=set()
        def dfs(level,sys):
            nonlocal nodes,complete
            if nodes>=max_nodes or time.monotonic()-start>max_seconds:complete=False;return
            key=(level,sys)
            if key in seen:return
            seen.add(key);nodes+=1
            if level==len(links):
                if sys not in loci:loci[sys]={'dimension':n-len(sys),'blocks':blocks,'rref':encode(sys)}
                return
            for other in ops[links[level]]:
                merged=normalize(sys+other,n)
                if merged is not None and admissible(merged,active,es):dfs(level+1,merged)
                if not complete:return
        dfs(0,())
        if not complete:break
    return {'kite':row['kite'],'dart':row['dart'],'active_parameters':active,
            'rotation_domain':'w^k, k=0..9; reflections and cyclic shifts',
            'vertex_deletions':False,'option_counts':op_counts,'partitions_entered':partitions,
            'nodes':nodes,'complete':complete,'loci':list(loci.values()),
            'positive_dimensional_loci':sum(v['dimension']>0 for v in loci.values()),
            'elapsed_seconds':round(time.monotonic()-start,3)}

if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--checkpoint',required=True);a.add_argument('--output',required=True)
    a.add_argument('--max-seconds-per-pair',type=float,default=90);a.add_argument('--max-nodes',type=int,default=100000)
    args=a.parse_args();out=Path(args.output);results=json.loads(out.read_text()) if out.exists() else []
    done={(r['kite'],r['dart']) for r in results}
    for line in Path(args.checkpoint).read_text().splitlines():
        row=json.loads(line)
        if row['dead'] is not None or not row['interior_faces']:continue
        pair=(row['kite'],row['dart'])
        if pair in done:continue
        if len({c['corners'] for c in row['classes']})>2:
            r={'kite':pair[0],'dart':pair[1],'complete':True,'loci':[],
               'reason':'more than two genuine side counts; vertex deletions excluded'}
        else:r=run(row,args.max_seconds_per_pair,args.max_nodes)
        results.append(r);tmp=out.with_suffix(out.suffix+'.tmp');tmp.write_text(json.dumps(results,indent=1)+'\n');tmp.replace(out)
        print(json.dumps({k:v for k,v in r.items() if k not in ('loci','option_counts')}),flush=True)
