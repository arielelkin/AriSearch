# Complete periodic escape for binary two-run B with paired qq corners

Status: **VALID after [fresh whole-family synthesis review](../reviews/branching-hexagon-two-run-paired-qq-classification-review.md).** The forward single120, forward mixed-homogeneous and separate reversed-qq slices are independently VALID. This is a complete specified family of A/B pairs with B's qq corners exactly120±2delta, not a classification of arbitrary B qq geometry or the unrestricted target.

## Exact scope and canonical statement

Let0<delta<30 and take A with native lengths(p,q,p,q,p,q), p,q positive and distinct, and directions

    (0,60+delta,120,180+delta,240,300+delta).

Let B be any strictly convex hexagon with native length word(p,p,p,q,q,q), all six sides retaining their native indices. Assume its two qq native angles form the unordered pair{120-2delta,120+2delta}. Reflections are allowed in the tiling convention.

Normalize q1 by common scaling. If necessary reflect and reindex B so that its qq corner order is chi=120-2delta,psi=120+2delta. Write alpha=B1,beta=B2 for its ordered pp angles, and B0,B3 for its mixed angles. This canonical reflection swaps both pp and qq orders and both mixed angles; it does not identify their numerical orders silently.

**Theorem. The pair is tileable if and only if its canonical B belongs to one of the two following reviewed periodic cones. Every tileable pair in this whole family has a doubly periodic tiling.**

1. Equal pp angles:

       beta=alpha, 60+delta<alpha<180,
       p=2cos(delta)/(1-2cos(alpha)),
       (B0,B3)=(240-alpha-delta,240-alpha+delta).

   This is the equal-pp cone with gamma=180-alpha. Exclude p1 in the stated distinct-length scope.
2. Complementary pp angles:

       beta=180-alpha, 60-delta<alpha<120-delta,
       p=2cos(delta),
       (B0,B3)=(240-alpha-delta,60+alpha+delta).

The B qq angles in both alternatives are the fixed canonical pair. These formula lists determine its strictly convex geometry up to congruence. Both whole cones have independently reviewed exact periodic quotients and flat-cover proofs; no positive inference is made from an angle-frequency or seam primal alone.

## Closure geometry follows from the paired qq condition

Rotate canonical B so its side0 has direction0. Its first three p directions are

    0,180-alpha,360-alpha-beta,
    P=1-exp(-i alpha)+exp(-i(alpha+beta)).

The qq turns are60+2delta and60-2delta. Write its q directions as

    rho+120-delta,rho+180+delta,rho+240-delta.

Their unit vector sum is-2cos(delta)exp(i rho). Whole B closure therefore gives

    pP=2cos(delta)exp(i rho).

In particular P cannot vanish; p=2cos(delta)/|P|, and rho is the actual lifted phase determined by B's ordered native directions. The mixed angles are

    B0=60+rho-delta,
    B3=420-rho+delta-alpha-beta.

Strict convexity forces delta-60<rho<delta+120 together with0<B3<180. On the two forward pp-homogeneous slices the p-chain has positive real and imaginary parts, hence the actual lift necessarily agrees with the principal phase0<rho<90 used in their complete slice lemmas. On reflected slices the separately derived reversed mixed-angle formulas, not an assumed unchanged phase convention, apply.

## No homogeneous pp star: actual double-end theorem applies

The four possible homogeneous qq triples have angle sums360-6delta,360-2delta,360+2delta,360+6delta. None sums360 because delta>0. Thus there is never a legal homogeneous qq star in this family.

Suppose also that no pp homogeneous star is legal. The actual AAq seam possibility can then be excluded exactly. At either endpoint of a shared A q side, the third corner is pp and thus belongs to B. The two A endpoint angles are either H/H at one end and L/L at the other, or H/L at both ends. The latter would demand a native B pp corner120, permitting a forbidden homogeneous triple of that corner. The former demands pp angles120-2delta and120+2delta. Consequently an AAq seam would force the unordered pp pair to equal the unordered qq pair.

