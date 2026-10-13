# Fresh hostile review:837-degree requirement exceeds a two-polygon budget

Date: 2026-10-13. Independent reviewer: sol, distinct from root/luna producer.
**Verdict: VALID** for all two-convex-polygon compilers in the fixed tau=1/100,
point-preserving degree3/4 domain. This excludes high-sided partners in that
same domain, not arbitrary pairs containing the local pentagon.

## Reusable mathematical bound

For any genuine convex polygon, positive exterior deficits pi-alpha sum to
2pi over its native corners. Given distinct required interior angle values,
choose one actual native occurrence of each from the two polygons. Distinct
values cannot choose the same occurrence, so their exterior sum is at most
4pi. Repeated angles and unused native corners consume additional positive
budget rather than enlarging it. Rotations and reflections preserve alpha.
If a tiling omits one polygon, allowing both polygons' full budget is only a
relaxation; contradiction with4pi still excludes it. Flat sectorpi has deficit0
and is correctly ignored as a side-interior host, not a genuine native corner.
The bound has no side-count limit and needs no density or periodicity theorem.

## Geometric domain is the reviewed fixed local relaxation

The previously reviewed geometry certificate reconstructs all35 complete
four-neighbour rhomb points, all3/4-ray subsets,26 exact distinct nonflat
angle values and six choice signatures. Every point must remain an intrinsic
degree3/4 graph vertex with unchanged surviving original rays. Larger clusters
and multiple equal-shape dissections remain allowed; no false pairwise-fusion
restriction is used. A final convex face with a nonflat sector at such a
point has that sector as an actual native corner angle. Thus the union C of
selected sectors is necessarily among the final shapes' native angle values.

Selecting only six representatives of repeated signature constraints is a
necessary independent-choice relaxation, justified in the earlier hostile
palette review. It cannot inflate the lower bound relative to an actual
compiler: its representative angle union is a subset of the actual full
patch requirement. Possible global deletion inconsistencies only remove
assignments and cannot supply a cheaper union. Degree2 straight collapse,
point elimination, new graph edges/nodes and changed point coordinates remain
outside this model; the theorem does not discard those reopening hypotheses.

## Exact lower bounds and complete finite cost enumeration

Each phase z=exp(i alpha) has alpha in(0,pi), so delta=pi-alpha is also in
(0,pi), where cosine strictly decreases. The displayed comparisons
-Re(z)<=cos(d degrees) and -Re(z)>cos((d+1) degrees) are exactly equivalent
to d<=delta_degrees<d+1. The weak lower and strict upper comparisons are
correct even for an integer-degree deficit. Thresholds are exact real parts
of powers of the360th root of unity, and AA comparisons have no tolerance.
Floating candidates are not trusted; every one of the26 retained integers
is independently certified before entering the cost calculation.

For each of all1296 signature products, use the SET union of selected ids
and add their certified integer lower bounds. This pays each distinct required
angle once, exactly as in the reusable budget lemma; duplicate occurrences
cannot falsely strengthen the bound. The checker reproduces the entire
cost histogram, obtains minimum837 and verifies its independently enumerated
witness C={0,2,3,5,7,8,10,12,13,14,16,17,20,23,24}.
Every actual deficit sum is at least this integer sum. Since837>720, every
possible local representative union already exceeds4pi, and no two genuine
convex shapes of ANY finite side counts can implement the stated compiler.
The result does not rely on a numerical estimate being837, CP-SAT optimum,
rounding to nearest degree or absence of a bounded-search witness.

## Replay and non-consequences

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/check_penrose_dual_fusion_exterior_budget.py

Outcome: PASS. Reviewed geometry is reconstructed first, all26 floor pairs
are checked in exact algebraic arithmetic, and all1296 integer costs and their
histogram are replayed without producer imports or solver calls. No random
seed, timeout, source enlargement or finite-to-infinite assertion is needed.

This supersedes only the14-angle bound's side-count limitation: h>=9 no
longer survives in the SAME fixed-point degree3/4 compiler. It does not
invalidate the exact local nonmonohedral pentagon, rule out compilers changing
those consequential assumptions, or solve the original two-convex-tile
problem. The closed fixed compiler must not be reopened merely by increasing
partner side counts or source patch size.
