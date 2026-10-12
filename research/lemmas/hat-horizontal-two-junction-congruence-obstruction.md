# Horizontal two-junction hat cut: a pentagon-angle obstruction

Status: [fresh independent review VALID](../reviews/hat-horizontal-two-junction-congruence-obstruction-review.md)
for the fixed horizontal two-junction cut described below.

For the normalized hat outline Tile(1,b), b>0, choose
`V=(u,(sqrt3−b)/2)` strictly left of h8, and a free internal W.
Suppress the flat h8 vertex on the first hexagon. The four words are

* `P0=[h0,h1,h2,h3,h4,W]`;
* `P1=[h4,h5,h6,h7,V,W]`;
* `P2=[h8,h9,h10,h11,V]`;
* `P3=[h11,h12,h0,W,V]`.

This is a genuine two-junction feature with a nonempty strict convex
partition domain: b=sqrt3, V=(2,0), W=(7/6,−sqrt3/6) gives four
strictly convex pieces, disjoint interiors and exactly the source boundary.
Thus the failure below concerns the two-class condition, not the existence
of the source partition.

## Necessary side inventories

Write K=|Vh8|>0, so |Vh7|=K+1, and write D=|VW|, F=|Wh0|,
A=|Wh4|, J=|Vh11|. Hexagon congruence gives the multisets

    {b,1,2,1,A,F}={b,b,1,K+1,D,A},
    hence {1,2,F}={b,K+1,D}.

Pentagon congruence gives

    {K,b,b,1,J}={J,1,b,F,D},
    hence {K,b}={F,D}.

If F=b and D=K, cancellation yields {1,2}={K,K+1}, forcing K=1.
If F=K and D=b, the hexagon equation is {1,2,K}={b,b,K+1}.
The repeated b requires K=1 or2. K=2 is impossible because K+1=3
is absent on the left. K=1 gives b=1. Both cases therefore yield

    K=1, D=1, F=b,
    V=((sqrt3 b+1)/2,(sqrt3−b)/2).

These are multiset identities, so repeated lengths and reflections are
included without a distinctness assumption.

## Congruent pentagons force only two possible W directions

The edge h11→V is `(sqrt3 b−1)(1,−sqrt3)/2`. Strict convexity of
P2 requires b>1/sqrt3. Its five angles are then, in the word starting
at V, `(120,90,120,90,120)`. At h0 of P3, the incoming edge h12→h0
points vertically downward. Congruence therefore requires the outgoing
h0→W direction to be330 degrees (angle120) or0 degrees (angle90).
Since F=b, the only possibilities are

    W=(sqrt3 b/2,−b/2), or W=(b,0).

This argument uses corner angles only and includes every cyclic/reflected
correspondence, even when native side lengths coincide.

For the first possibility, h4=(3−sqrt3 b/2,−b/2), so h4→W is
horizontal with signed x increment sqrt3 b−3. The signed turns of
P0 at W and h4 respectively are

    det(W−h4,h0−W)=(sqrt3 b−3)b/2,
    det(h4−h3,W−h4)=−sqrt3(sqrt3 b−3)/2.

If b<sqrt3 the first is negative; if b>sqrt3 the second is negative;
if b=sqrt3 the vertices W and h4 coincide. Thus P0 is never strict.

For the second possibility, D=1 gives

    |V−(b,0)|²−1=b((2−sqrt3)b−1)=0.

As b>0, b=2+sqrt3. At this value the h4 turn of P0 is

    det(h4−h3,W−h4)
      =[3sqrt3−(1+sqrt3)b]/2=−5/2.

Thus the second possibility is also reflex.

Consequently there is no strict four-piece two-class realization of
these words. Side inventory followed by pentagon-angle forcing suffices;
no large congruence enumeration or monohedral classification is needed.
The result excludes this horizontal two-junction compiler, not other
source partitions or arbitrary pairs. No new full-plane pair or
unrestricted recognition theorem follows from the valid local partition.
