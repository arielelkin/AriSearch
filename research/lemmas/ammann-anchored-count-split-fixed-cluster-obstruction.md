# Ammann anchored count split and the fixed-content cluster obstruction

Date: 2026-10-13. Status: **independently adversarially reviewed VALID**;
[fresh review](../reviews/ammann-anchored-count-fixed-cluster-fresh-hostile-review.md). This is an exclusion of a specified source-fusion mechanism, not a two-tile impossibility theorem or novelty claim.

## Source and exact hypotheses

Use [the reviewed generic Ammann forcing theorem](ammann-forcing-aperiodicity.md), Lemmas5 and6, with J in its stated generic domain G*. All source tiles H6,P1,P2 are genuine compact convex polygons of three distinct congruence classes. Every admitted source tiling permits arbitrary reflections/contacts; the forcing theorem excludes partial contacts and establishes one handedness and canonical reconstruction of a legal marked thin/thick rhomb tiling. We do not assume the conditional Euler incidence counts from the older coordinate-parameterization artifact.

Let h(R),p1(R),p2(R) count source polygon anchors in a square of sideR. Let t(R),T(R) count thin/thick reconstructed unit-rhomb anchors in the same square. Arbitrary fixed interior anchors are allowed. Constants in boundary errors depend only on the fixed shapes. The theorem below needs the reviewed piece partition/bijection and hierarchy; it does not identify the marking with P3 or invoke an unproved frequency split.

## Lemma1: bounded-displacement anchor bijections

There is a canonical bijection from H6 copies to reconstructed thin rhombs, a canonical bijection from P1 copies to reconstructed thick rhombs, and a canonical bijection from P2 copies to reconstructed thick rhombs. All three maps have uniformly bounded displacement. Consequently,

    h(R)=t(R)+O(R),
    p1(R)=T(R)+O(R),
    p2(R)=T(R)+O(R).

Proof. In reviewed Lemma5, each H6 has its distinguished quadABJD; its thin group consists of that quad and the two uniquely specified triangles at its J corner. Each thin reconstructed rhomb is exactly one such group. Every piece belongs to exactly one group, so the H6-quad assignment is injective and surjective.

Each P1 has its distinguished quadEFLK. Its thick group contains that quad, the quadKLGH of the uniquely placed P2 sharing its c edge with K matched toK andL matched toL, and the specified triangles atK,L. Every thick rhomb is exactly one such group. Distinct P1 groups cannot share a P2 quad because the piece partition in Lemma5 is disjoint. Every P2 quad is assigned to some group, again by that same partition. Thus pairing across the c edge is a bijection between P1 andP2 copies, and both are in bijection with thick rhombs. The source atlas fixes the full edge and endpoints; no assumption about frequencies is used.

Each assigned polygon and rhomb share its distinguished quad. Their diameters are uniformly bounded, so any fixed interior anchors move only a bounded distance. Tiles whose anchors fall in the boundary annulus of fixed width areO(R), by disjoint inscribed-disk packing. Therefore the three window equalities hold. QED.

This is a new count proof from the later reviewed piece grouping. It does not retrospectively certify the older marking-graph Euler hypotheses or its pending rereview.

## Lemma2: the marked source hierarchy forces the irrational ratio

For every legal marked-rhomb tiling in reviewed Lemma6,

    T(R)-phi*t(R)=o(R^2),
    T(R)/t(R) -> phi,

where phi=(1+sqrt5)/2. Consequently, for every generic source Ammann tiling,

    p1(R)/h(R) -> phi,
    p2(R)/h(R) -> phi,
    p1(R)/p2(R) ->1.

No existence of separate absolute densities is assumed or needed.

Proof. Split each thin rhomb into its two marked red Robinson halves and each thick rhomb into two blue halves, as specified in the reviewed composition proof. The two exact deflation rules are

    red -> one red + one blue,
    blue -> one red + two blue.

Thus the child-count matrix, with rows(red,blue) and columns(parentred,parentblue), is

    M=[[1,1],[1,2]].

The row vector q=(-phi,1) satisfies qM=phi^(-2)q; equivalently phi^(-2)=2-phi. Reviewed Lemma6 supplies a legal composition at every scalephi^k, whose repeated deflation partitions the original half tiles into the M^k children of its half tiles.

Fix k and count the complete scalephi^k parent halves lying within the square. Let n_k=(a_k,b_k) be their count vector. Every original half sufficiently far from the square boundary belongs to one of these parents. Since parent diameters areO(phi^k), the unassigned original half tiles lie in an annulus of thicknessO(phi^k). For fixed k, their count isO_k(R). Hence the original half-count vector c(R) satisfies

    c(R)=M^k*n_k+O_k(R),
    q*c(R)=phi^(-2k)*q*n_k+O_k(R).

Each parent half has area at least a0*phi^(2k), where a0>0 is the minimum unit-half area. The disjoint complete parents lie in the square, so a_k+b_k <= R^2/(a0*phi^(2k)). Therefore

    abs(q*c(R)) <= C*phi^(-4k)*R^2+O_k(R),

