# Exact monohedral classification on the paired-repeat Cairo stratum

**Status:** freshly independently hostile-reviewed **VALID**; see [review](../reviews/partial-contact-cairo-paired-repeat-classification-review.md). This resolves only a=d,b=c, then supports a
finite equality-pattern reduction for Cairo monotiles. No imported polygon
classification is used.

## Statement

Let w=sqrt3 and let a genuine Cairo pentagon have a=d,b=c, so its native
side word is(a,b,b,a,e) with positive e=wb-a. Then it admits any unrestricted
monohedral plane tiling if and only if

    a=b,  or  b=w*a (equivalently e=2a).              (1)

Every retained case has a periodic monotiling. The proof allows all
reflections and partial contacts, and makes no assertion that every admitted
tiling is periodic.

## Untileability outside the two stated cases

Assume a!=b. Every same-perpendicular90-arm event has equal banks: a
perpendicular arm has bank b, while a b perpendicular arm has bank a.
The two-T switch invariant would make unequal opposing arms require equal
totals2a and2b, impossible. Hence no native arm hosts a T and all arm/arm
contacts from120 endpoints are full equal-length native matches.

Any e side hosting a T must have e=2a or e=2b. Positive closure gives

    e-2b=(w-2)b-a<0.

Thus if e!=2a there are no T anywhere. Every e side must whole-match
another e side. An endpoint type90 cannot coincide with120 in this angle
family, so a whole native arm/e mate is impossible even if lengths agree.
In either physical orientation sign of an e/e mate, its endpoint exposes
two a arms: both e-adjacent corners use a. The third120 sector cannot use
e because a whole e/arm match is impossible. It must be the isolated corner
whose two arms are b,b. In an edge-to-edge tiling those lengths would have
to equal a,a, contradicting a!=b. Therefore no tiling exists outside(1).

## All-equal case

If a=b, all four native arms agree and e=(w-1)a>0. This case is explicitly
periodic by the independently reviewed
[swapped-arm Cairo cone](partial-contact-cairo-swapped-arms-periodic.md):
set its parameters a=c and d=D=a, so both of its shapes are this same
pentagon. The two-species motif is then a monohedral periodic tiling.
This supplies sufficiency on the first stratum without any classification.

## A regular-hexagon carrier for the remaining case

If e=2a, closure wb-a=2a gives b=w*a. Normalize a=1. The shape is

    P=(1,w,w,1,2),

with native vertices

    (0,0),(1,0),(1,w),(-1/2,3w/2),(-1,w).

Center this tile at its isolated120 corner I=(1,w), and take its rotations
through0,120,240 degrees about I. Each tile occupies its entire120 sector
at the center; their interiors lie in disjoint sectors. The paired right
corners at the three internal b/c seam ends give straight banks1+1=2.
The remaining three boundary edges are native e sides of length2. All six
outer corners are120. The union is exactly a regular hexagon of side2,
with centered vertices

    (2,0),(1,w),(-1,w),(-2,0),(-1,-w),(1,-w).

The exact producer independently checks each constituent vertex is in this
hexagon, each constituent area is2w, and their total area6w equals the
hexagon. The verified disjointness makes that union claim exact.

Repeat these three original pentagon faces with lattice periods

    u=(3,w), v=(0,2w), det(u,v)=6w.

For completeness the checker verifies all possible original face/translate
intersections, using inverse-lattice vertex bounding intervals to derive
finite complete integer index ranges and then separating axes of the
convex pentagons. There are exactly28 potentially meeting ordered pairs,
maximum absolute lattice index1, all with disjoint interiors. Since the
three faces have area6w=covolume, periodic mean multiplicity is1; the locally
finite union of closed faces has no uncovered open set, so covers the plane.
Thus this is an actual admitted doubly periodic monotiling, not a finite
patch extrapolation. Scaling by a supplies every b=w*a case.

## Exact replay and remaining scope

[Producer](../searches/partial-contact-cairo-paired-repeat-periodic.py),
[certificate](../certificates/partial-contact-cairo-paired-repeat-periodic.json),
[record](../searches/partial-contact-cairo-paired-repeat-periodic.md).
It checks closure algebra,15 support determinants, all5 lengths, exact
threefold rotations, hexagon containment and area, and all28 complete
lattice comparisons. Arithmetic is exact in Q(sqrt3); no solver or search
is needed.

    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-paired-repeat-periodic.py

This classifies every paired-repeat metric a=d,b=c, including all original
contacts. It does not settle arbitrary two-species combinations of shapes
that are individually untileable. The unrestricted original target remains
open.
