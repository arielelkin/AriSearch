# Equilateral rational-angle obstruction: finite computation record

**Completion:** complete; exact certificate retained. These checks support
[the restricted theorem](../lemmas/new-angle-equilateral-rational-obstruction.md).
Independent hostile review pending.

Mathematical question: can the required corner L=180-theta in the acute or
boundary family, S=60+theta in the obtuse family, or 168 degrees in the
exceptional hexagon occur in any genuine-corner sum of 180 or 360 degrees
with a regular pentagon angle of 108 degrees? Does the exceptional unit-edge
root sum close exactly?

Object encoding and exact domains:

- Acute angle sums: target 180 or 360; theta in (0,30); counts
  (L,S,P) in {1,2} x {0,...,5} x {0,...,3} (48 count tuples per target).
  Integer affine equations are solved with rational arithmetic.
- Boundary theta=30: the same 48 count tuples for each target, now with
  fixed angles (150,90,108).
- Obtuse triple sums: all six nonnegative count tuples (n,m,k) summing
  to three with m>=1; theta in [30,90]. Retain every exact theta root.
  The absence of roots in (30,60) is the used implication.
- Exceptional sums: counts (168,60,108) in {1,2} x {0,...,6} x
  {0,...,3}, targets 180 and 360 (56 tuples per target).
- Regular pentagon sums: counts 1,2,3, targets 180 and 360.
- Exceptional closure: a single polynomial with coefficient one at
  exponents 5,6,12,18,24,25 reduced by Phi30 over the integers.

Every domain overincludes all possibilities used in its proof. Distinct
corner orders and face reflections leave these scalar sums unchanged;
this is not an edge or global tiling enumeration. No symmetry reduction,
solver, SAT formulation, stochastic seed, timeout, or configured memory cap
is used. The arithmetic classification of arbitrary root orders is imported
from primary theorems, never inferred from this bounded computation.

Replay:

    conda run --no-capture-output -n arisearch python3 research/searches/new-angle-equilateral-rational-verify.py

Output: [retained certificate](../certificates/new-angle-equilateral-rational-certificate.json).
All listed forbidden sum sets are empty. The obtuse triple roots are exactly
60,66,84 degrees. Exceptional closure has zero polynomial remainder.

Execution record: started 2026-10-09T21:35:31.960911+00:00; Python 3.12.13;
Linux x86_64; standard library only; elapsed
0.026190 seconds for the verification subprocess, excluding Conda launch;
maximum child resident set size 13056 KiB.
Exit status 0. No exhaustion, timeout, interruption, or solver failure occurred.

The results certify only the finite angle equations and exact fixed closure.
The complete restricted theorem additionally needs the root classification
and geometric periodic construction proved in the accompanying lemma.
Nothing establishes a solution to the unrestricted two-tile problem.

Primary-source queries used on 2026-10-09:

- minimal vanishing sums roots of unity weight six weight five Lam Leung 2000 theorem
- Schoenberg vanishing sums roots unity small weight 5 6 polygons equilateral pentagon

Primary PDF read: [Lam--Leung, arXiv:math/9511209](https://arxiv.org/pdf/math/9511209),
Theorems 3.3, 4.8, 6.5 and the definitions preceding them. A secondary search
result suggested the small-weight classification; it is not used as authority.
No novelty claim follows from this narrow literature check.
