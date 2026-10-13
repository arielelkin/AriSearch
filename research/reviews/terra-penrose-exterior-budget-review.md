# Hostile review: fixed-point exterior-angle budget obstruction

Date: 2026-10-13. Reviewer: terra, independent of author luna.
Claim: research/lemmas/penrose-fixed-point-two-shape-exterior-budget-obstruction.md.
Verdict: VALID on the stated retained-fixture degree3/4 point-preserving domain;
exact checker replay completion recorded separately below.

## Scope and assumptions checked

The source contains the retained marked rhomb fixture, the35 fully surrounded
points have exactly the retained coordinates, and every final network keeps
those points at degree3/4 using only original rays. No extra nodes, cuts,
changed points or degree2 collapse are covered. The final face closures are
actual convex polygons in two congruence classes. Flat sectors are explicitly
permitted and excluded from the required native-angle set.

## Attempts to invalidate the proof

1. A high-sided partner could supply arbitrarily many distinct angles: each
   genuine convex polygon still has total positive exterior angle360. Selecting
   one native occurrence for each distinct required interior angle bounds its
   collective deficit by720, independent of its side count.
2. Repeated angles or reflections could evade that bound: equal angles are
   counted only once, making a weaker necessary budget. Distinct interior
   values require distinct native occurrences. Reflections preserve values.
3. Contact-flat angles could create fake native requirements: the local checker
   ignores phase-1 sectors (exactpi) and rejects zero/reflex sectors. Thus a
   retained flat contact adds no budget and cannot cause the exclusion.
4. Cyclic ray order could change after point deformation: strict point interior
   and strict crossings of each source edge preserve cyclic edge order inside
   the convex rhomb. All those exact inequalities are reconstructed by the
   separate geometry checker. Deletion keeps a subsequence of those rays.
5. Local decisions are globally incompatible: the certificate intentionally
   relaxes global consistency. Every global rule selects an admissible local
   option at every retained point. Excluding ALL relaxed selections is sound.
6. Compressing35 points to6 signatures could miss helpful different choices:
   restrict any global selection to one point of each signature. Its required
   angle union is a subset of the full union. All integer costs are nonnegative,
   so the six-signature lower bound remains valid. Repeating signature choices
   cannot reduce the full union. No source extension is inferred from choices.
7. Normalized algebraic phases could represent distinct branches of an angle:
   all26 phases have positive imaginary part, selecting interior angles strictly
   between0 andpi. The phase map is injective there and exact distinctness is
   checked. Integer floor bounds use cosine monotonicity on the same interval.
8. The floor inequality direction or endpoint could be wrong: delta=pi-alpha;
   cos(delta)=-Re(z_alpha), and decreasing cosine gives c<=cos(d),c>cos(d+1)
   exactly for d<=delta<d+1. Exact algebraic equality at integer thresholds is
   accepted at the lower bound and rejected at the upper bound correctly.
9. More than two-face fusions might bypass the model: arbitrary fusions remain
   covered if points stay degree3/4 on original rays. No pairwise fusion or
   matching assumption enters the budget argument.

## Defects and limitations

No consequential defect or repair found. The finite fixture-occurrence and
fixed-ray premises must remain explicit; this is not a theorem excluding all
Penrose-derived or arbitrary two-shape constructions. Degree2 collapse, new
cuts/nodes, changed point geometry or source instances omitting the retained
fixture require new local constraints. The reusable two-shape720-degree budget
lemma itself has no Penrose or side-count restriction. The837-degree relaxed
finite lower bound gives a strict117-degree gap, not an infinite-covering claim.

## Nondestructive verification

Ran the exact independent checker through the required arisearch wrapper:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/check_penrose_dual_fusion_exterior_budget.py

PASS: all35 geometry constraints,26 distinct phases,6 signatures,1296 unions,
26 algebraic floor inequalities and minimum837 were independently replayed.
No new research domain or source enlargement was run.
