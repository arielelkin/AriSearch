# Two equiangular hexagons with two side lengths each

**Theorem.** Let A and B be strictly convex equiangular 120° hexagons, each
with at most two distinct numerical side lengths. If the pair tiles the
plane under arbitrary isometries and unrestricted contacts, it also admits
a rank-two periodic tiling. If neither member is centrally symmetric, the
pair does not tile at all.

For a positive cyclic side word `s=(s0,...,s5)`, exact vector closure is
`s0-s3=s2-s5=s4-s1=t`. The hexagon is central exactly when `t=0`.
If the word uses only distinct values `a,b` and `t≠0`, all three differences
must use the same sign of `b-a`; hence the word alternates `(a,b,a,b,a,b)`
up to cyclic shift. Every plane tiling by these 120° shapes is full-edge and
trivalent: a corner on another tile's side would leave a 180° half-plane
that cannot be filled by 120° corners.

For two alternating noncentral words, form the numerical corner graph from
their two unordered palettes. It has at most two nonloop edges and is
bipartite, even if the palettes overlap. At every trivalent vertex the
three physical ray lengths would have to form an odd closed walk of length
three in this graph, a contradiction. If one shape is central, its
opposite sides pair by translation. The resulting one-face, three-edge,
two-vertex flat torus has a Euclidean universal cover, giving a rank-two
monohedral tiling of that member and thus of the pair.

This is a restricted result; pairs using at least three lengths in one
member remain outside the theorem. Full proof, 64-word arithmetic audit,
and independent review:

- `../searches/two-equiangular-two-length-gate-sol-2026-10-19.md`
- `../searches/two-equiangular-two-length-gate-sol-2026-10-19.py`
- `../reviews/two-equiangular-two-length-hostile-imbalance-sol-2026-10-19.md`
