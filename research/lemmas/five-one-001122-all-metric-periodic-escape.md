# A001122 with five-plus-one B: periodic escape at every actual metric

Date: 2026-10-13. Status: [fresh independent hostile review VALID](../reviews/five-one-unused-aa22-support-fresh-hostile-review.md)
for the strengthened support theorem and this synthesis. The used-AA22
component also has its separate independent VALID review.

## Theorem

Let 108 < x < 126, x != 120, and set

    y=720-5x, z=4x-360, r=360-2x, s=360-2y.

Let A and B be actual strictly convex hexagons with counter-clockwise native
corner words (x,x,y,y,z,z) and (s,r,r,r,r,r), respectively. Their metrics
are arbitrary: all side-length equalities, including a4=a0, a4=a1, a4=a2
and all combinations or further specializations, are permitted. If the
pair admits an unrestricted plane tiling, it admits a plane tiling with a
nonzero translational symmetry. Reflections, original partial contacts,
and omission of either species have the conventions of the original
research problem.

This is a restricted-family exclusion of aperiodicity. It is not a theorem
for arbitrary two convex polygons and does not assert that every admitted
tiling of this family is periodic.

## Dependencies with precise roles

1. [Hexagon limit](hexagon-limit-and-periodicity.md): any original tiling
   supplies an admitted whole-side trivalent field; a monohedral limit
   yields an admitted periodic omission escape through the retained
   unrestricted convex-hexagon monohedral classification.
2. [B saturation](terra-five-one-b-saturated-chain-reduction.md), with the
   [full strict-convexity interval review](../reviews/five-one-full-strict-convex-angle-line-extension-review.md):
   a further admitted limit is pure A or mixed with every B of BB degree 2.
   Pure B is excluded by the complete star language
   AAAxyz, AABxxr, AAByys, ABBzrr.
3. [Used-AA22 escape](terra-five-one-001122-full-cross-22-escape.md), with
   [independent VALID review](../reviews/terra-five-one-001122-full-cross22-luna-hostile-review.md):
   if an actual whole-side trivalent field uses even one AA seam at native
   A side 4, A belongs to a sufficient periodic monohedral H2 family. It
   covers all 96 endpoint configurations and all 203 actual A length
   partitions. Its sole formal non-H2 partition (a,b,c,a,b,c) has no positive
   closed polygon on the full interval, by an exact half-plane separator.
4. [Unused-AA22 support theorem](five-one-all-mask-no-cross-periodic-escape.md):
   an actual mixed saturated field in which every native A side 4 meets B
   supplies a periodic escape, with no restriction on length aliases.
   Its proof extracts a no-AAA/all-curved field, derives a periodic species
   base, reduces every full-native fibre to two states using actual B
   closure where necessary, and applies the reviewed binary equality and
   actual metric development theorems.

## Proof: dichotomy in one actual saturated field

Assume an unrestricted tiling exists. Dependencies 1 and 2 supply either
a periodic omission escape already, or an actual mixed saturated field T
for the same two fixed polygons. No contact restriction has been imposed
on the original tiling; T is a possibly different admitted limit.

If T contains an AA seam using native side 4 of an A, apply dependency 3.
Both endpoints are AAAxyz because side 4 has two z corners and neither
AAB star contains z. Thus all its local hypotheses hold. It yields a
periodic tiling using A alone, which the original pair admits.

Otherwise no such AA seam occurs anywhere in T. Every side in T has a
whole-side partner, so every native A side 4 meets B. T therefore meets
all three hypotheses of dependency 4: whole-side/trivalent, saturated B,
and unused AA22 support. It yields a periodic tiling by the same actual
polygons.

These are exhaustive alternatives for an actual field, including the case
where a formal cross match is permitted by equal lengths but not used.
Length equality is never substituted for existence of a contact; absence
of a contact is never substituted for length inequality. Every unrestricted
tilable pair in the stated native-angle family therefore has the required
periodic escape. QED.

## Exact evidence and review scope

The existing native finite obligations are sufficient; no new metric-grid,
solver, radius, or timeout search is required by this synthesis.

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/five-one-all-mask-no-cross-binary-lift.py --check research/certificates/five-one-all-mask-no-cross-binary-lift.json
    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_terra_cross22_luna.py

The first checks 2 words x 2 species bases x 8 cells, all 12 indexed poses
per cell, the metric branches, symmetric profile quotient and symbolic
closure identity. The second independently reconstructs the complete
A001122 two-ended cross domain and exact closure obstruction. Neither
checker replaces the analytic sparse-extraction, periodic-lift or synthesis
proof. The linked fresh review checks those implications, the full interval,
retention of all metric aliases, and original contact/omission quantifiers.

No new literature priority claim is made. The global research objective
remains unresolved.
