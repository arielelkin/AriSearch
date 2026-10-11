"""Exact necessary augmented-corner balance at all three f resonances.
Optional native a,b T locations come from the two-T switch; c,d stay whole.
An UNSAT system carries a rational dual; a SAT answer is only local evidence.
"""
import argparse
from collections import Counter
from itertools import product, combinations_with_replacement
import json
from pathlib import Path
from fractions import Fraction
import z3
from sage.all import QuadraticField, AA
K=QuadraticField(3,'w',embedding=AA(3).sqrt());w=K.gen()
RATIOS={'f2c':(28*w+13)/37,'fac':w,'f2a':(20*w-11)/13}


def variants(kind):
    a=K(1);b=RATIOS[kind];c=((3+w)+(1-w)*b)/4;d=((3-w)+(1+w)*b)/4
    e=(w-1)*(1+b)/2
    vals={'a':a,'b':b,'c':c,'d':d,'e':e,'h':a-c,'j':b-d}
    out=[]
    for species in ('P','Q'):
        for sa,sb in product((0,1),repeat=2):
            for cut in range(2 if kind=='fac' and species=='Q' else 1):
                if species=='P':
                    labels=['a','b','c','d','e'];angles=[120,90,120,90,120]
                else:
                    banks={'f2c':['c','c'],'f2a':['a','a'],
                           'fac':(['a','c'] if cut==0 else ['c','a'])}[kind]
                    labels=['a','d','b','c']+banks;angles=[120,90,120,90,120,180]
                # A native side has a prescribed direction of endpoint angles;
                # replace its edge and add the straight corner after first piece.
                refined=[];newangles=[]
                for idx,label in enumerate(labels):
                    pieces=[label]
                    if idx==0 and sa:pieces=['c','h'] # a: beta to right
                    if label=='b' and idx<4 and sb:
                        pieces=['j','d'] if species=='P' else ['d','j']
                    for k,piece in enumerate(pieces):
                        refined.append(vals[piece]);newangles.append(angles[idx] if k==0 else 180)
                corners=[]
                for i,ang in enumerate(newangles):
                    corners.append((ang,)+tuple(sorted((refined[i-1],refined[i]))))
                out.append((species,sa,sb,cut,corners))
    return out


def eulerian(edges):
    degree=Counter();adj={}
    for x,y in edges:
        degree[x]+=1;degree[y]+=1
        adj.setdefault(x,set()).add(y);adj.setdefault(y,set()).add(x)
    if any(v%2 for v in degree.values()):return False
    seen=set();todo=[next(iter(degree))]
    while todo:
        x=todo.pop()
        if x in seen:continue
        seen.add(x);todo.extend(adj[x]-seen)
    return seen==set(degree)


def fraction(expr,model):
    val=model.eval(expr,model_completion=True)
    return str(Fraction(val.numerator_as_long(),val.denominator_as_long()))


def check(kind, output_dir=None):
    vs=variants(kind);kinds=sorted(set(c for row in vs for c in row[-1]))
    ids={c:i for i,c in enumerate(kinds)}
    type_vectors=[Counter(ids[c] for c in row[-1]) for row in vs]
    stars=[]
    for count in (3,4):
        for star in combinations_with_replacement(range(len(kinds)),count):
            cs=[kinds[i] for i in star]
            if sum(c[0] for c in cs)==360 and eulerian([c[1:] for c in cs]):stars.append(star)
    freqs=[z3.Real('f_'+str(i)) for i in range(len(vs))]
    xs=[z3.Real('x_'+str(i)) for i in range(len(stars))]
    solver=z3.Solver();solver.add(*(v>=0 for v in freqs+xs),sum(freqs)==1)
    for i in range(len(kinds)):
        solver.add(sum(star.count(i)*x for star,x in zip(stars,xs)) == sum(row[i]*f for row,f in zip(type_vectors,freqs)))
    result=solver.check()
    record={'kind':kind,'variants':[(s,sa,sb,cut) for s,sa,sb,cut,_ in vs],
            'corner_kinds':[(ang,[str(z) for z in u.list()],[str(z) for z in v.list()]) for ang,u,v in kinds],
            'type_counts':[{str(k):v for k,v in t.items()} for t in type_vectors],
            'stars':stars,'result':str(result)}
    if result==z3.unsat:
        weights=[z3.Real('w_'+str(i)) for i in range(len(kinds))]
        dual=z3.Solver();dual.add(*(sum(weights[i] for i in star)>=0 for star in stars),
                                *(sum(weights[i]*count for i,count in row.items())<=-1 for row in type_vectors))
        assert dual.check()==z3.sat
        record['dual']=[fraction(expr,dual.model()) for expr in weights]
    elif result==z3.sat:
        model=solver.model();record['type_frequencies']=[fraction(v,model) for v in freqs]
        record['star_frequencies']=[fraction(v,model) for v in xs]
    else:raise RuntimeError(result)
    if output_dir is not None:
        path=Path(output_dir)/('partial-contact-cairo-alternate-'+kind+'-marginals.json')
        path.write_text(json.dumps(record,indent=2)+'\n')
    print(kind,result,'variants',len(vs),'corner kinds',len(kinds),'stars',len(stars))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output-dir')
    args=parser.parse_args()
    for kind in RATIOS:check(kind,args.output_dir)
