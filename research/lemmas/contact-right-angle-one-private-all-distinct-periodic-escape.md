# One private octagon side and five distinct pentagon sides

Date: 2026-10-13. Status: independently reviewed VALID; [complete hostile audit](../reviews/contact-right-angle-one-private-all-distinct-complete-hostile-review.md).

## Theorem

Let P be a genuine convex pentagon with one90 and four112.5 corners and
five pairwise distinct native side lengths. Let Q be a genuine convex
octagon with eight135 corners and exactly ONE native side slot whose
length is absent from all five P lengths. Reflections, arbitrary partial
contacts and species omission are allowed. If the pair tiles the plane,
it admits a rank-two periodic tiling. More precisely, up to simultaneous
similarity and reflection, the only tileable pair in this family is the
[exact hosted pair](contact-structure-one-private-x2u-periodic-carrier.md).
Its independently checked six-P/two-Q carrier establishes existence.

This is a complete classification within the stated family, not a solution
of the unrestricted two-convex problem. No side-host equation is imposed
as a hypothesis; every possible host plane is retained and then derived.

## Native reduction and whole-Q incidence counts

Use the [reviewed native reduction](contact-right-angle-unrestricted-native-reduction.md)
and its [fresh audit](../reviews/contact-right-angle-hosted-side-necessity-hostile-review.md).
Name P lengths cyclically (x,u,v,y,w), with u,v incident to its90 corner.
Set c=cos(pi/8), t=sin(pi/8), r=sqrt2. Closure gives

    u-v=rc(y-x), w=(u+v)/r-t(x+y).

All five lengths are distinct, so u!=v and x!=y. P typeR has Qcontacts
on u,v,w; typeS has Qcontacts on x,y. Every Qcontact is whole on both
sides. Q has at most two QQ slots, separated by cyclic distance3 or4.
The private slot, of length H, always has a Q mate. Its H mate uses the
same unique native H slot. A reflected mate would require u=v at the
P90 endpoint; therefore the mate is its midpoint half-turn. Neither P
nor Q tiles alone: a native P112.5 corner cannot be completed using only
P90/P112.5, and Q135 cannot be completed using only Q135, including a
flat host in either case. An actual tiling has positive uniform Q density
by coverage and the angular ledger.

Count centroid-anchored tiles and native contacts in squares of side2R.
Errors below are uniform O(R), by bounded diameters and positive areas.
Let p_R,p_S,q be the tile counts and D the total QQ native-side incidences.
Let n_L be the fixed number of Q slots of a particular nonprivate length
L, and E_L the count of its QQ native incidences. Native corners give

    p_R=D+O(R), p_R+p_S=4q-D+O(R),
    p_S=4q-2p_R+O(R), q-O(R)<=D<=2q+O(R).

These identities retain flat and four-right stars: R90 is PQQ; S90 is
a flat or four-right star. Whole-Q side counts give

    n_L*q-E_L=p_R+O(R), L in {u,v,w},
    n_L*q-E_L=p_S+O(R), L in {x,y}.

Every E_L is nonnegative. There are exactly seven nonprivate Q slots.
The [independent incidence audit](../reviews/contact-right-angle-one-private-global-incidence-review.md)
checks these unrestricted identities.

Choose any subsequential limit a=p_R/q in [1,2]. If 1<a<2, each of
n_u,n_v,n_w is at least2, and each of n_x,n_y is at least1 because
p_S/q tends to4-2a>0. This needs at least eight nonprivate slots, a
contradiction. Thus the fixed integer shape counts support only a=1 or2.
No existence or uniqueness of an invariant tile frequency is assumed.

## The a=2 alternative is impossible

At a=2 each of n_u,n_v,n_w is at least2. Only one nonprivate slot remains.
Hence at least one of x,y is absent from the whole Q alphabet. A typeS
P requires Qneighbors of both lengths x and y, so no S tile can occur
anywhere, independently of the subsequential limit. All P are R.
Their90 corners are then all PQQ; flats and four-right stars are absent.
The actual field is intrinsically edge-to-edge and trivalent.

