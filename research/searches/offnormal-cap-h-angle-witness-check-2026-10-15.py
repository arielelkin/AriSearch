"""Independent stdlib exact witness verifier; no solver or producer imports.
Reconstruct all sixteen source/parity/endpoints and each actual D6 alias.
"""
import ast,json
from fractions import Fraction as Q
from pathlib import Path
j=json.loads(Path('research/certificates/offnormal-cap-h-angle-gate-2026-10-15.json').read_text())
assert j['status']=='sat'
H=[Q(x) for x in j['H']]
b={ast.literal_eval(k):Q(v) for k,v in j['base'].items()}
theta={ast.literal_eval(k):Q(v) for k,v in j['theta'].items()}
E={ast.literal_eval(k):Q(v) for k,v in j['external'].items()}
assert len(H)==6 and sum(H)==720 and all(0<x<180 for x in H)
assert set(b)==set(theta)=={(Z,r) for Z in ('X','Y') for r in ('tail','head')}
assert all(0<x<90 for x in b.values())
for Z in ('X','Y'):
    assert theta[Z,'tail']+theta[Z,'head']==180-b[Z,'tail']-b[Z,'head']
    for role in ('tail','head'):
        t=theta[Z,role];assert 0<t<180
        pair=[E[Z,role,k] for k in (0,1)]
        assert sum(pair)==180+t and all(t<x<180 for x in pair)
# Independently encoded actual arrow source incidences, by physical edge.
ARROWS={'thin':[(0,1,'X'),(2,1,'X'),(2,3,'Y'),(0,3,'Y')],
        'thick':[(0,1,'X'),(1,2,'Y'),(3,2,'Y'),(0,3,'X')]}
expected=[]
for species,arrows in ARROWS.items():
    for parity in (0,1):
        for receiver in range(1-parity,4,2):
            for endpoint in (receiver,(receiver+1)%4):expected.append((species,parity,receiver,endpoint))
assert [(r['species'],r['parity'],r['receiver'],r['endpoint']) for r in j['aliases']]==expected
patterns=set()
for r in j['aliases']:
    species,parity,receiver,v=r['species'],r['parity'],r['receiver'],r['endpoint']
    T,J,Z=ARROWS[species][receiver]
    incoming='tail' if v==T else 'head'
    donor=(v-1)%4 if v==receiver else v
    assert donor%2==parity
    DT,DH,DZ=ARROWS[species][donor]
    outgoing='tail' if v==DT else 'head'
    sigma=((36,144) if species=='thin' else (72,108))[v%2]
    alpha=Q(sigma)+b[Z,incoming]-b[DZ,outgoing]
    assert Q(r['alpha'])==alpha
    alias=r['alias'];assert 0<=alias<12
    start,bit=divmod(alias,2);direction=1 if bit else -1
    indices=tuple((start+direction*k)%6 for k in range(6))
    angles=[H[i] for i in indices]
    assert angles[:3]==[alpha,E[Z,incoming,0],E[Z,incoming,1]]
    M=angles[3];inner=360-alpha-theta[Z,incoming]-M
    assert 0<M<180 and 0<inner<180
    assert all(x>inner for x in angles[4:])
    assert sum(angles[4:])==180+inner
    patterns.add((str(alpha),incoming,indices,str(inner)))
assert len(patterns)==4
print(json.dumps(dict(status='PASS',source_contexts=16,exact_D6_patterns=4,H=[str(x) for x in H],scope='necessary H angle compatibility only; no metric or P/cap compatibility'),sort_keys=True))
