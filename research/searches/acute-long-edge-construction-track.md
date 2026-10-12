# Parallel construction track: acute pentagons with genuine long-edge contacts

Date: 2026-10-12. **Active exploratory track.** This record follows the
explicit feature -> small exact family -> immediate periodic attack order.
No viable aperiodic pair, full-plane carrier, substitution, or unrestricted
forcing theorem has been established. A valid local module is a geometric
feature, not an existence proof. The construction track remains separate
from the completed narrow hexagon impossibility census.

## Feature chosen before enumeration

The current seed has native angle word

    (60,60,150,120,150) degrees.

Unlike the previous failed word, it has two acute corners. The native long
side between those two 60-degree corners can have genuine interior
contacts. Both flat180+60+120 and flat180+60+60+60 are legal. Reflections
are part of the permitted tile set and are essential in the explicit
four-tile acute module below.

The construction is not a full spoke dualization of a source tiling,
not a finite cut within the earlier marked-rhomb domain, and not an
all-obtuse-hexagon mechanism. It constructs polygon coordinates directly.
The missing global work is stated explicitly rather than replaced by a
source patch or unproved compiler.

## Exact positive three-parameter polygon family

Put r=sqrt(3). Choose c,d,e>0 with c<d+r*e, and define

    b=e+(d-c)/r,
    a=e+(c+2d)/r.

The five directed edge vectors, in native order, have lengths(a,b,c,d,e)
and directions(0,120,150,210,240) degrees:

    (a,0),
    (-b/2,r*b/2),
    (-r*c/2,c/2),
    (-r*d/2,-d/2),
    (-e/2,-r*e/2).

They close exactly. Their successive exterior turns are
120,120,30,60,30 degrees, giving the stated genuine native corners.
Positive lengths and the single full turn make the closed polygon strictly
convex; the exact checker also verifies every global supporting half-plane.
The long side a exceeds each of b,c,d,e throughout the positive domain.

The reviewed Rao-table monohedral gate gives only two possible periodic
monohedral loci:

    c=e, or b=d.

The other angle-compatible Type2 systems c=a,d=a have no positive metric
solution. Types5 and8 force a=b,a=d or a=e, also impossible. The generic
family therefore avoids the imported monohedral classification after these
two loci are removed. This does not prove it tiles with a partner or avoid
mixed periodic tilings. The primary-classification import remains separate
from its exact algebraic application here.

## Controlled three-tile A/A/B endpoint module

For A choose e_A,d_A>0 with d_A>e_A and

    ((3+r)*e_A+(r-1)*d_A)/2 < c_A < d_A+r*e_A.

Set a_A,b_A by the family formulas. Define

    e_B=a_A-d_A,
    a_B=c_A,
    c_B+2*d_B=r*(c_A-e_B),

with positive c_B,d_B and b_B=e_B+(d_B-c_B)/r>0. The upper cone makes
c_A>e_B, so positive choices exist. As an immediately checkable subfamily,
set c_B=d_B=r*(c_A-e_B)/3, giving b_B=e_B. Remove all monohedral loci
for both tiles; no generic metric solution is being presumed.

A concrete exact pair is

    A:(c,d,e)=(4,3,1),
      (a,b)=(1+10/r,1-1/r);
    B:(c,d,e)=(t,t,E),
      t=2*r-10/3, E=10/r-2,
      (a,b)=(4,E).

All sides are positive and both shapes avoid c=e and b=d. Let A sit with
its long a side from(0,0) to(a_A,0), and put q=(d_A,0). Place a copy of A
rotated by-30 degrees with its native120-degree corner3 at q, and a copy
of B rotated by300 degrees with native60-degree corner0 at q. Their
native d_A and e_B sides cover the two parts of the source A long edge.
Their internal native c_A/a_B seam is a full matching side of length4.
The junction at q has sectors180+120+60 and the three polygons have
pairwise disjoint interiors.

At the three other endpoints the attached native corner sums are210,
leaving150-degree sectors available from the family. Thus this module
avoids the earlier impossible30-degree endpoint gap. It does not assert
that all those sectors can be filled simultaneously in a full-plane tiling.

## Genuine four-tile acute partial contact

This module exists for every positive seed P. Put q=(a-e,0), strictly
inside its long a side. In addition to the source P, place three copies
with native corner0 at q:

    rotate180(P),
    rotate300(reflect(P)),
    rotate300(P),

where reflection is(x,y)->(x,-y). Their 60-degree sectors partition the
lower half-plane at q and give the genuine four-tile junction

    flat180 + 60 + 60 + 60 = 360.

