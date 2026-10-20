# Independent hostile re-review: angle nonresonance

**Date:** 2026-10-19
**Reviewer:** fresh independent Sol reviewer; no authorship of the lemma or its earlier repair.
**Artifact:** [angle-nonresonance-edge-forcing.md](../lemmas/angle-nonresonance-edge-forcing.md).
**Earlier record:** [angle-nonresonance-review.md](angle-nonresonance-review.md).
**Verdict:** **valid** for the stated edge-to-edge theorem. Two ancillary wording qualifications are recorded below. No author files were edited.

## Exact claim and assumptions checked

A plane tiling means a cover of the plane by closed isometric copies of finitely many positive-area compact convex polygons, with pairwise disjoint interiors. Each polygon is represented without redundant straight vertices. Every genuine angle is therefore strictly between zero and pi. Assume that no nonempty finite sequence of these angles, allowing arbitrary repetitions, sums to pi. The conclusion is that intersections of distinct tiles are empty, a common genuine vertex, or a complete native side of both tiles. Reflections are allowed.

The finite protoset, compactness, convexity, positive area, genuine vertices, and arbitrary repetitions all matter to the proof. No edge-to-edge or local-finiteness assumption is being smuggled into the tiling definition.

## Independent proof audit

Let a>0 be the minimum tile area and D the maximum tile diameter. Every tile meeting a compact set K lies in its closed D-neighborhood. Any finite collection of n such tiles has disjoint interiors and total area at least na, bounded above by the area of that bounded neighborhood. Thus only finitely many tiles meet K. This proves local finiteness even when it is not part of the definition.

Suppose a genuine vertex p of tile Q lies in the relative interior of a side of another tile P. Local finiteness permits a sufficiently small disk about p in which every tile meeting the disk contains p, and every incident tile agrees with its local polygonal cone. To justify this choice, first enumerate the finitely many tiles meeting a fixed compact disk, exclude the positive distances from p to tiles not containing p, and then exclude all nonincident edges of the remaining polygons.

No incident tile can contain p in its interior: its interior would overlap the positive local sector of P. Each incident tile therefore contributes either a half-disk (p in a side interior) or a genuine corner sector. Tile P contributes one half-disk. Any second side-interior tile would have to occupy precisely the opposite half-disk, because open angular sectors cannot overlap. That would leave no positive sector for Q, whose angle is strictly positive. Consequently every other incident tile contributes a genuine corner sector on the opposite side of P. Finitely many such sectors cover that half-disk and have pairwise disjoint angular interiors, so their angles sum to pi. This contradicts the hypothesis. In particular, an isolated vertex-to-side touch is excluded just as effectively as a positive-length T-junction.

For completeness, two distinct convex tiles with disjoint interiors cannot have a two-dimensional intersection: such an intersection would contain a point interior to both. Their intersection is therefore empty, a point, or a segment. At a point contact, a vertex-to-side incidence has already been excluded. Two side interiors cannot meet transversely, since their interior half-planes would overlap in an open sector. If their supporting lines coincide, two side interiors have a positive-length overlap. Thus any isolated point contact is a common genuine vertex.

A segment intersection lies on one native side of each polygon. If the two side intervals are not identical, some endpoint of one lies strictly inside the other whenever they overlap in positive length. That endpoint is a genuine vertex, giving the excluded incidence. Hence the two sides coincide completely. This establishes the usual full edge-to-edge conclusion, including the condition on isolated point intersections.

Reflection does not change a tile's interior angle or the half-plane/sector argument. No orientation, chirality, periodicity, or global extension assumption occurs.

## Counterexample attacks and findings

* **T-junctions and partial side contacts:** each forces a genuine endpoint in another side interior and hence a pi angle sum.
* **Isolated point contacts:** vertex-to-side contacts force the same sum; genuine vertex-to-vertex contacts remain permitted.
* **Collinear vertices:** native straight vertices are explicitly excluded. A genuine corner cannot be disguised as a straight-through tile, since its angle is less than pi. Collinear rays from different genuine corners cause no problem in the angular partition.
* **Accumulating tiles:** ruled out by the explicit area/diameter packing proof above.
* **Reflected placements:** preserve all hypotheses and the contradiction.
* **Higher valence:** the proof only excludes pi sums. It does not exclude a genuine corner multiset summing to 2pi with four or more entries. Trivalence is not established by this theorem.

No counterexample to the theorem survives these attacks. The validity verdict rests on the complete proof above, rather than on bounded testing or failure to find an example.

## Defects, repairs, and remaining qualifications

No defect requiring a repair of the theorem or its repaired proof was found. The earlier review's addition of isolated point contacts is sufficient and has been independently checked here. No repair was made in this review.

Two sentences in the explanatory discussion should be interpreted with care:

1. “The possible tiling vertices are exactly the finite angle multisets summing to 2pi” describes the finite **angle-compatible candidates**. It does not establish that every such multiset is geometrically realizable, much less globally extendible. The earlier review already notes this limitation.
2. “Angle nonresonance by itself does not bound valence” is literally too strong: for any fixed finite protoset, positivity gives the explicit bound floor(2pi/alpha_min). The sound intended conclusion is that this condition does not prove trivalence or exclude higher valence. It does not furnish a tiling with higher-valence defects or a pentagon/hexagon encoding.

The finite pi-sum rejection bound floor(pi/alpha_min) is correct. Repetition must be allowed even if an angle appears only once among the labelled prototile corners. Numerical noncoincidence cannot certify the hypothesis. This review establishes no global realization claim for candidate vertex languages and does not audit the curvature identity discussed in the earlier review.

**Final verdict:** **valid** edge-to-edge forcing theorem under its exact stated hypotheses; independently reviewed after the isolated-point-contact repair. Ancillary discussion has the two scope qualifications above. No theorem-level uncertainty remains from this audit.
