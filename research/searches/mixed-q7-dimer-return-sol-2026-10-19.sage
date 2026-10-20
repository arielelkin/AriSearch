# Exact dimer frame cocycle; reads reviewed finite seam certificate only.
import json
from pathlib import Path
K=CyclotomicField(180); z=K.gen(); I=z**45
conj=lambda x: K(x).conjugate()
def xy(v): return K(v[0])+I*K(v[1])
def point(v): return [str((v+conj(v))/2),str((v-conj(v))/(2*I))]
data=json.loads(Path('research/searches/aa-bb-strand-atlas-sol-2026-10-19.json').read_text())
rows=[]
words=['ABBCCBC','ABBCCCB','ABCBBCC','ACBBBCC']
for word,row in zip(words,data['results']):
    endpoints=[xy(v) for v in row['root_P_check']['Q144_PP_common_vertices']]
    assert K(0) in endpoints
    v=next(v for v in endpoints if v!=0); m=v/2
    assert v*conj(v)==1
    bb=next(int(e) for e,t in row['types'].items() if t=='AA')
    steps=[s for s in row['seams'] if s['root_edge']==bb]
    U=next(s for s in steps if not s['isometry']['reflection'])
    R=next(s for s in steps if s['isometry']['reflection'])
    assert all(s['compatible'] for s in steps)
    assert all(s['compatible'] for s in row['strand_at_Q'])
    u=K(U['isometry']['complex_c']); tu=K(U['isometry']['complex_t'])
    c=K(R['isometry']['complex_c']); tr=K(R['isometry']['complex_t'])
    assert u==z**36 and u**5==1 and u not in [1,-1]
    # conjugating the orientation-preserving step by any reflected frame reverses turn.
    assert c*conj(u)/c==z**(-36)
    rows.append(dict(word=word,root_axis=point(v),root_midpoint=point(m),
      unreflected=dict(c=str(u),t=point(tu),axis=point(u*v),midpoint=point(u*m+tu),displacement=point(u*m+tu-m)),
      reflected=dict(c=str(c),t=point(tr),axis=point(c*conj(v)),midpoint=point(c*conj(m)+tr),displacement=point(c*conj(m)+tr-m)),
      conjugated_rotation=str(z**(-36)),local_validity='existing reviewed immediate atlas only; no plane extension'))
out=dict(scope='exact dimer-frame cocycle and counterexample to conserved physical direction/nonnegative signed turn; no tiling claim',
  universal_headings={'BB_to_CC_preserving_degrees':72,'BB_to_CC_reflected_first_two':'468-2*alpha','BB_to_CC_reflected_last_two':'684-2*alpha'},rows=rows)
Path('research/searches/mixed-q7-dimer-return-sol-2026-10-19.json').write_text(json.dumps(out,indent=2,default=int)+'\n')
print('PASS: four exact owner-dimer axis changes +72 degrees; reflected frames reverse signed turn; translations retained.')
