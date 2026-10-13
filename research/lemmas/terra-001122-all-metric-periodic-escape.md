# Generic ternary A001122: arbitrary metrics have periodic escapes

Date: 2026-10-13. Status: independently adversarially reviewed VALID;
[fresh review](../reviews/terra-001122-all-metric-periodic-escape-fresh-hostile-review.md).
This is a restricted angle/native-word coverage theorem, not the global target.

## Statement and dependencies

Let actual strictly convex hexagons A,B have respectively two copies of each
angle x,y,z and r=360-2x,s=360-2y,t=360-2z, with x+y+z=360 and90<x,y,z<180.
Assume all six angle values distinct and the complete trivalent star language
exactly AAA=(x,y,z), BBB=(r,s,t), and AAB=(x,x,r),(y,y,s),(z,z,t).
A has native angle word001122. B may have any native order. Actual side lengths
of both polygons are arbitrary, including every additional equality.

If the pair tiles, it admits a periodic tiling. Reflections, original partial
contacts and omission of either type are included. The theorem uses the
reviewed defect-free limit and monohedral theorem, generic ternary B-B
propagation, honeycomb indexing, exact one-B rings, full-A-tuple lifting and
metric development in the named repository dependencies. It does not assume
that the original tiling has no AAA stars or is edge-to-edge.

