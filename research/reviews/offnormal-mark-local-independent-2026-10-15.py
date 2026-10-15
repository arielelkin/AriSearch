"""Independent stdlib exact relaxation of every cyclic shared-tail angle case.
No producer imports. JSON stdout only; angle units are degrees.
"""
from fractions import Fraction as F
from itertools import product
import json

counts={"branches":0,"feasible_closed_relaxations":0}
minimum=None
# Reflection normalizes the 36->s->t occurrence to indices 0,1,2.
for j,d,k in product(range(1,6),(-1,1),range(1,6)):
    counts["branches"]+=1
    parent=list(range(6))
    def find(a):
        while parent[a]!=a:
            a=parent[a]
        return a
    def union(a,b):
        parent[find(a)]=find(b)
    union(1,(j+d)%6); union(2,(j+2*d)%6)
    groups={find(a) for a in range(6)}
    fixed={}
    bad=False
    for a,value in ((0,36),(j,72),(k,144)):
        a=find(a)
        if a in fixed and fixed[a]!=value:
            bad=True
        fixed[a]=F(value)
    if bad: continue
    # The remaining four vertices are >108, <180. Relax to closed bounds.
    bounds={}
    for a in range(6):
        if a not in (0,j):
            g=find(a)
            if g in fixed and not 108<=fixed[g]<=180: bad=True
            bounds[g]=(F(108),F(180))
    if bad: continue
    weight={g:sum(find(a)==g for a in range(6)) for g in groups}
    objective={g:sum(find(a)==g for a in (1,2)) for g in groups}
    unknown=[g for g in groups if g not in fixed]
    # A box intersected with one affine hyperplane has a minimizer with
    # at most one variable away from its bounds. Enumerate all such vertices.
    opt=None
    free_choices=unknown or [None]
    for free in free_choices:
        rest=[g for g in unknown if g!=free]
        for bits in product((0,1),repeat=len(rest)):
            x=dict(fixed)
            for g,b in zip(rest,bits): x[g]=bounds[g][b]
            remaining=F(720)-sum(weight[g]*v for g,v in x.items())
            if free is None:
                if remaining: continue
            else:
                x[free]=remaining/weight[free]
                if not bounds[free][0]<=x[free]<=bounds[free][1]: continue
            val=sum(objective[g]*x[g] for g in groups)
            if opt is None or val<opt: opt=val
    if opt is None: continue
    counts["feasible_closed_relaxations"]+=1
    assert opt>=288,(j,d,k,opt)
    minimum=opt if minimum is None else min(minimum,opt)
assert counts["branches"]==50
assert minimum==288
print(json.dumps({"status":"PASS","method":"exact all cyclic placements plus box/hyperplane vertices",**counts,"minimum_pair_sum":str(minimum),"minimum_tail_angle":str(minimum-180)},indent=2))
