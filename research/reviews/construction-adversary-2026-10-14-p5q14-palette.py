"""Independent native-palette extension check of the same mandatory P5/Q14 patches.
No larger patch, producer verdict or periodic quotient is used.
"""
from pathlib import Path
from functools import cache
from itertools import combinations
import argparse,json,runpy
D=runpy.run_path(str(Path(__file__).with_name('construction-adversary-2026-10-14-p5q14-independent.py')))
K=D['K'];z=D['z'];v=D['v'];P=D['P'];cross=D['cross'];real=D['real'];conj=D['conj'];sign=D['sign']
def encode(g):
    c=g.list();return [str(t) for t in c]+['0']*(12-len(c))

@cache
def partial(F,G):
    for subject,clip,reverse in [(F,G,False),(G,F,True)]:
        for c,p in enumerate(subject):
            for e,a in enumerate(clip):
                b=clip[(e+1)%len(clip)]
                if cross(b-a,p-a)==0 and sign(real((p-a)*conj(p-b)))<0:
                    return {'subject_from_second_face':reverse,'native_corner':c,'host_edge':e,'point':encode(p),'host_start':encode(a),'host_end':encode(b)}
    return None

def run():
    source=json.loads((Path(__file__).resolve().parents[1]/'certificates'/'construction-adversary-2026-10-14-p5q14-independent.json').read_text())
    result=[];totals={'disjoint_patches':0,'forbidden_partial_contact':0,'unextendable_native_star':0,'no_obstruction_in_this_patch':0}
    for row in source['rows']:
        word=row['word'];Q=D['polygon']([(v if bit else 1)*z**(2*k) for k,bit in enumerate(word)])
        opts=[D['options'](Q,k,word) for k in range(14)]
        for r in row['native_cycles']:
            if r['one_Q_attack']['status']=='FORCED_LOCAL_OVERLAP':continue
            cycle=r['cycle'];faces=[Q]+[opts[k][c]['face'] for k,c in enumerate(cycle)]
            for F in faces[1:].copy():
                M=D['mate'](F)
                if not any(set(M)==set(G) for G in faces):faces.append(M)
            assert len(faces)==21
            bad_partial=None
            for f,g in combinations(range(len(faces)),2):
                defect=partial(tuple(faces[f]),tuple(faces[g]))
                if defect is not None:bad_partial={'face_pair':[f,g],**defect};break
            groups={}
            for f,F in enumerate(faces):
                for c,p in enumerate(F):
                    counts=groups.setdefault(p,[0,0,0])
                    counts[2 if f==0 else 0 if c==0 else 1]+=1
            bad_star=next(({'counts':counts,'point':encode(point),'corner_occurrences':[[f,c] for f,F in enumerate(faces) for c,p in enumerate(F) if p==point]} for point,counts in groups.items() if not any(all(n<=m for n,m in zip(counts,full)) for full in [(2,1,0),(0,2,1)])),None)
            totals['disjoint_patches']+=1
            if bad_partial is not None:status='forbidden_partial_contact'
            elif bad_star is not None:status='unextendable_native_star'
            else:status='no_obstruction_in_this_patch'
            totals[status]+=1
            result.append({'word':word,'cycle':cycle,'status':status,'first_partial':bad_partial,'first_unextendable_star_counts':bad_star})
        print('Exact palette check word',''.join(map(str,word)),'patches total',totals['disjoint_patches'],flush=True)
    assert totals['disjoint_patches']==364
    return {'schema':'independent-P5Q14-mandatory-palette-v1','summary':totals,'patches':result,'scope':'Only existing21face mandatory-dimer completion domain; absent defect is not plane existence.'}

def main():
    p=argparse.ArgumentParser();p.add_argument('--output');p.add_argument('--check');a=p.parse_args();r=run()
    if a.check:assert json.loads(Path(a.check).read_text())==r
    if a.output:
        with Path(a.output).open('x') as f:json.dump(r,f,indent=2);f.write('\n')
    print(json.dumps(r['summary'],indent=2))
if __name__=='__main__':main()
