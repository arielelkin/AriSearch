# Complete unsigned-angle resonance gate for the last B word

Date: 2026-10-19. Status: exact finite census, [independently hostile-reviewed PASS](../reviews/hexagon-thirtytwo-resonance-strata-hostile-sol-2026-10-19.md) after correcting a report-only lift-count typo. The original problem is unresolved.

## Domain and result

Fix A=(0,1,2,0,3,4), B=(0,1,2,0,3,1), with distinct positive numerical lengths for different colors. Corner i is at the end of side i. The reviewed native upper atlas has32 cyclic signed stars. Forgetting signs and ordering leaves exactly16 triples, each with exactly two signed lifts:

    012, 018, 027, 078, 126, 168, 267, 2:7:11,
    345, 3:6:10, 3:10:11, 459, 678, 6:9:10, 7:8:11, 9:10:11.

Here indices0..5 are A corners and6..11 are B corners. The certificate lists these as unambiguous integer arrays. Unsigned masks use that displayed order, least significant bit first.

The complete domain of65536 unsigned subsets closes to628 distinct rational affine angle spaces modulo the two polygon totals. The census uses no symmetry quotient and has no timeout, randomness, or solver. Of those spaces306 force a pure consecutive triple and therefore admit a conditional monohedral periodic escape. After fixed-point seam pruning,300 further spaces fail necessary full corner cover. The remaining22 spaces have necessary full corner cover and at least one of the existing100 formal A-dimer boundary coronas. Of those22,13 have complete deterministic signed-neighbor tables and9 branch. No additional corona or quotient size was searched.

There are99 spaces passing the necessary corner-cover and corona filters in total;77 of these are already among the306 pure-triple escape spaces. No separate corona-only rejection occurred. The count306 gives priority to the pure escape test, so its members can also fail other filters.

## Exact affine and strict-angle calculation

Angles are measured in pi units. Put x_i=alpha_i-2/3. Every unsigned star equation becomes the homogeneous equation sum(x_i for its three corners)=0; polygon totals become sum(x_i for each species)=0. Thus ordinary rational row-span closure in12 coordinates is exactly affine closure in alpha coordinates. The script starts at the closure of the two totals, repeatedly adjoins each missing unsigned row, and deduplicates closed masks. It also exhausts every one of65536 masks by the identity cl(M union {i})=cl(cl(M) union {i}), checking that the two enumerations have identical images.

Every affine space has the exact strict point alpha=(2/3)^12, so strict feasibility0<alpha_i<1 never rejects a space. This supplies a rational feasibility certificate directly without an LP solver. For a closed set, every excluded row restricts to a nonzero linear functional on its homogeneous nullspace. A finite union of proper rational hyperplanes cannot cover that nullspace. Choose a rational vector outside this union and multiply it by a sufficiently small positive rational epsilon; alpha=2/3+epsilon*x then has precisely this compatible unsigned support and remains strict. This proves the exact angle strata are nonempty, including excluded-star inequalities. It proves no closed polygon metric or common-length realization. All628 affine dimensions are at least4; no stratum forces all angles to120 degrees.

## Necessary filters and escape implications

Every unsigned closed set is lifted to ALL of its signed stars. For each active signed star and each of its three seams, at least one compatible remote-endpoint star must survive. Iterate deletion to a fixed point. Every actual star in a plane ETE trivalent tiling survives this necessary operation, since its actual remote endpoint supplies a continuation. The certificate records every deletion round.

Full cover means every corner of both species occurs among the surviving stars. This is necessary for an ETE tiling that uses both species; this filter alone says nothing about a tiling omitting one species. The scope of these census exclusions is explicitly the full-cover mixed component. Pure-triple periodic escapes are unconditional on use of both species. A complete unrestricted application must separately handle monohedral tilings through the already reviewed hexagon classification; full cover is not silently imposed on the problem.

The100 previously enumerated A-dimer coronas are filtered by requiring an active signed star realizing every one of their ten boundary factors. This is a necessary condition, not a claim of distinct tile identification, geometric nonoverlap, or plane extension. The private A side5 forces an A-A dimer whenever A occurs.

