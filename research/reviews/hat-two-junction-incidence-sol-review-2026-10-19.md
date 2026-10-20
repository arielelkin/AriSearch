# Independent Sol hostile review: Hat two-junction incidence gate

Date: 2026-10-19

Verdict: FAIL for the written domain: flat corners at reflex boundary leaves are omitted. The tree classification and junction-only arithmetic pass, but the claim of exhaustive 32-case enumeration and the forced interior T junction do not follow. The four reported survivors are abstract signatures, not geometric dissections.

## Material inspected and independent check

Reviewed `research/searches/hat-two-junction-incidence-gate-2026-10-19.md`, its `.py` producer, `research/certificates/hat-two-junction-incidence-gate-2026-10-19.json`, and the exact `hat_outline` in `research/certificates/hat-eight-kite-convex-cluster-gate.json`.

Ran a separate Python verifier without importing the producer or overwriting its certificate. It parsed the outline using Fraction arithmetic, representing each coordinate as `(x, y/sqrt(3))`; this positive linear rescaling preserves orientation. Exact signed area and turns confirm that every outline vertex is nonflat and that the reflex indices are precisely 0,4,8,11. Their successive edge distances are 4,4,3,2. A separately constructed adjacency graph and recursive leaf-to-leaf paths recover junction/sector incidences, nominal counts, and every recorded survivor. Result: PASS, 32 signatures, survivor totals 4 and 0.

## Attempts to break completeness and counting

With four leaves and exactly two degree-three interior vertices, a tree has six vertices and five edges. The interior vertices must be joined, each carrying two leaves. The three abstract leaf bipartitions are 01|23, 02|13, and 30|12. In a disk with the prescribed cyclic boundary order, 02|13 would provide vertex-disjoint paths joining alternating boundary endpoints, which cannot coexist without crossing. The remaining two are the complete planar possibilities; exchanging names of interior vertices adds no case.

The embedded tree cuts the disk into four faces, one per open boundary arc between adjacent leaves. Each face boundary is that arc plus the unique tree path. Thus an arc with b edges has b plus path-length nominal sides. The graph-path calculation independently gives (6,7,5,5) and (7,6,6,4). It also confirms that each interior junction belongs to three distinct faces, so choosing its flat face is unambiguous.

At an uncut original convex vertex, its original angle remains strictly below pi. However, at a reflex leaf the two sector angles sum to an original angle alpha strictly between pi and 2pi. Convexity allows the split pi and alpha-pi. Deleting the flat corner leaves a convex polygon exactly as the written domain requires. The claim that both split angles must be strictly below pi is false.

This is a concrete local issue for the exact outline: vertex 8 is (3,0), with incident vertices 7=(4,0) and 9=(3,sqrt(3)). Its interior angle is 3pi/2. A spoke initially directed left from vertex 8 is the inward extension of edge 7--8 and splits the interior into pi and pi/2. The flat angle lies in boundary-arc sector 1, joining vertices 4 and 8. A sufficiently short such spoke is inside the Hat and has no boundary overlap. This local observation does not construct the full two-junction dissection.

## Minimal corrected finite domain and consequences

Keep the two planar trees and the four choices at each interior junction. At each boundary leaf i, additionally choose no flat, flat in sector i-1 modulo 4, or flat in sector i. A reflex angle below 2pi permits at most one flat split at a leaf. Subtract one side in the selected sector for each flat junction or flat boundary leaf. This gives 2 * 4^2 * 3^4 = 2592 abstract signatures before side-count filtering. These remain necessary cases only, because correlated directions and all geometric constraints are untested.

I ran this small expanded arithmetic enumeration independently: 32 passing signatures for 01|23 and zero for 30|12. Ten of the 32 have no flat interior junction in sector 1. For example, choose no interior flats and only leaf 2 (original vertex 8) flat in sector 1; nominal (6,7,5,5) becomes (6,6,5,5). This is a side-incidence counterexample to the claimed forced interior flat, not a geometric witness.

Pairing 30|12 remains impossible by this necessary count because its fourth sector starts with four sides and flat removal cannot increase it. Pairing 01|23 must still lose at least one nominal corner from sector 1, but that loss may occur at either endpoint leaf as well as at either interior junction. The present producer cannot certify which mechanism occurs.

No claim about geometric realizability, tile congruence classes, source extension, intrinsic decoding, plane existence, or aperiodicity is established or refuted by this review. A corrected report must enumerate boundary flats or explicitly narrow its domain to forbid them.