The reflected middle copy shares its whole native e side with the first
copy and its whole native a side with the third. The three child interiors
are disjoint, and all are below the source's long-side line. The short
outer e side ends exactly at the source long-edge endpoint. The other
outer a side extends past the source's left endpoint.

Remaining endpoint gaps are120,150,60,240 degrees. They have available
native decompositions120;150;60;120+120 respectively. This is a concrete
endpoint-safe higher-valence feature; availability of those sector
angles is weaker than simultaneous metric completion and global existence.

## Immediate attacks completed before a larger search

1. **Monohedral escape gate:** c=e or b=d, as above, with rotations and
   reflections included. The retained exact pair avoids both.
2. **Endpoint geometry:** exact closure, every global strict convexity
   test, both modules' native seams, and pairwise interior disjointness
   pass exact arithmetic checks.
3. **Small mixed periodic quotients:** the four-face full-side gate
   checked216 pairings/chirality patterns (144 connected cross-seam cases),
   with no flat torus. The long-side atomic version checked3240 pairings/chirality
   patterns with the A a side split into d_A+e_B, also with no flat torus.
   These are bounded controls, not exclusions of arbitrary periodic
   tilings or evidence of aperiodicity. No larger search has been started.

The full-side control includes every full-side pairing in the exact length
classes; its connected cases have A c/B a cross seams. The atomic
control considers all pairings of the exact atomic length classes in two
A and two B faces. Longer subdivisions, different tile counts, and other
partial-contact motifs remain outside those controls.

## Exact cap recurrence arrests after six copies

Apply the same acute cap operation to the first half-turned tile's long
side. Its cap point is the original source origin. One child is exactly
the already present source polygon. The two additional children are

    rotate120(reflect(P)) at the original origin,
    rotate120(P) at the original origin.

All six resulting tile interiors are disjoint. Two long a sides overlap
with offset e; their unmatched tails are covered by neighboring e sides.
The other four tiles occur in two full a/a pairs, with seam directions120
and300 degrees. Every long-side occurrence is already covered. A cap on
one of those full a/a seams would insert children into the neighbor's
interior. Thus the specific cap operation has no further propagation:
it is a finite six-copy cell, not an expanding hierarchy.

For the exact A sample, cancellation of the internal seams leaves a
simple18-edge boundary. There is a concrete periodic strip completion of
these cells: translate by

    T=(1+5*sqrt3/3,1+sqrt3).

Adjacent cells share exactly one full c=4 boundary edge, with no interior
overlap or additional isolated contact. If W is the projection width of
one cell in direction T, exact inequalities give

    |T|^2 < W < 2*|T|^2.

Therefore cells separated by two or more periods are strictly separated
by projection. All integer translates form a connected periodic strip
with two unbounded boundary chains, rather than a full-plane tiling.
This positive construction is exact; it makes the cap-only carrier
periodic instead of supplying an aperiodic existence route.

A plane covered only by these A cells would give a monohedral A tiling,
which the imported monohedral gate excludes for this exact sample. A
mixed completion needs a separate B-boundary operation. In particular
one cannot choose only the intended partial long sides while ignoring
geometrically admitted full long-side pairs. A typed carrier would need
an actual species/endpoint theorem distinguishing those states.

## The earlier feature that was rejected

The first trial used angle word(90,150,90,150,60) and the exact family

    b=e-(a+c)/r, d=e+(a-2c)/r,
    P=[(0,0),(a,0),(a+r*b/2,b/2),
       (r*d/2,(b+r*c)/2),(0,e)].

Its initial golden long-edge module ended a short side at a150-degree
corner inside a partner's straight edge. The remaining sector was30
degrees, below the minimum native angle60. Thus that proposed local
carrier could not extend.

A revised reflected five-tile cap repaired that local endpoint but failed
a global tight-inventory gate. Give native60 corners weight2, native150
corners weight-1, and native90 corners weight0; flat sectors have weight0.
Every such pentagon has weight zero. Every allowed vertex star has
nonnegative total weight. The only acute-containing zero-weight star is
150+150+60. In particular a flat180+60+60+60 cap has weight6 and must
have zero intensity in every invariant tiling measure (or O(R) count in
large windows by the corresponding corner sum). Such a cap can occur as
a sparse defect; it cannot be forced at bounded gaps by a hierarchical
carrier. This is not a claim that every original tiling is defect-free.

