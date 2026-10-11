# Hostile review: two obtuse angle values with a pentagon

**Date:** 2026-10-09. **Reviewer:** independent construction-angle agent,
which did not develop this two-angle family.
**Verdict:** valid as the stated restricted necessary-condition theorem,
with the explicitly imported unrestricted monohedral hexagon classification.
No main-problem solution is reviewed or asserted.

## Exact claim reviewed

[The lemma](../lemmas/two-obtuse-angle-pentagon-reduction.md) claims that
an all-obtuse two-angle pair containing a pentagon reduces to three rational
angle/multiplicity rows, with the specified finite ranges of side counts for
its second polygon. It excludes n=5, excludes aperiodicity for n=6, and
proves untileability at n=10 in the 3pi/5,4pi/5 row. Four signatures remain
for potentially aperiodic pairs, with no closure or tiling existence claim.
The generator, retained JSON, independent table verifier, all-obtuse
forcing theorem, and needed side-count/compactness arguments were read.

## Attacks and checks

1. **One vertex count globally:** a star has three angles; subtracting the
   equations for two distinct alpha multiplicities gives
   (p-pprime)*(alpha-beta)=0. Thus p is fixed over all vertices, regardless
   of connectedness questions, orientation, or cyclic corner order.
2. **p=0 and p=3 omissions:** p=0 permits additional *formal algebraic*
   rows (alpha/pi,beta/pi)=(5/9,2/3),(7/12,2/3),(3/5,2/3), with pentagon
   alpha counts 3,4,5. They do not define tilings: an alpha corner would
   have to occur in a vertex, but every allowed vertex contains only beta.
   The lemma explicitly and correctly applies this corner-incidence
   obstruction before its twelve-row search. If p=3, every present tile
   similarly has only the 2pi/3 alpha angle and must be a hexagon.
3. **Angle linear systems:** both elimination formulas and all twelve
   k-values recompute correctly. The determinant is 3k-5p, nonzero for
   integer k and p=1,2. Strict order and obtuse inequalities leave exactly
   (p,k,x,y)=(1,4,4/7,5/7),(1,5,3/5,7/10),(2,5,3/5,4/5).
4. **Unbounded n, not a search cutoff:** solving the second polygon sum
   gives l=14-2n,20-3n,10-n in the corresponding rows. The conditions
   0<=l<=n give [5,7],[5,6],[5,10], respectively, after n>=5. Therefore
   enumeration through ten is analytically complete in this restricted
   family; no finite-model principle is being assumed.
5. **Odd-face obstruction:** at n=10 each Q corner is beta, each P corner
   is alpha, and every star has exactly two P corners and one Q corner.
   At each corner of a selected P tile, the two incident full-edge
   neighbours are therefore one P and one Q. The neighbour type of an
   edge is unchanged between its endpoints. Five neighbours in cyclic
   order cannot alternate. Convexity and all-obtuse forcing ensure full
   edges; reflections do not change the type argument. This is a finite
   contradiction at one actual face, not an unproved extension claim.
6. **Possibility that P is omitted:** Q alone with n>6 is excluded by the
   unrestricted global side-count theorem. Q alone with n=5 cannot form
   the all-obtuse trivalent tiling. Q alone with n=6 provides the same
   monohedral periodic escape used in that case. Thus aperiodic components
   cannot evade the reduction by omitting P.
7. **n=5 and n=6 global exclusions:** for a trivalent edge-to-edge window,
   the boundary count identity gives N5-(n-6)*Nn=O(R), uniformly under
   translation. At n=5 it contradicts quadratic tile counts. At n=6 it
   makes pentagons uniformly sparse. The referenced grid-and-compactness
   proof yields a monohedral Q tiling; it does not incorrectly assert
   that the original mixed tiling itself is periodic.
8. **Imported hexagon scope:** the [primary v2 source](https://arxiv.org/html/2508.01404v2)
   was read on 2026-10-09. Its Main Theorem applies to congruent straight
   hexagons with at least three tiles at each vertex; convex hexagons
   satisfy that condition. The source explicitly includes non-edge-to-edge
   tilings, and its classification works with flipped tile copies.
   Its conclusion is membership in the three Reinhardt families. The
   periodic matching constructions for these families are the named
   external step retained in the dependency file. This review checks
   scope and the reduction; it is not a new independent proof of the
   whole external classification preprint.

## Computation checked

The generator and independent verifier agree on twelve exact rational
angle rows and every retained face row. The independent verifier was run:

    conda run --no-capture-output -n arisearch python3 research/reviews/verify_two_obtuse_angle_pentagon.py

It passed on Python 3.12.13 in Conda arisearch. Counts are multiplicities,
not cyclic orders or tile placements; both artifacts state that scope.

A separate exploratory recalculation admitted p=0,...,3. Its first assertion
incorrectly expected the twelve-row table to be the full *algebraic* table;
it failed because of the three formal p=0 rows listed above. Applying the
explicit corner-incidence condition eliminates those rows, agreeing with
the written proof. This was an audit expectation error, not a defect or
counterexample to the lemma. It supplies no global existence evidence.

## Defects, repairs, and uncertainty

No mathematical defect was found in the stated result. No repair to the
lemma was made by this reviewer. The finite search and its checker do not
independently prove the all-obtuse edge theorem, global side-count theorem,
sparse-type compactness, or external hexagon classification; those are
explicit proof dependencies. The needed elementary reduction and sparse
limit arguments were checked for the uses above. The four surviving
signatures still omit exact side lengths, cyclic order, both-edge-endpoint
compatibility, plane existence, and universal nonperiodicity, as the lemma
already states.

**Final verdict:** valid as written and relative to its named external
classification theorem. The surviving signatures remain only necessary
angle data for future construction attempts.
