#!/usr/bin/env python3
"""706 one-centre matched-endpoint star recipes on a finite P2 patch.

One centre per source type. Every active source-edge orbit carries one
matched endpoint and a centre spoke from each owner. Degree-two endpoints
are deleted CONDITIONAL on the alignment equations and opposite-dot
inequalities checked by edge-alignment.py. Additional spokes go to any
subset of the four source corners, with centre degree at least three.
All source edges erased. No source-edge chord or neighbour-dependent rule.
Finite-patch exclusions are witnesses; additional shape classes do not
exclude special parameter loci. Abstract dart fans are a geometric superset.
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

def tables(kind,mask,active,roles):
    chosen=[2*i for i in range(4) if mask>>i&1]
    chosen += [2*i+1 for i in range(4) if roles[kind,i][0] in active]
    chosen=sorted(chosen);assert len(chosen)>=3
    boundary={};pieces=[]
    for pi,u in enumerate(chosen):
        v=chosen[(pi+1)%len(chosen)];k=u
        while k!=v:boundary[k]=pi;k=(k+1)%8
        pieces.append([('P',u),(v,'P')])
    assert len(boundary)==8
    return boundary,pieces

def analyze(mk,md,active,P,owners,roles):
    tiles=P['tiles'];verts=[tuple(x) for x in P['verts']]
    tabs={k:tables(k,m,active,roles) for k,m in [('kite',mk),('dart',md)]};parent={}
    def find(x):
        while parent.setdefault(x,x)!=x:parent[x]=parent[parent[x]];x=parent[x]
        return x
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
        for ri,pi in members:
            kind,gv,a=tiles[ri]
            def node(s):
                if s=='P':return ('p',ri,'P')
                if s%2==0:return ('v',gv[s//2])
                return ('e',*sorted((gv[s//2],gv[(s//2+1)%4])))
            darts.extend((node(x),node(y)) for x,y in tabs[kind][1][pi])
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
        # Every endpoint has exactly two incident spokes. Convexity forces
        # collinearity with opposite directions, so delete it before counting.
        cyc=[nd for nd in cyc if nd[0]!='e']
        R=min(ri for ri,pi in members);vR=verts[tiles[R][1][0]];aR=tiles[R][2];forms=[]
        for nd in cyc:
            if nd[0]=='v':f={'c':arith.mulwk(arith.sub(verts[nd[1]],vR),-aR)}
            else:
                ri,s=nd[1:];kind,gv,a=tiles[ri]
                f={'c':arith.mulwk(arith.sub(verts[gv[0]],vR),-aR),
                   p2.PARAM[kind,s]:arith.mulwk((1,0,0,0),a-aR)}
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
            'class_count_unconstrained':True}

def main():
    a=argparse.ArgumentParser();a.add_argument('--patch',required=True);a.add_argument('--checkpoint',required=True);a.add_argument('--summary',required=True)
    args=a.parse_args();start=time.monotonic();cp=Path(args.checkpoint)
    lock=cp.with_suffix(cp.suffix+'.lock').open('a+')
    try:fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
    except BlockingIOError:raise SystemExit('This endpoint star checkpoint is already running')
    P,V,owners,components,roles,pairs=align.source(args.patch)
    h=hashlib.sha256(Path(args.patch).read_bytes()).hexdigest();rows=p2.checkpoint(cp)
    assert all(r['patch_sha256']==h for r in rows)
    done={(tuple(r['active_orbits']),r['kite_mask'],r['dart_mask']) for r in rows}
    assert len(done)==len(rows)
    order=[]
    for active in [(0,),(1,),(0,1)]:
        allowed=[m for m in range(16) if m.bit_count()+2*len(active)>=3]
        order.extend((active,mk,md) for mk in allowed for md in allowed)
    assert len(order)==706
    with cp.open('a') as f:
        for active,mk,md in order:
            if (active,mk,md) in done:continue
            r=analyze(mk,md,active,P,owners,roles)
            r.update(active_orbits=list(active),kite_mask=mk,dart_mask=md,patch_sha256=h)
            f.write(json.dumps(r,separators=(',',':'))+'\n');f.flush();rows.append(r)
    result={'domain':'One centre per P2 type; one matched endpoint per active long/short orbit; arbitrary corner-spoke subsets; centre degree >=3; all source edges erased',
            'patch':args.patch,'patch_sha256':h,'recipes_total':706,'recipes_processed':len(rows),'complete':len(rows)==706,
            'stats':dict(Counter(r['dead'] or 'alive' for r in rows)),
            'by_orbit':{str(active):dict(Counter(r['dead'] or 'alive' for r in rows if tuple(r['active_orbits'])==active)) for active in [(0,),(1,),(0,1)]},
            'alive':[{k:v for k,v in r.items() if k!='classes'} for r in rows if r['dead'] is None],
            'positive_dimension_requires_alignment':True,'conditional_endpoint_deletion':True,
            'constrained_class_collapse_not_searched':True,'elapsed_seconds':round(time.monotonic()-start,3)}
    p2.atomic_json(Path(args.summary),result);print(json.dumps(result),flush=True)
if __name__=='__main__':main()
