#!/usr/bin/env python3
"""Checkpointed bounded P2 recomposition search (exact algebra/combinatorics).

Domain: the 98 plane-graph types from ammann-two-class-decorations.py on
EACH labelled P2 source tile; <=2 strictly interior, distinct nodes, spokes,
PQ and source diagonals; no source-edge endpoints, neighbour dependence,
or transport. All source edges erased, so components are recomposed faces.
The dart is nonconvex; abstract types are a geometric superset. A rejection
is valid only if its specified embedding is geometrically realized with
nonzero decoration edges. Counts come from a finite source patch.

Positive dimension is NOT inferred from a class count. Two generic classes
means congruence identically for independent complex point variables.
More classes remain eligible for constrained positive-dimensional loci.
No float decisions. Reflections included by full distance-matrix signatures.
Resume appends only missing pairs; exclusive flock prevents duplicate jobs.

Replay: conda run --no-capture-output -n arisearch python
 research/searches/penrose-kite-dart-recomposition.py --patch PATCH.json
 --checkpoint ROWS.jsonl --summary SUMMARY.json [--max-seconds SECONDS]
"""
import argparse, fcntl, hashlib, importlib.util, json, os, time
from collections import Counter, defaultdict
from pathlib import Path

HERE=Path(__file__).resolve().parent

def module(name, file):
    s=importlib.util.spec_from_file_location(name,HERE/file)
    m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

arith=module('p2arith','ammann-two-class-pairs.py')
dec=module('p2dec','ammann-two-class-decorations.py')
Z=arith.Z0
PARAM={('kite','P'):0,('kite','Q'):1,('dart','P'):2,('dart','Q'):3}

def phi_sign(u,v):
    # u+v*phi, phi=(1+sqrt(5))/2. Compare integers only.
    A=2*u+v; B=v
    if B==0:return (A>0)-(A<0)
    if A==0:return (B>0)-(B<0)
    if (A>0)==(B>0):return (A>0)-(A<0)
    d=A*A-5*B*B
    return ((A>0)-(A<0))*((d>0)-(d<0))

def real_sign(v):
    assert arith.conj(v)==v
    return phi_sign(2*v[0]-v[2]+v[3],v[1]+v[2]-v[3])

def cross_sign(a,b):
    v=arith.mul(arith.conj(a),b)
    return phi_sign(v[1],v[2]+v[3])

def distance(a,b):
    d=arith.form_sub(a,b);out=defaultdict(lambda:Z)
    for i,v in d.items():
        for j,u in d.items():
            k=(-1 if i=='c' else i,-1 if j=='c' else j)
            out[k]=arith.add(out[k],arith.mul(arith.conj(v),u))
    return tuple((i,j,*v) for (i,j),v in sorted(out.items()) if v!=Z)

def congruence_key(poly):
    n=len(poly)
    D=[[distance(a,b) for b in poly] for a in poly]
    keys=[]
    for start in range(n):
        for orientation in (1,-1):
            seq=[(start+orientation*i)%n for i in range(n)]
            keys.append(tuple(D[seq[i]][seq[j]] for i in range(n) for j in range(i+1,n)))
    return n,min(keys)

def serialize(forms):
    return [{str(k):list(v) for k,v in f.items()} for f in forms]

