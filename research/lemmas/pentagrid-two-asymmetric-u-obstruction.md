# Two U-angle pentagons: a maximum-side contact obstruction

**Status:** adversarially reviewed; the [fresh hostile review](../reviews/pentagrid-two-asymmetric-u-obstruction-review.md) is VALID without mathematical repair for all one/two-type metrics and unrestricted contacts.
The native-measure reduction is imported from the separately developed
[pentagrid U native-measure lemma](pentagrid-u-word-native-measure-and-maximal-ray.md),
whose own review status must also be respected. This file is not an
independent review of that dependency. No general finite-collection
asymmetric theorem is claimed.

## Statement and hypotheses

Let the reference set consist of at most two genuine convex pentagons with
cyclic angles (36,108,144,144,108) degrees. Give the two shapes arbitrary
positive metrics, and allow all translations, rotations, reflections,
partial contacts, and omission of a reference type. This set cannot tile the plane.

There is no equal-long-side, common-scale, algebraic-length, or
edge-to-edge hypothesis. The proof uses no monohedral classification.
The two-type hypothesis is essential to the argument below; identifications
of a forced tile with the only lower-maximum type cannot be reused for
three or more reference types.

## Exact facts used

A reference shape can be oriented so its acute-incident lengths are A,B,
its remaining lengths are b,c,d, and c joins the two144 corners. The b,d
sides join144 to108. With phi=(1+sqrt(5))/2,

    A=phi*b+phi*c+d,  B=b+phi*c+phi*d.                  (1)

Both A,B exceed every own short. More precisely,

    A<phi*B, B<phi*A,
    A-B=(b-d)/phi,
    A>b+c+d, B>b+c+d.                                (2)

For each short r there is a long strictly exceeding phi*r: use A for b,
either long for c, and B for d. These statements are strict because all
shorts are positive.

By the imported nonnegative native-corner measure and translated-limit
argument, a hypothetical plane tiling gives another admitted plane tiling
using only these stars:

    full334: (108,108,144),
    full1144: (36,36,144,144),
    half14: (36,144) and one straight180 sector.       (3)

At every native vertex at most one straight sector is possible. In
particular a native108 cannot lie in the relative interior of any native
side, and native108 and native36 cannot coincide: neither occurs in(3).
The same restrictions hold for reflected copies.

Restrict to actually used types. Let M be the largest long over those
one or two types. Every used short is strictly less than M. The imported
maximum-ray lemma excludes a length-M acute ray immediately bordering
native144. Thus its other side is native36 or a straight sector.

The following elementary contact rules will be used explicitly.

* At an acute36 ray of length N whose other endpoint is108, a neighboring
 144 arm (b or d) must have length N. A mismatch puts the shorter side's
 108 endpoint inside the other side.
* If the neighboring144 edge is c, it cannot exceed N. Equality is
 possible geometrically. If c<N, its far144 vertex lies inside the long
 side, forcing another acute36 tile. This new tile has one long N-c and
 its other long equal to the far arm r of the144 tile. Both endpoint
 equalities follow from the no-interior108 restriction.
* At a108-to36 long side of length M, if a neighboring144 base c<M
 starts at the108 endpoint, its far144 vertex likewise forces an acute
 tile. The new tile's arm-facing long equals the neighbor's arm r.
 Its forward long must be strictly greater than M-c: shorter gives an
 interior108, and equality puts108 and36 at the same point.

All these rules concern whole native sides and their actual endpoints;
they do not impose an edge-to-edge condition on the tiling.

## 1. A shorter acute ray of a maximum-bearing type

Take any tile whose one acute long is M; denote its other long by L.
If its L ray borders144, an arm match or a base equality would make a
neighbor long >phi*L>M, by(2). Thus the neighbor must use a base c_R<L,
and the forced new acute tile S has longs r_R,L-c_R, both<M.

Consequently a used type with both longs<M exists. If both reference
types had a long M, this would already be impossible. Otherwise there is
a unique maximum-bearing type P and a unique lower type Q. The144
neighbor cannot be Q: S would also be Q, but r_R would be an own Q short
and an own Q long. Therefore the neighbor is P, and S is Q.