Pure triples are(0,1,2),(3,4,5),(6,7,8),(9,10,11). Closed row-span membership tests their implication exactly. Either A triple forces the other by total4, as do either B triple. Each implies that the equal-length opposite sides0 and3 of its polygon are antiparallel. The reviewed universal monohedral strip construction therefore gives a periodic tiling for every strict closed metric in such a space, conditional only on metric realization. See `hexagon-five-four-two-more-universal-omissions-2026-10-19.md` and its cited general strip proof. No new metric realization is asserted.

For the13 deterministic residuals, the certificate retains all24 signed native side states and their alternatives. Each has exactly one alternative, and the map is checked involutive. Neighbor native side and relative handedness determine the complete isometry across a full side. Thus the reviewed intrinsic determinism theorem applies to any ETE trivalent plane tiling restricted to those pruned supports, giving two independent periods. The13 strata reduce to only three active signed supports:

    {2,5,13,15,17,20,22,23},
    {3,7,8,10,18,21,22,23},
    {2,5,12,14,18,21,22,23}.

The first is the earlier reviewed eight-star locus. The other two tables use the same finite complete-placement argument. The defect-free limit can supply an ETE trivalent tiling from an unrestricted tiling under its reviewed hypotheses, but a formal corona cannot do so. The linked independent review checked this conditional application.

## Exact uncovered branching residuals

The following is the entire remaining list after pure escapes and the necessary filters. Dimensions count affine angle freedom. Branches count signed side states with more than one alternative; full alternatives are retained in each stratum's `signed_neighbor_table` and `branching_states`.

| unsigned mask | dimension | signed lifts before pruning | witnessed formal coronas | branching states |
|---:|---:|---:|---:|---:|
|3162|6|12|4|8|
|3778|6|12|4|8|
|3802|5|16|9|14|
|3814|5|16|4|8|
|27672|6|12|1|10|
|27714|6|12|1|12|
|27738|5|16|4|16|
|27750|5|16|1|12|
|27836|5|18|1|10|

The active signed-star count after seam pruning is 12 for masks 3814,
27750 and 27836; for the other six rows it equals the displayed lift
count. The certificate retains both lists separately.

The inclusion-minimal branching masks are3162,3778,27672,27714. As an explicit example, mask3778 allows signed side(A3,+) to meet either(B0,-) or(B0,+); side(B1,+) can meet either(B1,+) or(B5,-). These are distinct complete placements, so the previous intrinsic deterministic propagation proof does not apply. Branches in the table are local necessary possibilities, not witnessed geometrically realizable transitions.

No new prospective global invariant has been identified on these nine loci. Therefore no closure/Jacobian calculation is justified by the stopping rule merely because branches remain. The exact missing obligation is to realize a distinct-positive-common-length metric on a residual stratum and supply a new unbounded forcing or periodic-construction mechanism for it. The common strict angle witness does not solve polygon vector closure: at all120 degrees the closure of these two native words collapses colors, violating distinctness. Existing local filters and deterministic propagation do not settle that nonlinear metric/global obligation. Stop this route under protocol section5 until a materially new mechanism is supplied; preserve the nine strata as uncovered, not excluded.

## Artifacts and replay

Producer: `research/searches/hexagon-thirtytwo-resonance-strata-sol-2026-10-19.py`.
Certificate: `research/certificates/hexagon-thirtytwo-resonance-strata-sol-2026-10-19.json`.
Software versions are retained in the certificate. Arithmetic is Sage QQ throughout proof-relevant row membership. Original atlas reconstruction uses its retained exact combinatorial producer. No wall-time cap or seed applies.

Replay without rewriting retained evidence:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-thirtytwo-resonance-strata-sol-2026-10-19.py --check

The producer retains the normalized rational x-row basis, all signed lifts, seam-deletion rounds, exact corona indices, all surviving neighbor tables, and uncovered residuals. This is a restricted finite angle-support classification. It neither resolves the original problem nor proves a general finite-to-plane theorem. No novelty claim is made and no new literature theorem is invoked.
