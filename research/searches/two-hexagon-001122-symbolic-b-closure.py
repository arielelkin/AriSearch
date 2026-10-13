#!/usr/bin/env python3
"""Eleven necessary B residues for closed A001122 with paired adjacent sides.
Finite symbolic domain11 bracelets, exact Laurent polynomials. No geometric
zero-set classification or infinite covering is inferred from factorization.
"""
import argparse,json
from itertools import permutations
from pathlib import Path
import sympy as s
U,V=s.symbols('U V',nonzero=True)
W=-1/(U*V)
S=(1+U,U*V*(1+V),-V*(1+W))
def bar(p):return s.cancel(p.subs({U:1/U,V:1/V},simultaneous=True))
def cross(p,q):return s.cancel(bar(p)*q-p*bar(q))
weights=(cross(S[1],S[2]),cross(S[2],S[0]),cross(S[0],S[1]))
assert s.cancel(sum(a*b for a,b in zip(S,weights)))==0
canonical=lambda word:min(t[k:]+t[:k] for t in (word,word[::-1]) for k in range(6))
words=sorted({canonical(w) for w in permutations((0,0,1,1,2,2))})
turns=(-1/U**2,-1/V**2,-1/W**2)
palette={(0,0):0,(0,1):0,(1,1):1,(1,2):1,(2,2):2,(0,2):2}
rows=[]
for word in words:
    edge=1;R=0
    sides=[]
    for i in range(6):
        if i:edge*=turns[word[i]]
        k=palette[tuple(sorted((word[i],word[(i+1)%6])))];sides.append(k)
        R+=weights[k]*edge
    num,den=s.fraction(s.cancel(R))
    rows.append({'word':list(word),'side_classes':sides,'numerator':str(s.factor(num)),
                 'denominator':str(s.factor(den)),'identically_zero':num==0})
    print(''.join(map(str,word)),s.factor(num),flush=True)
assert [r['word'] for r in rows if r['identically_zero']]==[[0,1,2,0,1,2]]
out={'domain':'11 B bracelets; A001122 adjacent paired lengths given by exact closure kernel',
     'variables':'U=exp(iu), V=exp(iv), W=-1/(UV); 0<u,v,w<90; u+v+w=180',
     'weight_numerators':[str(s.factor(q)) for q in weights],
     'rows':rows,'status':'Exact algebraic factorization; remaining unit-domain zero-set analysis required'}
p=argparse.ArgumentParser();p.add_argument('--output',type=Path);p.add_argument('--check',type=Path);args=p.parse_args()
if args.check:assert json.loads(args.check.read_text())==out
if args.output:args.output.write_text(json.dumps(out,indent=2)+'\n')
