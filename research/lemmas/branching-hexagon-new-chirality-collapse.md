# Chirality branching forces a monohedral escape in a fixed repeated-side family

**Status:** freshly independently hostile-reviewed **VALID**, with a no-author-import algebraic checker; see [review](../reviews/branching-hexagon-new-chirality-collapse-review.md). No novelty claim. This is a restriction on a given second hexagon, not a selected-partner construction and not a classification of arbitrary repeated-side pairs.

## Family and statement

Let A be a genuine convex hexagon with threefold rotational symmetry, alternating side lengths p,q with p!=q, and alternating interior angles

    alpha_plus=120+delta, alpha_minus=120-delta,
    0<delta<60 degrees.

Choose its indexing so its side0 has length p and corner0 has angle alpha_plus. Such an A is given by directed edges of length p in directions 0,120,240, interleaved with edges of length q in directions 60+delta,180+delta,300+delta. Each three-edge orbit sums to zero. A is chiral: a reflection of its unequal-length triangle orbits could preserve both only if their relative direction parameter were a multiple of 60 degrees, excluded by 0<delta<60.

Let B be any genuine convex hexagon whose native numerical side word is

    (r,p,q,q,q,q),       r,p,q pairwise distinct.          (1)

Its angles are beta0,...,beta5. Its three qq corners are exactly corners3,4,5.

**Branch-collapse theorem.** If a fixed A p-side has both an orientation-preserving A mate and an orientation-reversing A mate, each with trivalent full-edge corner fillers at both seam endpoints from A,B, then B admits a doubly periodic monohedral plane tiling. Consequently such two-ended chirality branching cannot encode strong aperiodicity in this family.

The premise requires only both endpoint stars; the conclusion therefore applies in particular to two compatible whole-tile patches or two plane extensions. No implication from a local patch to an infinite extension is used.

## Direct branch proof

Threefold rotations identify the three p slots intrinsically. There are precisely two possible physical A mates along a fixed p segment, one for each orientation sign. A has no reflection symmetry under the stated hypotheses, so these two mates are intrinsically distinct.

Across an orientation-preserving seam, endpoint reversal pairs alpha_plus with alpha_minus at each end. The third angle must therefore be 120. Across the orientation-reversing seam, one endpoint has two alpha_plus corners and the other has two alpha_minus corners. Their third angles must be 120-2delta and 120+2delta.

At every such seam endpoint, the two remaining ray lengths are q,q. A has no qq corner. Hence each third corner is one of B corners3,4,5. The three required angle values are distinct because delta>0. Thus

    {beta3,beta4,beta5}={120-2delta,120,120+2delta}.

In particular beta3+beta4+beta5=360. Strict convexity also forces delta<30, since 120+2delta<180.

The direction turn from B edge2 to B edge5 is

    (180-beta3)+(180-beta4)+(180-beta5)=180.

These two opposite edges have the same length q, so their directed vectors are negatives. The following direct two-face construction proves the promised monohedral periodic tiling without importing a monohedral classification.

## Direct periodic witness from equal parallel opposite sides

Write the six B vertices V0,...,V5, with V0=0. Put x=V1, u=V2 and w=V3-V2. The equality of opposite directed edges E2=-E5 gives V5=w and V3=u+w. Set

    v=V3+V4-V1.

Use the two counterclockwise faces

    face0=B, face1=x-B.

Pair the following sides, reversing boundary endpoints; translations are added to the second face:

| First face,side | Second face,side | Translation |
| --- | --- | --- |
| 0,0 | 1,0 | 0 |
| 0,1 | 1,1 | u |
| 0,3 | 1,3 | v |
| 0,4 | 1,4 | v-u |
| 0,2 | 0,5 | u |
| 1,2 | 1,5 | -u |

The identities V5=w, V3=u+w prove all twelve endpoint equations directly. The four true circular corner links are

    (0,0),(1,1),(0,2); (0,1),(1,2),(1,0);
    (0,3),(1,4),(0,5); (0,4),(1,5),(1,3).

Each link has three angles totaling 360: the last two use beta3+beta4+beta5=360 and the first two use beta0+beta1+beta2=360, following from the hexagon total720. This connected orientable closed surface has V=4,E=6,F=2 and is a flat torus. Its complete simply connected flat universal cover develops globally into the plane. The lifted whole B faces consequently tile the plane with disjoint interiors. The seam shifts provide periods u,v, which satisfy

    det(u,v)=2 area(B)>0.

The determinant identity follows by expanding the shoelace area using V3=V2+V5. Both periods are therefore independent. This is an infinite periodic witness, not a finite-patch extrapolation.

## Further fixed-B rigidity if there is no monohedral escape

Suppose a trivalent edge-to-edge A,B plane tiling exists and

    beta3+beta4+beta5 != 360.                            (2)

This is a necessary restriction for an aperiodic pair by the preceding explicit monohedral witness. Then every such tiling satisfies the following two-ended contact implications:

