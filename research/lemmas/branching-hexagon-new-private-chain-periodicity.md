# Fixed-B private-chain transport excludes nonresonant qq branching

**Status:** independently hostile-reviewed **VALID after a seam-tangent repair**, with root separately verifying that repair; see [review](../reviews/branching-hexagon-new-private-chain-periodicity-review.md). No novelty claim. This is an every-tiling statement for an explicitly given repeated-side pair, not selected-partner existence.

## Exact hypotheses and conclusion

Let A be a genuine compact strictly convex hexagon with threefold rotational symmetry, alternating side lengths p,q, p!=q, and alternating corner angles

    alpha_plus=120+delta, alpha_minus=120-delta,
    0<delta<60 degrees.

Index its p sides by 0,2,4 and its q sides by 1,3,5, with angle alpha_plus at even corners. One exact model has directed p edges in directions0,120,240 and directed q edges in directions60+delta,180+delta,300+delta. Reflection copies are allowed.

Let B be any given genuine compact strictly convex hexagon with native side word

    (r,p,q,q,q,q),  r,p,q pairwise distinct.             (1)

Write its vertices V0,...,V5, V0=0, its angles beta0,...,beta5, and its corners by incoming/outgoing side lengths:

    corner0=rq, corner1=rp, corner2=pq,
    corners3,4,5=qq.

Assume the exact angular nonresonance condition

    n3*beta3+n4*beta4+n5*beta5 != 360
    for every nonnegative integer n3+n4+n5=3.          (2)

There are precisely ten triples in (2). Thus no three native qq corners of B can form a trivalent vertex. Reflections do not change their angles.

**Theorem.** Every edge-to-edge plane tiling by A,B with three native corners per vertex has a nonzero translation period. The period has length

    L=|V2+V3-V0-V1|>0.                                (3)

Its direction may depend on the tiling. The theorem does not require a finite fundamental cell or assume either tile frequency.

**Unrestricted-pair corollary.** Under these shape hypotheses the pair either admits no unrestricted plane tiling or admits a tiling with a nonzero translation period. This uses the independently reviewed defect-free hexagon limit theorem; it does not assert every original tiling is edge-to-edge.

**Every-original-tiling corollary.** If every native angle of B is greater than90 degrees, every original A,B tiling has a nonzero translation period. Existence under (2) forces delta<30 below, so every A angle is also greater than90. The reviewed all-obtuse contact theorem then makes every original tiling edge-to-edge and trivalent. If delta>=30, the pair cannot tile under (2).

## Step1: the unique r seam fixes two A placements

Every native r side belongs to B and is side0. Along any full r seam its only possible physical B mates differ by orientation sign. An orientation-reversing mate has two rp corners at one endpoint and requires a third pp corner. Neither A nor B has a pp corner. Therefore every r seam is matched by the orientation-preserving half-turn about its midpoint.

At each endpoint the two B corners are corners0 and1, and the third corner must have lengths pq. Available pq corners are A and B corner2. If the third corner were B2, its angle sum would give

    beta0+beta1+beta2=360.

A hexagon's total is720, so this would imply beta3+beta4+beta5=360, forbidden by (2) with n3=n4=n5=1. Thus the third tile is always A, with the same endpoint angle

    kappa=360-beta0-beta1
           in {alpha_plus,alpha_minus}.              (4)

In particular at B corner0 this A neighbors B across its q side5, while at corner1 it neighbors B across its p side1. Hence both B sides1 and5 meet A, and their actual A placements are unique modulo A's intrinsic threefold rotations. Indeed all native p slots of A and all native q slots are intrinsically equivalent; their two chirality choices exchange alpha_plus and alpha_minus at a selected endpoint. The fixed value kappa chooses one chirality. A has no reflection symmetry under p!=q and0<delta<60, because a reflection preserving its two unequal-length triangle orbits would require their relative direction60+delta to be a multiple of60.

If an entire tiling omitted A, the r-seam argument would already contradict (2). If it omitted B, A's sole corner pair pq cannot form a three-ray triangle when p!=q. Thus every tiling covered by the theorem uses both types. No quantitative frequency assumption is needed.

