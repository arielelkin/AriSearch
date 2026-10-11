# Independent hostile review of the full sole-shared Cairo interval

**Reviewer:** branching_hexagons, freshly assigned by root. The reviewer audited the earlier isolated fixture, but did not develop this symbolic extension and did not accept it by continuity. No author code was executed or imported. A separate exact checker independently reconstructs every native slot/event comparison and all interval inequalities.

**Artifact:** [symbolic family obstruction](../lemmas/partial-contact-cairo-single-shared-family-obstruction.md).
**Verdict:** **VALID after one minor algebraic correction**, for exactly I=(1/sqrt3,2-1/sqrt3) minus the three named metrics. The corrected author lemma and producer have been freshly inspected. Root independently reconstructed the repaired center calculation from the raw native quadrant tip and axis notch and confirmed it in verify_cairo_single_shared_roots_independent.py. No additional exceptional metric or theorem-strength gap was found.

## Exact scope

Let w=sqrt3 in its positive embedding; r in I; t=2-r. The two Cairo pentagons have side words

    P=(1,r,(3w-r)/2,(wr-1)/2,2),
    Q=((wt-1)/2,(3w-t)/2,t,1,2).

The proof excludes every r outside r0=(2w-1)/(w+2),1,r2=5/(w+2). Neither this review nor the reviewed claim settles those excluded metrics. It permits all isometries, original arbitrary contacts, and omission of a species. It supplies untileability, not an aperiodic construction or a global answer to the original problem.

## Complete native-length and event audit

The reviewer reconstructed both polygons directly with edge directions0,90,150,240,300. Positive-length inequalities, symbolic closure and all30 nonincident supporting-edge determinants hold throughout the open interval. This independently establishes genuine strict convexity; no numerical endpoints or samples are used.

All28 unordered distinct-arm comparisons were checked:12 within species and16 across species. The only identical arm polynomials are Pa=Qd=1. The complete set of interior roots of all other comparisons is precisely{r0,1,r2}, with the named root incidences matching the author. Thus there are no unstated repeated native arms at a generic parameter in the claimed domain.

The checker then constructs all eight oriented native90-corner slots, each specifying its perpendicular arm and collinear bank arm. All36 unordered slot pairings with repetition are compared. Outside the excluded roots, exactly nine right-corner events exist: eight self events and the Pa/Qd cross event. Its banks are r,t and sum2. The two self events whose bank is the common length1 also have total2. All other totals are twice the remaining six distinct private arm values.

Crucially the checker independently compares all36 pairs of these nine event bank sums, rather than assuming that the arm table was sufficient. The only identical-sum class is the three events of total2; every other interior coincidence root lies in the same three excluded metrics. Comparing every event sum with e=2 adds no new generic parameter. Hence singleton private-bank classes, the sole exceptional bank set{1,r,t}, and the e-host restrictions required for the canonical fourfold-cluster proof hold throughout the claimed domain.

Two extra equalities with e occur inside I: Pc=2 at r=3w-4 and Qb=2 at r=6-3w. They are not missing cases. The privacy assertion concerns native90-to120 arms. An e side joins120 to120 and cannot be a full perpendicular90-to120 mate; the endpoint angle inventory prohibits that match even if lengths agree. Nor can these equalities create an unequal arm switch: switches depend on the already exhausted90-corner bank events, not arbitrary side-length equalities. The reviewed private-arm contact theorem explicitly allows e to equal an arm. These two values therefore require no exception.

## Uniform clusters and exhaustive notch continuation

The canonical-cluster proof depends only on the verified angle inventory, native slot privacy, singleton event classes and e-host comparison. Its private Pc/Pd and Qa/Qb rays cannot participate in the sole bank switch or an e-hosted fragment, and therefore remain whole reflected native seams. Their perpendicular private90 corner cannot be a T. The complete fourfold clusters are thus forced at every generic parameter. Neither the existence equivalence of macrotilings nor the fixture's initial fillers is used as an existence proof.

Each individual pentagon has four distinct native arm slots outside the exceptions, so the reviewed one-species private-arm obstruction excludes omission of either species. A hypothetical tiling consequently contains an S(r) host.

All macro boundary angles remain90,120,240 and their side-interior value180. A240 host notch leaves exactly120; it cannot be filled by multiple permitted sectors or a side-interior contact. The fixed length1/2 E-corner edge rays are independent of the parameter. The earlier independent raw16-placement enumeration used only these rays, with each E coordinate affine in the filler width. Its matrices do not change with r or z. Directly the two ray assignments and intrinsic axis reflections give only the same physical fillers at centers(d_r+d_z+1,plus/minus w). No unseen orientation or reflected type appears as the width changes.

The unit breakpoint remains the midpoint of a native e2. The reviewed two-T theorem forces the perpendicular90-to120 seam to be whole; its private bank length z is either Pb or Qc. Only its same native slot can mate, with reflection preserving the90 endpoint. The reflected original tile carries the reflected native canonical center, so the entire reflected cluster is forced. This is a local theorem application at that T, not an assertion that every r/t bank is always whole elsewhere.

## Fresh universal overlap proof and repaired center

In filler-center coordinates the seam point is X=(-wz/2,-3w/2), and the bank direction is(w/2,1/2). The checker constructs the line reflection from this unit vector. It independently verifies the author's W is fixed by reflection and computes all five oriented edge determinants in the actual quadrant pentagon. Each is strictly negative over the entire open interval. The sign proof uses exact algebraic polynomial roots, nonnegative endpoint evaluations and a positive interior value for each negated determinant; it does not use finite sampling or continuity from the fixture.

Because W is an interior point and is fixed by the reflection, it belongs to the interiors of two actual original pentagons in the filler cluster and its forced mate. The reflected center is

    ((9-wz)/4,(3z-9w)/4)=(3w-z)*(w/4,-3/4).

The first draft incorrectly stated that center coincidence requires z=3. The reviewer found the correct value z=3w, and the author corrected the lemma and added the explicit symbolic center identity to the producer. On I the first center component is strictly positive, so the clusters are distinct throughout the claimed domain. Thus the error never affected interval distinctness, but it has been removed from the actual proof. Root independently freshly checked this repair from native coordinates in verify_cairo_single_shared_roots_independent.py, so the reviewer who proposed the correction is not its only auditor.

Distinct canonical clusters cannot share a tile or overlap original interiors. The strict overlap therefore contradicts a tiling. Horizontal reflection excludes the lower filler and z=r,t exhausts both species.

## Independent replay and limitations

[Independent checker](verify_partial_contact_cairo_single_shared_family_independent.py) imports no author code. Arithmetic is Q(sqrt3)[x] with an explicit positive algebraic embedding; Sage AA root comparisons are exact algebraic decisions. It verifies positive lengths, closure,30 strict support inequalities, all28 arm comparisons, all36 native slot pairings, all36 bank-sum comparisons, both harmless arm=e roots, five universal strict overlap inequalities and the repaired center distinction.

Replay:

    conda run --no-capture-output -n arisearch python research/reviews/verify_partial_contact_cairo_single_shared_family_independent.py

Completed output: PASS. No solver, random seed, floating-point acceptance decision, failed deadline or bounded extension search is used. This is an independently checked full-interval proof with explicitly excluded metrics, not extension by continuity. The original two-convex-polygon problem remains unresolved.

## Separate repair audit completed

Root independently reconstructed the corrected center from raw native tip/notch coordinates and verified its symbolic factorization and outside-interval zero. See [root audit](partial-contact-cairo-single-shared-roots-review.md) and its [checker](verify_cairo_single_shared_roots_independent.py), which replayed PASS. The requested separate repair audit is complete.
