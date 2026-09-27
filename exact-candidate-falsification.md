# Exact candidate-falsification workstream

This is one workstream within the mathematical search, not the immediate
objective of the whole project. First select an explicit candidate family or
construction mechanism and state the finite question to be answered. Implement
only the exact machinery needed for that question.

## Implement now

### 1. Exact geometry

Represent both prototiles, placements, translations, and period vectors in one
explicitly embedded real algebraic field (or a common compositum). Retain
defining polynomials, embeddings or isolating intervals, exact coefficients,
and a canonical serialization. Placements are exact orthogonal matrices and
translations; reflections are permitted.

This algebraic restriction applies only to this search and certificate
machinery, not to the mathematical target or all admissible tilings. Any
claim of completeness beyond that domain requires a separate proof.

Implement in Sage only the predicates required by the active search:

* orientation, convexity, and containment;
* segment intersection and collinear overlap;
* polygon interior-overlap detection;
* exact transformation and congruence; and
* contact classification, including partial-edge contacts and T-junctions.

Floating point may guide plots, but must not decide geometric branches.

### 2. Doubly periodic witness certificates

Define a certificate containing:

* two exact, linearly independent period vectors;
* the prototile type and exact isometry of each tile orbit; and
* any finite boundary or contact data required for replay.

Allow oblique lattices. Call this a **doubly periodic witness**: it is a decisive
counterexample, but it does not cover tilings with exactly one independent
period. Rank-1 periodicity remains a separate global proof obligation.

### 3. Independent exact verifier

Keep the verifier separate from the candidate generator and its search code.
It must:

* check lattice independence and every tile's congruence;
* enumerate all lattice translates that can intersect the representatives;
* reject pairwise interior overlap, including overlap with self-translates; and
* verify that total tile area equals the absolute lattice determinant.

For finitely many closed polygon images on the quotient torus, disjoint
interiors plus area equality proves coverage. State and test this lemma rather
than requiring a general polygon-overlay engine. Specify representative and
boundary conventions in the certificate format.

### 4. Monohedral rejection gate

Reject a pair if either polygon admits a periodic monohedral tiling, because a
valid tiling need not use both prototiles. Reject triangles and quadrilaterals
immediately. Apply exact membership tests for established convex-pentagon and
convex-hexagon tiler families, accounting for cyclic relabeling and reflection.

Whenever practical, emit an explicit periodic witness instead of relying only
on a classification citation.

### 5. Candidate-specific finite searches

Pass only finite, exactly verified placement catalogues to a solver. Every
consequential search must state its finite domain and include a candidate-specific
argument that the catalogue is exhaustive for the claim being tested. Solver
UNSAT without that argument applies only to the supplied catalogue.

## Benchmarks

Begin with small fixtures that test:

* oblique periods and seam-crossing tiles;
* reflections;
* partial-edge contacts and T-junctions;
* gaps, pairwise overlaps, and self-overlap under a lattice translate; and
* exact area equality.

Unmarked Penrose rhombs are useful only if the periodic search bypasses the
monohedral gate and requires both tile types; otherwise either rhomb alone is a
trivial periodic witness.

Use the hat only as a small exact-placement smoke test at first. Reproducing
its computer-assisted hierarchical forcing proof is a separate project and
should be attempted only if it advances an active convex two-tile route.

## Division of labor

Use SageMath for proof-relevant geometry and verification. Use CP-SAT for
finite selection, exact-cover, and bounded doubly periodic searches after
geometric enumeration is complete. Use Z3 only for carefully bounded rational
or polynomial feasibility problems.

Use Nauty/Traces only when canonicalization preserves tile type, reflection
state, contact subdivisions, cyclic order, and embedded-map information.
Abstract adjacency alone is insufficient.

## Deferred dependencies

Add a dependency only after an active route demonstrates a limitation:

* **CGAL and a C++ compiler:** for exact arrangements or overlays Sage cannot
  handle;
* **CaDiCaL and an independent proof checker:** for proof-relevant Boolean
  UNSAT certificates; or
* **plantri or a custom embedded-map generator:** for an exhaustive planar-map
  search.

Do not add proof-relevant floating-point geometry, another general solver, or
a generic tiling framework at this stage.

## Implementation order

1. Select an active candidate family and exact finite question.
2. Define the certificate semantics and completeness obligation.
3. Implement the exact types and predicates that question requires.
4. Build the independent verifier and small adversarial fixtures.
5. Add monohedral filters and candidate-specific bounded searches.
6. Expand the machinery or benchmarks only when the mathematics requires it.

## Mathematical status

This workstream can certify counterexamples, bounded enumerations, and finite
forcing lemmas. Failure to find a witness proves neither aperiodicity nor the
absence of rank-1 periodic tilings. A successful candidate still needs separate
proofs of existence and of nonperiodicity for every admitted tiling, including
reflected, non-edge-to-edge, unintended, and monohedral tilings.
