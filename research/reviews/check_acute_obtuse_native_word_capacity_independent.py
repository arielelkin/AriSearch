#!/usr/bin/env python3
"""Independent exhaustive doubled-angle and native endpoint audit.
No producer imports, certificate input, solver, density or defect-free limit.
"""
from itertools import combinations_with_replacement
from collections import Counter

# Native A0..A4 then B0..B4 corners; angle degrees multiplied by2.
angles=(130,281,295,150,224,80,289,272,94,345)
assert sum(angles[:5])==sum(angles[5:])==1080
assert min(angles)==80

def sums(target):
    return [row for n in range(1,target//min(angles)+1)
            for row in combinations_with_replacement(range(10),n)
            if sum(angles[i] for i in row)==target]
flat=sums(360)
full=sums(720)
assert flat==[(0,3,5)]
assert full==[(0,2,2),(1,3,6),(1,8,9),(2,5,9),(4,4,7),
             (0,4,7,8),(0,0,7,8,8),(0,0,3,3,5,5),(5,)*9]

def completions(pair):
    demand=Counter(pair)
    return [row for row in full if not demand-Counter(row)]
assert not completions((1,1))    # z/z far end of A1/alpha seam
assert not completions((1,4))    # z/y far end of A1/alpha seam
assert not completions((2,7))    # x/u far end of A2/B1 seam
assert completions((0,2))==[(0,2,2)]
nonflat=set(range(10))-{j for row in flat for j in row}
assert {1,2,6,7,9}<=nonflat
# All20 possible native partner endpoint orders, retaining forbidden-star
# candidates at this initial gate; every z/x sum with a partner exceeds180.
partners=[]
for species in range(2):
    for side in range(5):
        endpoints=(5*species+side,5*species+(side+1)%5)
        for order in (endpoints,endpoints[::-1]):
            assert angles[1]+angles[order[0]]>360
            assert angles[2]+angles[order[1]]>360
            if completions((1,order[0])) and completions((2,order[1])):
                partners.append((species,side,order))
assert partners==[(0,2,(3,2)),(1,0,(6,5)),(1,3,(8,9)),(1,4,(9,5))]
# Removing Ax² leaves unique x and delta support; w belongs exactly P/Q.
remaining=[r for r in full if r!=(0,2,2)]
assert [r for r in remaining if 2 in r]==[(2,5,9)]
assert [r for r in remaining if 6 in r]==[(1,3,6)]
assert [r for r in remaining if 9 in r]==[(1,8,9),(2,5,9)]
assert all(r.count(5)==1 for r in remaining if 2 in r)
assert all(r.count(3)==1 for r in remaining if 6 in r)
assert flat[0].count(0)==flat[0].count(3)==flat[0].count(5)==1
print('PASS:1flat/9full stars; all20 A1 endpoint orders; exactly4 partners; all far-star and resource-support claims')