Normalize P by reflection so

    A_P=M>B_P=L,   b>d,   L=b+phi*c+phi*d.

The far arm cannot be d, since

    L-c=b+c/phi+phi*d > phi*d,

contrary to the ratio bound for S. Hence that far arm is b, the near arm
is d, and the fixed lower type has long multiset

    Q_longs={b,L-c},  with b<L-c.                       (4)

In particular every Q short is <b<L. This conclusion does not claim
that every acute ray of a maximum-bearing tile borders144; it is used
only where the ray actually does so.

## 2. Acute-to-acute maximum rays cannot occur

If a length-M ray borders another36 sector, that sector's long on the
shared ray must also have length M: a shorter neighbor would put108
inside the M side. This is a full native1144 star with adjacent36
sectors. Each other acute ray borders144, so section1 applies to each.
If both used types contain M, the forced lower type is already
impossible. Otherwise both acute tiles are P, and both144 neighbors are
P with the far arm b and near arm d.

At this star the36/36 seam and the opposite144/144 seam are collinear:
on each side the intervening36+144 is180. Hence the two near d sides
of the144 neighbors coincide in full. Their far endpoints coincide,
carrying two108 corners; (3) forces a third144 tile K.

The other side at the108 endpoint of a P d side is its A=M long.
Thus both boundary rays of K's144 sector run along length-M sides
starting at108 and ending at36. One of K's incident sides is an arm,
strictly shorter than M, and its far108 would lie inside one of those
length-M sides. This violates(3). Therefore this maximum-ray case is
impossible.

## 3. A straight short-side carrier cannot occur

Suppose the maximum ray starts at x in the relative interior of a host
side R, and points forward. If R uses its base c_R, the forward endpoint
is144 at distance h<c_R<M. The forced acute tile S there has longs
M-h and r_R, where r_R is an arm of R. The ratio bound gives
M<h+phi*r_R<c_R+phi*r_R, while an R long exceeds the latter quantity,
contradicting M. This is the base-carrier exclusion.

If R uses an arm of length r1, its forward endpoint cannot be108,
because its distance is <r1<M. Thus it is144 at distance h<r1. The
forced acute S has forward long L_S=M-h; its other long K_S faces the
R base c_R.

If K_S<c_R, its108 lies inside that base. If K_S=c_R, the ratio gives
M<h+phi*c_R<r1+phi*c_R, below an appropriate R long by(1). If
K_S>c_R, the far base vertex forces a second acute tile S', whose longs
are r2 and K_S-c_R, where r2 is the other R arm.

Neither S nor S' can have a long M. For S this uses the imported maximum-ray
exclusion: if K_S=M, that ray directly borders R's native144 sector.
It is the forward ray M-h that borders the original straight side. All other displayed longs are strictly<M. Therefore both S
and S' are Q. If R were Q, r2 would be an own Q short and long, impossible.
So R=P. Equal long multisets for S and S' force

    r2=K_S, K_S-c_R=M-h.

Indeed K_S-c_R<K_S, so it must be the other member M-h of that fixed
two-element multiset; if the members are equal the equality is already
impossible. It follows that

    M=h+r2-c_R<r1+r2-c_R<b+c+d<M,

a contradiction. Thus every surviving straight carrier is a long side.

## 4. A straight long-side carrier

Let a maximum ray start at x in the interior of a host long H of length
N<=M. Its forward endpoint cannot be108 because its distance h<N<=M;
therefore it is the host's acute36 corner y. At y the maximum tile has a
straight sector, so a144 tile R fills the half-star. Let T be H's other
long, which faces R at y.

### 4a. The host has a long M

If the carrier is its shorter long, T=M borders native144 and the
imported maximum-ray exclusion applies immediately. Thus the carrier
itself has length M. Section1 applies to T, requiring a unique top type
P, host H of type P, T=L, and relation(4). It also identifies R as P,
whose near arm at y is d. That d side runs forward along the original
maximum side; its far108 must coincide with the original maximum
side's108 endpoint. Hence

    h=M-d.

