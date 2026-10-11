"""Exact necessary endpoint-colored augmented-corner balance at all three f resonances.
Optional native a,b T locations come from the two-T switch; c,d stay whole.
A ray symbol includes the number of beta endpoints on its entire shared piece.
A120 corner cannot match90 or180, so this is necessary endpoint information.
An UNSAT system carries a rational dual; a SAT answer is only local evidence.
"""
import argparse
from collections import Counter
from itertools import product, combinations_with_replacement, permutations
import json
from pathlib import Path
from fractions import Fraction
import z3
from sage.all import QuadraticField, AA
K=QuadraticField(3,'w',embedding=AA(3).sqrt());w=K.gen()
RATIOS={'f2c':(28*w+13)/37,'fac':w,'f2a':(20*w-11)/13,
        'e2c':1+w,'eac':1+4*w/3,'e2a':1+2*w}


def variants(kind):
    a=K(1);b=RATIOS[kind];c=((3+w)+(1-w)*b)/4;d=((3-w)+(1+w)*b)/4
    e=(w-1)*(1+b)/2;f=((w-5)+(1+3*w)*b)/4
    vals={'a':a,'b':b,'c':c,'d':d,'e':e,'f':f,'h':a-c,'j':b-d}
    out=[]
    for species in ('P','Q'):
        for sa,sb in product((0,1),repeat=2):
            hosting = ('Q' if kind.startswith('f') else 'P')
            cuts = ([-1]+list(range(2 if kind.endswith('ac') else 1))) if species==hosting else [-1]
            for cut in cuts:
                if species=='P':
                    labels=['a','b','c','d','e'];angles=[120,90,120,90,120]
                else:
                    labels=['a','d','b','c','f'];angles=[120,90,120,90,120]
                if species==hosting and cut>=0:
                    banks={'2c':['c','c'],'2a':['a','a'],
                           'ac':(['a','c'] if cut==0 else ['c','a'])}[kind[1:]]
                    labels=labels[:4]+banks;angles=angles+[180]
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
                    prev=(refined[i-1],int(newangles[i-1]==120)+int(ang==120))
                    nxt=(refined[i],int(ang==120)+int(newangles[(i+1)%len(newangles)]==120))
                    corners.append((ang,)+tuple(sorted((prev,nxt))))
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


def locally_complete(star, kinds):
    # Any ray between two genuine right corners is a whole native arm:
    # its first120 endpoint cannot lie inside the other's native arm.
    # Therefore its far endpoint is beta, never an artificial straight cut.
    for order in set(permutations(star)):
        corners=[kinds[i] for i in order]
        for flips in product((0,1),repeat=len(order)):
            pairs=[(c[1],c[2]) if not flip else (c[2],c[1]) for c,flip in zip(corners,flips)]
            good=True
            for i in range(len(order)):
                j=(i+1)%len(order)
                if pairs[i][1]!=pairs[j][0]:good=False;break
                if corners[i][0]==corners[j][0]==90 and pairs[i][1][1]!=1:
                    good=False;break
            if good:return True
    return False


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
            if sum(c[0] for c in cs)==360 and eulerian([c[1:] for c in cs]) and locally_complete(star,kinds):stars.append(star)
    freqs=[z3.Real('f_'+str(i)) for i in range(len(vs))]
    xs=[z3.Real('x_'+str(i)) for i in range(len(stars))]
    solver=z3.Solver();solver.add(*(v>=0 for v in freqs+xs),sum(freqs)==1)
    for i in range(len(kinds)):
        solver.add(sum(star.count(i)*x for star,x in zip(stars,xs)) == sum(row[i]*f for row,f in zip(type_vectors,freqs)))
    result=solver.check()
    record={'kind':kind,'variants':[(s,sa,sb,cut) for s,sa,sb,cut,_ in vs],
            'corner_kinds':[(ang,([str(z) for z in u[0].list()],u[1]),([str(z) for z in v[0].list()],v[1])) for ang,u,v in kinds],
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
        path=Path(output_dir)/('partial-contact-cairo-alternate-'+kind+'-native-seam-marginals.json')
        path.write_text(json.dumps(record,indent=2)+'\n')
    print(kind,result,'variants',len(vs),'corner kinds',len(kinds),'stars',len(stars))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output-dir')
    args=parser.parse_args()
    for kind in RATIOS:check(kind,args.output_dir)
