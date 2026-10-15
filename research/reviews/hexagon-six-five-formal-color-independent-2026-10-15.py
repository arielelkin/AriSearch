#!/usr/bin/env python3
"""Independent color-index checks for the noninjective length transfer.
No author import and no numerical metric distinction. Full word domains
are checked by the four pre-existing independent finite verifiers.
"""
from collections import Counter
A=tuple(range(6))
CASES=[
 ((0,2,4,6,5,6),((0,1,6),(2,3,7),(4,8,10),(5,9,11))),
 ((0,1,5,1,4,2),((0,1,11),(2,3,10),(4,7,9),(5,6,8))),
 ((0,2,6,5,3,6),((0,1,6),(2,7,10),(3,4,9),(5,8,11))),
 ((0,1,3,5,1,2),((0,1,11),(2,7,10),(3,4,8),(5,6,9))),
]
def color_preserving_dihedral(word):
 return [(sign,shift) for sign in (-1,1) for shift in range(6)
         if all(word[i]==word[(sign*i+shift)%6] for i in range(6))]
assert color_preserving_dihedral(A)==[(1,0)]
for separation in (1,2,3):
 w=[None]*6;w[0]=w[separation]=0;unused=iter(range(1,5))
 for i in range(6):
  if w[i] is None:w[i]=next(unused)
 assert color_preserving_dihedral(w)==[(1,0)]

maps=0
for B,support in CASES:
 words=(A,B)
 assert Counter(c for st in support for c in st)==Counter(range(12))
 at={c:st for st in support for c in st}
 edgepairs={c:{words[c//6][c%6],words[c//6][(c+1)%6]} for c in range(12)}
 assert all(len(p)==2 for p in edgepairs.values())
 # Deliberately maximally noninjective physical color-to-length function.
 ell={c:1 for w in words for c in w}
 for f,w in enumerate(words):
  for side,color in enumerate(w):
   correspondences=[]
   for i in ((side-1)%6,side):
    c=6*f+i;star=at[c]
    assert len(set().union(*(edgepairs[d] for d in star)))==3
    d,=[d for d in star if d!=c and color in edgepairs[d]]
    g,j=divmod(d,6)
    neighbor_side,=[k for k in (j,(j+1)%6) if words[g][k]==color]
    assert ell[w[side]]==ell[words[g][neighbor_side]]
    correspondences.append((d,g,neighbor_side))
   (d0,g0,s0),(d1,g1,s1)=correspondences
   assert (g0,s0)==(g1,s1)
   assert {d0,d1}=={6*g0+(s0-1)%6,6*g0+s0}
   maps+=1
assert maps==48
print('PASS: all D6 color-preserving frame ambiguities excluded; 48 full-side native endpoint maps in four partition supports, with every physical color length set equal to 1.')
