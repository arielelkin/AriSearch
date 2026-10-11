"""Finite positive-witness search at e2c and eac alternate Cairo resonances.
Two copies of the recorded marginal-positive variant per species, all mirror
choices modulo one global reflection, all equal-length endpoint-colored
edge matchings. Failures are bounded evidence only. Default replay writes
nothing; --output-dir explicitly retains positive certificates.
"""
import argparse
from itertools import product
import json
from pathlib import Path
import runpy
from sage.all import QuadraticField,AA
H=runpy.run_path(str(Path(__file__).with_name('partial-contact-cairo-alternate-four-face.py')))
matchings,evaluate=H['matchings'],H['evaluate']
K=QuadraticField(3,'w',embedding=AA(3).sqrt());w=K.gen()
RATIOS={'e2c':1+w,'eac':1+4*w/3}

def base(kind):
    a=K(1);b=RATIOS[kind];c=((3+w)+(1-w)*b)/4;d=((3-w)+(1+w)*b)/4
    e=(w-1)*(1+b)/2;f=((w-5)+(1+3*w)*b)/4
    vals={'a':a,'b':b,'c':c,'d':d,'e':e,'f':f,'h':a-c,'j':b-d}
    if kind=='e2c':
        pl=['a','b','c','d','c','c'];pa=[120,90,120,90,120,180]
    else:
        pl=['c','h','b','c','d','c','a'];pa=[120,180,90,120,90,120,180]
    return vals,[('P',pl,pa),('P',pl,pa),('Q',['a','d','b','c','f'],[120,90,120,90,120]),('Q',['a','d','b','c','f'],[120,90,120,90,120])]


def search(kind,output_dir=None):
    vals,rows=base(kind);attempted=0
    for free in product((0,1),repeat=3):
        flags=(0,)+free;faces=[]
        for i,(species,labels,angles) in enumerate(rows):
            labels=list(labels);angles=list(angles)
            if flags[i]:labels.reverse();angles=[angles[0]]+list(reversed(angles[1:]))
            faces.append({'species':species,'mirror':bool(flags[i]),'labels':labels,'angles':angles,
                          'lengths':[vals[label] for label in labels]})
        groups={}
        for i,face in enumerate(faces):
            for j,length in enumerate(face['lengths']):
                beta=int(face['angles'][j]==120)+int(face['angles'][(j+1)%len(face['angles'])]==120)
                groups.setdefault((length,beta),[]).append((i,j))
        if any(len(items)%2 for items in groups.values()):continue
        choices=[list(matchings(v)) for v in groups.values()]
        for blocks in product(*choices):
            attempted+=1;pairs=[pair for block in blocks for pair in block]
            vertices=evaluate(faces,pairs)
            if vertices:
                cert={'ratio_name':kind,'ratio_coefficients':[str(x) for x in RATIOS[kind].list()],
                      'faces':[{k:v for k,v in face.items() if k!='lengths'} for face in faces],
                      'paired_edges':pairs,'vertex_classes':vertices,'attempts_before_witness':attempted}
                if output_dir:
                    path=Path(output_dir)/('partial-contact-cairo-alternate-'+kind+'-quotient.json')
                    path.write_text(json.dumps(cert,indent=2)+'\n')
                print('WITNESS',kind,'attempts',attempted,'vertices',len(vertices));return cert
    print('EXHAUSTED SPECIFIED FOUR-FACE DOMAIN',kind,'pairings',attempted)
    return None

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output-dir');args=parser.parse_args()
    for kind in RATIOS:search(kind,args.output_dir)
