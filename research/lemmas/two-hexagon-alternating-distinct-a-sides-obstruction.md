# Alternating A with six distinct sides cannot tile in the complementary-angle family

Date: 2026-10-12. Status: [fresh hostile review VALID](../reviews/two-hexagon-alternating-distinct-a-sides-review.md).

Consider the exact complementary-angle family with native words
A=(p,q,p,q,p,q), B=(r,s,r,s,r,s), where q=240-p, r=360-2p,
s=360-2q,90<p<150,p!=120. If all six actual A side lengths are pairwise
distinct, the fixed pair cannot tile the plane, with arbitrary reflections
and partial contacts permitted.

## Reduction and private reflected AA seams

Use the reviewed defect-free hexagon limit and global SFT encoding. Any
original tiling would give a trivalent whole-side field with exactly2A+1B
at each vertex. B occupies one index-three coset; each A has three AA and three AB neighbors in alternating side slots.

Across any AA seam, equality of whole side lengths and the distinct-A-side
hypothesis force the same native side index j on both tiles. Its native
endpoint angles p,q are different. Same-colour vertex stars match p to p
and q to q, forcing the pointwise endpoint correspondence. The adjacent
congruent A copy is therefore reflection in the supporting line, not a
half-turn. No globally chosen native AA parity is needed for the following local argument.

## Local homogeneous B corners give the contradiction

At either endpoint of an AA seam, the reflection fixes the matched native
A corner index. The two A copies' OTHER incident sides, bounding the B
sector, therefore have the same native index and the same actual length.
Thus the two side rays incident to EVERY B corner have equal lengths.
All six consecutive B side pairs agree, so B is equilateral with some
positive side length L.

Every A has three AB whole-side matches in the trivalent species phase.
Those three native A sides must all have length L, contradicting that
all six A lengths are pairwise distinct. This is a local metric
contradiction; no connected reflection orbit or carrier-hole argument
is necessary. QED.

This proves non-tileability, rather than merely failure of a selected
periodic witness. Coincident A side lengths may permit other native-index
matches and escape the argument; no such case is included. The original
partial-contact tiling is treated only through the independently reviewed
defect-free reduction. The longer reflected-triangle explanation gives
the same contradiction but is not a premise of this short proof.
