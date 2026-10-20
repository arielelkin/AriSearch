# Seven signed-star supports: nonresonance and three entire periodic support families

Date: 2026-10-19. Status: proved with exact computation and [independently Sol-reviewed](../reviews/hexagon-five-four-nonresonant-support-sol-review-2026-10-19.md), including the universal three-support periodic escape. This is a restricted-family result, not a resolution of the two-convex-tile problem.

## Domain and dependencies

Use A=(0,1,2,0,3,4), B=(0,1,1,0,2,3), and the reviewed signed-star atlas reconstructed by `hexagon-five-four-forced-dimer-2026-10-19.py`. The seven minimal masks retained by the earlier support gate are 33416,41032,1118212,2625540,20774,22550,3543044. The present work takes that seven-mask list as input; it does not independently certify the earlier 2^22 enumeration. Handedness does not affect an interior-angle equation. All angles below are in units of pi.

For each mask impose its retained trivalent-star sums (each 2) and both native polygon totals (each 4). The certificate records the exact augmented rational echelon forms. Affine dimensions in mask order are 7,7,8,8,6,6,8.

## Complete resonance test and positivity domain

Each support contains e=(2/3,...,2/3). Hence no resonance equation n dot alpha=1, for any nonzero n in N^12, is an identity on any support: evaluating at e would give 2 sum(n)/3=1, impossible for an integer sum(n). This proves the identity claim over **all finite multisets**, without imposing an unjustified uniform cardinality bound over the entire positive cone.

For an explicit finite domain take the compact relative slice K=F intersect [3/5,4/5]^12 of each affine support F. It contains e in its relative interior. The positive lower bound is 3/5. Any multiset summing to 1 has cardinality at most floor(5/3)=1. The exhaustive twelve singleton candidates are recorded; each is impossible since its angle is at most 4/5. Thus the pi-sum multiset list is empty throughout K. In particular F intersect (3/5,4/5)^12 is a nonempty relatively open nonresonant domain. This is not asserted to exhaust possible resonance multisets outside K. The all-finite identity test above does apply to the whole affine support.

Formal angle feasibility alone supplies no polygon closure. The following construction separately supplies exact common-length closure on three of the seven supports. Its all-obtuse angles need not belong to the smaller compact slice K; obtuseness independently excludes pi sums.

## One exact common-length metric

Take five distinct lengths

    l0=2, l1=1, l2=101/100, l3=51/50, l4=103/100.

Let D=sqrt(3). For positive a,b define

    y(a,b)=(3+a^2-b^2)/(2D),
    h(a,b)=sqrt(a^2-y(a,b)^2),

with the positive radical. For either native length word (s0,...,s5), set

    (ht,yt)=(h(s1,s2),y(s1,s2)),
    (hb,yb)=(h(s5,s4),y(s5,s4)).

The vertices in counterclockwise order are

    (-s0,0), (0,0), (ht,yt), (0,D), (-s0,D), (-s0-hb,yb).

Since s3=s0 in both words, the six side lengths are exactly their required native values, including the repeated l1 in B. Algebraic real arithmetic verifies all side squares, strict halfplane inequalities for every directed side and every nonincident vertex, and negative scalar products of the two inward rays at every corner. Consequently both polygons are simple strictly convex, have positive area, and all twelve genuine angles lie strictly between pi/2 and pi. Any two angles exceed pi, and a singleton is less than pi, so no finite nonempty angle multiset sums to pi. The Sol-reviewed angle-nonresonance theorem therefore applies to this exact pair.

Sides 0 and 3 are equal and oppositely directed. Convexity implies the first three exterior turns sum pi, as do the final three; thus each corresponding interior-angle triple sums 2pi. Exact augmented-row containment verifies that these four block equations imply every star equation of masks 1118212,2625540,3543044. In each of these three cases the support augmented rank, block augmented rank, and stacked augmented rank are all 4. Consequently the affine support space equals the four-block equation space, in both directions. No claim is made that all formal retained stars embed or occur in an actual tiling.

## Explicit two-copy monohedral periodic tiling

This argument applies separately to each constructed hexagon P. Let v=(0,D), cR=midpoint(side1), cL=midpoint(side4), and H_R(x)=2cR-x, H_L(x)=2cL-x. Set w=2(cR-cL). Its horizontal coordinate is 2s0+ht+hb>0, so v,w are independent.

The translates P+n v, n in Z, form a vertical strip S. To see this directly, both lateral two-edge chains are graphs x=L(y),x=R(y), periodic in y with period D: their intermediate vertex heights lie strictly between 0 and D. At every height L(y)<=-s0<0<=R(y), and convexity says the horizontal section of P is exactly the interval between the two chains. Horizontal sides at successive periods coincide, so the strip is covered without interior overlap.

