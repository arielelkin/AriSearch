# Fresh hostile review: two-angle pentagon pair Cairo reduction

**Reviewed source:** `research/lemmas/two-angle-pentagon-pair-cairo-reduction.md`.

**Reviewer:** construction_angles, independently of root's derivation.
The reviewer did not develop this family and did not repair the source.

**Verdict:** valid as the stated necessary-condition theorem, with no
unresolved mathematical defect found. Every aperiodic pair of genuine convex
pentagons whose combined angle set has at most two values must have both
angle words `(90,120,90,120,120)` up to cyclic rotation and reflection.
This does not prove closure for arbitrary lengths, mixed tiling existence,
or aperiodicity of any surviving metric pair.

## Exact audited scope and dependencies

The theorem permits arbitrary isometries, arbitrary side lengths, partial
contacts, and omission of either member. Neither all-obtuse angles nor
edge-to-edge contact is assumed in the k=1,2,3 arguments. The k=4 branch
uses the separately reviewed all-obtuse forcing theorem. I read that proof
and the square-window boundary estimates, and independently derived the
needed trivalent pentagon curvature identity below. The lattice construction
uses the stated elementary centrally symmetric hexagon lemma, which explicitly
permits arbitrary side lengths. No monohedral pentagon completeness theorem,
monohedral hexagon classification, angle rationality restriction, or bounded
valence search is imported.

## Full and half sectors include the contact loopholes

At a native corner point, no other tile can contain the point in its interior:
that would overlap the positive native corner sector. Each incident convex
tile consequently contributes either a native corner sector, of angle
strictly between 0 and pi, or a straight sector of angle pi. Local finiteness
holds by the fixed positive area and maximum diameter. The sectors cover a
small punctured disk with disjoint interiors. Two straight sectors leave no
room for the native corner, so there are either zero or one straight sectors.
The sum of genuine corner angles is respectively 2pi or pi. This includes
vertex-to-side contacts and high-valence stars.

After establishing two angle values alpha<beta, both polygons necessarily
have the same alpha multiplicity k. Their equal angle sum gives
`(k_P-k_Q)(alpha-beta)=0`. Thus a rare or omitted type cannot evade an
incidence contradiction: each present pentagon contributes k alpha corners
and 5-k beta corners. The average angle 108 implies beta>108. Therefore every
full star has q <=3 beta sectors and every half star has q <=1. Alpha-only
stars may have higher valence and are not omitted; they satisfy all count
inequalities used in k=1 and k=2 automatically.

For the selected square-window tile count N, all native corners of tiles
away from its fixed-width boundary strip lie inside the window. Every tile
contributing an error meets that strip, and there are only O(R) such tiles.
Hence counts by native corner position satisfy
`C_alpha=kN+O(R)` and `C_beta=(5-k)N+O(R)`, with N=Theta(R^2).
Summing a pointwise corner inequality over complete stars therefore gives
the claimed inequalities with O(R) error. Although the constant can depend
on the positive angle alpha, there is no requirement that it be uniform over
all hypothetical angle data. This addresses arbitrarily small alpha and
correspondingly large finite valence.

## Independent audit of all multiplicities

Write x=alpha/pi. The source handles the one-value case correctly: the sole
angle is3pi/5, and neither pi nor 2pi is a positive integer multiple of it.
If k=0 or5 then both polygons reduce to this one-value case.

For k=1, beta/pi=(3-x)/4 with0<x<3/5. A full star with q=3 and p>=1 has
angle at least3beta+alpha=(9+x)pi/4>2pi. Withp=0 it requires beta=2pi/3,
x=1/3. Away from x=1/3 there are no q=3 stars. For full q=2,
`p=(1+x)/(2x)>1`, so integral p >= 2. For full or half q=1, p is positive and
therefore at least 1. Thus every star obeysp>=q, and summation requires
`N>=4N+O(R)`, impossible. At x=1/3 the unique 60 corner is adjacent to a 120
corner, providing the exact 180 endpoint sum used by the periodic construction.

For k=2, beta/pi=1-2x/3 with0<x<3/5. Fullq=3 requires
`(2-p)x=1`, whose only allowed integer solution is p=0, x=1/2.
Fullq=2 requiresp=4/3 and is impossible. Fullq=1 requires
`x=1/(p-2/3)`; its interval forces integer p >= 3. Half q=1 again requires
p=2/3. Therefore, away from x=1/2, every star obeysp>=3q, including alpha-only
stars. The global inequality is `2N>=9N+O(R)`, impossible. At x=1/2 the
angles are90 and120, with two90 corners. If either member has adjacent90
corners, their sum180 supplies a periodic monohedral escape. Two nonadjacent
marked positions on a five-cycle have one dihedral orbit, giving the stated
Cairo word.

