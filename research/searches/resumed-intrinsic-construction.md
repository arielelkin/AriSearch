# Exact search record: intrinsic Voronoi pair

Date: 2026-10-13. **Status: certified exact periodic pair; independently reviewed
VALID; falsified as an aperiodic construction.**

The exact definitions and complete mathematical proofs are extracted to
[the counterexample](../counterexamples/resumed-voronoi-periodic-nonmonohedral-pair.md).
The independent [hostile review](../reviews/resumed-intrinsic-construction-hostile-review.md)
and [verifier](../reviews/resumed_higher_voronoi_verify.py) remain separate.

## Question and finite domain

One fixed point motif S=Z²+{0,±(1/10,49/100)} is tested for exactly two
convex classes, absence of either monohedral omission tiling, and a repeatable
nonconvex parent. One specified moved site tests a period-breaking operation.
No old enumeration or metric sweep was resumed.

For each of the three motif sites s, the Voronoi polygon is encoded as the
intersection of the same-coset unit square with the75 bisector halfplanes
from t=n+b, n in {-2,-1,0,1,2}², b in {0,d,-d}; the self halfplane is vacuous.
Omitted-site constraints are analytically redundant, as proved in the
counterexample. Thus this finite domain describes the complete infinite
Voronoi cell. The one defect moves d to d+(1/10000,0), and its origin cell
uses the same75-site domain with this one site replaced.

Corners are exact rational vertices. Interior-angle phases are primitive
Gaussian integers formed from rational edge dot/cross products. The complete
necessary-star domains are251 vectors k in N^5 with1<=sum(k)<=5 for P,
and34 vectors k in N^4 with1<=sum(k)<=3 for Q; strict angle bounds give
half-star caps2 and1. Product sign excludes full/half stars. Reflections
preserve angles and half stars explicitly handle unrestricted partial contacts.
There is no symmetry reduction, solver, seed or floating-point branch.

## Results and retained certificate

The motif yields a strict convex pentagon P and octagon Q, each individually
untileable. Their mixed tiling has periods (1,0),(0,1). Grouping 2P+Q yields
an exact area1 fourteen-gon parent with four reflex corners and pointwise
lattice compatibility. The isolated phason creates a noncentral octagon,
hence a third congruence class. These are exact consequences of the stated
finite domains and analytical completeness proofs, not bounded patch evidence.

Producer: [resumed_intrinsic_voronoi_pair.py](resumed_intrinsic_voronoi_pair.py).
Certificate: [resumed_intrinsic_voronoi_pair.json](../certificates/resumed_intrinsic_voronoi_pair.json).
Python standard-library Fraction and integer arithmetic only. Completed
successfully, no timeout or resource cap. Retained coordinates, areas,
parent boundary, real-product witnesses and changed octagon reconstruct exactly.

Read-only replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/resumed_intrinsic_voronoi_pair.py --check research/certificates/resumed_intrinsic_voronoi_pair.json

Independent verification:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/resumed_higher_voronoi_verify.py

## Mechanism state and restart condition

The lattice carrier decisively kills this pair despite both omission
attacks failing. The isolated period-breaking operation fails exact two-class
closure. No novel aperiodic pair or unrestricted impossibility theorem follows.
A successor needs changed metric shapes, no admitted periodic carrier, and
an exact globally compatible two-class covering. Repeating this same periodic
pair or enlarging the isolated-defect experiment has no forcing implication.