Any periodic two-edge chain is invariant under halfturn about the midpoint of either one of its edge types. Indeed if its successive edge vectors are u,t,u,t,..., reflection in the midpoint of a u edge maps its two endpoint vertices to each other, and the next vertices to their neighbors in reverse order, modulo period u+t. The exact producer verifies this vertex permutation modulo v for both chains. Consequently H_R fixes the right strip boundary as a set and H_L fixes the left boundary. H_R(S) lies directly to the right of S and shares precisely its right boundary. Since H_R H_L is translation by w, the strip S+w lies directly to the right of H_R(S), sharing the image of the left boundary of S. Thus

    S+n w, H_R(S)+n w, n in Z

are successive strips with pairwise disjoint interiors. Their boundaries are periodic graphs with bounded horizontal coordinate before translation; since w_x>0 they tend to both horizontal infinities as n tends to plus/minus infinity. They cover the plane. Expanding each strip into P+n v proves a monohedral tiling with lattice generated by v,w and representatives P,H_R(P). Rotations by pi are allowed by the target; no reflection restriction is used.

As an additional exact consistency check, det(w,v)=2 area(P), and both chain midpoint symmetries are checked algebraically. Area agreement is not used as a substitute for the strip coverage proof. The two shapes are distinct congruence classes because their side multisets differ. Either monohedral tiling already disproves aperiodicity of this particular pair, regardless of mixed tilings.

## Universal periodic omission on the three block-angle supports

**Conditional theorem.** For any of masks 1118212,2625540,3543044, let A,B be any strictly convex polygons with the specified native length words, whose labelled angles satisfy that support's equations. Then each polygon separately admits a two-orbit monohedral periodic tiling. Thus every such pair has a periodic escape, independently of distinctness of lengths, angle nonresonance, actual star realization, or existence of a favored mixed tiling.

Here the angle at index j is the corner between native sides j and j+1, consistently with the source atlas. Since the support space equals the four-block space, the first three interior angles of either polygon sum 2pi. The corresponding three exterior turns sum pi, so side3 is antiparallel to side0. Both words assign the same length to sides0 and3. Hence if the counterclockwise vertices are P0,...,P5, we have

    P4-P3=-(P1-P0), v=P3-P1=P4-P0.

Rotate and translate so P0=(-a,0),P1=(0,0), with a>0. Strict convexity and antiparallelism imply that side1 and side2 have directions strictly between 0 and pi, and side4 and side5 have directions strictly between pi and 2pi. This follows because every exterior turn is strictly positive and the total turn from side0 to side3 is exactly pi. Thus sides1,2 strictly increase height, sides4,5 strictly decrease it, and D=v_y>0. In particular both lateral two-edge chains are graphs over height.

For the geometric proof only, apply the invertible shear (x,y) -> (x-v_x*y/D,y). This makes v=(0,D), leaves side0 horizontal, preserves convexity and tilings, and conjugates every halfturn to a halfturn. It is only an analysis of the already fixed isometric copies; no affine images are introduced as permitted physical tile placements. In these coordinates P3=(0,D),P4=(-a,D). Strict convexity puts P2 strictly to the right of chord P1P3, and P5 strictly to the left of chord P0P4. Consequently the strip boundaries obey L(y)<=-a<0<=R(y), with their intermediate heights strictly between 0 and D. The vertical-strip construction in the preceding section now applies verbatim.

More explicitly let cR=(P1+P2)/2,cL=(P4+P5)/2 and w=2(cR-cL). Writing P2_x=hR>0 and P5_x=-a-hL with hL>0 gives w_x=2a+hR+hL>0. Each chain is invariant under the halfturn about its chosen side midpoint, because its two successive edge vectors repeat with period v. The strips S+n w,H_R(S)+n w are consecutive and exhaust the plane, since their boundary graphs remain bounded before translation and w_x>0. Expanding S into P+n v gives the same two-orbit lattice tiling. Undoing the shear sends v,w to independent lattice vectors and each translated/halfturned tile to precisely the corresponding translated/halfturned copy of the original P. Hence the resulting tiling uses allowed isometries of the original polygon.

This proves the theorem for every strictly convex metric in these three affine support families. Additional angle equations from larger supports do not invalidate the implication: any metric satisfying a support containing one of these three minimal supports still belongs to the corresponding block-angle family and has the periodic omission. The theorem does not assert that every affine angle point has polygon closure, and does not require it.

## Reproducibility and remaining scope

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-five-four-nonresonant-support-2026-10-19.py

Producer and certificate share this basename under `research/searches/` and `research/certificates/`. The command passed. The producer uses exact Sage algebraic reals; displayed decimal coordinates are diagnostic, while the radical recipe and rational lengths define the exact polygons. No numerical solver, increased timeout, or angle grid was used.

This closes the requested nonresonance identity question for all seven supports and eliminates the entire strictly convex metric families of masks 1118212,2625540,3543044 from aperiodic-pair consideration by conditional monohedral periodic omission. The exact witness illustrates that these families are nonempty. The four other minimal-support metric gates remain unresolved. No claim is made concerning their external neighbor identities, geometric local-star realizability, propagation, or unrestricted plane tilings; the overall two-convex-tile problem remains unresolved.
