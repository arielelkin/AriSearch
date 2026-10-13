# Fresh hostile review: fourteen-angle fixed-point palette obstruction

Date: 2026-10-13. Independent reviewer: sol, distinct from luna producer/checker.
**Verdict: VALID** for the stated fixed tau=1/100, point-preserving degree3/4
deletion compiler. It excludes two final shapes with at most13 genuine native
corners in total, not arbitrary pairs containing the local pentagon.

## Finite scope and geometric soundness

The domain is precisely every retained source rhomb whose four adjacent
rhombs are present, not just a selected illustrative star. Reconstructing
shared source edges selects35 such rhombs, matching the retained certificate.
At each point the candidate domain is all C(4,3)+C(4,4)=5 retained-ray subsets
before convexity filtering. No source point is shifted further, eliminated,
replaced, or joined to an added graph node. The point-preserving degree3/4
hypothesis is consequential; straight degree2 points and vanished points are
outside this finite model.

The checker reconstructs points in Q(zeta10), verifies every source point is
strictly inside its rhomb, and verifies connecting segments cross shared
source edges internally. Thus cyclic order of the connecting rays agrees
with cyclic source-edge order, using each rhomb's own orientation. Reversing
clockwise source records is necessary and correctly done. Convexity of the
source rhomb and interior crossing place each ray in its corresponding
boundary direction interval; arbitrary drawing-based ray orders are not used.

For consecutive retained rays the normalized exact ratio outgoing/incoming
is their counterclockwise unit sector phase. Positive imaginary part gives
a unique sector in(0,pi); negative imaginary part gives a sector exceedingpi
and is rejected. Real phase-1 means exactlypi and is allowed as a relaxation,
then omitted from the intrinsic palette: a straight face occurrence need
not be a genuine native polygon corner. Phase+1 would mean a degenerate
zero/full sector and is correctly rejected. Therefore partial side hosts
are not silently counted as new native angle values. Retaining every3/4
subset covers all permitted deletions at these points.

## Exact values, signature quotient and exhaustive bound

All26 unit phases are reconstructed from retained raw ratios and source
coordinates; they have positive imaginary part and are pairwise distinct in
QQbar. Hence they represent26 distinct actual angles without branch alias.
Every allowed sector is found in this list. Independently checking the
certificate also confirms every one of the26 ids is used by an actual allowed
choice, so unused extra values do not inflate the claimed geometry domain.

A local choice contributes the SET of its nonflat angle values; repeated
occurrences of one value rightly use only one palette entry. The35 point
constraints have six distinct lists of such sets, with4,3,3,3,4,3 choices.
Any assignment to all35 points restricts to an assignment on one representative
of each list. Thus a lower bound for these six representatives is a necessary
lower bound for the full source patch, regardless of global edge consistency.
Conversely in the independently relaxed model, an optimal representative
choice can be copied to all points with that signature, establishing the
same relaxed minimum. This quotient does not conflate native geometry for
an actual global compiler; it deliberately forgets constraints and therefore
can only make existence easier.

All1296 products of the six signature lists are enumerated directly. Every
union contains at least14 values, and the checker independently finds a
14-value union. The proof relies on that complete solver-free enumeration,
not CP-SAT's reported optimum, a timeout or absent witness. Reflections and
rotations of final polygons preserve their interior angles, so they cannot
provide extra palette values beyond their native corners.

## Coverage implication and density boundary

Two genuine convex polygons with n+m native corners provide at most n+m
distinct native angle values. The required14 therefore excludes every pair
with total<=13 in this compiler's stated domain. It includes5+5 through5+8
and6+6, not just5+6. A pentagon-containing survivor requires h>=9; equality
or repeated angles cannot evade the count. This is only a necessary condition
and supplies no actual9-sided partner or infinite-covering mechanism.

The displayed generalized degree3/4 density equations are correct under
retention of every original rhomb point. With V=N+O(R), E=2N-M+O(R) and
F=N-M+O(R), solving5F5+hFh=2E yields Fh=(3M-N)/(h-5)+O(R) and
F5=((h-4)N-(h-2)M)/(h-5)+O(R). Subtraction gives the curvature identity
F5-(h-6)Fh=2(N-2M)+O(R), nonnegative up to boundary error because N-2M
counts retained degree4 points. These formulas do not cover collapsed points,
point deletions, other face sizes or purely local patches.

## Replay and non-consequences

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/check_penrose_dual_fusion_angle_palette.py

Outcome: PASS, reconstructed35 points/26 angles/six signatures and complete
1296 products; independently attained witness ids
[0,1,5,7,8,10,12,13,14,16,17,20,23,24]. Finite exact algebraic geometry and
set-union enumeration, no solver, seed or timeout required by the checker.
No larger source search is warranted by this negative result.

No claim is made for other tau values, deleting rhomb points, added graph
nodes, changed cuts, high-sided partners or an arbitrary admission of the
local pentagon as a shape. Neither local convexity nor passing monohedral
gates proves global existence or forcing. The full research problem remains
unresolved; reopen this closed compiler only with a changed consequential
hypothesis, not merely a larger patch.
