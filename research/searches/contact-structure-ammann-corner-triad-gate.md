# Exact Ammann corner-triad resection gate

Date: 2026-10-13; reviewed 2026-10-14. **Independently reviewed VALID for this fixed boundary gate** ([review](../reviews/ammann-cross-source-resections-independent-review.md)). This is a restricted cross-source construction obstruction, not an exclusion of arbitrary Ammann resections or the target.

Use the exact generic aperiodic Ammann source fixture J=1/2+(4/5)ζ, ζ=exp(iπ/5), and the H,P1,P2 coordinates in ../lemmas/ammann-forcing-aperiodicity.md. Form the three source faces H, ζ⁻²P1, ζ⁻²P2. Their source labels meet at the genuine H-J′/P1-K/P2-K vertex star. Since K=ζ²J′, the shared central vertex is J′; the other endpoints of the three shared full sides are 0,1,ℓ=ζ⁻²L. The three positively oriented strictly convex faces have pairwise disjoint interiors. This changes the construction mechanism to a resection spanning source species, rather than a source-by-source area module or pinwheel corner edit.

Their union has ten distinct nonflat outer corners, in cyclic order

    1,J,ζ,J″,0,ζ⁻²J′,ζ⁻²,ℓ,1+ζ⁻²,ζ⁻²J2.

Exactly two corners are reflex: 1 and ℓ. Their boundary arcs contain three and seven edges. The exact producer contact-structure-ammann-corner-triad-gate.py independently checks strict supports of all three faces, pairwise separation by supporting lines, cancellation of exactly three shared edges, the complete outer boundary, and the two reflex signs in QQbar. Replay passes. Decimal algebraic displays are descriptive only; all decisions use exact algebraic signs and coordinate definitions.

Any partition of this union into exactly two full-dimensional convex polygons has a straight common interface: two convex sets with disjoint interiors intersect, if along a positive-length seam, in a line segment. A reflex outer corner must belong to both polygons, since a single convex polygon cannot occupy its entire reflex neighborhood. Thus both 1 and ℓ must be seam endpoints. The only possible seam is [1,ℓ]. The three-edge boundary arc gives a polygon with at most four genuine sides; the other gives at most eight. Any incidental collinearity can only decrease these numbers. Consequently no such binary convex resection yields two polygons both having at least five sides. If the quadrilateral is used as a prototile, its ordinary halfturn periodic tiling already supplies the allowed omission escape.

This gate does not assume the triads globally partition an Ammann tiling. It rules out this local replacement before that additional covering problem arises. The alternative P1-J′ K-star, multi-triad replacements, partitions into more than two pieces, and resections crossing a different source boundary remain outside the claim.
