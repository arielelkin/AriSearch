#!/usr/bin/env python3
"""Independent exact audit of the fixed Robinson height/wedge boundary screen.

No producer imports. Enumerate words by Cartesian symbol powers, recognize
native fans by Boolean dynamic programming, and use lifted vertex shoelaces.
Only necessary boundary conditions are checked; this is no placement search.
"""
from collections import Counter
from itertools import combinations, product
import json
from pathlib import Path

PAIRS=tuple(combinations(range(5),2))
SYMBOLS=("s","u","l")
COEFFICIENTS={"u":(1,0),"l":(0,1),"s":(-1,1)}
FAN_EDGES=(("u","u",1),("u","u",3),("u","s",2),("s","u",2),
           ("u","l",1),("l","u",1))
FIXTURES={
 "U":([(1,2),(1,2),(1,0),(1,0),(1,0)],[0,4,6,7,8],[1,3,4,4,3],(7,9)),
 "V":([(1,0),(1,3),(1,0),(0,2),(0,2)],[0,3,6,7,9],[2,2,4,3,4],(9,16)),
}


def words(a,b):
    result=[]
    for size in range(1,a+2*b+1):
        for word in product(SYMBOLS,repeat=size):
            if tuple(sum(COEFFICIENTS[x][j] for x in word) for j in (0,1))==(a,b):
                result.append(word)
    return result


def fan(start,finish,budget):
    reachable=[set() for _ in range(budget+1)]
    reachable[0].add(start)
    for used in range(budget+1):
        for a,b,w in FAN_EDGES:
            if a in reachable[used] and used+w<=budget:
                reachable[used+w].add(b)
    return finish in reachable[budget]


def basis(k):
    k%=10
    return tuple((1 if k<5 else -1) if j==k%5 else 0 for j in range(5))


def step(symbol,k):
    offsets={"u":(0,),"l":(-1,1),"s":(-2,2)}[symbol]
    return tuple(sum(basis(k+d)[j] for d in offsets) for j in range(5))


def boundary_lift(boundary,directions):
    vertices=[(0,)*5]
    for word,k in zip(boundary,directions):
        for symbol in word:
            d=step(symbol,k)
            vertices.append(tuple(x+y for x,y in zip(vertices[-1],d)))
    return vertices


def shoelace(vertices):
    return tuple(sum(a[i]*b[j]-a[j]*b[i]
                     for a,b in zip(vertices,vertices[1:])) for i,j in PAIRS)


def passes_fans(boundary,angles):
    for i,word in enumerate(boundary):
        if not all(fan(a,b,5) for a,b in zip(word,word[1:])):
            return False
        if not fan(word[-1],boundary[(i+1)%5][0],angles[i]):
            return False
    return True


def main():
    retained=json.loads((Path(__file__).parents[1]/"certificates"/
                         "pentagrid-robinson-height-boundary.json").read_text())
    assert retained["direction_pairs"]==[list(p) for p in PAIRS]
    R=(1,-1,1,-1,1)
    for k in range(10):
        assert tuple(u+s-l for u,s,l in zip(step("u",k),step("s",k),step("l",k)))==tuple((-1)**k*x for x in R)
    for name,(lengths,directions,angles,content) in FIXTURES.items():
        stages=Counter()
        histogram=Counter()
        for boundary in product(*(words(a,b) for a,b in lengths)):
            stages["all"]+=1
            vertices=boundary_lift(boundary,directions)
            ns=sum(word.count("s") for word in boundary)
            multiplier=ns-1 if name=="U" else 3-ns
            assert vertices[-1]==tuple(multiplier*x for x in R)
            if vertices[-1]!=(0,)*5:
                continue
            stages["zero_height"]+=1
            B=sum(map(len,boundary))
            assert B==(10 if name=="U" else 13)
            assert sum(w.count("u") for w in boundary)==6
            q=shoelace(vertices)
            fans=passes_fans(boundary,angles)
            nonnegative=min(q)>=0
            if fans:stages["zero_height_and_fans"]+=1
            if nonnegative:stages["zero_height_and_nonnegative_wedge"]+=1
            thin=sum(q[t] for t,(i,j) in enumerate(PAIRS) if j-i in (1,4))
            fat=sum(q)-thin
            assert (thin,fat)==content
            if not (fans and nonnegative):continue
            stages["all_necessary_conditions"]+=1
            histogram[",".join(map(str,q))]+=1
        expected=retained["fixtures"][name]
        assert dict(stages)==expected["stages"],(name,dict(stages),expected["stages"])
        assert dict(histogram)==expected["wedge_histogram"]
        witness=expected["first_witness"]
        vertices=boundary_lift(witness["side_words"],directions)
        assert vertices==[tuple(v) for v in witness["lifted_vertices"]]
        assert list(shoelace(vertices))==witness["oriented_triangle_counts"]
        assert vertices[-1]==(0,)*5
        assert min(shoelace(vertices))>=0
        assert passes_fans(witness["side_words"],angles)
        print(name,dict(stages),"distinct surviving wedge vectors",len(histogram))
    print("Independent exact fixed height/wedge boundary audit passed; no assembly claim.")


if __name__=="__main__":
    if not __debug__:raise RuntimeError("Run without optimization")
    main()