The analytic argument in the [generic one-private obstruction](contact-right-angle-one-private-generic-obstruction.md)
now applies from its all-R section onward. Its no-host assumption was
used only to derive this ETE/all-R conclusion, already established here.
A Q with only one QQ side would have word (H,u,w,w,w,w,w,v), contradicting
vertical closure u!=v. Thus each Q has two QQ sides. The native positions
of the middle w sides and acute u/v sides fix its second mask to3,4or5.
Whole tagged contacts give public counts two u,two v,two w. At masks3/5,
short-gap bevel matching forces equal acute tags; closure then forces the
second QQ length J=H. At mask4 the unique H half-turn makes its flanks
opposite u/v tags, and coordinate closure again gives J=H. This would
create a second private slot, contradicting the original hypothesis.
The [fresh complete obstruction audit](../reviews/contact-right-angle-one-private-generic-hostile-review.md)
checks those mask arguments, and the incidence audit checks their transfer.

## The a=1 alternative forces actual dimers pointwise

The shape counts satisfy n_u,n_v,n_w>=1 and n_x,n_y>=2. Their sum is
seven, so exactly

    (n_u,n_v,n_w,n_x,n_y)=(1,1,1,2,2).

A Q with two QQ sides would need FOUR distinct public flanking slots
carrying u/v: mask spacing3/4 makes the four flanks distinct, and each
QQ endpoint has a P90 sector whose incident whole side is an acute leg.
But Q has only TWO native u/v slots in total, already flanking H.
Consequently every Q has exactly one QQ side, H, pointwise. No compactness
or persistence of a contact pattern is required.

Up to reflection and cyclic indexing, Q's native word is

    H,u,perm(x,x,y,y,w),v.

The individual side values distinguish R guests on u,v,w and S guests
on x,y, without markings.

## Partial contacts force exactly the aligned or crossed host word

The [native bridge proof](contact-structure-one-private-distinct-native-bridge-reduction.md)
retains all optional P-P flat contacts. A whole R-S interface would match
{x,y} with {u,v,w}, impossible. An R-S partial interface must be a
both-obtuse R host x or y, split into two S acute legs. R middle w is a
Qcontact and cannot host P; S middle w can host only S acute guests,
so optional w=2u/2v never bridges the R/S types.

At least one R-S bridge is needed because every Q has both types of
public guest. At most one of the four equations x=2u,x=2v,y=2u,y=2v
can hold. If x,y were both doubled same-leg hosts, x=y; the opposite
assignments in P closure require either u=v or rc=1/2, impossible.
Normalize by reflection to the x host case.

The R guest on public v exposes the nondoubled y PP side, whose neighboring
Q guest must also be R; the only other adjacent eligible R guest is the
middle w guest. Thus w is the public slot next to v and the four S slots
form one consecutive block. If x=2u, a terminal S guest must expose its
u leg to the R host, and hence its Qbevel x at either block end. The
fixed multiset leaves y,y in the block middle. If x=2v, both block ends
are y, leaving x,x in the middle. Optional S-S middle-w caps cannot alter
these terminal tags. The only two words are therefore

    aligned: (H,u,x,y,y,x,w,v), x=2u,
    crossed: (H,u,y,x,x,y,w,v), x=2v.

The [independent native-bridge audit](../reviews/contact-right-angle-one-private-native-bridge-hostile-review.md) verifies this reduction without imposing
an edge-to-edge rule.

The [crossed-host closure proof](contact-structure-one-private-x2v-closure-obstruction.md)
gives y/x=-t/(1-1/r+t)<0; no positive crossed shape exists.
The aligned P/Q closure equations with x=2u have exactly one positive
kernel ray. Normalize x=1,u=1/2. Then

    y=(r+2c-t-1)/(2c+t+1/r), v=1/2+rc(1-y),
    w=1+(c+1/r)(y-1), H=y-(u+v-y-1)/r.

All lengths are positive and distinct; all other host equations fail.
The exact [coordinate certificate](../certificates/hosted-oneprivate-x2u-periodic-carrier.json)
and [independent frozen-geometry checker/audit](../reviews/contact-right-angle-one-private-hosted-carrier-hostile-review.md)
give its six-P/two-Q periodic plane carrier. Native ordered angles and
lengths determine each original shape up to allowed isometries; scaling
restores the original metric. This proves the stated classification.

## Remaining target gaps

Repeated P side lengths, zero/two private partners, nonequiangular Q and
other angle palettes remain outside this theorem. The exact certificates
are used for the single positive aligned ray's periodic existence; all
family reductions are analytic, with explicit global incidence and native
contact arguments. No novelty claim or unrestricted final report is made.
