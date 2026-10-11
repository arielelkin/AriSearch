# Pentagrid-angle pentagons with golden-ratio lengths

**Status:** active user-proposed construction avenue, normalized2026-10-10.
This record replaces the informal `steve-hunch.md`; it is a scoped research
formulation, not a theorem or a claim that the avenue is exhausted.
The original unrestricted two-convex-polygon target is unchanged.

## Exact object and desired mechanism

Seek two distinct genuine convex pentagons P,Q whose interior angles belong
to {pi/5,2pi/5,3pi/5,4pi/5}, with exact positive side lengths involving
phi=(1+sqrt5)/2. First test the finite common-unit alphabet {1,phi}, then
positive exact length families over Q(sqrt5). Relative scales must be stated
explicitly; failure for the common-unit alphabet cannot exclude other scales
or the general positive field-valued family.

Both pentagons must fail monohedral plane tilability. The pair must have a
proved whole-plane tiling, and its geometry must exclude every translational
period in every admitted tiling, including reflections, partial contacts,
right/acute corner subdivisions and omission of a type. A substituted
Penrose-style hierarchy is only an intermediate construction until these
shape-only obligations are proved.

The proposed information carrier is a combination of a finite native-star
angle language and unequal whole/partial side lengths. Partial contacts must
be modeled explicitly; they cannot be discarded from a native length graph.

## Corrections to the informal motivation

A lattice period vector can itself contain phi. A periodic arrangement does
not inherently require an impossible rational integer relation between1 and
phi. The reviewed [three-angle periodic family](../lemmas/new-angle-three-pentagon-private-length-counterexample.md)
closes and has a flat torus for every positive private parameter ratio,
including phi. Its angles are outside the pentagrid set, so this refutes the
irrational-length shortcut without exhausting the present joint-angle family.
The same artifact gives exact periodic examples with irrational angles and
irrational area ratios. A new proof must derive a particular forbidden integer
relation from all admitted geometry rather than assert irrationality alone.

The [side-count reductions](../lemmas/side-count-and-monohedral-obstructions.md)
and [hexagon limits](../lemmas/hexagon-limit-and-periodicity.md) already address
the informal average-corner argument; they do not imply that two hexagons
are too rigid for a hierarchy. The [affine mirror hexagon example](../lemmas/hexagon-affine-mirror-periodic-escape.md)
has an exact periodic mixed tiling with repeated non-equilateral lengths;
its fresh monohedral/classification audit is valid. No broader stiffness
claim is assumed here.

Ammann convex recompositions are already recorded as potential shape-only
sources; they should not be grouped indiscriminately with notched or marked
rules. The [exact parameterization](../lemmas/ammann-coordinate-parameterization.md)
retains specific primary diagram relations, while unrestricted forcing and a
usable global two-class partition remain unproved. The current pentagrid
enumeration is a changed direct-geometric route, not a claim that those
source obligations have been established.

## Exhaustive angular front end

A genuine pentagrid pentagon has an integer word(m0,...,m4),1<=mi<=4,
with sum15, because its angles sum3pi. Enumerate all such words modulo cyclic
rotation and reflection. This is a finite exact angular domain, not a bound
on coordinates or tiling patches.

