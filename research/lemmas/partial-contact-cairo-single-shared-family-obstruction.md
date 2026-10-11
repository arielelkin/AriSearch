# Full open-interval obstruction for the sole-shared-arm Cairo family

**Status:** freshly independently hostile-reviewed **VALID**; see [full interval review](../reviews/partial-contact-cairo-single-shared-family-obstruction-review.md) and [separate repaired-center audit](../reviews/partial-contact-cairo-single-shared-roots-review.md).
This excludes an explicit one-parameter family except three stated metrics;
it does not settle those exceptions or the original two-tile problem.

## Exact family and conclusion

Let w=sqrt3 and I=(1/w,2-1/w). For r in I put t=2-r and

    P=(1,r,(3w-r)/2,(wr-1)/2,2),
    Q=((wt-1)/2,(3w-t)/2,t,1,2).

These are positive genuine convex Cairo pentagons. Define

    r0=(2w-1)/(w+2), r1=1, r2=5/(w+2)=2-r0.

**Theorem.** For every r in I outside{r0,r1,r2}, this pair admits no plane
tiling under all isometries and arbitrary contacts.

At r1 there are extra internal and cross arm equalities. At r0 and r2
there is an extra cross arm equality. These metrics are explicitly outside
the proof, rather than inferred untileable by continuity. No periodic or
aperiodic claim on any of them is made here.

## Exhaustive equality and event audit

Both shapes satisfy exact Cairo vector closure for all r. Positive dP and
aQ are equivalent to r,t>1/w. All other sides are then positive. Their
increasing cyclic edge directions0,90,150,240,300 with positive closure
produce genuine convex pentagons.

Within I, the only internal arm equality in either species occurs at r=1.
The cross arm comparison table has one identity Pa=Qd=1. Its nonidentical
equalities can hold in I only at the following parameters:

* r0: Pb=Qa;
* r1: Pa=Qc, Pb=Qc, Pb=Qd, Pc=Qb, Pd=Qa;
* r2: Pd=Qc.

The exact symbolic checker enumerates all12 internal and16 cross comparisons,
solves every nonzero linear equality, and proves that every other root is
outside I. Thus outside the three listed parameters the four arms are
internally distinct and exactly one cross arm is shared.

There are eight self right-corner events and one cross event. The only
repeated total is

    2Pa=2Qd=Pb+Qc=2=eP=eQ.

Every other total is twice one of the six private arm values. Since those
values are distinct, the six totals are mutually distinct and none equals2.
This checks every privacy and singleton event condition used in the
[canonical cluster reduction](partial-contact-cairo-single-shared-fourfold-clusters.md),
whose geometric proof consequently applies verbatim here. It partitions
any original tiling into canonical S(r),S(t) clusters with the displayed
quadrant polygons. Each individual pentagon is monohedrally untileable by
the reviewed four-distinct-arm theorem, so a hypothetical tiling contains
S(r).

## All notch fillers still force the same reflected mate

Fix S(r) at origin and its notch(d_r,0). The missing sector is120, and the
only possible macrotile filler is its unique native convex120 corner type.
For z=r or t its two possible physical placements have centers

    (d_r+d_z+1, plus/minus w).

This enumeration uses only the fixed angular directions and positive native
side lengths1,2. It is independent of r and the width of the cluster.
The filler unit-side tip is strictly inside the host e2, forcing a T of two
native90 corners. The perpendicular arm has private native length z (Pb
or Qc), so its full same-slot mate is reflection in that arm line. The
canonical mate cluster is therefore the reflection of the entire filler
cluster in its bank line. This is the same exhaustive geometric argument
as in the [exact fixture obstruction](partial-contact-cairo-single-shared-notch-obstruction.md),
with no new extension search.

## A universal strict-overlap witness

Translate the upper filler cluster's center to origin. The seam point and
reflection matrix are

    X=(-wz/2,-3w/2),
    F30=((1/2,w/2),(w/2,-1/2)).

Its quadrant(+,-) pentagon has vertices

    (0,0),(d_z,0),(d_z+1,-w),
    (d_z+1/2,-3w/2),(0,-c_z).

Set

    W=(wz/5+3/10,7z/10-7w/5).

Direct substitution gives W=X+F30*(W-X): W lies on the reflection line.
Its five signed edge determinants in this clockwise pentagon are

    7/20*(wz-1)*(z-2w),
    -(z+3w)/5,
    (w-8z)/10,
    -z*(2wz+3)/10,
    wz^2/10-3z/4-9w/20.

All are strictly negative throughout z in I. The first uses wz>1 and
z<2<2w. The second and fourth use z>0. The third uses z>1/w=w/3>w/8.
For the last, wz<2w-1<3, so z*(wz/10-3/4)<0, and its remaining term is
negative as well. Thus W is strictly inside that filler pentagon and,
being fixed by the reflection, strictly inside its mate pentagon.

The entire two clusters have different centers: the original center0 is
not on the seam line through X: the reflected center is
((9-wz)/4,(3z-9w)/4), which coincides with0 iff z=3w, outside I.
They are different canonical clusters and cannot share original tiles.
Therefore these two pentagon interiors overlap in a hypothetical tiling,
a contradiction. The lower filler choices follow by horizontal reflection.
Every z=r,t and both orientation choices are excluded.

This proves the stated theorem for exactly I minus the three exceptions.

## Replay and limits

[Symbolic checker](../searches/partial-contact-cairo-single-shared-family-obstruction.py)
works over Q(sqrt3)[r] and Q(sqrt3)[z]. It checks closure, all equality roots
with exact interval decisions, the witness reflection identity and all five
determinant factorizations. Strict inequalities are proved explicitly above;
no floating-point endpoint or sampling argument is used. The concrete
fixture checker separately verifies complete polygons and all reflected
witnesses. No solver, random search or timeout inference occurs.

The separate full interval review certifies equality-root completeness, all-parameter privacy, fixed angular filler enumeration and the uniform strict witness. The repaired center formula additionally passed a separate fresh root audit. This is an obstruction family, not a claimed
aperiodic construction or unrestricted solution.

**Fresh audit correction:** the first draft stated z=3 for reflected-center
coincidence; the independent reviewer recomputed the center and found the
correct value z=3w. The explicit formula and symbolic producer now verify
that value. It is outside I, so the obstruction conclusion is unchanged.
