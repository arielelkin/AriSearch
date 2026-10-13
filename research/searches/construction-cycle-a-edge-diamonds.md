# Track A: barycenter edge diamonds, with one pentagonal-kink repair

Date: 2026-10-13. Status: completed and independently reviewed; aperiodic construction falsified. Finite question fixed before computation. Original unrestricted definitions retained; B5+1 remains closed and paused.

## Finite question and exact proposal

Use the already reviewed infinite edge-to-edge H/P1/P2 source at J=1/2+(4/5)w, w=exp(i*pi/5), and its paired H/D precursor. For every original source face F, put c_F equal to the arithmetic mean of its native vertices. For every full original source edge e=[p,q] shared by F,G, replace the two source fan triangles conv(p,q,c_F), conv(p,q,c_G) with their union Q_e, with cyclic boundary (p,c_F,q,c_G), ordered positively. This rule restores the original P1/P2 c seam inside D. Every H/P1 or H/P2 diamond crosses an old H/D macro boundary. This is the sole initial surgery.

Finite question fixed BEFORE arithmetic: can complete edge diamonds have at least five genuine corners and survive omission, and can the sole proposed kink repair remove the corner-count failure while keeping both adjacent faces convex? No congruence search or environment sweep is authorized after failure of this topology gate. Exact evidence domain is ONE required H/P1 seam in the K-type H-J' star at the fixed J sample, its two fan triangles, and ONE kink on its J'-to-H-centroid boundary. Evidence arithmetic certifies local signs, area reassignment, and a periodic omission carrier only. It does not enumerate an entire source atlas or claim a two-shape collapse.

## Coordinates and the required branching star

J'=1+w^4(J-1), J''=w+w^6(J-w), K=w^2+w^6(J-1), L=1+w^7(J-1-w), J2=1+w+w^2-J.
H=(0,J',1,J,w,J''), P1=(0,J',1,L,K), P2=(K,L,1+w^2,J2,w^2).
At the required K star, H native corner J' meets P1-K and P2-K. The side H 0--J' has length a, so it meets P1 side K--0, whose length is a, while H J'--1 has length b and meets P2. In the explicit seam placement H stays in its reference coordinates and P1 is rotated/translated by g(z)=u*z, where u=J'/K; thus g(K)=J', g(0)=0. The exact evidence checks |u|=1, and opposite source interiors. No choice enumeration is performed.

At J' the three original source edges separating H,P1,P2 become three edge diamonds, bounded pairwise by spokes to the respective source centroids. Thus the macro degree-two J' becomes a degree-three final boundary vertex. At a source centroid c_F the diamond subdivision has degree equal to the native side count of F. Each complete Q_e has four listed vertices at most. New source-edge-crossing faces AND restored branching distinguish this from incidence-preserving convexification.

## Infinite covering gate, separated from convexity/classes

Every arithmetic mean of the vertices of a strictly convex positive-area polygon is strictly interior (each supporting inequality averages strictly positive values from off-edge vertices). Its fan triangles partition that polygon with disjoint interiors. Adjacent source faces assign exactly one triangle to each common full source edge, so pairing triangles yields bounded simple quadrilateral supports with disjoint interiors whose union is the entire plane. Their boundaries may be nonconvex. Boundedness is uniform since each support is contained in the union of two source tiles of uniformly bounded diameter. The construction is isometry-equivariant, including reflections, and requires no infinite patch extrapolation. Its compatibility domain is every full edge of the existing edge-to-edge source, without any larger-neighborhood hypothesis: the same two fan triangles are assigned by the two incident cells, so there is no conflict between neighboring operations. The radius of the rule is bounded by two source diameters. It uses the proved source existence, full-edge pairing and source convexity. It establishes an infinite finite-prototile polygonal covering, NOT an infinite two-convex-shape covering: complete convexity and exactly two congruence classes are separate unproved gates. Finiteness of possible supports follows from finite source sides and two choices of endpoint assignment for isometric gluing.

Every final support has at most four corners. Therefore if the proposed final shapes were all convex and collapsed to exactly two congruence classes, either class would be a triangle or convex quadrilateral and would independently admit a periodic tiling. The two-class construction claim is already falsified conditionally on its required convexity and shape-count gates, regardless of whether those gates themselves pass. This does not assert that the actual whole diamond field is convex.

## Exact omission witness for the audited convex crossed diamond

