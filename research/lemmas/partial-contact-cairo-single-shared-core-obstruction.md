# The specified sole-cross pattern Pa=Qd: an exact obstruction whenever the private cores are forced

**Status:** freshly independently hostile-reviewed **VALID**; see
[review](../reviews/partial-contact-cairo-single-shared-core-obstruction-review.md).
This extends the earlier fixed one-parameter notch obstruction. It gives an
unrestricted obstruction under explicit contact hypotheses, and a finite
exceptional-stratum reduction for the specified internally distinct
sole-cross pattern Pa=Qd. It does not classify the remaining exceptional strata.

## Exact statement and sufficient metric hypotheses

Let w=sqrt3. Let the two Cairo pentagons, with the usual directions
0,90,150,240,300 degrees, have words

    P=(s,b,c,d,e), Q=(A,B,C,s,f),

with all lengths positive and the Cairo closure identities. Assume each
species has four distinct native arms and their only cross-species arm
length equality is Pa=Qd=s. In particular the four core arms c,d,A,B are
globally private native arm slots. All original isometries and arbitrary
partial contacts are allowed.

If

    b+C is unequal to each of 2c,2d,2A,2B,
    e and f are each unequal to each of 2c,2d,2A,2B,

then P,Q admit no plane tiling, even allowing omission of a species.
Equivalently any tileable internally distinct pair with this specified sole shared
native arm must lie on at least one of the twelve explicitly listed
hyperplanes b+C=2x, e=2x or f=2x, x in {c,d,A,B}. Some hyperplanes may be
inconsistent with positivity or exact arm privacy; no existence is asserted.

More intrinsically, the geometric obstruction only assumes that every P
is forced into the fourfold reflected cluster centered at its native c,d
right corner, and every Q into the analogous cluster at its native A,B
right corner. The displayed metric hypotheses are sufficient for that
property; no assumption is made about the remaining contacts.

## Why the fourfold clusters are forced

Use the reviewed [two-T switch invariant](partial-contact-cairo-two-t-switch.md).
The complete native right-corner event bank multisets are

    {s,s}, {b,b}, {C,C}, {b,C},
    {c,c}, {d,d}, {A,A}, {B,B}.

The first event can have either species' perpendicular slot, but its banks
remain s,s. Distinct individual arm values make every self-event total
unique among self-events. The only possible different-bank collision for
a core self-event is with b+C, explicitly excluded. An unequal opposing
arm ray using a core arm would require precisely such a collision, hence
cannot occur. A core arm cannot face an e-hosted fragment either: its T
bank event would be its self-event, forcing e or f equal to twice that
core arm, also excluded. Thus each core arm whole-matches the same native
slot, with 90 and120 endpoints preserved, by seam reflection.

At a P c,d right corner, a T would have bank total 2c or2d. An e/f host
is excluded. An arm host would force a two-T switch with another bank
multiset of that same total; none exists. Thus four90 sectors meet.
The two perpendicular reflected seams generate exactly four P copies
sharing this native corner. The analogous argument gives four Q copies
at each A,B right corner. Each original tile belongs to exactly one such
cluster, so these clusters partition any hypothetical original tiling.
This is a necessary forced partition, not an assumed grouping.

## The actual macrogeometry and the notch contact

Native reflection sends Q to M(Q)=(s,C,B,A,f). Both macro shapes can
therefore be expressed as four axis reflections of a first-quadrant
pentagon with word (s,h,k,l,g). The quadrant vertices are exactly

    (0,0), (l,0), (l+g/2,w*g/2),
    (l+(g-s)/2,w*(g+s)/2), (0,k).

They follow directly by rotating a native pentagon about its private
right corner. Their axis-reflected union has four convex90 corners,
four convex120 corners and four reflex240 notches. At a right-axis notch
(l,0), the two boundary segments both have length g; every convex120
macro corner has incident native lengths s,g. The original five angles
and positive sides ensure the quadrant is convex and occupies its quadrant.

A macro240 notch must be filled by exactly one macro120 corner: no side
interior or sum of two available corners can occupy the remaining120.
After choosing either reflection sign, its incident sides s and g_G align
with the host's two g_H sides.

The s side must end strictly inside the host g_H side. If s>g_H, the host
original120 endpoint would lie inside the filler native side, impossible.
If s=g_H, its original90 endpoint would coincide with that original120
endpoint, also impossible. At s<g_H its90 endpoint is a T on the host's
native e/f side. The perpendicular arm of that filler90 corner is h,
which is Pb=b or Qc=C. It is globally private, so the whole perpendicular
mate is the identical native slot of the same species. Both T banks have
length s. The reviewed e-host event rule therefore forces g_H=2s.

The other incident side has length g_G. If g_G<g_H, its ending macro240
notch would lie inside the host boundary segment, requiring more than360
around that point. If g_G>g_H, the host's original120 endpoint would lie
inside its native side. Consequently g_G=g_H. The two orientation signs
are mirror images and obey the same argument.

Each species is monohedrally untileable by the reviewed private-arm theorem,
so both occur in any tiling. Applying the notch argument to their clusters
forces

    e=f=2s.

No contact exclusion or event genericity beyond the forced-core hypotheses
was used in this geometric step.

## The forced reflected mate always overlaps a constituent

Scale s=1. A macro of either filler type is then S(z), where

    (1,z,(3w-z)/2,(wz-1)/2,2),
    1/w<z<3w.

These bounds are exactly positivity of its two private core arms. Choose
the upper notch placement and put the filler center at0. Its shared-arm
endpoint is X=(-wz/2,-3w/2). The T's private perpendicular seam forces a
reflection of an actual filler constituent across the line through X at
angle30. The canonical cluster containing that mate is the reflection of
the filler cluster across the same line. This follows from the intrinsic
private right corner, rather than any choice of macro subdivision.

Take the actual lower-right constituent with clockwise vertices

    A0=(0,0), A1=(d,0), A2=(d+1,-w),
    A3=(d+1/2,-3w/2), A4=(0,-c),
    d=(wz-1)/2, c=(3w-z)/2.

The reflection line has equation

    -x+w*y=(wz-9)/2.

Its signed values at A0 and A2 straddle this line strictly, since z<3w
and z>1/w. Thus the exact point

    W=lambda*A2, lambda=(9-wz)/(wz+7),

is fixed by reflection and 0<lambda<1. A0 and A2 are nonadjacent vertices
of a strictly convex pentagon, so W is strictly inside this constituent.
It is therefore strictly inside both that constituent and its reflected
copy. This is an overlap of original convex tile interiors.

The reflected cluster is distinct: its center is

    ((9-wz)/4,(3z-9w)/4)=(3w-z)*(w/4,-3/4),

which is nonzero throughout the positive interval. The forced canonical
partition therefore makes the overlap impossible. The lower notch placement
is a mirror image. This proves the obstruction.

## Exact computation, scope and review boundary

[Producer](../searches/partial-contact-cairo-single-shared-core-obstruction.py)
checks the general quadrant identity from raw native coordinates, all
symbolic event banks, closure of the normalized family, the reflection
axis, exact fixed point and all five strict supporting determinants.
The finite scope is algebraic identities and sign factorizations on the
full open interval; no patch search, timeout, numerical inequality or
existence inference is involved. The linked no-author-import independent checker has passed.
Mixed e-adjacent/isolated shared slots and two isolated shared slots are
separate native pattern orbits outside this theorem. The remaining core-event resonances e/f=2x or b+C=2x are not covered.