with C independent ofk. Divide byR^2 and letR tend to infinity withk fixed; the limsup is at most C*phi^(-4k). Then letk tend to infinity. This proves q*c(R)=o(R^2).

The counts of red/blue halves differ from2t(R),2T(R) respectively byO(R), by bounded displacement inside their source rhombs. Thus T(R)-phi*t(R)=o(R^2). Also t(R)+T(R)=Theta(R^2), since the source rhombs have two fixed positive areas and cover the plane. Substituting T=phi*t+o(R^2) yields t(R)=Theta(R^2), justifying division and the ratio limit. Lemma1 transfers that ratio to h,p1,p2. QED.

## Theorem: no fixed-content fusion with one untouched pentagon class

Suppose a generic Ammann source tiling is partitioned into final tiles of two congruence classes as follows:

1. A final tile of the first class is a single untouched P1 (alternativelyP2).
2. Every final tile of the second class is the union of a finite cluster of whole source tiles. Its source content is the same integer vector u=(uH,u1,u2) for every cluster copy, including reflected or rotated copies.
3. There is a uniform bound on the cluster diameter; all source tiles are used exactly once. No cuts, overlaps or uncovered source tiles are allowed.

Then no such partition exists. Convexity and the number of sides of the fused cluster do not matter. In particular, raising the proposed partner from a hexagon to a9-gon or higher does not repair this fixed-content mechanism.

Proof for singletonP1. Let m(R) count second-class cluster anchors. Bounded displacement within each fixed finite cluster and inscribed-disk packing give

    h(R)=uH*m(R)+O(R),
    p2(R)=u2*m(R)+O(R).

The two source species H6 andP2 have positive quadratic counts by Lemmas1,2. Therefore uH,u2 are both positive; if one were zero, the corresponding source species could not be covered. The same equalities imply m(R)=Theta(R^2), and hence

    p2(R)/h(R) -> u2/uH in Q.

Lemma2 gives the limit phi, which is irrational. Contradiction. The singletonP2 case interchanges p1,p2. The vector may contain additional P1 copies inside clusters; that does not change the omitted-species contradiction. QED.

An equivalent finite-rational formulation is u2=phi*uH: no positive integer solution exists because phi is irrational. This excludes every choice of fixed finite source content at once; no patch or fusion enumeration is necessary.

## Stronger necessary condition for any two fixed-content classes

Suppose both final congruence classes have fixed whole-source content vectors u,v in Z_(>=0)^3, with bounded displacement and exact partition as above. Then u,v must be linearly independent and each must contain equally many P1 andP2 tiles:

    u1=u2, v1=v2.

Proof. Window counts satisfy c(R)=u*m(R)+v*n(R)+O(R). Choose any nonzero rational row vector a annihilating u andv; one exists because there are only two vectors in Q^3. Divide a*c(R)=O(R) by h(R)=Theta(R^2) and use the exact source ratios. This gives

    aH+phi*(a1+a2)=0.

Irrationality forces aH=0 and a1+a2=0. Thus every rational vector in the annihilator lies in the one-dimensional span of(0,1,-1). The annihilator cannot have dimension2, so u,v have rank2; its one-dimensional annihilator is exactly that span. Consequently both u,v are annihilated by(0,1,-1), proving the equal-count statements. QED.

This condition does not assert that balanced clusters exist geometrically, are convex, have the same prescribed shape across the source, or force aperiodicity. It adds a design requirement: a fixed-content two-class compiler must put equal P1/P2 counts in **each** class, and have two independent content vectors whose nonnegative cone contains the limiting source vector(1,phi,phi). An untouched singleton pentagon fails this requirement immediately.

## Exact limits and material reopening hypotheses

This is not an exclusion of arbitrary two convex polygons or all Ammann-based compilers. In particular it does not exclude:

* the same final congruence class having two or more different source-content vectors;
* clusters with cuts or transfers of fractions of source tiles;
* a first final shape that is itself a nontrivial cluster;
* a different source decoration, nongeneric J outside the reviewed forcing domain, or absence of global Ammann decoding.

Congruence of final cluster shapes alone does **not** establish fixed content. A single convex shape might admit different dissections by source tiles; proving impossibility of that coincidence would be a separate obligation. A genuinely changed variable-content proposal must give at least two exact source clusters, congruent as unmarked shapes, whose omitted-species content ratios can support the irrational source ratio. The present theorem allows reflected copies because reflection preserves the integer source-content vector. It does not supply unrestricted forcing for either final shape.

No new enumeration or geometric cluster construction was run for this theorem. Its proof-relevant finite arithmetic is just the2x2 child matrix and the exact anchor bijections already stated in the reviewed reconstruction. Fresh hostile review must inspect those bijections, the two-limit window argument and the fixed-content quantifiers before this result is used as reviewed coverage.
