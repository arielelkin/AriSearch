# Opposite-angle A: remove isolated ABB resonance by a corner potential

Date: 2026-10-13. Status: independently adversarially reviewed VALID;
[fresh review](../reviews/two-hexagon-opposite-a-resonance-removal-fresh-hostile-review.md).

## Statement

Let actual strictly convex hexagons A,B have angle multisets
A=2x+2y+2z and B=2(360-2x)+2(360-2y)+2(360-2z), where
90<x,y,z<180 and x+y+z=360 degrees. A has native word012012; B has any
native word. Suppose x,y,z are pairwise distinct and none equals120.
There is no side-length restriction. If the pair admits any plane tiling,
it admits a periodic tiling, allowing reflections, partial original contacts,
and omission of either type.

This extends the [exact-star arbitrary-metric theorem](terra-ternary-opposite-a-all-metric-escape.md)
across six nongeneric resonance lines. Equal-angle loci and the three loci
where an A angle is120, including their all120 intersection, remain outside
this theorem. The earlier complementary-angle theorem excludes its p=120
parameter and is not used to classify this intersection.

## Complete finite angle stratification

Use deviations A=(u,v,-u-v) from120, and B=-2A. A triple sums360 exactly
when its deviation sum is zero. All56 unordered triples among the six types
are exhausted by the [ledger](../searches/two-hexagon-ternary-resonance-ledger.py)
and [certificate](../certificates/two-hexagon-ternary-resonance-ledger.json).
Five triples are identically allowed: Ai Ai Bi for i=0,1,2, A0 A1 A2,
and B0 B1 B2. Every other triple vanishes on one of twelve distinct lines
through(u,v)=(0,0):

- three equal-angle lines Ai=Aj;
- three lines Ai=120;
- six ordered lines Ai=4Aj-360, i different from j.

The ledger uses primitive integral line normals, so proportional equations
and substitution of x+y+z=360 are included in the equality check. Every
nonzero point lies on at most one of these lines. On each ordered line the
ONLY additional type triple is Ai Bj Bj. In the open angle region its
parameter is112.5<Aj<126. At Aj=120 all angles are120; elsewhere all three
A angles and all six A/B angle values are distinct. The remaining hypothesis
in the statement therefore leaves either the original five-star language
or exactly that language plus one ABB type.

The finite classification is an exact angle statement; it does not assert
that arbitrary joint side metrics realize polygons or tilings. Domain:
56 type triples, no solver, seed or timeout; deterministic integer arithmetic.
The certificate retains all51 nonidentity triples and their line classes.

## Sparse extra-star lemma

First apply the reviewed [hexagon defect-free-limit theorem](hexagon-limit-and-periodicity.md)
to an original admitted tiling. This supplies an admitted trivalent
edge-to-edge field T, possibly omitting a species. The argument below is
applied to T: original higher-valence or partial-contact stars are not assigned
nonnegative weights by assumption.

On an ordered resonance line Ai=4Aj-360 choose p_i=1,p_j=-1 and p_k=0 for
the remaining colour. Assign corner weights p_l to A_l and -2p_l to B_l.
The sum of corner weights on EACH complete tile is zero, because each colour
occurs twice and sum p=0. Every original identity star has weight zero;
the additional Ai Bj Bj star has weight p_i-4p_j=5. These are all possible
stars in T. Hence all star weights are nonnegative.

Select all tiles whose centres lie in a translated square Q_R. Sum their
corner weights; the sum is exactly zero. Vertices for which every incident
tile is selected contribute their full star weight. Vertices with some but
not all incident tiles selected lie within a fixed-width strip about the
square boundary. The diameter bound and positive minimum tile area bound
the number of these tiles and corners by C R, uniformly in square position.
Their partial weight has absolute value at most C' R. Thus the number of
additional stars with all incident tiles selected is at most C' R/5.
All stars inside Q_(R-D), where D bounds tile diameters, are of this kind.
Consequently the additional stars have a uniform O(R) bound in every square.
No invariant mean, positive frequency or existence of a periodic tiling is
used in this argument.

