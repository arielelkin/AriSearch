# Shifting the cut attachment onto h10–h11 preserves a reflex corner

For the normalized hat outline `Tile(1,b)`, with `b>0`,

    h10=(3/2,b+sqrt3/2), h11=(1,b), h12=(0,b).

Let `W=h10+s(h11−h10)` with `0<s<1`. The proposed changed partition
has boundary word

    P9=[h0,h4,V,W,h11,h12].

Its signed turn at h11 is

    det(h11−W,h12−h11)
      = det((1−s)(−1/2,−sqrt3/2),(−1,0))
      = −(1−s)sqrt3/2 < 0.

The source boundary uses the counterclockwise orientation: the adjacent
turn at h12 in this same piece is `det((-1,0),(0,-b))=b>0`.
Thus the boundary has both signs and cannot be convex, regardless of V.
Reversing or reflecting the boundary changes both signs and preserves
this obstruction. This is a uniform geometry exclusion before any
congruence or metric search.

Consequently the proposed two-pentagon/two-hexagon words
`P9=[h0,h4,V,W,h11,h12]`, `P192=[V,h8,h9,h10,W]`, together with
the previous P6 and P48, never form four strictly convex pieces when W
lies in the open h10–h11 source edge. This statement excludes only this
cut attachment. It does not exclude other source cuts or polygon pairs.

## The analogous h0 and h4 shifts fail too

The source corner h0 is also reflex. Here h12=(0,b), h0=(0,0), and
h1=(-sqrt3 b/2,-b/2). Moving its cut attachment onto the open edge
h12–h0 gives W=(0,w), 0<w<b. The proposed hexagon
`[W,h0,h1,h2,h3,h4]` has signed turn

    det(h0−W,h1−h0)=−sqrt3 b w/2<0.

This excludes the proposed two-pentagon/two-hexagon O-shift regardless
of the internal V coordinates. At h4 the native incoming/outgoing
vectors are `(1/2,sqrt3/2)` and `(sqrt3 b/2,−b/2)`, with determinant
`−b<0`. Shifting its attachment onto either adjacent open source edge
leaves h4 strictly inside one face's boundary word, and multiplies this
negative determinant by a positive edge fraction. That face is reflex.

All these exclusions are instances of the same necessary feature:
every strictly reflex source vertex must remain a partition junction
in any convex-piece partition. Moving such a junction off its vertex
without adding another cut there cannot produce a convex partition.
