# Fresh hostile review of the unrestricted two-U obstruction

**Reviewer:** pentagrid_metric. This reviewer did not develop the native
measure, maximum-ray lemma, or the new two-type contact argument.

**Verdict: VALID** for at most two fixed genuine convex U-word pentagons,
arbitrary positive real metrics, all rotations and reflections, arbitrary
partial contacts, and omission. No mathematical repair is required. The
review imports the separately
[reviewed native-measure reduction](pentagrid-u-word-native-measure-and-maximal-ray-review.md).
It does not establish a theorem for three types or for other angle words.

The inspected candidate is
[the two-asymmetric-U lemma](../lemmas/pentagrid-two-asymmetric-u-obstruction.md).
The auxiliary six-tile strip and its producer are diagnostic examples;
their existence or any computational assertion is not needed for this
analytic verdict. No bounded search or monohedral classification enters.

## Metric facts, maximum selection, and endpoint restrictions

The side labeling is important: the108 endpoint of A is incident to d;
the108 endpoint of B is incident to b. The acute corner joins A,B, and
c joins the144 corners. Direct closure gives

    A=phi*b+phi*c+d, B=b+phi*c+phi*d,
    A-B=(b-d)/phi,
    phi*A-B=phi*b+c, phi*B-A=c+phi*d.

Subtracting b+c+d gives(b+c)/phi and(c+d)/phi. Thus both longs exceed
the sum of shorts and their ratio is strictly below phi. A exceeds
phi*b and phi*c; B exceeds phi*d and phi*c. These statements hold for
all b,c,d>0 and are invariant under swapping the reflected labels.

The maximum M must be taken over the types actually present in the
zero-measure limit. Their own shorts are then all<M. A maximum-bearing
type cannot be mirror symmetric: if both acute longs were M, one of
the acute rays at every allowed acute star borders144, contradicting
the imported maximum-ray lemma. Thus any surviving maximum-bearing
type has another long L<M. This implicit fact justifies the strict
normalization A=M>B=L in section1; it is not an extra hypothesis.

The imported zero-star list has full334, full1144, and half14 with one
straight sector. Hence native108 is never in another side's relative
interior, and native108 never coincides with native36. These restrictions
apply to actual endpoints, including beyond a T-junction. Along overlapping
rays whose far endpoints are both108, unequal lengths are therefore
impossible. If one far endpoint is36, equality with an108 endpoint is
also impossible. The candidate uses this latter strictness only where
the endpoint is really the acute36 of a tile, rather than108.

## The forced lower type and the acute-to-acute branch

Suppose a maximum-bearing tile's L ray borders144. An arm match would
make a neighbor long>phi*L>M. A base longer than L puts the original108
inside that base; equality likewise gives a neighbor long>phi*L>M.
Thus the base c_R is shorter than L. Its far144 vertex lies on the
original long's interior, so the half14 star forces an acute tile S.
The endpoint restrictions give its two longs exactly r_R,L-c_R, both<M.

At most two used types now forces one unique maximum-bearing P and one
unique lower Q. If R were Q, r_R would be both an own Q short and own
Q long. Thus R=P. Reflecting the reference labeling gives A=M,B=L,b>d.
If the far arm were d, L-c=b+c/phi+phi*d>phi*d would violate S's ratio.
Therefore the far arm is b, the near arm d, and

    Q_longs={b,L-c}, b<L-c<L.

Every Q short is strictly below b. This type identification is valid
only in branches where this shorter-ray contact actually occurs; the
candidate respects that scope.

For a maximum ray bordering another acute36, matching far108 endpoints
force the other long to have length M. The full1144 cyclic order then
puts144 along both other acute rays. The preceding argument identifies
both acute tiles and both144 neighbors as P. The opposite144/144 ray is
collinear with the36/36 seam; the two near d sides coincide in full,
producing a rear108/108 star. Its missing144 tile has both boundary rays
along M sides starting at108. One incident144 side must be an arm<M
ending108; that endpoint would be inside an M side. This contradiction
also covers reflected copies and either labeling of the two acute tiles.

## Straight short-side carriers

The original maximum ray's origin is strictly inside the carrier side,
so the forward distance h is strictly below that native side's length.
This strict inequality is maintained through every estimate.

For a base carrier, h<c_R and the new acute longs are M-h and its far
arm r. Their ratio gives M<h+phi*r<c_R+phi*r, smaller than an R long.
For an arm carrier, a forward108 would lie inside the M side; the
forward endpoint must instead be144. The new acute tile S has longs
M-h,K, with K facing c_R. K<c_R is forbidden by108 inside a side.
K=c_R gives M<h+phi*c_R<r1+phi*c_R, again below an R long.

For K>c_R, the far base vertex forces a second acute tile S' with longs
r2,K-c_R. S cannot have K=M because that ray directly borders144;
its other long is M-h<M. Both S' longs are also<M. Thus S,S' are the
unique lower Q, whose fixed unordered long multiset gives

    {M-h,K}={r2,K-c_R}.

