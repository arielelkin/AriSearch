# Exact boundary completion and fixed residual rhombs

**Status:** boundary geometry has a [VALID fresh audit](../reviews/pentagrid-robinson-boundary-geometry-review.md), including independent exact clipping. The residual-rhomb search completed its finite domain with positive cluster witnesses; its [fresh full audit](../reviews/pentagrid-robinson-residual-rhombs-review.md) is VALID, with all positive witnesses checked independently and all17 negatives independently replayed. No
source arrows, whole-plane repartition or shape-only forcing are established.

## Mathematical question and dependencies

For the fixed b=c=1 U/V pentagons in the
[Robinson partition record](pentagrid-golden-metric-robinson-partitions.md),
can either parent be an actual cluster of specified halves of an edge-to-edge
unit rhomb tiling? These are the exact unit thin/fat scales, not arbitrary
scaled triangles. The [height screen](pentagrid-robinson-height-boundary.md)
first leaves30 U and311 V ordered boundary words. All reflections are included
through the oriented source geometry; no equivalence removes distinct words.

The [source-height formalization](../lemmas/pentagrid-robinson-source-height-and-stokes.md)
retains the necessity arguments and has a [distinct VALID fresh analytic review](../reviews/pentagrid-robinson-source-height-and-stokes-review.md). The height producer itself has a VALID fresh
independent integer-enumeration audit; that does not audit the geometry below.

## Unique boundary-diagonal triangles

For a CCW boundary diagonal starting at x in direction z^k, the only specified
unit triangle on the inside has apex x+z^(k+2) for s=phi^-1 and apex
x+z^(k+1) for l=phi. Thus all boundary-diagonal halves are fixed by the word.
Let d_ij count those halves in each of the ten direction pairs, and q_ij be
the oriented triangle counts from the height wedge. Every interior source
diagonal pairs two halves of the same rhomb, so

    q_ij >= d_ij,  q_ij = d_ij modulo2.

[The diagonal producer](pentagrid-robinson-diagonal-boundary.py) completely
re-enumerates625/21801 boundary words with exact integer height/fan/wedge
checks, then uses exact cyclotomic-field signs for parent containment and
pairwise separating-axis tests. No solver, stochastic seed, symmetry
reduction, coordinate cutoff or timeout is used. In Conda arisearch the
recorded run completed in45.951 seconds.

| Parent | Height/fan/wedge survivors | Pair counts/parity | All halves contained | All halves disjoint |
| --- | ---: | ---: | ---: | ---: |
| U |30|28|28|28|
| V |311|191|191|191|

The [diagonal certificate](../certificates/pentagrid-robinson-diagonal-boundary.json)
retains every surviving word and the first exact set of forced triangles.
These are necessary strips, not full source clusters.

## Whole source rhombs, including outside the macro

Every forced diagonal triangle must be completed to its entire source rhomb.
For inside apex a and diagonal endpoints x,y, its other apex is x+y-a.
That mate is outside the parent. Distinct boundary diagonals belong to
distinct source rhombs, because a rhomb has only one specified cut diagonal.
Their complete rhombs must have disjoint interiors and full native-edge
contacts even outside the macro. Testing only their inside halves would miss
this source-legality constraint.

[The exterior-completion producer](pentagrid-robinson-boundary-completion.py)
reads the retained28/191 words, constructs every exact four-vertex rhomb,
checks all unit edges and pairwise separating axes, then rejects any native
vertex in another rhomb's open edge. Exact real algebraic signs are memoized.
There is no timeout, solver or random seed. The run completed in19.524 seconds.

| Parent | Input words | Complete rhombs disjoint | Also no partial contacts |
| --- | ---: | ---: | ---: |
| U |28|28|28|
| V |191|191|185|

The [completion certificate](../certificates/pentagrid-robinson-boundary-completion.json)
retains all surviving words and first complete-rhomb coordinates. Neither
parent is excluded. All computations use Q(z), with z=exp(pi*i/5), the
specified root of z^4-z^3+z^2-z+1. Rational basis coefficients and the exact
real embedding determine every decision. Parent/root data are given in the
original geometry record. Author code imports existing exact arithmetic
helpers; independent verification is separate.

