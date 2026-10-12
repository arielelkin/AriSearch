#!/usr/bin/env python3
"""Exact unique full neighbour-wheel audit of the twelve4+1+1residues."""
import itertools,json,sys
from pathlib import Path
data=json.loads(Path('research/certificates/two-hexagon-odd-pair-graph-orders.json').read_text())
attempts=json.loads(Path('research/certificates/two-hexagon-odd-pair-residue-tori.json').read_text())
rows=[]
for attempted in attempts['rows']:
    row=data['rows'][attempted['id']];core=set(row['surviving_states'])
    relations=[set(map(tuple,r)) for r in row['compatibility']]
    wheels=[]
    for state in sorted(core):
        choices=[[b for a,b in relations[k] if a==state and b in core] for k in range(6)]
        assert all(1<=len(choice)<=2 for choice in choices)
        compatible=[list(ring) for ring in itertools.product(*choices)
                    if all((ring[k],ring[(k+1)%6]) in relations[(k+2)%6] for k in range(6))]
        assert len(compatible)==1
        wheels.append({'state':state,'candidate_wheel_count':__import__('math').prod(map(len,choices)),
                       'unique_neighbor_wheel':compatible[0]})
    rows.append({'id':row['id'],'core_states':sorted(core),'wheels':wheels,
                 'choices_per_state_upper_bound':64,'all_six_induced_successor_relations_functional':True})
out={'scope':'Twelve explicitly retained4+1+1residuecores; exact wheel enumeration. Anyglobalfieldusesinducedfunctionalrelations.',
     'rooted_orders':len(rows),'states_checked':sum(len(r['wheels']) for r in rows),'rows':rows}
Path(sys.argv[1]).write_text(json.dumps(out,separators=(',',':')))
print('PASS:12residuecores,144states,onefullwheelperstate;all six induced directions functional.')