1. Every r side pairs with another B's unique r side by the orientation-preserving half-turn. The reflected mate would put two rp corners at one endpoint and would require a nonexistent pp corner. Thus reflected r matching is impossible.
2. At both endpoints of that r seam, the third corner is A, with the same angle

       kappa=360-beta0-beta1 in {alpha_plus,alpha_minus}.

   The only available pq third corners are A and B corner2. If B corner2 filled even one such endpoint, beta0+beta1+beta2=360 would force beta3+beta4+beta5=360, contradicting (2).
3. Every B p side meets A. The reflected B/B p mate requires an rr corner at one endpoint, which does not exist. The orientation-preserving B/B p mate has an rp and a pq corner at each endpoint; its required rq corner is B corner0. Again their angle sum would force the excluded loop-angle sum360.
4. Every B q side5 meets A. At its rq endpoint, a B mate corner pq would require the B rp corner and force beta0+beta1+beta2=360. A B mate corner qq would require a second B rq corner, producing two corner0 sectors along the r seam, contrary to implication1. A B mate corner rq would require a nonexistent rr corner. These exhaust all possible B corners incident to a q side.

Consequently both A placements around the unique r dimer are determined physically, modulo A's intrinsic threefold rotations: their r-seam third angle is fixed kappa, which fixes which chirality of the alternating-length A can meet the adjacent p,q rays. This is a geometric transport restriction on a given B.

It leaves q-side2/3/4 contacts and A's other p contacts unclassified. It does not prove that these forced r dimers yield a hierarchy, infinite tilability, or a common period. Applying it to unrestricted original tilings uses the independently reviewed [defect-free hexagon limit theorem](hexagon-limit-and-periodicity.md); the implications describe that admitted edge-to-edge limit and do not silently impose a contact rule on every original tiling.

## Exact killed candidate with whole-tile chirality branches

Here delta=15 degrees, p=1/2,q=1. Let h2=sqrt(2)>0,h3=sqrt(3)>0 and put

    c75=h2(h3-1)/4, s75=h2(h3+1)/4.

The directed A edges are

    (1/2,0), (c75,s75), (-1/4,h3/4),
    (-s75,-c75), (-1/4,-h3/4), (h2/2,-h2/2).

The B edges are

    (-1/4-h3/2,-3/2+h3/4), (1/4,-h3/4), (1,0),
    (h3/2,1/2), (0,1), (-1,0).

They give r^2=13/4-h3/2, p^2=1/4, q^2=1. Every coordinate lies in Q(sqrt2,sqrt3). Exact primitive defining data are g=sqrt2+sqrt3, g^4-10g^2+1=0, 31/10<g<16/5, with h2=(g-1/g)/2 and h3=(g+1/g)/2.

B corners3,4,5 have angles150,120,90. Set a0=(1/2,0), and let R_phi be rotation by phi degrees. The two four-tile whole patches, with B_j its native vertices, are

    rotation mate: A, a0-A, R45(B-B4), a0+R225(B-B4);
    reflection mate: A, S(A), Rminus45(B-B5),
                    a0+R255(B-B3),   S(x,y)=(x,-y).

All five contacts in either patch are full native sides and all six unordered tile pairs have disjoint interiors. At the left endpoint the respective filler cones are [135,255] and [135,225], lying in x<=0. At the right endpoint they are [315,435] and [285,435], lying in x>=1/2. The A and mate sectors fill the complementary angles, so convexity separates every other pair. Thus the branch premise is exhibited by actual complete tiles, not merely numerical stars.

Nevertheless B tiles alone, with two-face periods

    u=(-h3/2,-3/2), v=(9/4,-1-h3/4),
    det(u,v)=15/4+h3/2=2 area(B)>0.

This exact candidate fails the universal-aperiodicity gate through a geometric branch-collapse mechanism.

## Replay and scope

[Producer](../searches/branching-hexagon-new-chirality-collapse.py), [certificate](../certificates/branching-hexagon-new-chirality-collapse.json), [computation record](../searches/branching-hexagon-new-chirality-collapse.md).

    conda run --no-capture-output -n arisearch python research/searches/branching-hexagon-new-chirality-collapse.py

The producer verifies closure, strict convexity, ten full branch contacts and twelve complete branch separations. It then checks six two-face seams, all four actual circular links, the area/covolume identity and sixteen complete candidate lattice comparisons from exact transformed bounding boxes. Arithmetic is exact in the specified real algebraic field. No bounded failure-to-find claim is involved. Independent hostile review and the exact checker return VALID/PASS.

The exact remaining constructive issue is whether the forced r dimers under (2), together with the unclassified q2/q3/q4 and A-p contacts, can force an infinite hierarchy or admit a periodic assembly. No existing argument establishes either. New branch information or a transport invariant is needed; larger patches alone do not resolve this obligation.


The later independently reviewed [complete fixed-B classification](branching-hexagon-new-fixed-b-classification.md)
closes every angular resonance for this same side-word family using a proved
saturated limit and native incidence parity. The earlier gap descriptions
above record the scope of this lemma; they are superseded within that family.
