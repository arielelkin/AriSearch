# Intrinsic c-seam feature: a bounded forcing gate

Date: 2026-10-14. Status: **negative local gate, not a two-polygon construction**.
[Independent hostile review](../reviews/ammann-c-seam-feature-hostile-review-2026-10-14.md): VALID for that scope.

The feature is the unique boundary edge of length `c` in each of Ammann's
two source pentagons. Work on the generic domain `G*` of the reviewed
[three-shape theorem](../lemmas/ammann-forcing-aperiodicity.md), with the four
native lengths `a,b,r,c` pairwise distinct. The unmarked cyclic side words are

```
P1: (a,b,a,c,a)       P2: (c,r,r,a,b).
```

These words prove intrinsic recognition without a drawn construction chord:
every copy, including every reflection, has exactly one `c` edge. A placed
pentagon's `c` edge is therefore independent of which of its five vertices
is called vertex zero. Its flanking corner pair is `(κ,216°−κ)` in P1 and
`(360°−χ−κ,144°−ψ+κ)` in P2. The ordered pair reverses under reflection;
it does not carry an absolute ambient chirality. The asymmetric side cycle
can distinguish the two endpoints intrinsically; this audit does not prove
that the resulting direction encodes a source X/Y arrow. All five undirected diagonals of
each pentagon remain candidate chords. This audit supplies no proof that a particular diagonal is the source cut
or a forced decoder; it does not claim that the side cycle cannot name
distinct diagonal roles.

The direct contact rule is only this: at a **full edge-to-edge** contact on a
`c` edge, the other tile also has a `c` edge, hence is P1 or P2. In a complete
tiling by the three Ammann shapes in `G*`, the [Lemma 4 vertex atlas](../lemmas/ammann-forcing-aperiodicity.md)
strengthens this to P1–P2: P1-K can occur only in a K-type star and P1-L
only in an L-type star, with the opposite `c` side supplied by P2-K/L. This
is a genuine geometric propagation rule, but its proof uses the **whole
three-shape corona**, including the H6 alternatives in the atlas. Lemma 3
separately excludes partial contacts in that same three-shape setting by
showing there are no 180° corner relations. Neither claim automatically
survives a new pair or a changed polygon boundary.

There is a sharp local obstruction to promoting this boundary signature to
the isolated predicate "every full `c` contact is heterotypic P1–P2."
Half-turn P1 about the midpoint of its `c` edge. The original and rotated
P1 lie on opposite sides of that supporting line and share their entire
`c` edge, with K opposite L at **both** endpoints. Convexity proves their
interiors disjoint. The corner sum at each endpoint is exactly
`κ+(216°−κ)=216°`, leaving 144°. Thus this is a positive-length P1–P1
contact satisfying endpoint angular feasibility: two 72° source corners
can fill each residual angle in a prospective corona. This is the flipped
P1 pair in the three-shape proof, eliminated **one edge away** by the vertex
atlas. The two-tile patch does not extend by itself to a whole-plane tiling
and does not refute a rule that explicitly relies on complete vertex
coronas. Reflection in the supporting line instead joins K to K and L to L;
that different patch is not the flipped pair used in this angular test.

Thus this particular boundary-edge feature alone cannot be the forcing
explanation for a new two-shape compiler. It has no intrinsic X/Y distinction at the rhomb edge:
the c seam is the internal thick-rhomb P1/P2 join, while X and Y arrows live
on the four reconstructed unit rhomb edges. It also gives no recognition of
the H6 thin-rhomb role, no global exclusion of wrong-arrow assemblies, and
no monohedral-omission obstruction. Supplying a unique diagonal based on a
visible source cut would not repair these missing steps; all potential
alternate diagonals must be audited in the actual output shape.

The stopping condition for this isolated feature is immediate: without an additional
proved corona condition for the **new two unmarked polygons** that rejects
the half-turned P1–P1 seam and all partial contacts, it cannot force matching.
Any proposed extension must also distinguish X from Y and their directions
across actual contacts, reconstruct both rhomb types, exclude homogeneous
wrong-arrow whole-plane coverings, and rule out either polygon tiling alone.
This note does not assume a two-shape source partition and does not reopen
the closed directed-offset family.

Finite audit: [checker](ammann-c-seam-intrinsic-feature-2026-10-14.py) loops
over all five cyclic shifts and their five reversals for each pentagon,
verifies a unique `c` edge in every labeling, and retains all five undirected
diagonals per pentagon. It uses no shape enumeration or parameter grid and
finishes in under one second. The exact corner and corona assertions come
from the cited reviewed theorem; the checker is intentionally only the
finite boundary-word check.
