# Exact golden-power pentagon metric search

**Status:** exact finite computations completed; independent verification pending. One periodic pair found. Other bounded failures are not aperiodicity evidence.

## Question and finite domain

Start with the three angle words U=(1,3,4,4,3), V=(2,2,4,3,4), W=(3,3,3,3,3), in units pi/5. These words are independently derived in [the angular reduction](../lemmas/pentagrid-pentagon-angular-reduction.md). Here an angle is at the vertex AFTER its indexed side. U and V contain no adjacent supplementary pair. W is equiangular and does not tile alone by angle arithmetic.

Use K=Q(z), z^4-z^3+z^2-z+1=0 with z=exp(pi*i/5), and phi=z+z^(-1). Set d0=1 and d_(j+1)=d_j*z^(5-angle_j). Independently test every exponent vector e in {0,1,2,3}^5 with min(e)=0 for sum(phi^e_j*d_j)=0. Each word has 781 vectors; the total domain is 2343. The minimum condition removes only common rescalings within this alphabet. No dihedral equivalence of length vectors is removed. Every closed polygon receives exact positive-length, angle-ratio and all-vertex supporting-side convexity checks.

[Generator](pentagrid-golden-metric.py); [retained certificate](../certificates/pentagrid-golden-metric-closure.json).

The closed vectors are:

    U: (3,3,0,0,0).
    V: (0,3,1,1,2), (1,2,1,0,0), (1,3,0,2,1),
       (1,3,2,0,2), (2,3,1,2,0), (3,3,3,0,0).
    W: (0,0,0,0,0), (0,2,1,1,2), (1,1,2,0,2),
       (1,2,0,2,1), (2,0,2,1,1), (2,1,1,2,0).

In particular the subalphabet {1,phi} closes only the regular W; no U or V closes in it. This is an exact finite fact, not an exclusion of positive Q(phi) side lengths.

## Full positive side-length kernels

For arbitrary positive real side lengths L2=x,L3=y,L4=t, closure uniquely forces

    U: L0=phi*(x+y)+t, L1=x+phi*(y+t);
    V: L0=x+(phi-1)*(y-t), L1=(phi-1)*(x+t)+y;
    W: L0=x+(phi-1)*(y-t), L1=(phi-1)*(y-x)+t.

Require also L0,L1>0. U satisfies those automatically. These formulas follow by splitting the exact complex closure equation into real and imaginary parts; they can be verified by substitution in K. They parameterize all lengths with these fixed side directions; positive closure and increasing turning angles imply strict convexity, or it can be tested by supporting-side inequalities. Choosing x=y=t=1 gives the U fixture (phi^3,phi^3,1,1,1). No conclusion about aperiodicity follows from being in this kernel.

## Four-face torus witness search

For each of the twelve V/W fixtures search a quotient with two U faces and two copies of that B metric. Each side is paired exactly once, only equal golden exponents are paired, identifications reverse the two endpoints, same-face pairings are allowed, and all four reflection assignments of the B faces are included. Fix both U faces unreflected: U has a reflection symmetry interchanging its two long sides and reversing its three unit sides, so this loses no geometric possibility. No lattice bounds are imposed; this is a prescribed four-face FULL-EDGE quotient domain, which omits partial contacts and larger quotients.

A completed pairing must have connected face adjacency and every native vertex-link angle sum10. A connected oriented closed flat quotient then has V=6,E=10,F=4 and is a torus. Pairings are generated recursively, choosing the least frequent remaining length first. The only pruning is an exact corner-class angle sum exceeding10; future endpoint identifications can only increase that sum. Corner classes are formed by unions of paired endpoints. The retained certificates contain all seam pairings and corner classes, not a trusted solver flag.

[Search](pentagrid-golden-metric-torus.py); [certificate](../certificates/pentagrid-golden-metric-four-face-tori.json).

All six U/V fixture domains and the five U/nonregular-W fixture domains were exhausted with no four-face full-edge quotient. Together their explicit matching domains contain 3738420 pairings (including reflection assignments). The U/regular-W search found a witness in the first reflection assignment, whose complete matching domain contains 6081075 pairings; it stopped after 381 nonpruned complete pairings and 12417 recursive pair branches. This assignment was not exhausted, nor were the later reflection assignments processed. The existence certificate, rather than completeness, proves the witness.

The successful periodic placement, exact periods, and global coverage proof are in [the counterexample](../counterexamples/pentagrid-golden-metric-periodic-pair.md). The U/V finite failures have no unbounded consequence. The five nonregular-W rows are rotations of one metric polygon; retaining them avoids relying on another congruence normalization.

## Arithmetic, dependencies and replay

Python 3 with the arisearch SageMath installation; no random seed, solver, floating equality, timeout, or dependency modification. Number-field equality and QQbar/AA exact ordering are used. The search runs completed successfully. The direct placement checker initially encountered a field-to-AA comparison mismatch, then was repaired to test the area identity wholly in K; the corrected check passed.

    conda run --no-capture-output -n arisearch python3 research/searches/pentagrid-golden-metric.py
    conda run --no-capture-output -n arisearch python3 research/searches/pentagrid-golden-metric-torus.py
    conda run --no-capture-output -n arisearch python3 research/searches/pentagrid-golden-metric-periodic.py

A new construction should choose a metric outside the killed U/regular-W instance and specify a global extension or substitution mechanism before increasing bounded quotient sizes. Known classification gate tests, and their source assumptions, are managed separately by the root agent. The present result is the explicit periodic pair, not a resolution of the main two-tile problem.