For k=3, convexity and order give1/3<x<3/5 and beta/pi=3(1-x)/2.
I independently derived all four equations, retaining every integer p >= 0:

| star kind | equation | complete allowed result |
| --- | --- | --- |
| full,q=1 | x=1/(2p-3) | none |
| full,q=2 | x=1/(3-p) | p=1,x=1/2 |
| full,q=3 | x=5/(9-2p) | p=0,x=5/9 |
| half,q=1 | x=1/(3-2p) | none |

There is no hidden finite p cutoff. For full q=1, positivity forces p >= 2;
p=2 givesx=1, p=3 gives the excluded endpoint1/3, and p>=4 givesx<=1/5.
For full q=2, positive denominators allow p=0,1,2; their values are 1/3,1/2,1.
For full q=3, p=0 gives 5/9; every positive denominator with p>=1 gives at least
5/7>3/5, and nonpositive denominators give no positive x. For half q=1,
p=0 gives the excluded endpoint1/3, p=1 gives 1, and p>=2 gives negative x.
These are exhaustive integer arguments.

If neitherx=1/2 nor5/9 holds, a native beta corner has no legal full or half
star. At x=5/9, beta=2pi/3 and all beta stars contain only three beta sectors.
No mixed star is possible, while an alpha-only full or half star would require
p=18/5 or9/5 respectively. Thus alpha corners cannot occur either.
At x=1/2, beta=3pi/4 and each pentagon has three right corners. An independent
set in the five-cycle has size at most 2, so two right corners are adjacent.
Again each member supplies the periodic escape. This rules out all k=3
aperiodic cases, without imposing edge-to-edge contact.

For k=4, beta/pi=3-4x, convexity givesx>1/2 and ordering givesx<3/5.
Every angle is strictly obtuse. The reviewed forcing proof excludes all
half stars, all native side subdivisions, and all full valences other than 3.
For completeness I checked the square-window contradiction directly.
For the selected planar patch, write B for boundary edges, V_b for boundary
vertices, q for their degree sum, and H for holes. Full edge contacts and
five native sides per face give `2E=5N+B`. Trivalence at nonboundary vertices
gives `2E=3(V-V_b)+q`. Euler gives `V-E+N=1-H`. Substitution yields

    N = B + 6 - 6H - 6V_b + 2q.

The established boundary strip estimates make B,V_b,H,q all O(R), hence
N=O(R), contradicting quadratic tile count. This uses no rank-two periodicity
assumption and does not apply merely the general side-count inequality
(which alone would not exclude pentagons).

## Global half-turn construction and arbitrary lengths

Let a genuine convex pentagon have consecutive interior angles adding to pi.
They are exactly the endpoints of a native side. Its half-turn about that
side's midpoint shares the full side, with interior in the opposite open
half-plane. The union is a simple polygon; no overlap or additional contact
between the two interiors is possible. At each seam endpoint, one of the
endpoint angles from each copy occurs, so their sum is pi and the boundary
is straight. The other six corners retain their original angles strictly
between 0 and pi. The union is consequently a genuine convex six-sided
polygon, centrally symmetric under the gluing half-turn. The boundary
segments formed by merging two collinear native edges have positive lengths.
No equality of distinct original side lengths was used.

The previously reviewed central-hexagon cut-and-translate proof accepts
arbitrary opposite side lengths and gives a rank-two lattice tiling. Keep
both original pentagons inside each translated hexagon. That yields a
monohedral tiling by the original pentagon, invariant under that same
lattice. Because an admitted pair tiling may omit the other prototile,
this refutes aperiodicity of the pair. The argument is valid even when the
original shape itself has no symmetry.

## Defects, repair authorship, and remaining uncertainty

No mathematical defect requiring a repair was found, and the source was
not modified by this reviewer. The k=3 equations, high-valence range, half
stars, rare/omitted type counts, k=4 curvature step, and unrestricted-length
periodic construction all passed the hostile audit.

The remaining uncertainty is the intended one: arbitrary metric pairs in
the surviving Cairo-angle family are not classified. The final paragraph's
Q(sqrt3)-linear metric lead does not enter the theorem or justify restricting
the general problem to field-valued side lengths. More than two combined
angle values are outside this reduction. No claim of tiling existence or
aperiodicity in those surviving families is certified by this review.
