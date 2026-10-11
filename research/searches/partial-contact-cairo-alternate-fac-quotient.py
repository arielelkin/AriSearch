"""Find an actual four-face periodic quotient at b/a=sqrt3.
Finite domain: specified one whole and one b-subdivided copy per species,
specified opposed f orders, every mirror choice modulo global reflection,
and all numerical equal-edge pairings. Normal replay is read-only.
"""
import argparse
from itertools import product
import json
from pathlib import Path
import runpy
from sage.all import QuadraticField,AA

helper=runpy.run_path(str(Path(__file__).with_name('partial-contact-cairo-alternate-four-face.py')))
matchings,evaluate=helper['matchings'],helper['evaluate']
K=QuadraticField(3,'w',embedding=AA(3).sqrt());w=K.gen()
vals={'a':K(1),'b':w,'c':w/2,'d':K(3)/2,'e':K(1),'j':w-K(3)/2}
BASE=[('P',['a','b','c','d','e'],[120,90,120,90,120]),
      ('P',['a','j','d','c','d','e'],[120,90,180,120,90,120]),
      ('Q',['a','d','b','c','c','a'],[120,90,120,90,120,180]),
      ('Q',['a','d','d','j','c','a','c'],[120,90,120,180,90,120,180])]

def search(output=None):
    attempted=0
    for free in product((0,1),repeat=3):
        flags=(0,)+free;faces=[]
        for i,(species,labels,angles) in enumerate(BASE):
            labels=list(labels);angles=list(angles)
            if flags[i]:labels.reverse();angles=[angles[0]]+list(reversed(angles[1:]))
            faces.append({'species':species,'mirror':bool(flags[i]),'labels':labels,'angles':angles,
                          'lengths':[vals[label] for label in labels]})
        groups={}
        for i,face in enumerate(faces):
            for j,length in enumerate(face['lengths']):groups.setdefault(length,[]).append((i,j))
        choices=[list(matchings(v)) for v in groups.values()]
        for blocks in product(*choices):
            attempted+=1;pairs=[pair for block in blocks for pair in block]
            vertices=evaluate(faces,pairs)
            if vertices:
                cert={'ratio_name':'fac','ratio_coefficients':[str(x) for x in w.list()],
                      'faces':[{k:v for k,v in face.items() if k!='lengths'} for face in faces],
                      'paired_edges':pairs,'vertex_classes':vertices,'attempts_before_witness':attempted}
                if output:Path(output).write_text(json.dumps(cert,indent=2)+'\n')
                print('WITNESS fac full augmentation; attempts',attempted,'vertices',len(vertices))
                print(json.dumps(cert,indent=2))
                return cert
    print('EXHAUSTED SPECIFIED FOUR-FACE DOMAIN; pairings',attempted)
    return None

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output');args=parser.parse_args()
    search(args.output)
