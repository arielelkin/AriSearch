#!/usr/bin/env python3
"""Exact necessary unit-modulus resultants of ten nonzero closure residues.
Domain: irreducible numerator factors in retained eleven-word symbolic data.
Factors U+1,V+1,UV-1 cannot vanish at positive acute turns; all remaining
reciprocal resultant roots still need exact unit-domain and geometry filtering.
"""
import argparse,json
from pathlib import Path
import sympy as s
U,V=s.symbols('U V',nonzero=True)
p=argparse.ArgumentParser();p.add_argument('--output',type=Path);p.add_argument('--check',type=Path);args=p.parse_args()
d=json.loads(Path('research/certificates/two-hexagon-001122-symbolic-b-closure.json').read_text())
rows=[]
for row in d['rows']:
    if row['identically_zero']:continue
    num=s.sympify(row['numerator'],locals={'U':U,'V':V})
    factors=[]
    for q,m in s.factor_list(num)[1]:
        impossible=any(s.cancel(q/r).is_number for r in (U+1,V+1,U*V-1))
        if impossible:
            factors.append({'factor':str(q),'multiplicity':m,'positive_acute_turn_exclusion':True})
            continue
        rec=s.fraction(s.cancel(q.subs({U:1/U,V:1/V},simultaneous=True)))[0]
        res=s.factor(s.resultant(q,rec,V))
        factors.append({'factor':str(q),'multiplicity':m,'reciprocal_numerator':str(rec),
                        'resultant_V':str(res)})
        print(''.join(map(str,row['word'])),res,flush=True)
    rows.append({'word':row['word'],'factors':factors})
out={'finite_domain':'All irreducible numerator factors of ten nonzero B closure rows; exact reciprocal elimination in V',
     'rows':rows,'scope':'Necessary zero conditions only; no angle-domain root exclusion asserted'}
if args.check:assert json.loads(args.check.read_text())==out
if args.output:args.output.write_text(json.dumps(out,indent=2)+'\n')