For any fixed L, a separated grid in Q_R supplies order R^2/(L+D)^2
candidate centres. One extra star lies in only a bounded number of their
radius L+D disks. Choosing R large compared to L^2 therefore produces a
disk of radius L+D containing no additional star. Translate such disks to
the origin, let L grow, and extract a convergent admitted tiling by compactness
for finitely many fixed polygon shapes. T was already defect-free, so the
uniform sector-disk vertex separation from the reviewed limit proof preserves
its whole-side contacts and trivalent vertices. A forbidden additional star
cannot appear in the limit: its incident corners and full matching sides
would persist in the approximants. The new limit has only the original five
type stars. A species may disappear, which is allowed and supplies a
monohedral escape.

## Periodic escape and scope

If the new limit is pure, the named unrestricted monohedral convex-hexagon
classification gives an admitted periodic tiling. If mixed, apply the
[arbitrary-metric exact-star theorem](terra-ternary-opposite-a-all-metric-escape.md):
a legal AAA star forces A centrally symmetric; absent AAA the native B-ring
colour contradiction excludes the mixed field. Either outcome gives an
admitted periodic escape. This proves the statement.

This is a coverage theorem for native A012012 on the distinct, non120 angle
stratum, including its six extra-ABB lines. It does not classify other native
A words or eliminate extra stars on equal-angle/120 lines. It says there
exists a periodic admitted tiling, not that every admitted tiling is periodic.

Replay without writing retained evidence:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/two-hexagon-ternary-resonance-ledger.py --check research/certificates/two-hexagon-ternary-resonance-ledger.json

Fresh hostile review is complete. Next obligations: examine the residual120/equal-angle
star languages or a different native word using a new geometric invariant.

## Exact limitation of this angle-type corner-potential mechanism

For an angle-type-constant potential that has zero score on all five base stars, write its three
A weights as p_i. The mixed identities force B weights to be -2p_i and the
AAA identity forces sum p=0; both species therefore have zero tile sum.
On a line Ai=Aj, the two additional stars Ai Ai Bj and Aj Aj Bi have
scores2(p_i-p_j) and -2(p_i-p_j). Nonnegativity requires p_i=p_j.
Every extra star on that line has projected coefficient proportional to the
same line normal, so every extra score is then zero. On a line Ai=120,
the additional stars Ai Ai Ai and Bi Bi Bi have scores3p_i and -6p_i.
Nonnegativity requires p_i=0, and again every additional score is zero.
Thus on each of those six residual lines no potential nonnegative on the
complete star language and zero on all five base stars can make any extra
star positive. The all120 intersection cannot improve this conclusion.

This proves a precise blockage of extending the present positive-star
removal mechanism to those lines while preserving its full five-star core.
It does not rule out a different zero core, edge/patch potentials, geometry
or periodic carriers. Do not assign another equivalent linear corner-weight
search on this unchanged obligation. The exact56-triple ledger supplies the
proportional-normal assertion used above; no numerical optimization is used.

[Independent reviewer](../reviews/two-hexagon-opposite-a-resonance-removal-fresh-hostile-review.md)
confirmed this limitation. It does not exclude weights distinguishing native
slots, a spatially pruned star language, or a different zero-score core.

## Native-word-independent transfer and additional coverage

The positive-star reduction above uses only angle multisets and the five-star
zero core; it is independent of the cyclic native A word. A proof of periodic
escape for an actual defect-free field whose USED stars lie in that core
therefore transfers across the same six isolatedABB resonance lines.
Such a proof need not assume that its polygons have no other unused angle
triples. The freshly reviewed [A001122 all-metric proof](terra-001122-all-metric-periodic-escape.md)
has exactly that property: its native rings, outerAAB coset, sufficient
Reinhardt identities and metric lift use only stars occurring in the field.
Consequently the distinct/non120 extension now covers both001122 and012012
at arbitrary actual metrics and all native B words. Equal-angle/120 loci
remain outside this statement. No new computation is required for this
native-word-independent application of the reviewed sparse potential.