def analyze(tk,td,verts,tiles,owners):
    tabs={'kite':arith.piece_tables(tk),'dart':arith.piece_tables(td)}
    parent={}
    def find(x):
        while parent.setdefault(x,x)!=x:
            parent[x]=parent[parent[x]];x=parent[x]
        return x
    boundary=[]
    for edge, os_ in owners.items():
        nodes=[(ri,tabs[tiles[ri][0]][0][side]) for ri,side in os_]
        if len(nodes)==1:boundary.append(nodes[0])
        else:
            assert len(nodes)==2
            a,b=map(find,nodes)
            if a!=b:parent[a]=b
    for ri,(kind,gv,a) in enumerate(tiles):
        for pi in range(len(tabs[kind][1])):find((ri,pi))
    comps=defaultdict(list)
    for x in list(parent):comps[find(x)].append(x)
    bad={find(x) for x in boundary}
    classes={};nfaces=0;crossing=0
    for root,members in comps.items():
        if root in bad:continue
        nfaces+=1;darts=[]
        for ri,pi in members:
            kind,gv,a=tiles[ri]
            def node(s):return ('v',gv[int(s)]) if s in '0123' else ('p',ri,s)
            darts.extend((node(x),node(y)) for x,y in tabs[kind][1][pi])
        witness={'pieces':[list(x) for x in members]}
        ds=set(darts)
        if len(ds)!=len(darts):return {'dead':'repeated-dart','witness':witness}
        if any((b,a) in ds for a,b in darts):return {'dead':'slit','witness':witness}
        nxt={}
        for a,b in darts:
            if a in nxt:return {'dead':'pinched-face','witness':witness}
            nxt[a]=b
        if not darts:return {'dead':'empty-boundary','witness':witness}
        start=darts[0][0];cyc=[start];cur=nxt[start]
        while cur!=start:
            if cur not in nxt or len(cyc)>len(darts):return {'dead':'broken-boundary','witness':witness}
            cyc.append(cur);cur=nxt[cur]
        if len(cyc)!=len(darts):return {'dead':'multiple-boundary-cycles','witness':witness}
        R=min(ri for ri,pi in members);vR=verts[tiles[R][1][0]];aR=tiles[R][2]
        forms=[]
        for nd in cyc:
            if nd[0]=='v':f={'c':arith.mulwk(arith.sub(verts[nd[1]],vR),-aR)}
            else:
                ri,s=nd[1:];kind,gv,a=tiles[ri]
                f={'c':arith.mulwk(arith.sub(verts[gv[0]],vR),-aR),
                   PARAM[(kind,s)]:arith.mulwk((1,0,0,0),a-aR)}
            forms.append({k:v for k,v in f.items() if v!=Z})
        changed=True
        while changed:
            changed=False;n=len(forms)
            if n<3:return {'dead':'degenerate-face','witness':witness}
            for i in range(n):
                a=arith.form_sub(forms[i],forms[i-1]);b=arith.form_sub(forms[(i+1)%n],forms[i])
                if not a or not b:return {'dead':'identically-zero-edge','witness':witness}
                if arith.cross_identically_zero(a,b):
                    k=next(iter(a));v=arith.mul(arith.conj(a[k]),b.get(k,Z))
                    if v==Z:return {'dead':'unresolved-identical-turn','witness':witness}
                    if real_sign(v)<0:return {'dead':'identical-spike','witness':witness}
                    forms.pop(i);changed=True;break
                if set(a)<= {'c'} and set(b)<= {'c'} and cross_sign(a['c'],b['c'])<0:
                    witness['forms']=serialize(forms)
                    return {'dead':'fixed-reflex-corner','witness':witness}
        if len(forms)<=4:
            witness['forms']=serialize(forms)
            return {'dead':'triangle-or-quadrilateral-escape','corners':len(forms),'witness':witness}
        spans=len({ri for ri,pi in members})>1
        crossing+=int(spans)
        key=congruence_key(forms)
        if key not in classes:classes[key]={'corners':len(forms),'count':0,'forms':serialize(forms),
                                          'source_tiles_in_example':sorted({ri for ri,pi in members}),
                                          'crosses_source_boundary':spans}
        classes[key]['count']+=1
    return {'dead':None,'interior_faces':nfaces,'crossing_faces':crossing,
            'generic_class_count':len(classes),'classes':list(classes.values())}

def checkpoint(path):
    rows=[]
    if path.exists():
        data=path.read_bytes();lines=data.splitlines(keepends=True);offset=0
        for i,line in enumerate(lines):
            try:row=json.loads(line)
            except json.JSONDecodeError:
                if i!=len(lines)-1:raise
                with path.open('r+b') as f:f.truncate(offset)
                break
            rows.append(row);offset+=len(line)
    return rows

def atomic_json(path,data):
    tmp=path.with_suffix(path.suffix+'.tmp');tmp.write_text(json.dumps(data,indent=1)+'\n');tmp.replace(path)

