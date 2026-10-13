# Fresh hostile review: arbitrary metrics for A012012

Date: 2026-10-13. Independent reviewer: sol, distinct from theorem author terra.
**Verdict: VALID** for the stated exact five-star language and actual strictly
convex A012012/B001122 angle multisets, allowing all actual metrics.

The claim reviewed is tileability implies an admitted periodic omission
escape. It does not classify other native A words or general angle strata.
Reviewed defect-free-limit, central-hexagon and unrestricted monohedral
hexagon dependencies were checked for applicability, not repeatedly audited.

## Independent reconstruction and attacks

The three exterior turns u,v,w are positive and sum180. Directions of
opposite edges are negatives. The closure kernel is therefore the span of
(sin w,-sin u,sin v). All components are nonzero. The displayed half-angle
identity proves strict triangle inequalities, so no signed sum of the three
positive sine values vanishes. One opposite equality or a relation involving
all three opposite differences with coefficients +/-1 forces the kernel
parameter zero. This reasoning is exact for every allowed angle; no numerical
or rational-angle assumption is hidden.

An AAA star has one corner per colour under the exact star-language
hypothesis. Fixing order012 loses no configuration: the other circular order
is its reflection. Each chosen corner can independently reverse its arms.
The64 cases are consequently complete as necessary local equality tests,
even though they may admit geometrically unrealizable reflected assemblies.
For the six consecutive-corner choices, the side-label equality graph has
precisely two odd-degree vertices, the two outer arms. Components of any
multigraph have an even number of odd-degree vertices, including loops and
parallel edges. The outer arms must therefore lie in one component, forcing
an opposite equality. For the other two corner choices, all six side labels
occur once. If the ray matching has no opposite pair, its union with the
opposite matching is a connected alternating six-cycle: a disconnected
component would require a two-cycle, hence a common pair. Summing differences
around this cycle yields the stated signed relation. Both mechanisms survive
arbitrary further length merges. No exceptional positive-angle degeneration
invalidates the strict triangle step.

For a noncentral A, AAA is thus impossible. In a genuinely mixed field,
no-ABB removes B-B contacts by propagation; BBB is consequently impossible.
Every remaining vertex is AAB. Around any A tile, successive neighbouring
species must alternate, since each vertex needs exactly one B neighbour.
Around a B tile its six A neighbours meet pairwise along AA edges. At their
outer endpoint the third cell is B, because AAA is absent. A012012 has three
distinct colours at every three consecutive native vertices, independently
of reflection. The two outer A colours are the missing colours from the two
adjacent B colour pairs. Their required equality forces b_(k-1)=b_(k+1).
Hence B has period two, contradicting its two corners of each of three
colours. This proves the ring obstruction locally and requires no additional
species-coset assumption or finite torus argument.

A plane tiling first supplies a defect-free connected limit under the named
reviewed dependency. If A is central it itself supplies an omission escape.
Otherwise the limit cannot be genuinely mixed; pure A also requires AAA,
so it is pure B and its monohedral periodic theorem applies. Loss of either
species in the limit is permitted by the original problem. The original
partial-contact tiling need not be pure or periodic.

## Equality classifications and scope

The independent retained checker was executed successfully. Its full203
side-equivalence truth table verifies every one of64 corner/reversal cases;
all52 partitions coarsening a0=a1 are explicitly checked, giving34 AAA
admitting patterns and five minimal ones. Thus further specializations are
included, rather than presumed covered merely because minimal ones were
listed. The kernel proof forces all34 to centrality in any actual closed
polygon. If the partition denotes exact distinct classes, only the partition
L=P=Q and M=V, or its all-equal merge, survives centrality among those34;
the others have no actual closed realization in the exact partition stratum.
For the18 nonadmitting partitions, geometric realization is irrelevant to
the implication: every realized polygon has no mixed-field extension.
Positive central lengths give actual strictly convex zonotope hexagons and
periodic omission escapes. No local feasibility is promoted to tilability.

No consequential defect was found. Equal angle colours, extra stars and other
native A words fall outside the theorem; especially at nongeneric angles an
AAA star need not choose one corner of each named colour, so the centrality
argument must not be promoted without a new star-language proof.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_terra_ternary_aaa_equalities.py

Outcome: PASS. The original unrestricted research problem remains unresolved.
