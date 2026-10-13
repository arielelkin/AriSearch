# Penrose dual single-fusion: a viable local pentagon and the global deletion obligation

Date: 2026-10-13. Status: **local deformed polygon and omission gate independently reviewed VALID**;
[fresh review](../reviews/penrose-dual-fusion-thin-deformation-fresh-hostile-review.md). No infinite two-shape covering or forcing theorem is claimed.

## Changed hypothesis and finite obligations

The reviewed [full-spoke obstruction](penrose-boundary-dual-spoke-obstruction.md) preserves one final face at every source vertex, and consequently retains triangles at trivalent source vertices. This attack changes that precise hypothesis: delete one edge of the dual network and fuse its two incident faces. The source remains an exact marked Robinson/Penrose rhomb patch. Crossings remain inside source edges. Reflection is not restricted.

First finite domain: the three edges at source vertex10 of the retained three-deflation patch. The originally retained vertex3 cannot be used for this computation because some of its neighbor stars reach the finite patch boundary. At vertex10 the central star is rhombs3,6,7; its three neighboring source stars have valences7,5,4. All source coordinates are retained in [source data](../certificates/penrose-centered-dual-single-fusion-source.json); they are in K=Q(w), w=exp(i*pi/5), with the basis1,w,w^2,w^3.

Question: does a single deletion repair the triangle while yielding a genuine convex pentagon or hexagon? Outcomes determine whether changing incidence is locally viable before any global enumeration. Exact center-coordinate results: deletions across source edges(2,10) and(7,10) have a reflex corner; deletion across(9,10) gives a genuine convex pentagon. Its exact angles are(126,108,72,162,72) degrees and native side lengths(s,s,s,t,t), with s^2=(3+w^2-w^3)/4 and t^2=(2+w^2-w^3)/4. The consecutive wraparound angles162+72+126 sum to360. Thus this centered pentagon belongs to the known Type1 monohedral periodic family. Admitting it as a prototile kills aperiodicity by omission of the partner. This periodic conclusion uses the established sufficient Type1 family, rather than the completeness theorem.

A second finite control, the three edges at source vertex11 with three valence5 neighbors, has one convex six-corner union and two reflex unions. No global interpretation or monohedral classification of that six-corner union is asserted.

## Exact changed-point local pentagon

Next symbolic domain: one real scalar tau. In the retained marked frame of each thin rhomb, with frame rotation w^a, put p_r(tau)=center_r+tau*w^a. Keep thick-rhomb points at their centers. Keep exactly the same deletion(9,10). Before any source enumeration, test the exact sample tau=1/100 against strict convexity and all known monohedral pentagon families.

The resulting pentagon has vertices, in order,

    (1,1/2,1,-1/2),
    (1,0,49/100,-1/2),
    (3/2,-1/2,1,-3/2),
    (3/2,0,3/2,-3/2),
    (3/2,1/2,3/2,-101/100),

where each tuple is a coefficient vector in the stated basis. These are the points of source rhombs3,5,58,6,7. Every source point of the finite fixture lies strictly inside its rhomb. Every center-line connection across an internal fixture edge crosses that source edge strictly inside both segments. The dual triangle(3,6,7), dual quadrilateral(3,5,58,6), and their fused pentagon satisfy every strict supporting half-plane inequality. Cancelling their shared edge therefore gives an exact locally valid convex union, rather than merely a formal boundary word.

For each vertex i let a_i=P_(i-1)-P_i and b_i=P_(i+1)-P_i. In the specified complex embedding,

    z_i=(a_i/b_i)/abs(a_i/b_i)=exp(i*alpha_i),

with0<alpha_i<pi. Products of the algebraic z_i give exact necessary tests for linear angle relations. A relation summing to360 degrees must have product1; one summing to180 degrees must have product-1. Failure of such a product is an exact exclusion, regardless of possible multiples of360 in the converse.

The finite domain is15 known families times10 cyclic/reflected relabelings =150. The side map under reflection is i -> h-i-1, while the corner map is i -> h-i. Each case fails an exact necessary angle relation; no case needs a metric rejection. The old wraparound Type1 product also differs exactly from1. Conditional on the imported completeness of Rao's fifteen-family classification, this pentagon cannot tile alone with arbitrary rotations, reflections or partial contacts. This is stronger than just breaking the single original Type1 relation, but it remains a **local polygon**, not a two-tile aperiodic construction.