The fixed golden cap also failed its intended linear-inflationφ area
route: its area ratio lies strictly between3/4 and4/5, whereas a positive
integer two-shape substitution with area factorφ² has ratiosφ or1/φ.
More fundamentally such a substitution has a parent made from only two
convex pentagons. Two genuine convex pentagons cannot fuse into a convex
pentagon: a convex union requires a full shared side, yielding eight
boundary vertices with at most two straight interface-endpoint reductions,
so at least six genuine corners remain. Thus merely tuning the area
cannot rescue that two-child stationary substitution route.

These failures were used to change the geometric feature before
enumerating a larger family. The current two-acute word has one spare
acute corner per tile after the150-pair ledger and avoids the former
zero-intensity acute-cap obstruction.

## Existing dissection obstruction constrains the carrier scale

The already reviewed [general convex-pentagon dissection theorem](../lemmas/pentagrid-golden-metric-small-substitution-obstruction.md)
requires at least six children in any nontrivial individual pentagon image.
The current two-acute angle inventory independently excludes two/three
children by its150-corner ledger, but that special argument is weaker
and does not enlarge the existing six-piece obstruction.

For a finite protoset with common similarity factor lambda and **every**
parent image nontrivial, the minimum-area parent yields lambda>=sqrt6.
Single-child images mapping to a differently sized similar prototile need
separate treatment; no unconditional scale bound is inferred. For an
area-phi pair, ordinary linear inflations phi and phi^2 require2/3 and5/8
children respectively, so the existing six-piece theorem blocks those
specific carriers. Larger or compound carriers remain unconstructed.

For the retained exact A/B sample the nontrivial-image hypothesis follows
from nonsimilarity. Its unique120-degree corner must map to the unique120
corner under any similarity, including reflections. The adjacent side
ratio is c_A/d_A=4/3 (or3/4 after reflection), whereas c_B/d_B=1. Thus the
two shapes are not similar. A one-child image at lambda>1 can be neither
a same-size copy of its own prototile nor the other nonsimilar prototile.
Consequently every ordinary substitution image for this exact sample is
nontrivial and its common linear inflation must satisfy lambda>=sqrt6.
This sample-specific conclusion is not asserted for all parameter choices.

## What a credible construction still requires

No full-plane tiling by the retained pair has been proved. The next positive
step must give actual covering geometry: either complete a finite periodic
contact carrier (which would immediately falsify this pair as aperiodic),
or construct a nonperiodic infinite covering or a verified expanding
supertile system. Angle sectors and area relations alone do not provide it.

If a covering survives the periodic attacks, a second, independent theorem
must force every unrestricted tiling, with reflections and partial contacts,
to decode the intended hierarchy. In particular all the residual120/150
endpoint completions need forced choices and all unintended direct/mirrored
seam assemblages need exclusion. That forcing theorem is not established
by these modules. Until both existence and unrestricted forcing are proved,
the retained pair is an exploratory geometric seed, not a credible positive
solution of the target problem.

## Artifacts and replay

The [exact feature checker](../reviews/verify_acute_long_edge_construction_features.py)
imports no solver or construction producer. It verifies the pair's exact
native angles/convexity, the three/four-tile placements and all relevant
seams, using Q(sqrt3), and independently checks the old nonnegative
corner-potential budget and the fixed golden area interval. The
[feature certificate](../certificates/acute-long-edge-construction-features.json)
retains exact coefficient vectors and all local polygon coordinates.

    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python3 research/reviews/verify_acute_long_edge_construction_features.py --check research/certificates/acute-long-edge-construction-features.json


The [bounded four-face checker](../reviews/check_acute_long_edge_four_face_periods.py)
retains all216 native and3240 atomic cases in
[its control certificate](../certificates/acute-long-edge-four-face-period-gate.json).
It proves only that those specified finite quotient domains have no flat
torus. The exact feature checker now also retains the six-copy boundary
and the infinite periodic strip proof; its certificate was regenerated.

    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python3 research/reviews/check_acute_long_edge_four_face_periods.py --check research/certificates/acute-long-edge-four-face-period-gate.json

## Exact transverse bridge obstruction

The six-copy strip has four exposed native c=4 sides per period. Attach
the reflection-symmetric B by its full a=4 side outside each. Its geometry
is uniquely determined, including reflected placements. Two attachments
intersect A tiles in the adjacent strip period with strictly positive
area; the feature certificate retains exact intersection polygons and
points strictly inside both tiles. The other two fit locally. Thus the
natural full-c/B-a bridge cannot complete this strip. This does not
exclude A/A contacts, subdivided sides, other strips or arbitrary plane
tilings. No full-plane existence or unrestricted forcing has been proved.
