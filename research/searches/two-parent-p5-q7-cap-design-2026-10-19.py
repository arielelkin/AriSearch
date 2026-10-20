"""One fixed pair of triangulated dual caps; no topology enumeration.
Replay: mise exec -- conda run --no-capture-output -n arisearch python research/searches/two-parent-p5-q7-cap-design-2026-10-19.py
"""
import json
from collections import defaultdict
from pathlib import Path

CORE = [("a","b","e"),("b","c","e"),("c","a","e"),("b","d","c"),("d","a","c")]

def cap(m,annulus,corners,species):
    triangles=CORE+annulus
    incidences=defaultdict(list)
    neighbors=defaultdict(set)
    for i,t in enumerate(triangles):
        for j in range(3):
            x,y=t[j],t[(j+1)%3]
            edge=tuple(sorted((x,y)))
            incidences[edge].append("v"+str(i))
            neighbors[x].add(y); neighbors[y].add(x)
    seams=[]
    boundary_nodes={}
    for i in range(m):
        edge=tuple(sorted(("u"+str(i),"u"+str((i+1)%m))))
        boundary_nodes[edge]="s"+str(i)
    for edge,ends in sorted(incidences.items()):
        if edge in boundary_nodes:
            assert len(ends)==1
            ends=ends+[boundary_nodes[edge]]
        else:
            assert len(ends)==2
        seams.append({"children":list(edge),"ends":ends})
    boundary=[]
    counts={x:len(n) for x,n in neighbors.items()}
    for i,k in enumerate(corners):
        child="u"+str(i)
        # u_i runs from s_(i-1) to s_i; parent corners subdivide this arc.
        word=["s"+str((i-1)%m)]+["p"+str(sum(corners[:i])+j) for j in range(k)]+["s"+str(i)]
        boundary.append({"child":child,"word":word})
        counts[child]+=1+k
    failures={x:{"native_sides":n,"required":5 if species[x]=="P" else 7} for x,n in counts.items() if n!=(5 if species[x]=="P" else 7)}
    return {"triangles":triangles,"boundary":boundary,"seams":seams,"species":species,"native_sides":counts,"failures":failures}

P=cap(4,[("a","b","u1"),("b","u2","u1"),("b","d","u2"),("d","u3","u2"),("d","u0","u3"),("d","a","u0"),("a","u1","u0")],[0,2,2,1],dict.fromkeys("abcde","P")|{"u0":"P","u1":"Q","u2":"Q","u3":"P"})
Q=cap(3,[("a","b","u1"),("b","u2","u1"),("b","d","u2"),("d","u0","u2"),("d","a","u0"),("a","u1","u0")],[3,2,2],dict.fromkeys("abcde","P")|dict.fromkeys(["u0","u1","u2"],"Q"))
assert len(P["triangles"])==12 and len(P["seams"])==20
assert len(Q["triangles"])==11 and len(Q["seams"])==18
assert P["native_sides"]=={"a":6,"b":6,"e":3,"c":4,"d":6,"u1":7,"u2":7,"u3":5,"u0":5}
assert Q["native_sides"]=={"a":6,"b":6,"e":3,"c":4,"d":5,"u1":7,"u2":7,"u0":8}
# Boundary-angle sum elimination, in units pi:
# P: 2I+p-2+B=31 versus target sum(n_i-2)=31.
# Q: 2I+p-2+B=30 versus target sum(n_i-2)=30.
assert 2*12+5-2+4==7*3+2*5
assert 2*11+7-2+3==5*3+3*5
# General saturated cap obstruction at the same fixed sizes.
assert 5*5-(20-4)==9  # P induced interior edges at least 9.
assert 5*5-(18-3)==10>3*5-6  # Q exceeds planarity.
result={"status":"rejected at native-side incidence gate","P":P,"Q":Q}
Path(__file__).with_suffix(".json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps({"P_failures":P["failures"],"Q_failures":Q["failures"],"scope":"one fixed cap pair, plus analytic saturated-cap obstruction"},sort_keys=True))