## Step2: BOTH endpoints force B side2 to match the same native slot

At B corner2, the A neighbor across p side1 has angle

    kappa'=240-kappa,

because the two endpoints of every A p side have opposite alternating angles. The third corner at this vertex has lengths qq. It cannot be A and is therefore a qq corner of another B. Consequently B q side2 meets B, with a qq corner of its mate at the original B corner2.

Every possible q mate slot is exhausted as follows:

* Mate side5 is impossible because every B side5 already meets A by Step1.
* Mate side3 or4 has qq corners at both ends. At the other seam endpoint the original B has corner3=qq and the mate also has a qq corner. Their third corner must also be qq, hence B. This is a forbidden three-B-qq star under (2). This argument permits either orientation sign and checks the second endpoint.
* Mate side2 is possible only with orientation-preserving endpoint reversal. An orientation-reversing side2 mate would put two pq corners at the corner2 endpoint and require a nonexistent pp corner. Its other endpoint would also have two qq corners and require a forbidden three-qq star.

Thus every B side2 pairs with another B's native side2 by the half-turn about the matched side midpoint. Its endpoints have the pairs B2/B3 and B3/B2, completed by A with angle kappa'. The angle equation is

    beta2+beta3+kappa'=360.                            (5)

This is a whole-seam implication, not an inference from a one-ended corner graph.

## Step3: all A neighbors of each B are physically fixed

The side2 seam just established forces B side3 to meet A at its corner3, with angle kappa'. Therefore the placed A across side3 is unique, by the same alternating-angle chirality argument as in Step1.

B side4 also meets A. Its possible B mates on sides2,3,5 are excluded because those slots already pair respectively with2,A,A. A mate on side4 would have qq corners at both endpoints and yield forbidden three-B-qq stars. Thus only A remains.

At B corner4, the known A across side3 has angle kappa, the other endpoint of its q side. Hence the A across side4 has the uniquely specified corner angle

    tau4=360-beta4-kappa.

In an existing tiling tau4 must equal alpha_plus or alpha_minus; that fixes its physical chirality and placement. The analogous angle at corner5 is

    tau5=360-beta5-kappa'.

Both endpoints belong to this same A q-side neighbor, so tau4+tau5=240. Consequently

    beta4+beta5=240.                                   (6)

There are only two possibilities: beta4=beta5=120, or

    beta4=360-2kappa, beta5=360-2kappa'.                 (7)

The first is excluded by (2), since three beta4 corners would sum360. Thus (7) holds, giving beta4,beta5=120-2delta,120+2delta in the order determined by kappa. Strict convexity therefore forces delta<30. Equations(4),(5),(7) are derived local restrictions on the given B, not extra assumptions of the theorem.

We have proved that each B has exactly this neighbor-type pattern:

    sides0,2: B by same-slot half-turn;
    sides1,3,4,5: A, with unique physical placements.   (8)

No A-p contact needs to be classified to establish uniqueness in (8).

## Step4: two half-turn seams form exact straight B chains

Inside a placed B, join the midpoint m0=(V0+V1)/2 of side0 to the midpoint m2=(V2+V3)/2 of side2. The open segment lies strictly in the tile interior: these sides are distinct and nonadjacent in a genuine strictly convex polygon. They have different midpoints, so

    T=2(m2-m0)=V2+V3-V0-V1 != 0.                       (9)

Step1 and Step2 join B tiles through side0 and side2, giving a graph of degree two on all placed B copies. Continue the midpoint segment through either endpoint. The neighboring tile is a half-turn about that endpoint. Its midpoint segment is therefore the straight continuation of the original segment, with the same length |m2-m0|. Repeating in both directions produces an entire Euclidean straight line subdivided into equal-length segments, each lying in one B interior except at seam midpoints.

This argument also rules out finite graph cycles: continuation advances along the straight line by a fixed positive distance at every step. Every graph component is an infinite chain. Two consecutive half-turns translate the B tiles by the physical image of T in (9), so each chain is invariant under that nonzero translation. Reflected B copies have the reflected T, with the same magnitude L.

