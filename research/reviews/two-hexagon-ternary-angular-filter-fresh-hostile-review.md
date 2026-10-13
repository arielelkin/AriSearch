# Fresh hostile review: complementary-ternary angular coverage cut

Date: 2026-10-13. Independent reviewer: sol, distinct from root author.
**Verdict: VALID** for the repaired exact predicate, and for pruning COMPLETE
native angle types in the stated convex-hexagon angular domain. No global
search was run. This certifies an escape cut, not SFT emptiness or joint
geometric realizability of angle assignments.

## Predicate and full reification

For either choice of distinguished species, coverage means its six angles
form three DISTINCT values occurring twice, each strictly between90 and180
degrees and different from120, and the other species has exactly two copies
of each complementary value360-2x. The predicate is symmetric in species and
independent of native word because the reviewed family theorem covers all
native orders and actual metrics. As a MATHEMATICAL coverage theorem, input
angles must satisfy the ordinary hexagon angle sums720 and strict convexity;
the predicate alone is not a polygon realization test.

All15 perfect matchings of six native positions are generated without omission
or duplication: pair the least remaining index with each other remaining
index, recurse on the four remaining positions. A matching passes precisely
when each pair is equal, its three representatives are pairwise unequal,
their values obey the two strict bounds/non120 guard, and each complement
occurs EXACTLY twice among the other six angles. Three distinct complements
with counts2 exhaust the opposite species. Conversely every covered assignment
has exactly such a matching. Thus the disjunction of matching guards is exactly
the point predicate.

The implementation reifies every equality, inequality and complement relation
in BOTH directions by conditioning it and its logical complement. The count
indicator also enforces sum(comp)==2 when true and sum(comp)!=2 when false.
Its negative clause for each matching is exactly the negation of the guard:
any unequal paired positions, equal representatives, failed bound,120 value
or failed complement multiplicity permits that branch; all successful guard
conditions forbid it. There are30 clauses across15 matchings/two species.
No arbitrary Boolean assignment can evade a true covered guard.

A scope gap was repaired during review: the first implementation explicitly
reified only the lower90 bound and relied on positivity of B complements to
infer A<180. The revised implementation fully reifies lt180 and its complement,
then includes the corresponding negative literal. This makes its logical
predicate equal to covered() even for arbitrary integer callers outside the
convex-angle box. The additional control with paired A=(190,200,210) and
negative complements remains feasible, rather than being falsely cut. The
proof's polygon interpretation still requires the independent angular sums
and actual convex input constraints of the global model.

## Exact angle-type invariance, including required negative information

Let T be the COMPLETE set of unordered native triples summing360 for a covered
legal hexagon angle assignment. Choose its distinguished species and the three
paired native classes. T contains all34 base native triples:8 pureAAA,8 pureBBB
and18 mixedAAB. The same34 equations hold at EVERY other realization of T.

Swapping either native occurrence within a pure star forces the two angles
of its class equal. The pureAAA equation gives x+y+z=360. Each mixed identity
with two copies of one chosen A corner gives its B complement360-2x. Thus the
core equations force precisely the two-dimensional complementary family.
The independently checked homogeneous native matrix has rank10 and the
explicit twelve-by-two family basis spans its entire kernel; arbitrary native
reorderings/species exchange only permute its coordinates.

The strict-convex B box0<r_i<180 then forces90<x_i<180. Because the ORIGINAL
covered point has x_i!=120, T excludes the repeated native triple(a_i,a_i,a_i).
Exact realization of the SAME T therefore cannot acquire x_i=120. Likewise,
if x_i=x_j, the pure-family sum forces2x_i+x_k=360 for the remaining k, so
(a_i,a_i,a_k) would become a new triple. That triple is absent from T at the
original distinct point. Exactness therefore also forbids such merging. Every
legal-angle realization of this EXACT T stays covered by the predicate,
regardless of polygon metric or realization existence.

Positive core equations ALONE do not enforce distinct/non120 values: an
ancestor or partial triple language can acquire extra triples on degeneracy
lines. The absence equations of complete T are consequential. This review
does not authorize pruning incomplete/noncovering ancestors merely because
one representative is covered. It preserves the distinction between exact
type coverage and angle-grid feasibility or actual closed polygons.

## Six sole-ABB strata and both species

Coverage deliberately includes the six ordered Ai=4Aj-360 lines, i!=j,
with pairwise distinct/non120 A values. The reviewed56-type ledger shows the
only added type star there is Ai Bj Bj. Sparse nonnegative corner-potential
removal supplies an actual base-star-used field; reviewed all-native escape
proofs then supply a periodic admitted tiling. Unused additional allowed
triples are not mistaken for a generic complete angle language.

The supplemental controls use each ordered line with Ai=124,Aj=121,Ak=115,
all six complementary values distinct. Both species orders and grids1,7 are
fixed and tested,24 cases. Their complete native languages contain40 triples
(core34 plus six added native variants) and have rank11, while the core still
has rank10. Hence the review does NOT infer that every covered full type has
rank10. Each full type excludes all native degeneracy triples used in the
invariance proof. Generic-family controls and rank10 apply separately.

## Replay and proof scope

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_ternary_angular_filter.py
    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_ternary_angular_filter_resonances_independent.py

Both outcomes: PASS. Original8100 native labelled arrangements,12 fixed
miniature CP controls and the34-star core kernel; supplemental24 ABB/species/
grid controls and six repaired-boundary controls. All CP models FIX all12
angles and use one worker. No global angular/SFT search, timeout, polygon
closure, or claim of global infeasibility was run. The infinite-domain Boolean
soundness and complete-type invariance are established by the proofs above,
not extrapolated from those finite controls.

This cut removes angular families already proved incapable of aperiodicity
whenever actual polygons tile. Such a family may have nonempty abstract SFTs
and periodic plane tilings; neither is asserted empty. The original research
problem and uncovered angular types remain unresolved.
