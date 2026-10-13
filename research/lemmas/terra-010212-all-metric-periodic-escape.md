# Generic ternary A010212: every legal mixed ring has a monohedral escape

Date: 2026-10-13. Status: internally proved; separate native checker PASS;
independent hostile review VALID. Restricted angle/native family theorem.

## Theorem

Let actual strictly convex A,B have two copies of each angle x,y,z and of
r=360-2x,s=360-2y,t=360-2z, with x+y+z=360 and90<x,y,z<180. Assume six distinct
angle values and exactly five trivalent star types AAA=(x,y,z), BBB=(r,s,t),
and same-colour AAB=(x,x,r),(y,y,s),(z,z,t). A has native word010212;
B has arbitrary native order. Both actual side metrics are unrestricted,
including every additional equality. Whenever the pair tiles, it admits a
periodic tiling with reflections, original partial contacts and omission
permitted. No genuinely mixed infinite construction is asserted.

Dependencies: reviewed defect-free hexagon limit and monohedral periodic
escape, reviewed generic no-ABB propagation, reviewed honeycomb native slots,
and the sufficient Reinhardt H1/H2 periodic families from the refreshed
[primary source](https://arxiv.org/html/2508.01404v2). These dependencies are
named and linked in [A001122 coverage](terra-001122-all-metric-periodic-escape.md).
This theorem needs no quotient, torus bound or metric-development construction.

## Finite native domain is exhaustive at every actual metric

Take a connected defect-free limit of an admitted original tiling. If pure,
the monohedral dependency already supplies a periodic escape. If genuinely
mixed, B has no B neighbour by no-ABB propagation; every B corner is AAB with
two A corners of its own colour. Each AB side matches those A/B endpoint
colours in spatial order.

A010212 has native endpoint pairs01,01,02,12,12,02. A B edge cannot have equal
endpoint colours. Exactly four of the11 bracelets remain:

    010212,012012,012021,012102.

Each of their edges has two compatible native A sides, one placed orientation
for each. Hence every indexed B placement has2^6=64 complete AB-compatible
A tuples. Keeping all12 rotations/reflections per bracelet gives3072 raw
rings. Native labels are retained even when a polygon symmetry makes some
placed colour profiles coincide; side-index choices are not merged away.

Every ring assigns each native B side its equal matched native A length.
Project every tuple through ALL203 partitions of the six native A side
lengths,623616 cases. This records every actual equality pattern and all its
specializations. B metric values and equalities are derived from that ring's
AB assignments, not chosen independently or assumed to be all different.

Consecutive A neighbours share native side-slots k+1 and k+4. Check all six
AA equalities. At each outer endpoint, check every possible native third
corner and either arm order: different A colours require the missing-colour
A corner, and equal A colours require the complementary B corner. In the
latter case its arm lengths use THIS ring's native B metric assignment.
This conditional necessity allows AAA holes; none are silently excluded.

The exact exhaustive native ledger yields8976 AA-compatible projected rings
and3360 that also admit all six outer completions. For each such case, at
least one of A or B satisfies a sufficient Reinhardt H1/H2 periodic condition
under a cyclic/reflected relabelling:

    H1: colours at0,1,2 are all distinct; side2=side5;
    H2: colours at0,1,3 are all distinct; side1=side3, side2=side5.

Each rainbow triple sums360 for both A and B. The complementary triple is
also rainbow because each colour occurs twice. These exact native angle
identities and actual metric equalities give an admitted monohedral periodic
tiling family. No completeness of this sufficient omission filter is needed.
After applying it, ZERO joint actual A/B metric cases remain.

An actual mixed field provides an actual B ring contained in this finite
domain. Its legal outer corners necessarily pass the completion tests, so
one of its ACTUAL shapes has a monohedral periodic tiling. Omit the partner.
Together with the pure-limit case this proves the theorem. Formal native
survivors without actual closure were never promoted to polygons or infinite
fields; their inclusion makes the necessary finite cover only broader.

## Certificate, verification and scope

[Producer](../searches/terra-010212-all-metric-native-rings.py),
[certificate](../certificates/terra-010212-all-metric-native-rings.json),
[separate no-import checker](../reviews/verify_terra_010212_all_metric_rings.py).

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_terra_010212_all_metric_rings.py

The checker reconstructs the complete B bracelet filter, all indexed placements,
all AB tuples, native B side assignments, AA constraints, every outer native
completion, all203 partition fibres and all sufficient monohedral labels.
Only standard-library native integer equalities are used. No solver, seed,
timeout, numerical acceptance, geometric-feasibility extrapolation or bounded
tiling inference. All original rotations/reflections and later side merges
are retained. Independent hostile review remains necessary before integration
as stable coverage.

This closes the stated family once reviewed. It supplies neither an unrestricted
hexagon theorem nor a pentagon construction; extra-star angle strata are
outside its hypotheses. The next justified work is hostile review and global
family synthesis, not enlarging the completed3072-ring domain.

Fresh independent review: [VALID](../reviews/terra-010212-all-metric-periodic-escape-fresh-hostile-review.md).