Distinct B-chain lines cannot intersect. At a proposed intersection the first chain's one incident B tile, or its two incident B tiles when the point is a seam midpoint, occupies a full neighborhood of the point. Choose a nearby point on the second line still in this neighborhood and away from the second chain's discrete seam midpoints. This point lies in the interior of a B tile of the second chain. Its open interior neighborhood meets the interior of at least one of the first chain's incident B tiles, even when the second line lies along their shared seam. Disjoint tile interiors therefore force a shared B tile and hence the same chain. Thus the infinite chain lines are pairwise disjoint, and all are parallel. Their translation vectors consequently agree up to sign, since they all have length L. Choose one physical vector t of length L in their common direction. Every B chain, and hence the entire set of placed B polygons, is invariant under t.

The chain direction argument is Euclidean and unbounded. No bounded patch size, graph canonicalization, compactness or frequency inference is used here.

## Step5: the whole A set inherits the B translation

Every A q side meets B. If two A tiles met along a q seam, both endpoint corners have pq, so the third corner at either endpoint would require pp, which does not occur in either type. Thus an A q edge has a B neighbor. It cannot meet B side2, already paired with2, so it meets one of B sides3,4,5.

Steps1--3 uniquely determine every A neighbor of every B on those sides. Therefore every placed A occurs in the set of physically fixed A neighbors generated from the placed B set. Conversely all those neighbors occur in the given tiling. This identifies the entire A set as an isometry-equivariant function of the B set. Translating B by t consequently translates this A set to itself. The whole polygon tiling has the nonzero period t.

This completes the theorem.

## Passage to unrestricted contacts

The only imported dependency for the unrestricted-pair corollary is the independently reviewed defect-free-limit theorem in [hexagon limits](hexagon-limit-and-periodicity.md): a tileable fixed pair of genuine convex hexagons has an admitted edge-to-edge trivalent limit tiling; either species may disappear. Here disappearance is impossible by the Step1 monohedral exclusions. Apply the theorem just proved to that limit to obtain an admitted periodic tiling. Thus the original unrestricted pair cannot be aperiodic.

The every-original-tiling corollary additionally uses the independently reviewed [all-obtuse contact theorem](obtuse-edge-forcing.md). As delta<30 is necessary for an admitted limit, every angle of A is greater than90. With all B angles greater than90, every original tiling is edge-to-edge and trivalent, so the theorem applies directly.

## What is and is not closed

The theorem closes given-B family(1) under exactly the ten-angle nonresonance inequalities(2), with reflections allowed and no requirement to use both types. It does not assert that every positive metric realizing these angles tiles. It proves a period if a tiling exists.

The first remaining branching cases require at least one legal three-qq B star:

    n3*beta3+n4*beta4+n5*beta5=360,
    n3+n4+n5=3.

The particular resonance beta3+beta4+beta5=360 already yields a direct monohedral periodic escape by [the chirality-collapse theorem](branching-hexagon-new-chirality-collapse.md). Other resonances can allow side2 to pair with side3 or4 and break the fixed straight-chain argument. The forced r dimer still survives when the sum of all three qq angles differs from360, but its q-side continuation is not yet classified. Longer chain words alone do not establish either global forcing or period absence.

Within the locally forced pattern(7), writing beta3=x, the ten qq triples are resonant precisely at x in {120,120-delta,120+delta,120-4delta,120+4delta}. This last finite list is conditional on pattern(7); it is not a classification of the remaining resonant cases where that pattern may fail.

No computational search is needed for the proof. The exact doubled-chirality fixture in [the prior producer](../searches/branching-hexagon-new-chirality-collapse.py) belongs to the resonant, monohedrally periodic family and is not evidence for existence under nonresonance(2). The independent hostile review returns VALID after the recorded seam-tangent repair.


The later independently reviewed [complete fixed-B classification](branching-hexagon-new-fixed-b-classification.md)
closes every angular resonance for this same side-word family using a proved
saturated limit and native incidence parity. The earlier gap descriptions
above record the scope of this lemma; they are superseded within that family.