At x the original P tile's shorter L ray borders native144. Section1
again identifies this144 neighbor R0 as P with near arm d. Its d side
runs backward along the host carrier, ending at the host's rear108
endpoint v=x-d. There are now two108 corners at v (H and R0), and the
star forces a144 tile K.

The R0 long starting at v and ending at its acute corner has length M.
K cannot use an arm against it, since every arm is<M and ends108.
Therefore K uses its base c_K<M. At its far144 endpoint the forced
acute tile S has an arm-facing long r_K and forward long >M-c_K, by
the third contact rule.

If K=Q, then r_K<min(Q_longs)=b<L, so S is neither P nor Q.
If K=P, S cannot be P because r_K is an own P short. It can be Q only
if r_K=b, since d<b=min(Q_longs). Its forward long is then L-c, which
is smaller than M-c_K=M-c, again impossible. This excludes the host
case 4a.

### 4b. The host has both longs below M

Call that lower host Q, and the unique maximum-bearing type P. The
144 tile R at y must be P. To see this, if its side facing T is an arm,
it cannot be Q because an own Q short cannot equal T. If it is a base,
c_R>T would put Q108 inside that base. If c_R=T it likewise cannot be
an own Q base. If c_R<T, the forced acute tile has longs r_R,T-c_R,
both<M, hence is Q; taking R=Q again equates an own short and long.
Thus R=P in every branch.

If R shares an arm r1=T with H's T long, its other side at y is c.
The possibility c>M-h puts the original P108 inside c. The equality
c=M-h gives

    M=h+c<N+c<phi*T+c,

below the appropriate P long. If c<M-h, the forced acute tile S has
longs r2 and M-h-c and is Q. Since Q's long multiset is {N,T=r1},
r2 must equal N unless r2=r1. The latter would give b=d and a mirror
maximum type, already excluded by the imported maximum-ray theorem.
In the former case

    M=h+c+T<N+c+T=r2+c+r1=b+c+d<M,

a contradiction.

If R instead shares its base c with H's T long, then c<=T. Its near
arm r1 runs forward along the original maximum side, so r1=M-h.
If c=T, the Q ratio N<phi*T yields

    M=h+r1<N+r1<phi*c+r1,

below a P long. If c<T, the forced acute tile S at the far base
vertex has longs r2,T-c and is Q. Matching the multiset {N,T} forces

    r2=T, N=T-c.

Indeed T-c<T and must equal N; it cannot equal T. Hence

    M=h+r1<N+r1=r2-c+r1<b+c+d<M.

This excludes case4b.

## Conclusion, scope, and finite diagnostic patch

Every maximum acute ray either borders144 (excluded by the imported
lemma), borders36 (section2), or borders a straight sector (sections3,4).
These exhaust(3). Therefore the assumed zero-star tiling does not exist;
the original unrestricted two-U tiling cannot exist. Both this proof and the
imported measure reduction have separate VALID fresh hostile reviews.

This argument does not exclude collections of three or more asymmetric
U metrics. It supplies no result for a pair with a non-U angle word.
It must not be presented as a solution of the original two-convex-polygon
aperiodicity problem.

A concrete locally legal six-tile strip illustrates why a local patch is
insufficient. Take P shorts b=10,c=d=1. Let Q shorts

    b_Q=1,
    c_Q=(10-1-phi^2*(1+1))/phi,
    d_Q=1+1+phi^2.

They are positive and Q longs are {10,B_P-1}. Two opposite P maximum
sides overlap in length M-1, two P base neighbors fill their acute
half-stars, and two Q tiles fill the smaller acute half-stars. These six
polygons have disjoint interiors, but their rear108/108 vertices force
precisely the case4a contradiction. The exact diagnostic producer is
`research/searches/pentagrid_asymmetric_u_maximal_strip.py`; it verifies
pairwise interior disjointness, boundary cycles, and area. A native108/108
boundary corner is not an admitted full-plane star until its missing144
sector has been filled, which this argument forbids.
