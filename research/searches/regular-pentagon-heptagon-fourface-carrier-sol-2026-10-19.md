# Regular pentagon / 144,124,128 heptagon: exact four-face carrier gate

## Finite domain and outcome

Completed exact combinatorial enumeration on two regular pentagons P and two copies of Q, over all ten rooted dihedral words (unique 144 corner, three 124 and three 128 corners). Q edges indexed from the 144 corner are required to meet P at slots 0,2,4,6 and Q at slots 1,3,5. P sides are unit. The quotient is oriented; both relative Q orientations are allowed. P reflection adds no possibilities because P is regular. Every native edge is paired reversing boundary orientation. PP=1, PQ=8, QQ=3, with same-face identifications allowed.

All five set partitions of the three QQ length symbols are enumerated, including all equal. Every compatible perfect matching of the six QQ darts is tested (15 before color rejection). Each of the eight Q-to-P darts is assigned injectively to the ten P darts; the remaining two P darts are paired. Thus the negative domain includes arbitrary coincidences of the three QQ lengths. Color partitions involving unit length add no pairings in this forced edge-type domain.

Only final connected quotients with eight circular links of three corners and angle triples (108,108,144) or (108,124,128) are accepted. Search prunes corner components as soon as their angle multiset is not a submultiset of an allowed triple; this pruning cannot remove a completion. No symmetry reduction besides rooted reversal of the Q angle word and fixing Q0 orientation is used.

| Q cyclic angles | Result |
|---|---|
| 144,124,124,124,128,128,128 | UNSAT |
| 144,124,124,128,124,128,128 | UNSAT |
| 144,124,124,128,128,124,128 | UNSAT |
| 144,124,124,128,128,128,124 | UNSAT |
| 144,124,128,124,124,128,128 | UNSAT |
| 144,124,128,124,128,124,128 | SAT |
| 144,124,128,124,128,128,124 | SAT |
| 144,124,128,128,124,124,128 | SAT |
| 144,128,124,124,124,128,128 | UNSAT |
| 144,128,124,124,128,124,128 | SAT |

Completion: 304 compatible QQ/color/orientation cases, 21160 recursive PQ-assignment nodes. SAT branches stop at their first witness; UNSAT branches exhaust all stated cases. Deterministic Python 3.12.13, standard library only; no seed or timeout.

## Positive certificate and geometric implication

All four SAT words use identical pairings, with no Q reflection and arbitrary independent positive QQ lengths. Dart labels are P0=0..4, P1=5..9, Q0=10..16, Q1=17..23, and each dart begins at its indexed corner. The retained JSON supplies every pairing and vertex orbit. The independent verifier computes vertex cycles as next(alpha(d)), checks all length matches, angle sums, connectivity and Euler characteristic zero.

Conditional on the actual Euclidean Q being closed, strictly convex, with these angles and unit PQ sides, glue the four Euclidean polygons by the certified reversed edge isometries. Circular trivalent links with angle sum 360 give an everywhere flat oriented compact surface. Connectivity and Euler characteristic zero make it a torus. Its complete simply connected flat cover is the Euclidean plane; each face lifts isometrically to its original convex polygon. Interiors are disjoint and the lifts cover the plane. The deck group is a cocompact free orientation-preserving Euclidean isometry group; its nonidentity elements are translations (a nontranslation orientation-preserving plane isometry has a fixed point). Hence this is an ETE doubly periodic tiling by the actual unmarked polygons. No numerical geometric placement is used.

## Scope and review

The [independent Sol hostile review](../reviews/regular-pentagon-heptagon-124-128-hostile-sol-2026-10-19.md) passed the search completeness and positive flat-torus implication at the stated four-face scope.

Six UNSAT results exclude only this 2P+2Q native-edge quotient domain, even with all QQ length equalities. They imply neither nonperiodicity nor failure of plane tilability. The metric feasibility gate is separate. The search and independent positive permutation verifier agree with the other metric-gate agent's independently implemented four-face results. Negative enumeration has no independent formal UNSAT certificate.

Replay:

```sh
mise exec -- conda run --no-capture-output -n arisearch python research/searches/regular-pentagon-heptagon-fourface-carrier-sol-2026-10-19.py
mise exec -- conda run --no-capture-output -n arisearch python research/searches/regular-pentagon-heptagon-fourface-verify-sol-2026-10-19.py
```