External dependency: [Rao, arXiv1708.00274v1](https://arxiv.org/abs/1708.00274), Table2. The primary abstract and current version record were refreshed2026-10-13; only v1 is listed. The family table is reused from the repository's independently reviewed pentagrid monohedral filter. The new algebraic geometry and150 exact tests have received independent hostile review with a VALID verdict. No novelty claim is made.

## Why one deletion is still insufficient

The retained deformed fixture has an untouched genuine convex quadrilateral at source vertex21, with dual boundary rhombs10,12,17,11. Exact coordinates and supporting-half-plane checks are in the deformation certificate. Any final protoset retaining this quadrilateral admits its monohedral periodic tiling, omitting the desired pentagon. Likewise any untouched trivalent source face is a triangle and gives an omission escape. A global incidence rule must therefore remove **every** triangle and quadrilateral that its actual source produces. Neither the local fusion nor the nonmonohedral pentagon supplies that rule.

For a proposed global deletion rule, a degree-two surviving network vertex must be straight if the two incident final faces are convex: their sectors add to2pi and each is at mostpi. Thus two remaining noncollinear rays are forbidden. Starting from the degree-four rhomb-point graph, deletion of two incident edges is legal only if the two surviving rays are exactly opposite. In the special case with no such opposite pairs AND every original rhomb point retained as an intrinsic network vertex, deleted edges must form a matching at rhomb points. This retained-point condition excludes deleting all four incident edges and removing that point. Then a triangular dual face can have exactly one incident deletion, while a quadrilateral can have at most two, necessarily disjoint along its boundary. This matching condition is conditional: the tau=1/100 fixture has some exact collinear thick-point triples, so one must retain those exceptions rather than silently applying the generic simplification.

There is also a conditional global density target. Suppose a plane rhomb source admits a deletion rule whose remaining graph has every rhomb point as a degree3 or4 intrinsic vertex, and whose final faces are only pentagons/hexagons. Let N count source rhombs and M deleted network edges in a large window; all boundary terms areO(R). Then V=N+O(R), E=2N-M+O(R), and F=N-M+O(R). From5F5+6F6=2E and F5+F6=F,

    F5=2N-4M+O(R),
    F6=3M-N+O(R),
    N/3 - O(R) <= M <= N/2 + O(R).

The number of degree4 points is N-2M+O(R)=F5/2+O(R), precisely the reviewed pentagon curvature requirement. Positive pentagon density demands deletion density strictly below1/2; nonnegative hexagon density demands at least1/3. These formulas do not cover collapsed degree2 points, other polygon sizes, or a merely local patch. They provide an inexpensive invariant that any claimed global rule must satisfy before extensive congruence or forcing searches.

## Fixed-point palette obstruction: the local pentagon does not extend to two5/6 classes

A later cheap global-design gate uses **only** the retained fixture at tau=1/100. Its finite domain is all35 source rhombs whose four neighboring rhombs are present. At each rhomb point retain any3 or4 of its four original rays. Order those rays by source-edge order; every source point is interior and every connecting segment crosses its source edge internally, so this is their actual cyclic order. Discard a choice if any consecutive sector exceeds pi. Allow pi sectors as a relaxation, and omit them from the required intrinsic angle palette.

Question: can at least one allowed local choice at each point be made using at most11 distinct native angle values? Two convex shapes with5 and6 vertices have at most11 native values, irrespective of rotations or reflections. A negative answer excludes all such point-preserving deletion compilers on the fixed sample before checking global edge-deletion consistency or congruence. A positive answer would give only local necessary choices and would not justify a larger patch.

There are26 distinct exact algebraic sector values and six distinct choice signatures among the35 points. Those signatures have4,3,3,3,4,3 choices respectively. Taking one representative point of each signature, all1296 Cartesian products can be enumerated exactly; each required union has at least14 values, and some have exactly14. Thus palette size<=11 is impossible even in the relaxed independent-choice model. CP-SAT first found optimum14; the proof-relevant bound is the subsequent **solver-free1296-product enumeration**, not its solver verdict.

[Finite certificate](../certificates/penrose-dual-fusion-angle-palette.json), [producer](../searches/penrose-dual-fusion-angle-palette.py), and [independently implemented geometry/combinatorics checker](../reviews/check_penrose_dual_fusion_angle_palette.py) retain the35 choices,26 exact angle representatives and all reconstruction data. The checker imports no producer or solver, reconstructs every local choice directly from source coordinates, verifies interior points/edge crossings and exact distinctness, then enumerates the1296 products. External hostile review is still required.

This kills the fixed tau=1/100 compiler **under the point-preserving degree3/4 hypothesis** whenever the two final shapes have at most13 native corners in total, allowing flat pi sectors. In particular it excludes pentagon partners with5,6,7 or8 sides, and two hexagons. A surviving pentagon-containing compiler in this scope needs a partner with at least9 sides. Coincident native angle values only reduce the available palette, so cannot evade this bound. It does not establish that the local pentagon is impossible in an arbitrary pair. Other sample parameters, elimination of rhomb points, added graph nodes, changed cuts, and other side-count pairs are outside the claim. For a putative pentagon/h-gon compiler, h>=6, the same no-collapsed-point Euler calculation gives

    Fh=(3M-N)/(h-5)+O(R),
    F5=((h-4)N-(h-2)M)/(h-5)+O(R),
    F5-(h-6)Fh=2(N-2M)+O(R)>=-O(R).

Thus the reviewed pentagon curvature requirement remains a design constraint for high-sided partners, not an exclusion of them. A9-gon or larger partner is not killed by the14-value palette certificate alone. The subsequent [837-degree exterior-budget obstruction](penrose-fixed-point-two-shape-exterior-budget-obstruction.md) excludes every partner side count under the same fixed point-preserving degree3/4 hypotheses. This closes that concrete compiler, not the general construction track.

A matching deletion in the network need not fuse only two original dual cells: deleting two opposite sides of a middle quadrilateral can join a three-face chain without shared deletion endpoints. No such false pairwise-fusion restriction was used by the palette obstruction.

## Restart point and abandonment rule

The centered single-fusion repair is killed when it selects the recorded Type1 pentagon. The deformed local pentagon survives convexity and all monohedral omission tests, but the fixed-point two5/6 compiler fails the14-versus11 palette obstruction. It does not provide two final congruence classes, global convexity, an infinite deletion rule, recognizability or universal shape-only forcing. This local route is blocked at a genuinely concrete global obligation: supply an exact source-local simultaneous edge deletion/fusion rule that removes all3/4-sided cells, respects straight degree2 exceptions and curvature, and yields only two prescribed convex congruence classes. Reopen global construction only with such a rule or a new exact invariant to derive it. Repeating center-point searches or enumerating larger source patches without that rule is not justified.

The next independent task is hostile review of the local algebraic sample, all150 relabelings, the untouched quadrilateral and the solver-free palette obstruction. If valid, a new proposed deletion rule should first be falsified on the existing complete stars and curvature identities; exact positive geometry must precede any infinite covering or forcing claim.

## Replay

All replay commands are nondestructive:

    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python research/searches/penrose-centered-dual-single-fusion.py --vertex 10 --check research/certificates/penrose-centered-dual-single-fusion-v10.json
    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python research/searches/penrose-centered-dual-single-fusion.py --vertex 11 --check research/certificates/penrose-centered-dual-single-fusion-v11.json
    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python research/searches/penrose-dual-fusion-thin-deformation.py --check research/certificates/penrose-dual-fusion-thin-deformation.json

    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python research/reviews/check_penrose_dual_fusion_angle_palette.py

The source fixture replays from Ammann/Robinson source code via research/searches/ammann-two-class-patchdata.py 3 OUT.json. Exact replay does not certify infinite tilability or universal aperiodicity.

Ancillary density/matching statements were narrowed after independent sol
review: boundary errors occur at both bounds, and the matching implication
requires all original rhomb points retained. [Fresh independent repair review](../reviews/terra-penrose-deletion-repair-review.md)
validates these exact qualifications;
the already reviewed local polygon/omission gate does not depend on these
ancillary design constraints.
