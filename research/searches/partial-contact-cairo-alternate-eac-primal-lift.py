"""Primal-guided eight-face orientable flat quotient; 1024 exact lifts.
Normal replay is read-only; --output explicitly retains a positive witness.
No negative conclusion beyond this specified lifted seam-pattern domain.
"""
import argparse,json,lzma,runpy
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from collections import Counter
helper=runpy.run_path(str(Path(__file__).with_name('partial-contact-cairo-alternate-four-face.py')))
def search(output=None):
    certificate=Path(__file__).parents[1]/'certificates/partial-contact-cairo-alternate-eac-reflection-seam-balance.json.xz'
    r=json.loads(lzma.open(certificate,'rt').read());vs=[i for i,x in enumerate(r['type_frequencies']) if F(x)]
    lookup={(i//2,i%2):n for n,i in enumerate(vs)}
    assert list(lookup)==[(8,0),(8,1),(12,0),(12,1)]
    ns={s:sum(c[0]==s for c in r['corners']) for s,flip in lookup}
    skeleton=set()
    for cyc,x in zip(r['oriented_stars'],r['star_frequencies']):
        if not F(x):continue
        assert F(x)==F(1,4)
        for k,o in enumerate(cyc):
            oo=cyc[(k+1)%len(cyc)];s,i,ang=r['corners'][o//2];flip=o%2;t,j,_=r['corners'][oo//2];fl2=oo%2
            ex=i if flip else (i-1)%ns[s];ey=(j-1)%ns[t] if fl2 else j
            a=(lookup[s,flip],ns[s]-1-ex if flip else ex)
            b=(lookup[t,fl2],ns[t]-1-ey if fl2 else ey)
            skeleton.add(tuple(sorted((a,b))))
    skeleton=sorted(skeleton);nonself=[p for p in skeleton if p[0]!=p[1]];selfs=[p[0] for p in skeleton if p[0]==p[1]]
    assert len(nonself)==10 and len(selfs)==4
    degree=Counter(e for pair in nonself for e in pair);degree.update(selfs)
    assert set(degree.values())=={1} and len(degree)==24
    base=[]
    for s,flip in lookup:
        labels=['c','h','b','c','d','c','a'] if s==8 else ['a','d','b','c','f']
        angles=[120,180,90,120,90,120,180] if s==8 else [120,90,120,90,120]
        if flip:labels=labels[::-1];angles=[angles[0]]+angles[:0:-1]
        base.append({'species':'P' if s==8 else 'Q','mirror':bool(flip),'labels':labels,'angles':angles})
    faces=[dict(face,base_face=u,copy=t) for u,face in enumerate(base) for t in (0,1)]
    count=0
    for bits in product((0,1),repeat=len(nonself)):
        count+=1;pairs=[]
        for ((u,i),(v,j)),bit in zip(nonself,bits):
            pairs.extend([((2*u+t,i),(2*v+(t^bit),j)) for t in (0,1)])
        pairs.extend([((2*u,i),(2*u+1,i)) for u,i in selfs])
        vertices=helper['evaluate'](faces,pairs)
        if vertices:
            r={'kind':'eac','source_primal':certificate.name.removesuffix('.xz'),'finite_domain':'1024 two-copy lifts of 14 supported typed seams',
               'faces':faces,'paired_edges':pairs,'vertex_classes':vertices,'lift_bits':bits,'attempts_before_witness':count}
            if output:Path(output).write_text(json.dumps(r,indent=2)+'\n')
            print('WITNESS',count,'faces',len(faces),'edges',len(pairs),'vertices',len(vertices));print(json.dumps(r));return r
    print('EXHAUSTED SPECIFIED 1024 LIFTS');return None
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output');args=p.parse_args();search(args.output)
