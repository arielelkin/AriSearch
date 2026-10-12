#!/usr/bin/env python3
"""Bounded endpoint-chord enlargement of P2 one-centre stars.

Add at most one chord from an active edge endpoint to a nonadjacent source
corner on each source type. Chords must lie in one fan face (no crossings).
Dart embeddings are a geometric superset. Interior degree-two vertices
are deleted CONDITIONALLY on convexity (which forces straightness). Higher
endpoint degrees are retained. Scalars r_long/r_short have artificial
complex-variable indices 4/5 in the holomorphic form representation;
real geometry must constrain their imaginary components to zero.
Generic signatures never by themselves exclude constrained two-class loci.
Checkpoint after each recipe with an exclusive lock and missing-row resume.
"""
import argparse, fcntl, hashlib, importlib.util, json, time
from collections import Counter, defaultdict
from pathlib import Path
HERE=Path(__file__).resolve().parent

def module(name,file):
    s=importlib.util.spec_from_file_location(name,HERE/file);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
p2=module('endpointp2','penrose-kite-dart-recomposition.py')
align=module('endpointalignment','penrose-kite-dart-edge-alignment.py')
arith=p2.arith;Z=p2.Z

def tables(kind,mask,active,roles,chord=None):
    """Split full fan cycles by one noncrossing endpoint-to-corner chord."""
    chosen=[2*i for i in range(4) if mask>>i&1]
    chosen += [2*i+1 for i in range(4) if roles[kind,i][0] in active]
    chosen=sorted(chosen);assert len(chosen)>=3
    cycles=[]
    for pi,u in enumerate(chosen):
        v=chosen[(pi+1)%len(chosen)];arc=[u];k=u
        while k!=v:k=(k+1)%8;arc.append(k)
        cycles.append(['P']+arc)
    if chord is not None:
        side,corner=chord;e,c=2*side+1,2*corner
        assert roles[kind,side][0] in active and corner not in (side,(side+1)%4)
        eligible=[i for i,C in enumerate(cycles) if e in C and c in C]
        if not eligible:return None
        assert len(eligible)==1
        i=eligible[0];C=cycles.pop(i);a,b=sorted((C.index(e),C.index(c)))
        if b-a==1 or b-a==len(C)-1:return None
        cycles.extend([C[a:b+1],C[b:]+C[:a+1]])
    boundary={};pieces=[]
    for pi,C in enumerate(cycles):
        edges=list(zip(C,C[1:]+C[:1]));internal=[]
        for a,b in edges:
            if a!='P' and b!='P' and b==(a+1)%8:
                assert a not in boundary;boundary[a]=pi
            else:internal.append((a,b))
        pieces.append(internal)
    assert len(boundary)==8
    return boundary,pieces

def recipes(active,roles):
    result={}
    for kind in ('kite','dart'):
        rows=[]
        for mask in range(16):
            if mask.bit_count()+2*len(active)<3:continue
            choices=[None]+[(side,corner) for side in range(4) if roles[kind,side][0] in active
                            for corner in range(4) if corner not in (side,(side+1)%4)]
            for chord in choices:
                t=tables(kind,mask,active,roles,chord)
                if t is not None:rows.append((mask,chord,t))
        result[kind]=rows
    return result