## Fixed six/nine-rhomb residual domain

After removing its forced4 U or7 V half triangles, any actual source cluster
has exactly6 U or9 V whole rhombs inside. Every other triangle diagonal
must have its mate inside; an unmatched diagonal would be another macro
boundary diagonal. Counts in the ten orientation pairs are exactly
(q_ij-d_ij)/2. The remaining boundary consists of whole unit source edges.

[The residual producer](pentagrid-robinson-residual-rhombs.py) starts from each
of the28/185 boundary words, subtracts those forced halves, and peels whole
unit rhombs from the remaining oriented boundary. Each selected boundary
edge has exactly four potential unit directions into its left half-plane.
Candidate rhombs must lie inside the parent, be disjoint from every already
placed rhomb and every completed boundary rhomb, respect native full-edge
contacts, and fit the exact remaining orientation counts. Each move reduces
the remaining number of rhombs by one. The resulting finite domain is
bounded by six/nine moves, with at most four branches at each move; there is
no guessed inflation or larger patch bound.

The algorithm chooses a boundary edge with the fewest currently viable
candidates and memoizes failed residual boundary/count states. It stops each
word on the first cluster witness or after complete failure. A single global
120-second deadline applies to the28/185 words, seed none. A deadline is
reported as UNKNOWN and records completed words only; it is never treated as
UNSAT. No arrow decoration or extension outside the completed boundary
rhombs is encoded. A positive result establishes only this finite source
geometry, still requiring global source legality and repartition.

The first residual invocation failed before exploring its first boundary:
Sage's number-field constructor accepts a list of coefficients but rejects
an immutable tuple. The serialization boundary was corrected to convert
cache keys back to coefficient lists. This is an implementation failure,
not a source-cluster exclusion, timeout, or mathematical result. The exact
same domain and120-second deadline are retained for the corrected run.

## Completed residual search

The corrected120-second run completed the entire fixed domain in75.023
seconds, without reaching its deadline:

| Parent | Boundary words | Completed | SAT source geometry | Complete residual-domain UNSAT | Search nodes |
| --- | ---: | ---: | ---: | ---: | ---: |
| U |28|28|28|0|196|
| V |185|185|168|17|1744|

The [retained residual certificate](../certificates/pentagrid-robinson-residual-rhombs.json)
contains a first positive exact witness for each parent and every completed
word's result, fixed orientation inventory, search statistics and exact SAT
rhomb coordinates. Every U witness consists of3 thin and3 fat residual
rhombs plus its4 boundary halves; every V witness consists of3 thin and6
fat residual rhombs plus its7 boundary halves. The [fresh independent checker](../reviews/verify_pentagrid_robinson_residual_independent.py) verifies all196 positive finite patches with exact clipping and unit-height consistency. All17 negatives fail at one initially exposed unit edge with no admissible rhomb, independently checked without failed-state memo. No complete Penrose
arrow assignment or infinite source containing these clusters is yet proved.
Do not infer those from finite ETE geometry. No bounded packing increase
followed the old phi^3 pentagon macro timeout: this search used a newly
proved source-mate inventory and its natural six/nine depth.

## Commands

    conda run --no-capture-output -n arisearch python research/searches/pentagrid-robinson-diagonal-boundary.py
    conda run --no-capture-output -n arisearch python research/searches/pentagrid-robinson-boundary-completion.py
    conda run --no-capture-output -n arisearch python research/searches/pentagrid-robinson-residual-rhombs.py --seconds 120

All print JSON without writing artifacts. Exact geometry checks require
SageMath from the retained arisearch environment and enabled assertions.
The exterior-completion domain depends on the diagonal certificate; root
checkpoints generated output only after successful completion. Finite cluster
existence would still leave Penrose markings, global partition, unrestricted
macro forcing and translational-period exclusion open.
