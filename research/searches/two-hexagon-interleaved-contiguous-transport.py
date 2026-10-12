#!/usr/bin/env python3
"""Sound global transport after corrected I/C polygon closure gates.

Includes every local closure that was not universally geometrically rejected,
regardless of which angle parameter actually realizes it. Thus an empty
triangle core excludes every angle and metric simultaneously.
"""
import importlib.util
import itertools
import json
import sys

def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    result=importlib.util.module_from_spec(spec);spec.loader.exec_module(result)
    return result

local=module('local_side_gate','research/searches/two-hexagon-interleaved-local-side-gate.py')
colour=module('colour_transport','research/searches/two-hexagon-rank-nine-colour-transport.py')

def main(source,path):
    ledger=json.load(open(source));row=next(r for r in ledger['rows'] if r['B']=='C')
    rejected={'NO_NONZERO_VECTOR_ALL_ADMISSIBLE_ANGLES','NO_STRICTLY_POSITIVE_LENGTH_VECTOR_AT_ANY_ADMISSIBLE_ANGLE'}
    allowed={tuple(r['closure']) for r in row['closure_records']
             if r.get('positive_length_gate',{}).get('verdict',r['verdict']) not in rejected}
    states=[]
    for bs in range(12):
        w=[local.WORDS['C'][local.corner(bs,k)] for k in range(6)]
        choices=[[a for a in range(12)
                  if local.WORDS['I'][local.corner(a,k+2)]==w[k]
                  and local.WORDS['I'][local.corner(a,k+3)]==w[(k-1)%6]]
                 for k in range(6)]
        for aa in itertools.product(*choices):
            eq=local.closure(bs,aa)
            if eq in allowed:states.append({'B':bs,'A_ring':list(aa),'closure':eq})
    relations=colour.relations(states);alive,trace=colour.prune(states,relations)
    result={'scope':'I/C full native rings not universally rejected by CORRECTED exact symbolic closure; union over all admitted angle parameters',
            'symbolic_source':source,'allowed_native_side_closures':sorted(allowed),
            'states':states,'compatibility':relations,'triangle_deletion_rounds':trace,'survivors':alive,
            'verdict':'EMPTY' if not alive else 'SURVIVOR'}
    with open(path,'w') as f:json.dump(result,f,indent=2)
    print('I/C geometric ring superset',len(states),'triangle core',len(alive),'rounds',len(trace),flush=True)

if __name__=='__main__':main(sys.argv[1],sys.argv[2])
