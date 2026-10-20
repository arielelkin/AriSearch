"""Independent permutation verifier for every retained positive carrier."""
import json
from pathlib import Path
cert=json.loads(Path('research/certificates/regular-pentagon-heptagon-fourface-carrier-sol-2026-10-19.json').read_text())
starts=(0,5,10,17); sizes=(5,5,7,7)
face={s+i:f for f,(s,n) in enumerate(zip(starts,sizes)) for i in range(n)}
nextdart={s+i:s+(i+1)%n for s,n in zip(starts,sizes) for i in range(n)}
for c in cert['results']:
    if c['status']!='SAT':continue
    alpha={a:b for a,b in c['pairs']}; alpha.update({b:a for a,b in c['pairs']})
    assert sorted(alpha)==list(range(24)) and all(alpha[alpha[d]]==d and alpha[d]!=d for d in alpha)
    words=[c['word'],c['word'][:1]+c['word'][:0:-1] if c['Q1_reflected'] else c['word']]
    angles=[108]*10+words[0]+words[1]
    assert angles==c['angles']
    colors={s+i:('unit' if i%2==0 else c['length_colors'][((6-i if c['Q1_reflected'] and s==17 else i)-1)//2]) for s in (10,17) for i in range(7)}
    colors.update({i:'unit' for i in range(10)})
    assert all(colors[a]==colors[b] for a,b in c['pairs'])
    remain=set(alpha); orbits=[]
    while remain:
        d=min(remain); orbit=[]; x=d
        while x not in orbit:
            orbit.append(x); x=nextdart[alpha[x]]
        assert x==d
        remain.difference_update(orbit); orbits.append(orbit)
    assert len(orbits)==8 and all(len(v)==3 and sum(angles[d] for d in v)==360 for v in orbits)
    assert sorted(map(sorted,orbits))==sorted(map(sorted,c['vertices']))
    counts={k:0 for k in ('PP','PQ','QQ')}; adj={f:set() for f in range(4)}
    for a,b in c['pairs']:
        f,g=face[a],face[b]; adj[f].add(g);adj[g].add(f)
        counts['PP' if f<2 and g<2 else 'QQ' if f>=2 and g>=2 else 'PQ']+=1
    seen={0}
    for _ in range(4):seen|=set.union(*(adj[f] for f in seen))
    assert len(seen)==4 and counts==dict(PP=1,PQ=8,QQ=3)
    assert len(orbits)-len(c['pairs'])+4==0
print('Verified four SAT oriented flat-torus carriers independently.')
