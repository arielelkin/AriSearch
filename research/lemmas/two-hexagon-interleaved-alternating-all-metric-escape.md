# Every interleaved/alternating metric pair is untileable or periodic

Date: 2026-10-12. Status: fresh independent finite reviews VALID for the
[complete metric-word census](../reviews/two-hexagon-interleaved-alternating-private-transport-review.md)
and the [equal-odd torus](../reviews/two-hexagon-interleaved-alternating-equal-odd-torus-review.md). The analytic private-seam domain is independently reviewed VALID.

For fixed strictly convex hexagons A,B with native angles

    A=(p,p,q,p,q,q), B=(r,s,r,s,r,s),
    q=240-p, r=360-2p, s=2p-120, 90<p<150, p!=120,

any admitted plane tiling implies an admitted periodic plane tiling. Reflections,
partial contacts, and omission of a type are permitted in the original problem.
This does not prove the unrestricted two-convex-polygon impossibility theorem;
it settles this angle family and native bracelet pair only.

The reviewed [private-seam lemma](two-hexagon-interleaved-alternating-private-seams.md)
applies to the admitted trivalent hexagon limit and restricts every AB seam to
odd native A sides1,3,5, every AA seam to the same even native side index,
and every B side to the odd A length alphabet. It also proves the exact native
B multiplicities. Coincidences with even A lengths do not enlarge the domain.

If A1,A3,A5 are not all equal, the
[nonconstant metric escape](two-hexagon-interleaved-alternating-nonconstant-metric-escape.md)
covers the complete necessary metric word domain:123 native words have empty
ring compatibility cores, and the twelve remaining nonconstant words have
explicit index-six metric tori. All three even A lengths remain independent in
those witnesses. Thus every tilable nonconstant odd metric has a periodic escape.

If A1=A3=A5=L, the domain lemma forces every B side to equal L. An explicit
index-nine metric torus covers every actual pair with this property. The
[producer](../searches/two-hexagon-interleaved-alternating-equal-odd-torus.py) and
[certificate](../certificates/two-hexagon-interleaved-alternating-equal-odd-torus.json)
give the full native labels and exact seams, without using a solver or the
additional equilateral-carrier geometric proof.

## The equal-odd constructive subset

For construction only, select from the216 private native rings the36 rings
whose successive A neighbours have opposite chirality. Since all AA matches
already use the same native side, opposite chirality gives reflection across
each AA seam. This restricts an allowed constructive subset; it is not claimed
that every original tiling has all seams reflected.

The36 rings have six full-native A-ring overlap signatures with six B choices
per signature. Listed lexicographically, the first orbit is

    S0=(1,7,5,9,3,11),
    S1=(3,9,1,11,5,7),
    S2=(5,11,3,7,1,9),

where placements0,...,5 are (r,+1) and6,...,11 are (r,-1). Their coarse B
successors are F0=(0 2 1), F1=(0 1 2), F2=F0, with opposite-direction inverses.
The other three signatures give a second orbit. Choose S0 at a B cell with
original x=0 modulo3 and apply F0 as x increases. B cells satisfy x-y=0 mod3.
Choose one retained B representative for each signature and put its native A
neighbours at their cell positions. Overlaps agree exactly. This gives a native
field periodic under3Z^2, HNF(3,0,3), of index9.

The certificate retains nine labels,18 canonical vertex stars,54 directed side
seams and the side-length classes

    A=(e0,L,e2,L,e4,L), B=(L,L,L,L,L,L).

The classes e0,e2,e4 are independent of each other and of L. Every AA seam uses
the same even A native side index; every AB seam is an odd A side of length L
against a B side of length L. Thus no additional equality is imposed on the
actual metric. Extra coincidences preserve all matches. Each canonical vertex
contains two A corners and one B corner of the same colour, so its angle sum is
360. Reflected side indices are checked by the endpoint-derived formula r-k-1.
The reviewed periodic-label development theorem realizes these labels as a
periodic Euclidean tiling for the actual strictly convex polygons.

The finite witness independently backs the root's
[equal-odd equilateral-carrier construction](two-hexagon-interleaved-alternating-equal-odd-carrier.md).
Neither proof needs to assume that a source tiling forces a shape hierarchy.
Together the nonconstant cases and this equal-odd witness cover every fixed
metric pair in the stated I/ALT angle family.