def analyze(mk,md,ck,cd,active,P,owners,roles):
    tiles=P['tiles'];verts=[tuple(x) for x in P['verts']]
    tabs={k:tables(k,m,active,roles,c) for k,m,c in [('kite',mk,ck),('dart',md,cd)]};parent={}
    def find(x):
        while parent.setdefault(x,x)!=x:parent[x]=parent[parent[x]];x=parent[x]
        return x
    global_darts={};neighbours=defaultdict(set)
    boundary_corners={v for edge,os_ in owners.items() if len(os_)==1 for v in edge}
    endpoint_owner={}
    for ri,(kind,gv,a) in enumerate(tiles):
        def node(s):
            if s=='P':return ('p',ri,'P')
            if s%2==0:return ('v',gv[s//2])
            nd=('e',*sorted((gv[s//2],gv[(s//2+1)%4])))
            endpoint_owner.setdefault(nd,(ri,s//2));return nd
        for pi,piece in enumerate(tabs[kind][1]):
            darts=[(node(x),node(y)) for x,y in piece];global_darts[ri,pi]=darts
            for u,v in darts:neighbours[u].add(v);neighbours[v].add(u)
    # With exactly two incident segments, convex faces require a flat turn.
    # Do not infer this at corners whose outside incident tiles are missing.
    flat={u for u,N in neighbours.items() if len(N)==2 and
          (u[0]=='p' or u[0]=='e' and len(owners[frozenset(u[1:])])==2 or
           u[0]=='v' and u[1] not in boundary_corners)}
    boundary=[]
    for edge,os_ in owners.items():
        for half in (0,1):
            nodes=[]
            for ri,side in os_:
                gv=tiles[ri][1];localhalf=half if gv[side]==min(edge) else 1-half
                nodes.append((ri,tabs[tiles[ri][0]][0][2*side+localhalf]))
            if len(nodes)==1:boundary.append(nodes[0])
            else:
                a,b=map(find,nodes)
                if a!=b:parent[a]=b
    for ri,(kind,gv,a) in enumerate(tiles):
        for pi in range(len(tabs[kind][1])):find((ri,pi))
    comps=defaultdict(list)
    for x in list(parent):comps[find(x)].append(x)
    bad={find(x) for x in boundary};classes={};nfaces=0
    for root,members in comps.items():
        if root in bad:continue
        nfaces+=1;darts=[]
        for ri,pi in members:darts.extend(global_darts[ri,pi])
        witness={'pieces':[list(x) for x in members]};ds=set(darts)
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
        cyc=[nd for nd in cyc if nd not in flat]
        R=min(ri for ri,pi in members);vR=verts[tiles[R][1][0]];aR=tiles[R][2];forms=[]
        for nd in cyc:
            if nd[0]=='v':f={'c':arith.mulwk(arith.sub(verts[nd[1]],vR),-aR)}
            elif nd[0]=='p':
                ri,s=nd[1:];kind,gv,a=tiles[ri]
                f={'c':arith.mulwk(arith.sub(verts[gv[0]],vR),-aR),
                   p2.PARAM[kind,s]:arith.mulwk((1,0,0,0),a-aR)}
            else:
                ri,side=endpoint_owner[nd];kind,gv,a=tiles[ri];ci,parity=roles[kind,side]
                v0,v1=verts[gv[side]],verts[gv[(side+1)%4]]
                if parity:v0,v1=v1,v0
                f={'c':arith.mulwk(arith.sub(v0,vR),-aR),
                   4+ci:arith.mulwk(arith.sub(v1,v0),-aR)}
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
                    if p2.real_sign(v)<0:return {'dead':'identical-spike','witness':witness}
                    forms.pop(i);changed=True;break
                if set(a)<= {'c'} and set(b)<= {'c'} and p2.cross_sign(a['c'],b['c'])<0:
                    witness['forms']=p2.serialize(forms);return {'dead':'fixed-reflex-corner','witness':witness}
        if len(forms)<=4:
            witness['forms']=p2.serialize(forms)
            return {'dead':'triangle-or-quadrilateral-escape','corners':len(forms),'witness':witness}
        key=p2.congruence_key(forms)
        if key not in classes:classes[key]={'corners':len(forms),'count':0,'forms':p2.serialize(forms),
                                           'source_tiles_in_example':sorted({ri for ri,pi in members})}
        classes[key]['count']+=1
    return {'dead':None,'interior_faces':nfaces,'generic_class_count':len(classes),'classes':list(classes.values()),
            'class_count_unconstrained':True,'degree_two_vertices_deleted':len(flat),
            'endpoint_degrees':dict(Counter(len(N) for u,N in neighbours.items() if u[0]=='e')),
            'flat_constraints_required':True}

def main():
    a=argparse.ArgumentParser();a.add_argument('--patch',required=True);a.add_argument('--checkpoint',required=True);a.add_argument('--summary',required=True)
    a.add_argument('--max-seconds',type=float,default=0)
    args=a.parse_args();start=time.monotonic();cp=Path(args.checkpoint)
    lock=cp.with_suffix(cp.suffix+'.lock').open('a+')
    try:fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
    except BlockingIOError:raise SystemExit('This endpoint-chord checkpoint is already running')
    P,V,owners,components,roles,pairs=align.source(args.patch)
    h=hashlib.sha256(Path(args.patch).read_bytes()).hexdigest();rows=p2.checkpoint(cp)
    assert all(r['patch_sha256']==h for r in rows)
    def key(r):return tuple(r['active_orbits']),r['kite_mask'],r['dart_mask'],tuple(r['kite_chord'] or ()),tuple(r['dart_chord'] or ())
    done={key(r) for r in rows};assert len(done)==len(rows)
    order=[];localcounts={}
    for active in [(0,),(1,),(0,1)]:
        local=recipes(active,roles);localcounts[str(active)]={k:len(v) for k,v in local.items()}
        order.extend((active,mk,md,ck,cd) for mk,ck,tk in local['kite'] for md,cd,td in local['dart'] if ck is not None or cd is not None)
    print(json.dumps({'recipes_total':len(order),'resumed':len(done),'local_types':localcounts}),flush=True)
    with cp.open('a') as f:
        for active,mk,md,ck,cd in order:
            if (active,mk,md,tuple(ck or ()),tuple(cd or ())) in done:continue
            if args.max_seconds and time.monotonic()-start>=args.max_seconds:break
            r=analyze(mk,md,ck,cd,active,P,owners,roles)
            r.update(active_orbits=list(active),kite_mask=mk,dart_mask=md,kite_chord=ck,dart_chord=cd,patch_sha256=h)
            f.write(json.dumps(r,separators=(',',':'))+'\n');f.flush();rows.append(r);done.add(key(r))
            if len(done)%500==0:print(json.dumps({'processed':len(done),'stats':dict(Counter(r['dead'] or 'alive' for r in rows)),'seconds':round(time.monotonic()-start,2)}),flush=True)
    result={'domain':'One centre per source; matched long/short endpoints with centre spokes; arbitrary corner spokes with centre degree >=3; at most one endpoint-to-nonadjacent-corner chord per source; abstract noncrossing fans; all source edges erased',
            'patch':args.patch,'patch_sha256':h,'recipes_total':len(order),'recipes_processed':len(rows),'complete':len(rows)==len(order),
            'local_types':localcounts,'stats':dict(Counter(r['dead'] or 'alive' for r in rows)),
            'alive':[{k:v for k,v in r.items() if k not in ('classes','patch_sha256')} for r in rows if r['dead'] is None],
            'conditional_degree_two_deletion':True,'endpoints_are_real_scalar_variables':True,
            'generic_class_count_is_unconstrained_upper_bound_for_specializations':True,
            'flat_alignment_and_constrained_class_collapse_not_searched':True,'elapsed_seconds':round(time.monotonic()-start,3)}
    p2.atomic_json(Path(args.summary),result);print(json.dumps(result),flush=True)
if __name__=='__main__':main()
