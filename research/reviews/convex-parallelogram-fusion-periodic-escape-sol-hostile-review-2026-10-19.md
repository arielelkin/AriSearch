# Independent hostile review: convex parallelogram fusion escape

Date: 2026-10-19. Reviewer: independent delegated agent, not the author.

## Claim and verdict

**Valid**, within the exact restricted scope below. Reviewed `research/lemmas/convex-parallelogram-fusion-periodic-escape-2026-10-19.md`, against `research-problem.md` and `research-protocol.md`.

If each of a finite pair of convex polygons admits a finite dissection into centrally symmetric convex polygons with nonempty interiors, then either the pair does not tile the plane, or one member tiles monohedrally and doubly periodically. Arbitrary orientations, reflections, partial edge contacts, and omission of a species are allowed. No resolution of the unrestricted two-convex-tile problem follows.

## Directional cancellation audit

I attempted to break cancellation using unequal edge subdivisions, T-junctions, point contacts, and multiple atom orientations. None breaks the proof. A finite dissection has a finite segment arrangement; on every positive-length internal elementary segment exactly two atom boundary traces occur, with opposite orientations. At a T-junction subdividing the long edge creates the same cancellation. Isolated points have zero length. Every centrally symmetric atom has equal opposing edge totals in each unoriented direction.

Convexity of the outer polygon is essential: after removing collinear redundant vertices, there can be at most two sides in any unoriented direction. Zero imbalance forces an opposite equal-length mate. Their cyclic order then implies a boundary vector list e_0,...,e_(2m-1) with e_(i+m)=-e_i, and therefore p_i+p_(i+m) is constant. This proves central symmetry without a hidden common-grid or common-orientation hypothesis.

## Infinite clipping and Euler audit

I independently eliminated Euler variables. With N the number of genuine face corners, and b,t,f the stated boundary-extra, interior-straight-sector and other interior vertex counts,

    N=p+2b+2t+3f+X,
    2E=N+p+b+t,
    F=1-(p+b+t+f)+E,
    6F-N=6-p+b+t+2X.

The classification handles partial contacts. An interior vertex has either one straight face sector, with at least two other genuine corners, or no straight sector, with at least three genuine corners. Two straight sectors exhaust the full angle and create no genuine corner: such a redundant valence-two point is omitted. A noncorner boundary vertex contributes at least two genuine corners; a domain corner contributes at least one. These justify X>=0 and the degree formula, rather than merely its algebra.

I specifically tested the apparent grazing loophole. For a generic square, a positive-area tile intersection cannot touch its boundary solely tangentially: such tangency would require a tile vertex on a square side or a collinear tile edge, both excluded. Square corners avoid tile edges. Intersections of zero area are omitted. Thus boundary-cut tiles are controlled by a fixed-width neighborhood of the square boundary. A tile meeting a bounded set has its chosen inscribed disk center within D of that set; disjoint radius-r disks prove local finiteness even without an initial local-finiteness axiom. The same packing gives O(R) boundary tiles. Their total area is O(R), since tile areas have a common finite upper bound. Area R^2 then forces Omega(R^2) full tiles. No tile-frequency premise is needed.

For all full tiles having at least eight genuine sides, the left side of the identity is at most -2F_i+3F_b; it eventually becomes negative while the right side is at least 2. Mixed species, arbitrary orientations, unboundedly small contact lengths, and T-junctions leave these bounds intact. Finiteness of the palette, its positive inradii, and its bounded diameters are material hypotheses.

## Four- and six-sided periodic witnesses

The quadrilateral case is the usual parallelogram lattice. For the hexagon I checked opposite-edge endpoint identifications directly. With vertices 0,u,u+v,u+v+w,v+w,w, the pair translations are b=v+w, b-a=w-u, and -a=-u-v, where a=u+v. The two corner classes are {0,2,4} and {1,3,5}. Each contains one representative from each opposite-angle pair, so each angle total is 2pi. The glued oriented surface has one face, three edges, and two vertices, hence Euler characteristic zero; it is a connected torus with a nonsingular flat metric. Its complete simply connected Euclidean cover supplies the claimed plane tiling. The translation periods a,b are independent because det(a,b) equals the positive hexagon area. Thus there is no unproved patch-extension inference in this step.

## Computation and remaining uncertainty

Replayed:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/check-convex-parallelogram-fusion-2026-10-19.py

It passed its exact symbolic area, endpoint, and Euler identities. This replay rewrites the existing deterministic certificate with the same mathematical data. These checks establish polynomial identities only; the geometry and infinite estimates were reviewed independently above.

No mathematical defect requiring a repair was found. No novelty claim was audited or added. The result excludes whole-atom fusions satisfying the stated symmetric-dissection premise; it says nothing about arbitrary cuts, nonsymmetric atoms, or the unrestricted existence question. All side counts must mean genuine corners after removing collinear redundancies, as the artifact specifies. This review changes neither the lemma nor `discovery-log.md`.