def main():
    a=argparse.ArgumentParser();a.add_argument('--patch',required=True);a.add_argument('--checkpoint',required=True)
    a.add_argument('--summary',required=True);a.add_argument('--max-seconds',type=float,default=0)
    args=a.parse_args();start=time.monotonic()
    cp=Path(args.checkpoint);cp.parent.mkdir(parents=True,exist_ok=True)
    lock=cp.with_suffix(cp.suffix+'.lock').open('a+')
    try:fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
    except BlockingIOError:raise SystemExit('This exact checkpoint is already being searched.')
    patch_bytes=Path(args.patch).read_bytes();P=json.loads(patch_bytes)
    verts=[tuple(x) for x in P['verts']];tiles=P['tiles'];owners=defaultdict(list)
    for ri,(kind,gv,orientation) in enumerate(tiles):
        for side in range(4):owners[frozenset((gv[side],gv[(side+1)%4]))].append((ri,side))
    T=dec.enumerate_types();assert len(T)==98
    types_bytes=(json.dumps(T,sort_keys=True)+'\n').encode()
    typepath=cp.with_suffix('.types.json')
    if typepath.exists():assert typepath.read_bytes()==types_bytes
    else:typepath.write_bytes(types_bytes)
    patch_hash=hashlib.sha256(patch_bytes).hexdigest()
    domain_hash=hashlib.sha256(patch_bytes+types_bytes).hexdigest()
    rows=checkpoint(cp)
    assert all(r['domain_hash']==domain_hash for r in rows), 'Checkpoint belongs to a different domain'
    done={(r['kite'],r['dart']) for r in rows};assert len(done)==len(rows)
    # Small point budgets first; deterministic order is retained explicitly.
    order=sorted(range(len(T)),key=lambda i:(T[i]['npoints'],i))
    pairs=sorted(((i,j) for i in order for j in order),key=lambda ij:(T[ij[0]]['npoints']+T[ij[1]]['npoints'],ij))
    print(json.dumps({'pid':os.getpid(),'resumed_pairs':len(done),'total_pairs':len(pairs),'source_tiles':len(tiles)}),flush=True)
    with cp.open('a') as output:
        for i,j in pairs:
            if (i,j) in done:continue
            if args.max_seconds and time.monotonic()-start>=args.max_seconds:break
            r=analyze(T[i],T[j],verts,tiles,owners)
            r.update(kite=i,dart=j,domain_hash=domain_hash)
            output.write(json.dumps(r,separators=(',',':'))+'\n');output.flush()
            rows.append(r);done.add((i,j))
            if len(done)%200==0:
                os.fsync(output.fileno())
                stats=Counter(r['dead'] or 'alive' for r in rows)
                print(json.dumps({'processed':len(done),'stats':dict(stats),'elapsed_seconds':round(time.monotonic()-start,2)}),flush=True)
    stats=Counter(r['dead'] or 'alive' for r in rows)
    alive=[r for r in rows if r['dead'] is None]
    result={'domain':'98 labelled plane-graph decorations per P2 kite/dart; <=2 interior points; source edges erased',
            'patch':args.patch,'patch_sha256':patch_hash,'domain_hash':domain_hash,'types':str(typepath),
            'source_tile_counts':P['tile_counts'],'pairs_total':len(pairs),'pairs_processed':len(done),
            'complete':len(done)==len(pairs),'finite_patch_only':True,'exact_decisions':True,
            'stats':dict(stats),'alive_count':len(alive),
            'generic_class_histogram':dict(Counter(r['generic_class_count'] for r in alive)),
            'generic_two_class_pairs':[[r['kite'],r['dart']] for r in alive if r['generic_class_count']==2],
            'constrained_congruence_loci':'NOT SEARCHED; extra generic classes do not exclude them',
            'elapsed_seconds_this_run':round(time.monotonic()-start,3)}
    atomic_json(Path(args.summary),result);print(json.dumps(result,sort_keys=True),flush=True)

if __name__=='__main__':main()
