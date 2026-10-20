#!/usr/bin/env python3
"""Independent retained-atlas support enumeration; no solver invocation."""
import hashlib,json
from pathlib import Path
root=Path(__file__).resolve().parents[2]
a=json.loads((root/"research/certificates/hexagon-five-four-forced-dimer-2026-10-19.json").read_text())
c=json.loads((root/"research/certificates/hexagon-five-four-metric-gate-2026-10-19.json").read_text())
r=next(r for r in a["rows"] if r["B"]==c["B"])
stars=[tuple(map(tuple,t)) for t in r["fixed_stars"]]
assert len(stars)==22
# Native side j joins corners j-1,j. Reflection exchanges entry and exit.
def edges(p):
    corner,sign=p; f,j=divmod(corner,6)
    e=(6*f+j,6*f+(j+1)%6)
    return e if sign==1 else e[::-1]
def other(p,side):
    f,j=divmod(side,6)
    endpoints=(6*f+(j-1)%6,side)
    return (endpoints[1] if p[0]==endpoints[0] else endpoints[0],p[1])
cover=[sum(1<<i for i,t in enumerate(stars) if any(p[0]==j for p in t)) for j in range(12)]
needs=[]
for t in stars:
    row=[]
    for j,p in enumerate(t):
        q=t[(j+1)%3]; remote=(other(q,edges(q)[0]),other(p,edges(p)[1]))
        row.append(sum(1<<i for i,u in enumerate(stars) if any((u[k],u[(k+1)%3])==remote for k in range(3))))
    needs.append(row)
# Enumerate each corona factor by matching ports directly, independent of
# the producer factor dictionary and retained endpoint_microstates.
cycles=[]
for cycle in r["boundary_coronas"]:
    groups=[]
    for j in range(10):
        left,right=map(tuple,cycle[j:j+2]); factor=j%5; eligible=0
        for i,t in enumerate(stars):
            for k,p in enumerate(t):
                prev,nxt=t[(k-1)%3],t[(k+1)%3]
                if factor and p==(factor-1,1):
                    hit=((edges(prev)[1],prev[1]),(edges(nxt)[0],nxt[1]))==(left,right)
                elif factor==0 and p==(4,1) and nxt==(5,1):
                    q=t[(k+2)%3]
                    hit=((edges(q)[1],q[1]),(edges(q)[0],q[1]))==(left,right)
                else: hit=False
                if hit: eligible|=1<<i
        groups.append(eligible)
    cycles.append(groups)
survivors=[]; counts=[0]*7; digest=hashlib.sha256()
for mask in range(1<<22):
    if any(mask&g==0 for g in cover):continue
    if any(mask>>i&1 and any(mask&g==0 for g in row) for i,row in enumerate(needs)):continue
    compatible=[j for j,groups in enumerate(cycles) if all(mask&g for g in groups)]
    if compatible:
        survivors.append(mask);digest.update(mask.to_bytes(3,"little"))
        for j in compatible:counts[j]+=1
minimal=[s for s in survivors if not any(t!=s and t&s==t for t in survivors)]
assert len(survivors)==c["support_count"]==446
assert counts==c["support_counts_by_corona"]
assert digest.hexdigest()==c["support_sha256_ascending_3byte_little"]
assert sorted(minimal)==sorted(c["minimal_supports"])
assert all(any(t&s==t for t in minimal) for s in survivors)
assert c["metric_results"]==[dict(support_mask=33416,star_indices=[3,7,9,15],result="unknown",seconds=c["metric_results"][0]["seconds"],reason="timeout")]
assert c["status"]=="blocked"
print("PASS independent native-endpoint subset predicate: 446 supports, seven minima, all corona counts and SHA256; retained first UNKNOWN only. No nonlinear query run.")
