# Hostile review: specific two-parameter hat four-pentagon deformation

Date: 2026-10-12. **VALID scoped exclusion.** The explicit (b,u) compiler has no aperiodic at-most-two-class realization.

[The independent checker](check_hat_four_pentagon_deformation.py) imports no producer. It reconstructs the thirteen affine outline vertices and the four prescribed pentagon boundary words over Q(sqrt(3))[b,u]. Their coordinates agree exactly with [the retained certificate](../certificates/hat-four-pentagon-deformation-gate.json). The parameter b changes the designated long outline directions at fixed unit scale; u moves the single cut vertex V horizontally at the height of outline vertex seven. No hidden independent vertex coordinates are introduced.

If four strictly convex five-corner pieces represent at most two congruence classes, some pair among P6,P48,P192 must be congruent. It is therefore sufficient to test these three pairs, even though P9 is not included in the distance-system list. Isometries between strict pentagons preserve cyclic corner order or reverse it, so all five shifts and both directions cover every possible correspondence, including reflections. Every system uses all ten pairwise squared distances; matching edges alone is not substituted for congruence.

The checker independently regenerates all thirty ideals and Gröbner bases. Twenty-four ideals are the unit ideal. Each of the remaining six is exactly (b−sqrt(3),u−2), not merely an approximate or selected real root. Thus every necessary pair congruence in the entire complex parameter plane lies at that one point. Convexity or source-domain filtering cannot create another solution. This stronger algebraic superset removes concern about omitted clockwise parameter branches or unverified admissibility inequalities.

At the sole point the checker verifies positive area, strict turns and global supporting half-planes for all four pieces. Exact clipping gives disjoint interiors; directed-edge cancellation gives the original source outline. All four pieces are congruent to the fixed two-kite pentagon independently reviewed in [the fixed compiler gate](hat-eight-kite-convex-cluster-review.md). Three copies of that pentagon partition a regular hexagon, yielding an admitted monohedral periodic tiling. The point therefore fails the aperiodicity requirement and also has only one distinct class.

Omitted boundary degenerations are soundly outside the viable gate. A compact convex positive-area piece with a straight listed vertex or repeated endpoint has at most four intrinsic corners and hence a monohedral periodic escape. A zero-area piece is not a valid final tile. Therefore any successful candidate must have all four prescribed pieces strictly convex with five intrinsic corners; it would be covered by the thirty systems. This does not classify collapsed pieces as empty algebraic loci—it removes them by the problem's periodic-escape or positive-area requirements.

No plane-source existence, source recognition or inherited aperiodicity theorem is used for this negative result. Geometry/assembly away from the sole point need not be proved, because no necessary two-class congruence survives there. Scope remains the stated four boundary words and horizontal-cut constraint. Changed words, additional cut vertices, source-boundary-crossing clusters and other hat deformation mechanisms are unclassified.

[Controls](hat-four-pentagon-deformation-check.json) retain the exact certificate digest. Shared Sage/Singular ideal arithmetic remains computational trust; no formal Gröbner certificate is supplied. The independent checker is nondestructive by default and accepts an optional --output PATH for temporary replay.

```bash
MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python research/reviews/check_hat_four_pentagon_deformation.py
```