Dependencies:
[hexagon limit](hexagon-limit-and-periodicity.md),
[ternary star and B-B gate](two-hexagon-ternary-angle-star-balance.md),
[reviewed one-B ring reduction and full-A quotient](two-hexagon-one-b-ring-spatial-reduction.md),
[reviewed global metric encoding](two-hexagon-global-sft-encoding.md),
and Reinhardt H1/H2 sufficient periodic families from the refreshed primary
[source](https://arxiv.org/html/2508.01404v2).

## Unique endpoint palette at arbitrary metrics

Number A corners by001122 and A sides by i joining corners i,i+1. Their
unordered colour pairs are respectively

    00,01,11,12,22,02.

These are all six possible pairs, each exactly once. In a genuinely mixed
connected defect-free field B has no B neighbour, by no-ABB propagation.
Every B vertex is a same-colour AAB vertex. Therefore every AB seam maps each
A endpoint colour to its B endpoint colour. Any B side has the same length
as the unique native A side with that endpoint pair. This remains true when
A lengths merge: endpoint COLOURS select the native side index before any
metric equivalence is applied. Reflections only reverse the endpoint order.

Consequently a B native word forces all its lengths from the six A sides.
A neighbour on a B side has exactly one native placement if the endpoint
colours differ, and two if they agree. There are only eleven B bracelets.
All their12 indexed placements and complete AB-compatible A tuples give360
raw ring states, independent of the A metric. This small domain includes
all genuinely mixed B neighbourhoods before any geometric-closure screening.

## Complete finite reduction, including all metric specializations

An actual equality relation on six A sides is one of Bell(6)=203 partitions.
The finite certificate projects every raw ring to every such partition,
73080 cases. It checks six AA seam equalities and necessary completion of each
outer endpoint by any native AAA or AAB corner, in both arm orders.
For each partition and native B word, it also checks sufficient monohedral
periodic escapes H1 and H2 under every cyclic/reflected relabelling:

    H1: corners0,1,2 have all three colours and side2=side5;
    H2: corners0,1,3 have all three colours and side1=side3,side2=side5.

The complementary three corners also have all three colours. Both A and B
colour triples sum360, so these are exact angle identities throughout the
stated stratum. They are sufficient escapes, not an asserted completeness
of this colour-level test. H3 is not needed.

The retained exhaustive native ledger establishes: whenever neither shape
has one of these sufficient escapes, and a fully outer-completable B ring
exists, its native word is one of

    010212,012021,012102.

There are369 residual partition/word records,123 per word. The raw ring and
all completion offers, projected survivors and monohedral labels are retained.
Formal partitions not jointly realizable geometrically are not discarded or
promoted to polygons; including them only strengthens this necessary test.

## Those three residual words force the global one-B coset

Each of the three words has no equal adjacent colours. Each indexed B
placement therefore has one and only one complete A tuple. Every one of its
six AA seam equalities matches a native A side index to itself. Moreover its
outer AA endpoints have SAME A colour, always, independent of lengths or
metric specializations. Every such endpoint is consequently AAB; AAA is
excluded there by the exact star language. All required native B corner arm
completions are available before any side merge. These facts are explicit in
the finite residual certificate and do not assume closure or extension.

Use the reviewed cell-lattice directions

    D=((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)),
    Delta_k=D_k+D_(k+1).

A B at z has A neighbours z+D_k and z+D_(k+1) at their shared outer AA seam.
The third cell at its outer endpoint is z+Delta_k. The preceding same-colour
conclusion forces this third cell to be B. Inducting in all six directions
therefore puts B at every point of

    z+L, L=span_Z{Delta0=(1,1),Delta1=(-1,2)}
         ={(p,q):p-q=0 mod3}.

Every cell outside this coset neighbours a B and must be A, since an ABB
vertex or B-B seam would force the connected field pure. Each elementary
triangle meets the B coset exactly once. Thus every star in this actual field
is AAB globally: a possible distant AAA region is not being ignored.

## Functional full-native overlap produces periodic escape

For each residual word the12 raw indexed B rings have six distinct FULL
ordered A-neighbour tuples, with two central-B native aliases per tuple.
No A symbol is forgotten. The overlap relations are exactly the reviewed
native equalities

    a_k=a'_(k+4), a_(k+1)=a'_(k+3).

For every direction and every one of the six quotient states there is exactly
one successor. The finite maps are involutions, opposite moves coincide,
the two basis maps commute, and the diagonal map is their product:

    T_(k+3)=T_k=T_k^-1, T0 T1=T1 T0, T2=T1 T0^-1.

These statements are retained and directly verifiable. In particular every
quotient field has period2 Delta0. The reviewed full-A-tuple quotient theorem
lifts it canonically to a periodic FULL native ring field by choosing an
available central B representative once per tuple. Overlap conditions do not
depend on that omitted B label. Every representative retained for the actual
metric already satisfies all native side and angle constraints. Further
metric equalities cannot create new quotient successors, and all203 cases
have been explicitly checked in any event.

The metric development theorem then gives an admitted actual polygon tiling
with a nonzero translation, after squaring a glide if required. This is an
existence-of-periodic-escape conclusion; it need not make every original B
alias choice periodic. No finite patch is inferred to extend merely because
it survives: an actual defect-free field supplies existence here, and the
reviewed canonical lift/development supplies the periodic replacement.

Finally pure defect-free limits already give monohedral periodic escapes.
If an original pair tiles, its reviewed defect-free limit is either pure,
has an immediate H1/H2 omission escape, or belongs to the residual functional
case. These alternatives exhaust all actual metrics and prove the theorem.

## Finite evidence and exact scope

[Native producer](../searches/terra-001122-all-metric-native-rings.py),
[203-partition certificate](../certificates/terra-001122-all-metric-native-rings.json),
[residual finite actions](../certificates/terra-001122-residual-functional-actions.json),
[separate no-import checker](../reviews/verify_terra_001122_all_metric_rings.py).

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_terra_001122_all_metric_rings.py

No solver, search timeout, seed, floating-point test or torus bound was used.
All finite tests are native integer equalities and exact indexed colour
identities. The all-angle result avoids extrapolating the fixed-fixture B
closure computation, which was insufficient for its former geometric claim.

Independent hostile review has checked the native finite domain, its separate
checker, all six overlap maps, outer-AAB coset propagation and actual-metric
transfer. A supplemental independent checker validates the premerge offers
and exact residual word-index coverage.
Other native A words and extra-star angle strata remain unresolved.
