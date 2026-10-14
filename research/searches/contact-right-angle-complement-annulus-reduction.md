# Component classification mechanism for a parallel periodic Q scaffold

Date: 2026-10-13. Status: superseded for the two-private application by the reviewed [complementary-bands theorem](../lemmas/contact-structure-two-private-octagon-complement-bands.md). This broader annulus mechanism remains an internally developed, separately unreviewed working argument. Application uses reviewed two-distinct-private Qcore theorem and whole PQanchoring, not the exact equal-private ring computation.

Let the Qscaffold be a locally finite polygon packing whose QQcomponents have proper disjoint core curves, each periodic under the SAME nonzero vectorVand consisting of a uniformly bounded finite motif. Suppose a plane completion by finitely many positive-area bounded polygon classes exists, each completion tile having a whole-side Qanchor. The following argument aims to derive the component hypotheses of the anchored-strip theorem.

## Uniform strip confinement

NormalizeVhorizontal. Each core lies within a uniform vertical distanceKof a horizontal reference line: the Qcore theorem derives a two-tile motif with fixed tile diameters, so Kdepends only on Q. The core family is locally discrete. Indeed every core meeting a bounded rectangle has a Qcentroid in a fixed enlargement; positive-area packing bounds that number. ModuloVthere are finitely many cores in any bounded transverse band, by the same estimate in one period slab. Thus the cores have a discrete planar vertical order.

A complement component cannot cross a core contained in the scaffold. Every completion point is within D_Pof the scaffold, since it belongs to a Qanchored tile of diameterD_P. Every Qpoint is within D_Qof its own core, by joining through its centroid. Hence every complement point is withinR=D_P+D_Qof a core. If the ordered core family had an extreme member, the far outside halfplane would violate this bound; therefore cores extend in both transverse directions. Each complement component is trapped in the region between two consecutive ordered cores.

For consecutive cores with reference heightsc1,c2, their inter-core region contains any horizontal band between c1+Kandc2-Kif the gap is large; a point in its middle cannot be withinRof any other core without crossing a bounding core first along a shortest segment. Thus |c2-c1|<=2K+2R(up to adjusting Kfor choices of reference heights). The entire region between the two cores is confined to a strip of uniform widthatmost4K+2R. Its two boundary cores are each individuallyVperiodic, so this inter-core region isVperiodic.

The proof should be audited for the chosen reference-line convention; an equivalent formulation can use the vertical extrema of a period motif and enlarge Ktoavoid order ambiguity. No wide-region conclusion is inferred merely from individual core widths; anchoring is essential.

## Compact annulus quotient and primitive stabilizers

Quotient an inter-core region byV. Two disjoint periodic proper core curves bound a topological strip, so the quotient is an annulus with finite polygonal boundary. In its compact closure, only finitely many scaffold polygons occur moduloVby area packing. Subdividing their straight edges with an artificial period seam produces a finite polygonal cell complex. Open complement components in this annulus thus have finite cell descriptions.

Let Dbe one quotient complement component, and Cany lift to the plane. Its translation stabilizer equals the image ofpi1(D)inpi1(annulus)=Z. That image is either0orALLZ, never a proper nonzero subgroupkZ. To see this, a loop with nonzero winding can be perturbed to polygonal general position within the open set and decomposed at transverse self-crossings into finitely many simple loops withinD. At least one has nonzero winding. A simple essential closed curve in an annulus has winding+1or-1byJordan separation. Thus the image contains1. In the nonzero case C is individuallyVperiodic.

In the zero-image case Cmaps homeomorphically to Dand is bounded. For an explicit finite justification, triangulate the finite polygonal quotient complement. Its finite face-adjacency graph has integer seam-crossing labels. All cycle sums in Dvanish because its winding image is0. Consequently the longitudinal lift coordinate is a well-defined graph potential, bounded on the finite graph. Each face has bounded lift diameter, so the whole lifted component is bounded. Its actual completion is finite by positive-area packing. Its Vtranslates are distinct because its stabilizer is trivial.

Thus each component is either a uniform-width invariant strip component or a bounded component with freeVtranslate orbit and finite actual completion. These are exactly the two explicit hypotheses required by the anchored-strip periodization lemma.

## Scope

This component mechanism does not apply to arbitrary singly periodic scaffolds without proper parallel core barriers, uniform motif bounds and whole-side anchoring. It does not assume every completion is periodic: the finite-state strip lemma constructs a periodic completion. The broader quotient argument still needs a self-contained stable extraction and hostile review before using it as an acceptance gate. The completed two-private synthesis uses the direct closed-strip theorem instead and does not depend on this working argument.
