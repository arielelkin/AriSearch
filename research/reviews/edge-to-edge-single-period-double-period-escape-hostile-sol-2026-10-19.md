# Independent hostile Sol review: single period to two periods

Date: 2026-10-19.
Reviewer: fresh Sol agent, independent of the author; no author artifact edited.
Verdict: **PASS — valid for the stated finite convex polygon, native edge-to-edge theorem.**

## Claim and scope

Reviewed `research/lemmas/edge-to-edge-single-period-double-period-escape-2026-10-19.md` against `research-problem.md` and `research-protocol.md`.

The claim checked is: a finite set F of compact convex polygons with nonempty interiors that admits a native edge-to-edge tiling invariant under one nonzero translation T also admits a native edge-to-edge tiling invariant under two independent translations. Reflections are permitted; there is no requirement that every type occur. The new tiling need not be the initial tiling. This review does not certify the optional nonconvex extension, novelty, or any result for unrestricted partial-side contacts.

## Attacks and positive checks

1. **Unbounded adjacency complexity despite bounded distance.** Each tile meeting a fixed-radius ball has an interior disk center within its diameter of that ball. Disjoint equal-radius subdisks give a uniform finite bound. A generic path between the two interior points avoids the finitely many vertices, crosses only finitely many sides, and therefore gives a bounded full-side walk. Loops can be removed from that walk. The bound may be very large and depend on |T|; no uniform bound over all possible periods is asserted or needed.

2. **Irrational rotation accumulation or infinite absolute orientations.** Each full-side transition has only finitely many indexed relative isometries. A bounded walk consequently has only finitely many composite isometries h. For the translated copy of an initial tile f(P), with f(x)=gx+b, the terminal physical set implies h(P)=P+g^{-1}T. Taking centroids removes any ambiguity from a symmetry of P. Thus w=g^{-1}T lies in a finite nonzero list. For each w there are at most two orthogonal g satisfying gw=T, including reflection. This is an actual finite-orientation proof, rather than an assumed finite-orientation convention. Duplicate congruent reference representatives can be consolidated, and polygon symmetries give only finite choices.

3. **Collars with continuously varying horizontal phase.** Normalize by an actual tile centroid, not by an arbitrary point. Every tile meeting the collar has a lift in a rectangle of bounded width and height about this centroid. Such a lift is connected to the anchor tile by a uniformly bounded adjacency walk. Its relative placement belongs to a finite list. Taking subsets of this finite list gives finitely many exact patches. The fixed vector T remains the same vector after translation normalization; normalization does not rotate T or replace it with a tile-dependent vector. Passing to the quotient by this same T preserves finite possibilities. Arbitrary x_n is therefore not a source of continuous collar states.

4. **A tile wider than the cylinder circumference or a tile crossing the chosen x seam.** The quotient need not be treated as a conventional embedded polygon decomposition. It suffices to retain complete planar tile orbits and their lifts in the bounded rectangle. T-periodicity identifies these lifts exactly. All finite-type and splice arguments work with these orbits, including boundary intersections with translates. No assumption that ell exceeds a tile diameter is used.

5. **Matching only visible pieces rather than whole crossing tiles.** The retained collar contains complete tiles meeting the collar, not clipped polygons. Equality of normalized orbit patches therefore identifies each complete seam-crossing tile, together with its centroid and side structure. Translation by U identifies the entire lifted local patch because both configurations have the same original period T.

6. **Half-open centroid choices leaving gaps, overlapping tiles, or omitting centroid ties.** Put the lower seam at a= y_i and upper seam at b=y_j. Near the repeated seam at b, the unrepeated layer supplies original tiles with centroid below b. The next layer supplies tiles translated by U whose original centroids are at least a. The collar equality identifies the latter with precisely the original tiles whose centroids are at least b. Tiles with centroid exactly b belong only to the latter selection. This gives the original complete local tiling near that seam. Translation handles every other seam. More quantitatively, within distance D/2 of a seam, any tile that can matter has centroid within 3D/2 of it, and all such tiles meet the retained 2D collar. Since L>10D, no distant layer can intrude. At a point farther than D from every seam, only its own translated source layer can contribute. These neighborhoods cover the plane, establishing coverage and disjoint interiors, as well as exact native edge-to-edge contacts.

7. **Skew second period and global coverage.** The horizontal component of U changes the source patch by the same amount at every seam and is already recorded in the exact collar equality modulo T. Its vertical component L is nonzero, so U is independent of T. Repeating the finite-height layer for all integral k covers every height; the preceding local argument proves actual planar coverage rather than only a consistent collection of boundary identifications.

## Counterexamples attempted

The mechanisms examined were arbitrary orientation accumulation, narrow cylinders and seam-wrapping tiles, nonprimitive T, symmetric reference tiles, reflected placements, continuously varying horizontal anchor phases, centroid ties, and skew seams. None defeats the hypotheses or construction. Sliding rows can defeat the orientation/collar argument for unrestricted partial-edge contacts, but those rows do not meet the native full-side premise used here. A nonperiodic transverse sequence of finitely many legal cylinder states is also harmless: equality of two thick states supplies a repeatable intervening layer; the theorem does not assert that the original sequence becomes periodic.

## Defects, repairs, and uncertainty

No substantive defect found; no repair made. The quotient phrase “cylinder tiling” is best understood as the periodic family of complete tile orbits, as explained above, so that no embedded-cell assumption is introduced. This is an interpretation already supported by the artifact's explicit lift convention, not a new hypothesis.

The finite-type and local splice steps have been positively checked, rather than accepted merely because no counterexample was found. No computation or imported literature theorem is required by this proof. This review makes no priority claim and does not audit the broader conditional extension to nonconvex polygons.

## Consequences for the research problem

If every tiling of a candidate pair is proved to be native edge-to-edge, exclusion of all doubly periodic tilings excludes all tilings with any translational period. A bounded torus search still does not exclude all doubly periodic tilings. The theorem neither forces edge-to-edge contacts under the original unrestricted definitions nor preserves a period under an unrelated limiting operation. It does not resolve the two-convex-tile problem.