Any adjacent pair mi+m_(i+1)=5 gives an explicit half-turn central-hexagon
monohedral periodic escape, by the reviewed
[two-angle reduction's unrestricted-length construction](../lemmas/two-angle-pentagon-pair-cairo-reduction.md).
Such a word cannot occur as either member of an aperiodic pair.

The first exact enumeration finds13 dihedral words, of which10 have this
escape. The three surviving words are

    U=(1,3,4,4,3), V=(2,2,4,3,4), W=(3,3,3,3,3).

Their angle lists are respectively(36,108,144,144,108),
(72,72,144,108,144), and(108,108,108,108,108) degrees.
The [angular lemma](../lemmas/pentagrid-pentagon-angular-reduction.md) and
[fresh review](../reviews/pentagrid-pentagon-angular-reduction-review.md) are
valid. The five remaining pairs are U/U,U/V,U/W,V/V,V/W; W/W is impossible.
All five pass the native-angle incidence relaxation, and W count is at most
its partner count up to an O(R) window error. None of this proves geometric
extension or aperiodicity.

At a native corner, genuine sectors sum pi or2pi, according as one or no
straight sector is present. The minimum angle pi/5 analytically bounds full
valence by10 and half valence by5. Thus all native-star multisets are exactly
the nonnegative integer4-vectors s with weighted sum5 or10. Use exact rational
corner-incidence cones for each unordered pair of surviving angle words,
allowing both positive type counts and either omitted type. Boundary errors
must be O(R) before converting local inequalities to plane impossibility.

## Exact metric and global steps

For each survivor, derive side directions from the exterior turns and solve
vector closure exactly. Field-valued lengths lie in Q(sqrt5); sine coordinates
can be represented in the positive real algebraic extension generated by
sin(pi/5), with root-isolation data sufficient for exact verification.
Positive closure must be followed by all supporting-side convexity tests.

The first common-unit metric screen has at most32 side assignments per word.
Retain exact closed shapes, not merely floating-point near-closures. Every
monohedral exclusion needs an actual geometric obstruction or an explicitly
source-checked complete classification, under the problem's unrestricted
isometry/contact convention. Pure corner feasibility does not prove tilability.

For a surviving exact pair, prioritize a concrete whole-plane extension or
recomposition and an inexpensive hostile periodic counterexample search.
A finite torus proves a periodic escape. Absence of a finite torus in a stated
bound proves no unrestricted aperiodicity theorem. If no extension/forcing
mechanism remains, mark that specific ansatz blocked and state a materially
new reopening condition.

## Secondary pentagon–heptagon suggestion

The informal alternative of a pentagon plus a larger convex heptagon is already
an active general family. The reviewed
[two-angle pentagon–heptagon witness](../counterexamples/two-angle-5-7-periodic-instance.md)
shows that neither individual tileability nor the forced1:1 curvature ratio
ensures aperiodicity. The [two-obtuse-angle reduction](../lemmas/two-obtuse-angle-pentagon-reduction.md)
and [distinct-length theorem](../lemmas/distinct-length-obtuse-pentagon-higher.md)
retain precise surviving hypotheses. Other heptagon metrics and nonobtuse
angles remain open; this file does not duplicate that family as a new hunch.

## Results of the first exact exploration

The complete common-unit power screen tests2343 normalized length vectors
(phi^e0,...,phi^e4), with each exponent in{0,1,2,3} and minimum0. It yields
one U, six V and six W vectors; all actual polygons and the complete domain
were freshly checked. The binary alphabet{1,phi} closes only regular W.
See [the metric search](pentagrid-golden-metric-search.md).

The natural U fixture with sides(phi^3,phi^3,1,1,1), paired with regular
unit W, has an explicit four-copy doubly periodic tiling. Its exact periods,
coverage proof and38 complete overlap comparisons are independently valid:
[the counterexample](../counterexamples/pentagrid-golden-metric-periodic-pair.md)
and [fresh review](../reviews/pentagrid-golden-periodic-review.md). This kills
that fixed candidate and the proposed irrational-length shortcut inside the
hunch's own angle family. It does not exhaust arbitrary metrics or scales.

The [Rao monohedral filter](../lemmas/pentagrid-pentagon-monohedral-filter.md)
has a valid fresh source and algebra audit, with independent exact rowspace certificates.
It excludes every positive U from monohedral tilability and characterizes
V's monohedral gates. Its classification is an explicitly imported external
theorem. Four V power fixtures remain after that reviewed filter; no whole-
plane mixed tiling is yet proved for them. The four-face full-edge search
failures have only their stated bounded scope. Partial contacts remain open.

The [corner-and-length obstruction](../lemmas/pentagrid-golden-metric-two-length-edge-obstruction.md)
for one U/V fixture is now independently valid for edge-to-edge tilings;
local partial contacts remain possible. Any eventual
aperiodic candidate still needs whole-plane existence and unrestricted
shape-only forcing. The angular relaxation alone leaves five pairs; the later reviewed two-U
metric theorem below excludes U/U. The other four full metric families
remain unresolved.

## A concrete area-compatible construction and its falsification gates

The [positive U/V family](pentagrid-golden-metric-area-compatible.md) has
exact area ratio phi and both shapes are individually untileable under the
reviewed imported classification. Independent coefficient verification
proves closure and genuine global convexity for every real b,c>0.
No mixed plane tiling is yet established.

The [minimum-six dissection theorem](../lemmas/pentagrid-golden-metric-small-substitution-obstruction.md)
is independently valid and kills the usual phi and phi^2 inflations.
The [metric boundary obstruction](../lemmas/pentagrid-generic-metric-substitution-obstruction.md)
is independently valid: for c/b outside Q(sqrt5), NO inflated U can be
finitely subdivided into the two shapes at ANY linear scale greater than1.
For field-valued parameter ratios, boundary lengths force scales in Z[phi].
These are subdivision obstructions, not exclusions of arbitrary plane tilings.

For the exact b=c=1 fixture, [the boundary/corner theorem](../lemmas/pentagrid-golden-metric-short-boundary-obstruction.md)
is independently valid and proves phi^3 is the first possible homothetic
scale. The [single13-child experiment](pentagrid-golden-metric-phi3-macro.md)
returned UNKNOWN (timeout) after120.205638seconds; its complete exact formula
and solver metadata are retained. No second run or larger patch bound was
launched. This gives no dissection or exclusion. The13/21 counts remain
necessary area counts only. A changed direct Robinson-triangle assembly
produced16/25 exact geometric pieces, but internal partial contacts prevent
those particular partitions from being clusters of an edge-to-edge Penrose
source. The exact source-legality obstruction is being extracted separately.
The [source-compiler attempt](pentagrid-golden-metric-robinson-partitions.md)
retains exact16/25triangle partitions,4/15partial contacts, and the precise
selected-compiler rejection. Complete625/21801boundaryword tests with
native fans and disk Euler parity leave150/9288choices, so this necessary
test does not kill every possible source partition. The [fresh hostile review](../reviews/pentagrid-robinson-partitions-review.md) is VALID for this scoped compiler rejection, and the independent checker passed.
A different actual source partition, or a new nonhierarchical whole-plane
construction, is required before this fixture can progress.

The [whole-area-family edge obstruction](../lemmas/pentagrid-area-family-edge-obstruction.md)
is freshly reviewed valid for every b,c>0, with no Rao import: any plane
tilings of these U/V shapes must use partial contacts. This does not exclude
regrouping an ETE triangulation into partially contacting pentagon macros.

A changed exact [U/W periodic continuum](../lemmas/pentagrid-u-w-periodic-continuum.md)
is adversarially reviewed for b>0,0<c<phi*b, with U sides(A,A,b,c,b),
A=phi^2*b+phi*c, and equiangular W sides(b,b,H,c,H),H=phi^2*b-phi*c.
The four-face torus needs a native index shift by3 on one W copy; its
complete linear seam identities and six circular vertex links are retained.
A degree-one local isometry and exact area identity prove coverage on the
whole domain. The [fresh hostile review](../reviews/pentagrid-u-w-periodic-continuum-review.md) is VALID, with independent coefficientwise identities and exact fixture verification. The b=1,c=sqrt(2) fixture independently
of the family argument passes38completeexactoverlaps; its parameter and
area ratios lie outside Q(sqrt(5)), yet the arrangement is periodic. The
remaining U/U,U/V,V/V,V/W families are not excluded.

## Native-corner measure and the asymmetric U/U obligation

The [native-measure reduction](../lemmas/pentagrid-u-word-native-measure-and-maximal-ray.md)
has a [VALID fresh hostile review](../reviews/pentagrid-u-word-native-measure-and-maximal-ray-review.md), including both corollaries. Giving native
36,108,144 corners weights 2,1,-2 makes each U tile have total weight zero
and every admitted native star have nonnegative weight. A translated limit
therefore has only 334,1144 and half 14 stars, even when partial vertices
merge; the argument uses vague continuity of the native-corner measure.
In that limit no native108 corner can occur inside another side.

The resulting reviewed maximum-long-side argument excludes every finite
collection of mirror U metrics (A=B), with arbitrary relative scales.
That native-measure lemma alone does not exclude asymmetric U/U: a longest acute ray can meet the
other36 sector of a full1144 star, forming a longest-side dimer; it may also border the straight sector in a
half14 star. Its other acute ray can be shorter. A separate reviewed corollary excludes every finite U collection from edge-to-edge
tilings, so any surviving asymmetric realization requires partial contacts. The two-type maximum-contact argument below now closes this gap for U/U;
three or more asymmetric U shapes remain unclassified. Do not silently replace the
longest ray by the shorter one or treat finite-patch failure as a proof.

## The U/U pair is now excluded with all partial contacts

The [two-U maximum-side theorem](../lemmas/pentagrid-two-asymmetric-u-obstruction.md)
has a [VALID fresh hostile review](../reviews/pentagrid-two-asymmetric-u-obstruction-review.md).
Its zero-measure limit comes from the separately reviewed native-measure
lemma. A maximum ray meets either144, another36, or a straight sector;
the proof excludes all three, including both short and long straight hosts.
The new identifications use the fact that only one lower-maximum type is
available; they do not extend to three or more asymmetric U shapes.
Reflections, relative scales, arbitrary real metrics, partial contacts and
omission are included. No Rao theorem is required.

Consequently the unrestricted pentagrid avenue now has four surviving word
pairs: U/V,U/W,V/V,V/W. Individual periodic metric subfamilies remain killed,
while their full metric classifications remain open. A changed [V/W dimer continuum](../lemmas/pentagrid-v-w-periodic-continuum.md)
has a VALID fresh full-family review and independent exact fixture checks. This
restriction does not exhaust the user avenue or solve the main problem.

## Actual finite source assemblies and the remaining extension gate

The changed [five-direction height test](pentagrid-robinson-height-boundary.md)
and [source-rhomb completion/assembly](pentagrid-robinson-source-clusters.md)
have separate VALID analytic, integer-enumeration and geometric reviews.
The complete fixed six/nine-rhomb residual search found28 U clusters and168
V clusters. Every positive witness and all17 rejected V boundaries passed
independent exact verification. [The retained diagram](pentagrid-robinson-source-clusters.svg)
shows the first exact witnesses and their compulsory outside source rhombs.
This supplies actual ETE rhomb-half geometry replacing the original failed
T-junction partitions. It does not yet establish Penrose arrows, infinite
source membership or a global two-class partition.

A new proper-Penrose acceptance-window test is active under fresh review.
The first U/V finite assemblies fail its necessary source layer condition;
other boundary words can pass that condition. Exact shifted-window tests
must distinguish actual global source membership from finite geometry and
must handle singular proper tilings through a justified finite-pattern
argument. Generalized noninteger-intercept pentagrid tilings are outside
this particular proposed gate. Neither its unreviewed result nor a finite
source cluster may be treated as shape-only aperiodicity.

The reviewed [V/W periodic family](../lemmas/pentagrid-v-w-periodic-continuum.md)
works for every b,c>0 with V sides(b,D,b,E,E), D=2phi*b+phi^2*c,
E=phi(b+c), and W sides(b,H,b,E,E), H=2b+phi^2*c. It gives four motifs,
ten seams, six ordered links and a whole-plane degree-one torus proof;
the b=1,c=sqrt2 member has32 independently checked complete overlaps.
These metric subfamilies have periodic escapes; arbitrary V/W metrics
remain open. A changed V/V construction mechanism is active independently.

## Current ownership and restart obligations

Angular enumeration/native-star inequalities and exact golden-length
construction proceed independently, with fresh review of each consequential
claim. Root integrates only reviewed conclusions into discovery-log.md.
No final mathematical report exists. The avenue is not yet exhausted.