The fixed arithmetic verifies Q=(A,B,C,D)=(0,g(c_P1),J',c_H) strictly convex. For any positively oriented convex quadrilateral Q, put t1=C-A, t2=D-B and Q*=A+B-Q (a half turn). Use copies Q+Lambda and Q*+Lambda for Lambda=Z*t1+Z*t2. The four edges AB, BC, CD, DA of Q meet reversed edges of Q* shifted respectively by 0,t1,t1+t2,t2. The determinant cross(t1,t2)=2*area(Q)>0. To verify a global cover without pictures, the locally finite multiplicity function has no jump across any edge because every directed boundary segment cancels with its reversed paired segment. Hence it is a constant integer almost everywhere on the connected plane; its average over one lattice cell is (area(Q)+area(Q*))/det(t1,t2)=1. Thus its constant value is one, giving disjoint interiors and full plane coverage. Coincident boundary segments cause no exception since their total oriented jumps cancel, and a finite intersection set does not disconnect the adjacent open cells. The closed supports cover boundary points by local finiteness. Both independent translations t1,t2 are periods. This proof permits half turns (hence uses allowed isometries), does not require the other tile species, and meets the unrestricted omission and single-period attack.

## One specifically justified repair

To remove the <=4 corner escape, change the shared interface U=J' to V=c_H between the diamond on H side0 and the adjacent diamond on H side1 from U--V to U--M--V. Write n=-(w-w.conjugate())*(V-U), an exact right normal, and M=(U+V)/2+epsilon*n with epsilon=1/1000 for the fixed evidence check. Restrict epsilon positively and small enough to keep the new two-segment path within the union of the two incident supports and away from all other boundaries; the exact check will determine whether this fixed value lies in that local domain. For the positively oriented side0 diamond this pushes the edge outward and transfers conv(U,V,M) from the side1 diamond. Their total support and area remain unchanged. No third face is introduced at M.

The repaired covering rule applies this one cap transfer at every H native J' spoke, using the source isometry to transport the reference M (so reflected H copies use the reflected cap). Each cap lies strictly in the H side1 fan triangle apart from its base, as the fixed exact check proves. Distinct H interiors are disjoint, and one cap is selected per H, so cap transfers are globally compatible without gaps or overlaps. The diamond on side0 gains that cap, and the diamond on side1 loses it. Both are H/P seams, so neither diamond receives conflicting requests from a second H. Thus the repair preserves an exact full-plane polygonal covering, but the losing faces are nonconvex. This is a source-generated rule, not an intrinsic decoder.

At M the two positive-area incident faces fill 2pi. If both were convex their sectors would both equal pi, so M would not be a new genuine corner. For any nonzero kink that is convex for the enlarged diamond, its neighbor has the complementary reflex angle. Algebraically the oriented turn of the two boundary paths at M has opposite nonzero signs. This is a local degree-two obstruction applying to every epsilon>0 in the admissible transfer domain. One repair only; no further branching repair or patch enlargement is authorized in this cycle.

## Universal forcing ledger, developed alongside existence

The source-generated field has a forward partition rule, but arbitrary unmarked diamond tilings have no proved intrinsic inverse. Reflections are admitted in the rule and periodic omission construction. Partial contacts are not prohibited by the final shapes; the source full-edge seam property cannot be imported into arbitrary final tilings. Omission already kills any convex two-class realization. A decoder would have to recover source centroids/vertices, distinguish original P1/P2 c seams from other edges, prove globally compatible source reconstruction for every final tiling including partial contacts, and be translation-equivariant. It is presently absent. Even a successful selected-source resection would therefore not prove aperiodicity. The periodic omission carrier above has two independent nonzero periods, so it also defeats the weaker demand to exclude a single-direction period.

## Stop decision and concrete obligation

Stop this surgery after the one kink repair. Preserve the exact four-corner obstruction and the degree-two kink obstruction. A restart requires a concrete resection whose complete faces all have at least five corners and whose attempted corner additions coincide with actual branching vertices, together with a finite complete incidence atlas; changing epsilon or searching centroid positions cannot change either obstruction. No novelty claim is made.

Dependencies: reviewed source Lemmas 7 and 5 converse in ammann-forcing-aperiodicity.md, native sides and required K star in ammann-hd-incidence-preserving-convexification-obstruction.md. Exact computational evidence is retained below; [independent hostile review](../reviews/construction-cycle-a-hostile-review.md) validates the scoped covering, obstruction and corrected sole repair.

## Evidence and replay

Producer [construction-cycle-a-edge-diamonds.py](construction-cycle-a-edge-diamonds.py) retains the finite ONE-seam/ONE-kink domain; [certificate](../certificates/construction-cycle-a-edge-diamonds.json). Replay without changing retained evidence:

```text
mise exec -- conda run --no-capture-output -n arisearch python research/searches/construction-cycle-a-edge-diamonds.py
```

The fixed kink epsilon passes strict containment in the neighboring H fan triangle, makes Q a strict convex pentagon, and produces a negative local turn at M in the adjacent diamond. Exact area reassignment passes. This certifies a genuine local pentagonal repair failure, not failure inferred from numerical rendering. No centroid, parameter, seam or size domain was enlarged.
