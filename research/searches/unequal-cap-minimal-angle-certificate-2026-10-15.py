"""Exact two-stage 478-branch H-angle obstruction and Farkas certificate verifier.
Standard library only; --output generates certificate, --verify checks it
without invoking elimination. No producer imports, metric search, randomness.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import argparse,json

def plus(a,b):return [x+y for x,y in zip(a,b)]
def times(a,k):return [k*x for x in a]
def row(const=0,terms=()):
    out=[Q(const)]+[Q(0)]*6
    for i,c in terms:out[i+1]+=Q(c)
    return out

def partitions(n):
    def visit(word):
        if len(word)==n:
            yield tuple(word);return
        for x in range(max(word)+2):yield from visit(word+[x])
    yield from visit([0])

def inputs(case):
    if case[0]=='separation':
        _,parts,sign=case
        # Required values: 144,72,a,b,c,d, with a+b=72,c+d=216.
        # Each block is represented by one H slot; remaining slots are free.
        f,g,a,b,c,d=parts
        eq=[row(-720,[(z,1) for z in range(6)]),row(-144,[(f,1)]),row(-72,[(g,1)]),row(-72,[(a,1),(b,1)]),row(-216,[(c,1),(d,1)])]
        iq=[row(0,[(z,1)]) for z in range(6)]+[row(180,[(z,-1)]) for z in range(6)]+[row(0,[(a,sign),(b,-sign)])]
    else:
        _,i,d,k=case
        eq=[row(-720,[(z,1) for z in range(6)]),row(-36,[(0,1)]),row(-72,[(i,1)]),row(0,[((i+d)%6,1),(1,-1)]),row(0,[((i+2*d)%6,1),(2,-1)]),row(-144,[(k,1)])]
        iq=[row(0,[(z,1)]) for z in range(6)]+[row(180,[(z,-1)]) for z in range(6)]+[row(-180,[(1,1),(2,1)]),row(270,[(1,-1),(2,-1)])]
    return eq,iq

def eliminate(eq,iq):
    ne,ni=len(eq),len(iq)
    augmented=[r[:]+[Q(int(i==j)) for j in range(ne)] for i,r in enumerate(eq)]
    pivots=[];r=0
    for col in range(1,7):
        pivot=next((i for i in range(r,ne) if augmented[i][col]),None)
        if pivot is None:continue
        augmented[r],augmented[pivot]=augmented[pivot],augmented[r]
        augmented[r]=times(augmented[r],1/augmented[r][col])
        for i in range(ne):
            if i!=r and augmented[i][col]:augmented[i]=plus(augmented[i],times(augmented[r],-augmented[i][col]))
        pivots.append((r,col));r+=1
    for rr in augmented:
        if not any(rr[1:7]) and rr[0]:return dict(kind='equality',equal=[str(x) for x in rr[7:]])
    inequalities=[]
    for i,original in enumerate(iq):
        rr=original[:]+[Q(int(i==j)) for j in range(ni)]+[Q(0)]*ne
        for pivot,col in pivots:
            coef=rr[col]
            if coef:
                er=augmented[pivot]
                rr[:7]=plus(rr[:7],times(er[:7],-coef))
                rr[7+ni:]=plus(rr[7+ni:],times(er[7:],-coef))
        inequalities.append(rr)
    while True:
        unique={}
        for rr in inequalities:
            if not any(rr[1:7]):
                if rr[0]<=0:return dict(kind='strict',weights=[str(x) for x in rr[7:7+ni]],equal=[str(x) for x in rr[7+ni:]])
                continue
            factor=abs(next(x for x in rr[1:7] if x))
            rr=times(rr,1/factor);key=tuple(rr[1:7])
            if key not in unique or rr[0]<unique[key][0]:unique[key]=rr
        inequalities=list(unique.values())
        if not inequalities:raise AssertionError('unexpected feasible branch')
        cols=[col for col in range(1,7) if any(rr[col] for rr in inequalities)]
        if not cols:raise AssertionError('constant handling failed')
        col=min(cols,key=lambda c:sum(rr[c]>0 for rr in inequalities)*sum(rr[c]<0 for rr in inequalities))
        pos=[rr for rr in inequalities if rr[col]>0];neg=[rr for rr in inequalities if rr[col]<0]
        zero=[rr for rr in inequalities if not rr[col]]
        inequalities=zero+[plus(times(p,-n[col]),times(n,p[col])) for p in pos for n in neg]

def verify(case,cert):
    eq,iq=inputs(case)
    E=[Q(x) for x in cert['equal']]
    assert len(E)==len(eq)
    total=[Q(0)]*7
    for a,r in zip(E,eq):total=plus(total,times(r,a))
    if cert['kind']=='equality':assert not any(total[1:]) and total[0]!=0
    else:
        assert cert['kind']=='strict'
        I=[Q(x) for x in cert['weights']]
        assert len(I)==len(iq) and all(x>=0 for x in I) and any(x>0 for x in I)
        for a,r in zip(I,iq):total=plus(total,times(r,a))
        assert not any(total[1:]) and total[0]<=0

parts=list(partitions(6))
assert len(parts)==203
cases=[('separation',p,sign) for p in parts for sign in [-1,1]]+[('pair',i,d,k) for i,d,k in product(range(6),[-1,1],range(6))]
assert len(cases)==478
parser=argparse.ArgumentParser();parser.add_argument('--output');parser.add_argument('--verify');args=parser.parse_args()
if args.verify:
    records=json.loads(Path(args.verify).read_text())['records']
    assert [r['case'] for r in records]==json.loads(json.dumps(cases))
    for r in records:verify(tuple(r['case']),r['certificate'])
else:
    records=[]
    for case in cases:
        cert=eliminate(*inputs(case));verify(case,cert)
        records.append(dict(case=case,certificate=cert))
    if args.output:Path(args.output).write_text(json.dumps(dict(domain='406 required-angle partition/separation branches plus72 D6/144-slot pair branches',records=records),indent=2)+'\n')
print(json.dumps(dict(status='PASS',branches=478,source_angle_separation_branches=406,dihedral_pair_branches=72,certificate='exact weighted-row contradiction for every branch',mode='verify' if args.verify else 'generate'),sort_keys=True))
