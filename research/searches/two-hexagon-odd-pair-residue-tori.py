#!/usr/bin/env python3
"""Positive metric-witness attempt at B-lattice indices3/4 (cell indices9/12).

Only the twelve explicit residual4+1+1cores. No absence theorem inferred.
"""
import importlib.util,json,sys
from fractions import Fraction
from pathlib import Path

spec=importlib.util.spec_from_file_location('metric',Path('research/searches/two-hexagon-balanced-root-ring-metrics.py'))
metric=importlib.util.module_from_spec(spec);spec.loader.exec_module(metric)
data=json.loads(Path('research/certificates/two-hexagon-odd-pair-graph-orders.json').read_text())
old=json.loads(Path('research/certificates/two-hexagon-odd-pair-graph-ring-metrics.json').read_text())
residues=[r for r in old['rows'] if r['queries'][0]['verdict']!='PERIODIC_ESCAPE']
assert len(residues)==12
report={'scope':'Twelve explicit4+1+1residualorders; positive periodic-witness attempt at original cell indices9/12, no global negative inference.',
        'seed':0,'workers':1,'timeout_per_query_seconds':3,'rows':[]}
for entry in residues:
    row=data['rows'][entry['id']]
    query=entry['queries'][0]
    classes=query['length_classes']
    assert all(metric.metric(row['states'][i])[0]==tuple(classes) for i in row['surviving_states'])
    angles=[Fraction(120)+Fraction(d,1000) for d in [1,10,100,1000,10000,-11111]]
    angles += [Fraction(360)-angles[a]-angles[b] for a,b in row['B_pair_order']]
    model=metric.sft.SFT([angles[:6],angles[6:]],[classes[:6],classes[6:]])
    result={'id':row['id'],'length_classes':classes,'torus_queries':[],'verdict':'NO_WITNESS_AT_9_OR_12'}
    for index in (9,12):
        found=False
        for n in range(1,index+1):
            if index%n:continue
            for shear in range(n):
                trial=metric.solve_torus(model,(n,shear,index//n))
                result['torus_queries'].append(trial)
                if 'labels' in trial:result['verdict']='PERIODIC_ESCAPE';found=True;break
            if found:break
        if found:break
    if result['verdict']!='PERIODIC_ESCAPE' and any(t['status']=='UNKNOWN' for t in result['torus_queries']):result['verdict']='UNKNOWN'
    report['rows'].append(result)
    Path(sys.argv[1]).write_text(json.dumps(report,separators=(',',':')))
    print(row['id'],result['verdict'],flush=True)
