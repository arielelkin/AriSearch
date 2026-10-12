#!/usr/bin/env python3
"""Local full native B-ring seam closures with interleaved A angles.

Exactly enumerates the Cartesian product of compatible native A placements
for each of twelve native B placements. No global adjacency, solver, or
bounded periodic absence is used. Rejecting closure means it forces period
two A lengths, incompatible with polygon closure away from p=120 degrees.
"""
import itertools
import json
import sys
from collections import Counter

WORDS={'C':(0,0,0,1,1,1),'I':(0,0,1,0,1,1),'ALT':(0,1,0,1,0,1)}
P=[(r,s) for s in (1,-1) for r in range(6)]

def corner(sym,k):
    r,s=P[sym]
    return (r+s*k)%6

def side(sym,k):
    r,s=P[sym]
    return (r+k if s==1 else r-k-1)%6

def closure(bs,aa):
    par=list(range(12))
    def find(i):
        while par[i]!=i:i=par[i]
        return i
    def union(i,j):par[find(j)]=find(i)
    for k in range(6):
        union(6+side(bs,k),side(aa[(k+1)%6],(k+3)%6))
        union(side(aa[k],(k+1)%6),side(aa[(k+1)%6],(k+4)%6))
    names={};answer=[]
    for i in range(12):
        f=find(i)
        if f not in names:names[f]=len(names)
        answer.append(names[f])
    return tuple(answer)

def main(path):
    rows=[]
    for b,bword in WORDS.items():
        counts=Counter(); representatives={};total=0;killed=0
        for bs in range(12):
            w=[bword[corner(bs,k)] for k in range(6)]
            choices=[[a for a in range(12)
                      if WORDS['I'][corner(a,k+2)]==w[k]
                      and WORDS['I'][corner(a,k+3)]==w[(k-1)%6]]
                     for k in range(6)]
            for aa in itertools.product(*choices):
                eq=closure(bs,aa);total+=1;counts[eq]+=1
                representatives.setdefault(eq,{'B_placement':bs,'A_ring':aa})
                bad=eq[0]==eq[2]==eq[4] and eq[1]==eq[3]==eq[5]
                killed+=bad
        classes=[{'closure':eq,'count':counts[eq],
                  'forces_A_side_period_two':eq[0]==eq[2]==eq[4] and eq[1]==eq[3]==eq[5],
                  'representative':representatives[eq]} for eq in sorted(counts)]
        rows.append({'A':'I','B':b,'native_ring_count':total,'period_two_rejections':killed,
                     'remaining_count':total-killed,'distinct_closures':classes})
        print('I',b,'native rings',total,'period-two killed',killed,'remaining',total-killed,
              'closures',len(counts),flush=True)
    result={'scope':'local B plus its six A neighbours; all 12 native B placements, all compatible native A placements; twelve whole seam equalities',
            'words':WORDS,'placements':P,'rows':rows}
    with open(path,'w') as f:json.dump(result,f,indent=2)

if __name__=='__main__':main(sys.argv[1])