Since K-c_R<K, the only possible assignment is r2=K and M-h=K-c_R.
This remains exhaustive if a hypothetical Q had equal longs: equality
would itself require c_R=0. The carrier cannot be Q since r2 would be
an own short and own long; it is P. Hence

    M=h+r2-c_R<r1+r2-c_R<b+c+d<M.

This rules out both kinds of short carrier without assuming all sides
are matched in full. The unique P/Q identification here is rederived
from S's strict-lower longs; it does not presume section1 occurred.

## Straight long carriers: rear108/108 completion

For a long carrier of length N<=M, its forward endpoint cannot be108,
since h<N<=M. It is the host acute36 corner y. The original maximum
tile has a straight sector at y; the half14 star supplies a144 neighbor R.
The host's other long T faces R there.

If the host bears M but its carrier were L, then its other long M would
directly border144. Thus the carrier is M, and section1 on its other
long L fixes the near arm of R as d. That arm ends108 on the original
maximum side, forcing d=M-h. At the original acute origin x, the L ray
also borders144, so section1 fixes the near arm of the backward R0 as
d. Its far108 is v=x-d, exactly the host's rear108, because the host
carrier has total length M and forward length h=M-d.

The resulting rear108/108 star genuinely forces a144 K. The side of K
along R0's M long cannot be an arm, whose108 endpoint would be inside
M. It is therefore its base c_K. At its far144 vertex, S has an
arm-facing long equal to r_K and a forward long strictly>M-c_K.
Here strictness is essential: equality would put S108 at R0's acute36;
a shorter long would put S108 inside R0's side. Both are prohibited by
the exact zero-star list.

If K=Q, its arm r_K<b is below every P and Q long. If K=P, that arm
cannot be any P long and can be a Q long only when r_K=b; d<b is too
short. Q's other long would then be L-c<M-c=M-c_K. Thus neither K
can complete the rear star. No alternative endpoint identification or
partial continuation removes this obstruction.

## A lower long carrier: exhaustive multiset cases

If the carrier has both longs below M, it is the unique Q, with longs
N,T. The144 R at its acute endpoint must be P. For an arm contact,
R=Q equates its own short and T. For a base contact, c_R>T puts Q108
inside that base; c_R=T equates own short and long if R=Q; c_R<T forces
a lower acute tile with an own R arm as a long. This last tile is Q,
so R=Q is again impossible. These exhaust both incident side kinds.

If R=P has an arm r1=T facing the host, its base c faces the original
maximum side forward. c>M-h puts the original108 inside c. Equality
gives M=h+c<N+c<phi*T+c below a P long. For c<M-h the forced acute
S has longs r2,M-h-c, both<M, so is Q. Its multiset must be {N,T=r1}.
If r2=r1, P has b=d and both longs M, already excluded. Otherwise
r2=N and M-h-c=T, giving M=h+c+T<N+c+T=b+c+d<M.

If R instead uses its base against T, then c<=T and its near arm
along the maximum side has length r1=M-h, since both far endpoints
are108. For c=T the Q ratio N<phi*T implies
M=h+r1<N+r1<phi*c+r1, below a P long. For c<T the far144 vertex forces
another Q with longs r2,T-c. The exact unordered multiset equality

    {r2,T-c}={N,T}

requires r2=T,N=T-c; the alternative would require c=0. Thus
M=h+r1<N+r1=r2-c+r1<b+c+d<M. No assumption about which of N,T is
larger has been inserted; their order is forced only in this last branch.

## Adversarial boundary and verdict

I tried allowing a mirror lower type, both reference types bearing the
same maximum, arbitrary relative scales, either forward host endpoint,
native108/144 coincidences, nonfull base contacts, both unordered long
assignments, and forward acute endpoints. Each is either explicitly
included in the preceding branches or ruled out by a stated strict
inequality or the exact zero-star list. The six-tile locally legal strip
does not evade the proof: its rear native108 pair has precisely the
unfillable144 completion in the previous section. A locally open boundary
corner is not itself a permitted full-plane star.

An acute maximum ray has only three possibilities: border144, border36,
or border a straight sector. Full1144 alternating order belongs to the
first case; adjacent acute sectors to the second; half14 to the first
or third. Straight carriers are native base, arm, or long, exhausted
above. Thus no native star, reflected placement, or partial-contact host
case is left out.

The argument also covers omission: restrict to present types in the
zero-measure limit. Whenever a lower type is required, a one-type or
two-maximum-type collection immediately contradicts that requirement.
The crucial repeated identification of every strict-lower tile with the
single Q fails for three types; no finite-collection extension is audited.

Subject to the separately valid native-measure dependency, the complete
two-U theorem is VALID. This excludes one angle-family candidate pair,
not the original class of all pairs of convex polygons. This review
makes no literature-priority claim. It is analytic; no numerical decision,
implementation-mirroring test, or enlarged finite patch bound is needed.