For that pair the first-three-unit-edge p-chain norm is exactly the q-chain norm. In general

    |P|^2=3-2cos(alpha)-2cos(beta)+2cos(alpha+beta).

Substituting alpha,beta=120∓2delta gives

    |P|^2=2+2cos(2delta)=4cos(delta)^2.

Positive closure therefore forces p=q, contrary to the scope. Hence actual AAq contact is impossible.

All hypotheses of the independently VALID double-end periodic reduction now hold: no homogeneous pp or qq star, AAq impossible, and distinct lengths. That theorem uses an actual saturated ETE limit obtained from the reviewed boundary count and defect extraction, then both endpoints of an actual whole B middle-q side and an actual outside-p seam. Its conclusion is precisely the two canonical periodic cones displayed above. This import does not assume equal species frequencies in each tiling, or turn O(R) defects into pointwise statements. The no-homogeneous case is thereby complete.

## Homogeneous pp stars: all four planes and both qq orders

A pp corner triple chosen with repetition from alpha,beta sums360 exactly on one of the four planes

    alpha120; beta120; 2alpha+beta360; alpha+2beta360.

There are no other homogeneous pp triples. The independent forward and reversed slice computations exhaust these planes with their intersections, not only generic points. Each retains every angle-legal indexed native star and its exact signed native seam features, leaves both species frequencies free nonnegative, and has negative per-tile duals for each rejected stratum. They apply to unrestricted contacts through the reviewed actual defect-free trivalent ETE limit.

At the fixed canonical qq order(low,high):

- alpha120: the forward single-120 complete slice says tileable exactly at beta120, giving p=cos(delta), the equal-pp first curve.
- 2alpha+beta360: the forward mixed-homogeneous complete slice says tileable exactly at alpha=beta120, again that first curve.
- beta120: reflect B. The reflected pp order is alpha'=120,beta'=alpha and its qq order is(high,low). The reversed single-120 complete slice says beta' is60 or120. Thus the original canonical pair is(alpha,beta)=(60,120) or(120,120).
- alpha+2beta360: reflect B. Its reversed pp order satisfies2alpha'+beta'=360. The reversed mixed-homogeneous complete slice says alpha'=beta'=120, so the original is(120,120).

The reflection/reindexing is exact: new sides correspond to old sides(2,1,0,5,4,3), and new native vertices to(3,2,1,0,5,4). Thus

    (B0,alpha,beta,B3,chi,psi)
       ->(B3,beta,alpha,B0,psi,chi).

There is no claim that a forward plane automatically covers its pp-swapped plane at the same qq order. The two reversed slice computations supply that missing scope.

The two homogeneous survivors are already in the stated cones: alpha=beta120 is the equal-pp cone at gamma60; alpha60,beta120 is the complementary cone at alpha60, which satisfies60-delta<60<120-delta for every0<delta<30. Every other canonical homogeneous pp case is untileable by the retained exact duals and actual closure filters. This proves necessity on all four planes and sufficiency by the existing periodic quotients.

## Boundaries of this synthesis

This is a whole family theorem with0<delta<30, both lengths positive and distinct, B binary two-run, and the exact unordered qq pair prescribed by A. It includes no-homogeneous strata, all four homogeneous pp planes, their intersections and the relevant native reflection orders. It excludes neither arbitrary qq geometry nor equal lengths. Positive constructions themselves remain valid where their own cone permits equal lengths, but no negative classification is asserted there.

Dependencies are the reviewed actual trivalent ETE limit and seam-boundary invariant; the equal/complementary periodic cone theorems; the double-end no-homogeneous reduction; the forward single120 and forward mixed-pp complete slices; and the separate reversed-qq homogeneous slice theorem. All listed dependencies and this synthesis have received fresh independent VALID reviews. No solver-only outcome, finite no-witness result or unreviewed transport manuscript is used.
