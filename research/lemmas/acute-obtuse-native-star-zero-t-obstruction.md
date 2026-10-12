# Native adjacency eliminates a full star and forces zero flat-contact density

Status: historical restricted argument; superseded for these native words by
the [reviewed all-metric untileability theorem](acute-obtuse-native-word-untileability.md).
This intermediate derivation has no separate completed review verdict.

Fix actual strictly convex pentagons with native words

    A=(65,140.5,147.5,75,112),
    B=(40,144.5,136,47,172.5).

No relation among native side lengths is assumed. All orientations,
reflections, partial contacts and vertex valences are admitted. The sole
native180 star is(A65,A75,B40). Call this flat-contact type T. Other
native angles are non-flat-eligible. The complete360 census is retained
in the [exact angle certificate](../certificates/acute-obtuse-long-edge-feature.json).

**Conclusion.** The full angle-legal star(147.5A,147.5A,65A) is geometrically
impossible for these native words. Consequently every plane tiling has
T-count O(R) in radiusR windows. Every translation-invariant tiling measure
has zero T intensity and equal A/B tile intensities. This forbids a
construction mechanism requiring recurrent or positive-density T contacts,
but does not forbid isolated or zero-density T defects in an original tiling.

## An endpoint continuation fact

Suppose two incident native sides meet along a positive seam ray from a
common vertex. If both far native endpoint angles are non-flat-eligible,
neither side can be shorter: its far endpoint would lie in the interior
of the other side. Thus their lengths and far endpoints must agree.
The two far corner angles must have a full360 native completion. This
is a local fact, independent of side subdivision elsewhere in the plane.

Write z=140.5, x=147.5, y=112, alpha=65. At x of A the incident native
sides are A1 to z and A2 to A75. At alpha they are A0 to z and A4 to y.

Assume a full star(x,x,alpha). Each x corner meets the alpha tile along
one seam. If it uses its A1 side, the far endpoint pair is z/z or z/y.
All those far angles are non-flat-eligible, so the continuation fact
would give a full far star. But z/z leaves79 and z/y leaves107.5,
neither of which is a native angle multiset. Hence neither x tile can
use A1 toward alpha. Both must use A2 toward alpha, leaving A1 on both
sides of their mutual x/x seam. That seam's far endpoints are z/z and
again have no completion. The full star(x,x,alpha) is impossible.

This argument includes every cyclic/reflected order and every choice of
actual side lengths. In particular changing the middle corner of a flat
fan or its seam length equalities cannot restore this star.

## Native corner capacity after the full-star exclusion

The x=147.5 angle cannot be flat, and the complete full-star census has
only two stars containing x: (x,x,alpha) and(x,B40,B172.5). Eliminating
the first means every A native x corner consumes one B40 corner in the
second. These stars are distinct because they each contain only one x.
Every T additionally consumes one B40 at a distinct flat vertex.

Every B144.5 corner is non-flat and has the sole full star
(A140.5,A75,B144.5). Thus every B consumes one A75 there. Every T
additionally consumes one A75, disjoint from those full vertices.
For translation-invariant intensities a,b,t this gives

    b >= a+t,
    a >= b+t.

Hence t=0 and a=b. This is a resource consequence of actual native
adjacency, stronger than the formal positive angle ledger which used the
now forbidden(x,x,alpha) star.

## Finite windows, sparse defects and scope

Count tile anchors and T vertices in a radiusR disk. All resource
associations move bounded distance. Fixed positive inscribed radii and
bounded diameters imply O(R) anchors and vertices in fixed-width annuli,
without a finite-local-complexity assumption. The same inequalities hold
up to O(R), giving

    T_R=O(R), |a_R-b_R|=O(R).

Thus flat T contacts cannot have positive area density. Arbitrarily large
T-free disks exist: for any fixed radius, thickening O(R) T vertices by
that radius occupies O(R) area while an interior disk has Omega(R²)
area. A translated compactness limit therefore supplies a defect-free
tiling with no corner-on-side contact. It is edge-to-edge, but need not be
trivalent or periodic; those conclusions are not asserted.

The theorem does not show all actual pairs with these words untileable,
nor all original tilings T-free. A local finite cap may occur without
contradiction. What it excludes is any positive-density or bounded-gap
flat-fan forcing mechanism for these words. A credible partial-contact
construction requires a changed native adjacency or angle inventory,
rather than a new middle-corner metric branch of this same family.
