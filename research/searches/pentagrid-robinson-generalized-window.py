#!/usr/bin/env python3
"""Exact generalized (noninteger intercept) window gate for fixed U/V objects.

Domain: 213 mandatory boundaries + 196 retained full assemblies. Test necessary
vertex-strip membership over ALL three real internal shifts, not integer layers.
Each positive answer gives an open window-feasible region, not a macro partition.
Independent proper-window graph reconstruction is reused; no source sufficiency
is assumed merely from a partial graph. Nondestructive unless --output supplied.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import argparse, importlib.util, json, sys, time
from sage.all import Polyhedron, matrix, vector, QQ
from sage.version import version

ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('proper_window_independent',ROOT/'research/reviews/verify_pentagrid_robinson_penrose_window_independent.py')
w=importlib.util.module_from_spec(spec);spec.loader.exec_module(w)
F=w.F
FACETS=w.derive_facets()
NORMALS=[tuple(-x for x in h[1:]) for h in FACETS]

def dependencies():
    circuits=[]
    for count in (2,3,4):
        for indices in combinations(range(len(NORMALS)),count):
            mat=matrix(F,[NORMALS[i] for i in indices]).transpose()
            kernel=mat.right_kernel().basis()
            if len(kernel)!=1:continue
            weights=list(kernel[0])
            if all(w.sign(x)<=0 for x in weights):weights=[-x for x in weights]
            if any(w.sign(x)<=0 for x in weights):continue
            weights=[x/weights[0] for x in weights]
            assert mat*vector(F,weights)==0
            circuits.append((indices,weights))
    return circuits

def gate(N,circuits):
    # Exact compression: same facet normal, minimum constant over all vertices.
    rows=[];witnesses=[]
    for h0,hk,ha,ht in FACETS:
        vals=[(h0+hk*k+ha*a+ht*t,n) for n in N.values()
              for k,a,t in [w.projected(n)]]
        c,n=min(vals,key=lambda q:q[0])
        rows.append((c,-hk,-ha,-ht));witnesses.append(n)
    for indices,weights in circuits:
        constant=sum(weight*rows[i][0] for i,weight in zip(indices,weights))
        if w.sign(constant)<=0:
            return {'verdict':'no strict shifted-window witness',
                    'dual_obstruction':{'facet_indices':list(indices),
                     'selected_vertex_lifts':[list(witnesses[i]) for i in indices],
                     'selected_rows':[[str(x) for x in rows[i]] for i in indices],
                     'positive_weights':[str(x) for x in weights],
                     'constant_sum':str(constant)}}
    poly=Polyhedron(ieqs=rows,base_ring=F,backend='field')
    assert poly.dim()==3, 'strict infeasibility must have a positive circuit'
    vertices=list(poly.vertex_generator());assert vertices
    shift=[sum(p[j] for p in vertices)/len(vertices) for j in range(3)]
    slack=min(c+a*shift[0]+b*shift[1]+d*shift[2] for c,a,b,d in rows)
    assert w.sign(slack)>0
    return {'verdict':'strict shifted-window witness','internal_shift':[str(x) for x in shift],
            'minimum_facet_slack':str(slack),'closed_region_vertex_count':len(vertices),
            'integer_intercept_sum':shift[0] in QQ and QQ(shift[0]).denominator()==1}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path);args=ap.parse_args()
    started=time.monotonic();deadline=started+120
    circuits=dependencies()
    completion=json.loads((ROOT/'research/certificates/pentagrid-robinson-boundary-completion.json').read_text())
    residual=json.loads((ROOT/'research/certificates/pentagrid-robinson-residual-rhombs.json').read_text())
    out={'scope':'All213 necessary mandatory boundaries and196 retained full assemblies, arbitrary real3D internal shifts. Vertex window gate only; no global macro partition or unrestricted shape forcing.',
         'source_window':'I([0,1]^5), canonical rho lift, generalized fixed Penrose slope',
         'deadline_seconds':120,'positive_circuit_count':len(circuits),
         'window_facets':[[str(x) for x in h] for h in FACETS],
         'environment':{'Sage':version},'domains':{}}
    for domain,source in [('mandatory',completion),('full',residual)]:
        out['domains'][domain]={}
        for label,record in source['fixtures'].items():
            objects=record['surviving_boundary_words'] if domain=='mandatory' else record['results']
            results=[];counts=Counter()
            for ix,obj in enumerate(objects):
                if time.monotonic()>deadline:raise TimeoutError('single120-second domain deadline; incomplete')
                if domain=='full' and obj['whole_rhombs'] is None:continue
                words=obj if domain=='mandatory' else obj['side_words']
                _,N=w.lifts(label,words,None if domain=='mandatory' else obj['whole_rhombs'])
                lo,hi=min(map(sum,N.values())),max(map(sum,N.values()))
                if hi-lo>=5:
                    result={'verdict':'fails strict five-layer-width necessity'}
                else:result=gate(N,circuits)
                counts[result['verdict']]+=1
                results.append({'source_index':ix,'side_words':words,'vertex_count':len(N),
                                'layer_interval':[lo,hi],'window_gate':result})
            out['domains'][domain][label]={'object_count':len(results),'counts':dict(counts),'results':results}
            print(domain,label,dict(counts),flush=True,file=sys.stderr)
    out['elapsed_seconds']=time.monotonic()-started
    data=json.dumps(out,indent=2)+'\n'
    if args.output:args.output.write_text(data)
    else:print(data,end='')
    print('COMPLETE generalized window domain in',out['elapsed_seconds'],'seconds',file=sys.stderr)

if __name__=='__main__':
    if not __debug__:raise RuntimeError('Assertions required')
    main()
