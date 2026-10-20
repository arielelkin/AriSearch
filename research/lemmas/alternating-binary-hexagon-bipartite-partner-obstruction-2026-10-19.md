# Alternating binary hexagon against a bipartite partner

**Theorem.** Let A be a strictly convex equiangular 120° hexagon with
consecutive side lengths `(a,b,a,b,a,b)`, `a,b>0`, `a≠b`. Let B be any
strictly convex equiangular 120° hexagon whose numerical corner graph is
bipartite: its vertices are actual side lengths, with an edge between each
adjacent pair in the cyclic side word. Then `{A,B}` does not tile the plane,
even with arbitrary rotations, reflections, partial contacts, or omission.

**Corollary.** If B is noncentral and has no equal adjacent side lengths,
its corner graph is bipartite and the pair is untileable. If B is central,
B alone has a periodic tiling. Thus any potentially aperiodic pair with
this A needs a noncentral B with an equal adjacent side-length pair.

**Proof.** The 120° sector count makes any tiling full-edge and trivalent.
At a trivalent vertex the three ray lengths form a length-three closed
walk in the union of the two numerical corner graphs. A's graph has only
the nonloop edge `a-b`; B's graph is bipartite and has no loops. If `a,b`
can be placed in opposite bipartition parts, their union is bipartite and
no vertex exists. The only other possibility is that `a,b` lie in the
same part of B's graph. Then every vertex must have exactly one A corner
and two B corners, with ray lengths `a,b,x`. Every native B corner must
contain exactly one of `a,b`, so B's word alternates public sides
`p,q,r∈{a,b}` with other sides `x,y,z∉{a,b}`:

    B=(p,x,q,y,r,z).

Exact closure gives `x=r-t`, `y=p-t`, `z=q-t` for one real `t`.
If all three public sides agree, no vertex can use the other public
length. Otherwise, exchanging `a,b` and cyclically shifting, put
`p=q=a,r=b`. Then the unique private length `x=b-t` lies between two
`a` sides, and no B corner pairs `b` with `x`; `x` differs from
`y=z=a-t` because `a≠b`. The mandatory B corner `(a,x)` therefore cannot
complete its trivalent vertex. Contradiction. The argument uses actual
numeric equality and is unchanged by reflection.

For the corollary, noncentral closure means `t≠0`, so opposite native
sides differ. With no equal adjacent sides, any repeated length can occur
only at cyclic distance 2 or 4. The even-slot and odd-slot numerical
palettes are disjoint and bipartition B's corner graph. A central B has
the standard opposite-edge flat-torus tiling.

The full proof includes a redundant global charge diagnostic; it adds no
scope to the local closure obstruction. Sources and hostile review:

- `../searches/hexagon-binary-partner-bipartite-charge-sol-2026-10-19.md`
- `../reviews/hexagon-binary-partner-bipartite-hostile-sol-2026-10-19.md`
