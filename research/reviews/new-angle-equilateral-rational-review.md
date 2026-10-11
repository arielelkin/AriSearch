# Independent hostile review: equilateral rational-angle obstruction

**Date:** 2026-10-09. **Verdict:** **valid for the stated restricted family**.
The reviewer did not develop the lemma or its verifier. No proof repair
was made by this reviewer.

## Exact claim reviewed

[The lemma](../lemmas/new-angle-equilateral-rational-obstruction.md) claims:
a pair of genuine convex equilateral polygons with rational interior
angles, one a pentagon and the other a pentagon or hexagon, either cannot
tile the plane or admits a doubly periodic plane tiling. The two side
scales may differ, reflections are permitted, and no edge-to-edge
restriction is imposed. The conclusion does not cover arbitrary convex
pairs.

## Imported arithmetic audited

I independently opened the primary Lam–Leung preprint
[On vanishing sums of roots of unity](https://arxiv.org/pdf/math/9511209),
and checked Theorem 3.3/Corollary 3.4, Lower Bound Theorem 4.8, and
Uniqueness Theorem 6.5, together with formula (6.1).
The positive coefficient and minimal-sum hypotheses are appropriate:
normalizing an equilateral polygon's side length produces five or six
unit complex roots whose sum vanishes. No signed coefficient
classification is substituted.

The bound is
\(p_1(p_2-1)+p_3-p_2=(p_1-1)(p_2-1)+(p_3-1)\).
It is at least six, with equality only at \((2,3,5)\).
For an asymmetric minimal sum of weight six the uniqueness theorem
applies even when the ambient order has extra prime factors or powers;
rotation removes that dependence. Its exceptional support is the two
primitive sixth roots plus the four nonidentity fifth roots.
A minimal sum of smaller weight is a complete prime orbit.
Decomposing a positive sum into minimal subsums gives exactly 5,
3+2 for weight five and 2+2+2,3+3, or exceptional 6 for weight six.
No weight-one component is possible. The arithmetic classification is
unbounded in root order and is not inferred from the finite verifier.

## Cyclic order and geometry attacks

A closed convex polygon traversed in one orientation has strictly
monotone edge directions modulo one full turn; a repeated direction
would require either a redundant collinear vertex or completing the
full turn before traversal ends. The genuine-side hypothesis excludes
both. Therefore sorting the root multiset cyclically recovers its only
convex edge order up to starting vertex and orientation. Arbitrary
permutations of a vanishing sum cannot generate omitted convex shapes.

For the nonregular pentagon, the antipodal pair's direction is defined
modulo 180 degrees and the triangle orbit is defined modulo 120 degrees.
These normalize their relative angle modulo 60 degrees. Endpoint
parameters 0 and 60 produce a repeated direction, hence no genuine
pentagon. At 0<theta<60 the specified cyclic order is forced.
The angles at the endpoints of the 120-degree edge are indeed
60+theta and 120-theta; their sum is 180 degrees.

I attacked the gluing step by checking whether distant portions could
overlap or whether the fused polygon could still be concave. A chosen
edge is a supporting segment of a convex polygon. The midpoint half-turn
puts the other copy in the opposite closed half-plane, and their
intersection is exactly that supporting edge. Thus the union is a
simple polygon. The seam endpoints become straight and all other
corners stay convex. It has six genuine corners and central symmetry.
This is an allowed rotation, so reflection permission causes no gap.

## Translation tiling of the fused hexagon

For cyclic sides a,b,c,-a,-b,-c, set u=a+b,v=b+c and
\(D=\det(u,v)=\det(a,b)+\det(a,c)+\det(b,c)>0\).
Directly solving for a in that basis gives

\[
\alpha=\frac{\det(a,b)+\det(a,c)}D,\qquad
\beta=-\frac{\det(a,b)}D,
\]

hence \(0<-\beta<\alpha<1\). This validates the claimed six-vertex
coordinate form and excludes a degenerate lattice.
The portions outside the unit square are precisely the stated bottom
and left triangles, with disjoint interiors. Translating them up/right
produces the top/right triangles whose common boundary joins
\((\alpha,1+\beta)\) to \((1,1)\). Together with the remaining
quadrilateral they partition the square. Thus this is an actual lattice
fundamental domain, not a patch or merely an equal-area argument.
The two-pentagon subdivision then repeats periodically at every scale.
The same lattice argument covers three antipodal pairs in a hexagon.

## Unrestricted contacts and angle exclusions

For a finite family of compact convex tiles, local finiteness follows
from positive minimum inradius and bounded maximum diameter: tile
centers whose tiles touch a fixed bounded set lie in a larger bounded
set and have disjoint fixed-radius interior disks. Around a genuine
corner, at most one incident tile can contribute a straight sector;
two straight sectors leave no room for that corner. Consequently the
180/360 angular dichotomy applies to arbitrary partial-edge contacts,
reflections, and both scales. It does not quietly assume a common
edge-length scale.

For the two-triangle-orbit hexagon I checked all three parameter ranges:

- Below 30 degrees, an L-corner cannot be completed to 180 degrees.
  A 360 star has either one L and 0–3 S sectors, or two L and no S;
  the displayed affine equations have no permissible parameter.
- At 30 degrees, reducing \(150n+90m+108k=360\) modulo 18 excludes
  n=1,2; adding another sector to a 150 corner exceeds 180.
- Above 30 and below 60 degrees, all sectors exceed 90 degrees.
  Straight-sector stars and four-corner stars are impossible; three
  sectors are necessary. With an S corner, the all-hexagon sums are
  3S,2S+L,S+2L, each meeting 360 only at theta=60. The one- or
  two-pentagon cases give theta=66,84 or constant 348. No case remains.

At theta=60 the hexagon is regular and already provides a periodic
monohedral tiling. This does not require the pentagon to appear.
The exceptional root support gives corner angles 60,168,108,108,108,168.
A 168 corner cannot occur in a half-plane star. A full star with one
such corner requires \(9k+5m=16\), which has no nonnegative solution;
with two, the remaining 24 degrees is smaller than every sector.
A pair using only regular pentagons has no corner sum of 180 or 360,
regardless of their scale ratio.

## Computational check and its finite scope

I replayed

    conda run --no-capture-output -n arisearch python3 research/searches/new-angle-equilateral-rational-verify.py

It passed. I independently checked that every stated finite count domain
overincludes all relevant angle-sector counts, the exceptional polynomial
uses exponents 5,6,12,18,24,25 in order 30, and its divisor is Phi_30.
Its exact arithmetic certifies those finite identities and inequalities;
the all-orders classification and lattice construction were checked
separately above. No finite patch-to-plane or bounded-search inference
is used.

## Defects, repairs, and uncertainty

No mathematical defect was found in the stated restricted theorem.
No repair is requested. The optional wording that a generic centrally
symmetric hexagon has arbitrary positive opposite side lengths must be
read as allowing different lengths among opposite pairs, with equality
within each pair; the preceding side-vector statement already makes
that precise.
The imported Lam–Leung theorems remain external dependencies, and the
review is a mathematical audit rather than machine formalization.
No claim about irrational angles, unequal side lengths within a tile,
a partner with seven or more sides, or unrestricted-pair impossibility
follows. Priority of this restricted result was not independently
established by this review.
