# Generic formal side-pairing identities for the dodecagon family

**Completion:** exact formal endpoint identities and full native vertex
cycles passed. This is an author-side checker. The same universal claims
were independently verified by the [fresh checker](../reviews/verify_regular_dodecagon_independent.py),
which derives ordered corner cycles and additionally verifies the symbolic
area identity; the [full hostile review](../reviews/all-obtuse-pentagon-regular-dodecagon-review.md) is valid.

## Question and domain

Are all seven-motif side pairings displayed in the
[classification lemma](../lemmas/all-obtuse-pentagon-regular-dodecagon-classification.md)
identities for every parameter, and do they produce the claimed local
three-corner surface?

This is an exact polynomial-identity problem, not a finite parameter sample.
Use the cyclotomic24 field K=Q(z), with z=exp(pi*i/12) and defining polynomial
Phi24=x^8-x^4+1. The ring K[ell,rho] has two formal variables. Every motif
coordinate and period is affine over this ring: R=z+z^-1, omega=z^8,
P=[0,ell,ell+z^5*rho,ell*omega-z^15*rho,ell*omega],
q0=ell+R*rho, z0=(1+omega)q0, u=(omega-1)q0, v=(omega^2-1)q0.
One Q plus three P rotations and three half-turn copies are checked.

Every one of the21 unordered paired-side entries must match its endpoints
in reverse order, with the listed integer u,v offsets. There are42 oriented
native edges; each is paired exactly once. Union-find on all42 native
corner labels traces the endpoint identifications modulo the lattice. The
result must be14 classes of three native corners each: two P triples all
at vertex0, and twelve Q/P/P classes with native P index pairs (1,4) or
(2,3). No orientation symmetry reduction or class quotient is assumed.

The field generator is handled exactly by Sage, and equality in the
polynomial ring is exact coefficient equality. Thus every verified endpoint
identity holds after substituting any ell,rho. For the geometric theorem
rho=exp(-ip) is unit and ell,p satisfy the analytic positive-convex domain.
Those inequalities, rank of the lattice, surface chart orientation, area,
and covering degree are proved separately in the lemma; this code does
not claim them from endpoint equality alone.

## Artifacts and reproducibility

Checker: [regular_dodecagon_gluing_identities.py](regular_dodecagon_gluing_identities.py).
Certificate: [regular-dodecagon-gluing-identities.json](../certificates/regular-dodecagon-gluing-identities.json).

The certificate retains all21 edge-pair entries and14 vertex classes. The
checker imports no fixed-witness producer, uses no solver, random seed,
floating-point value, timeout, resource cap, or parameter sampling. The
run completed normally in arisearch with Python3.12.13 and SageMath10.9.
Assertions are proof relevant; run without Python optimization.

```text
conda run --no-capture-output -n arisearch python research/searches/regular_dodecagon_gluing_identities.py
```

The normal completion reports the generic domain,21 pairs,14 native vertex
classes, two120-degree P triples, and twelve complementary Q/P/P stars.
The accompanying fixed asymmetric witness has a separate complete62-shift
interior-overlap certificate; neither domain substitutes for the other.

## Scope

This verification removes an erroneous-side-table or untraced-native-star
risk for the exact symbolic recipe, over its entire continuous parameter
family. It is not an independent proof review, and it does not prove
plane existence without the lemma's positivity and degree-one argument.
It classifies no other pair and carries no novelty assertion. The full
family has passed the fresh hostile review linked above. This author-side
identity script is a redundant replay of the side table; independent
acceptance relies on the separately structured fresh checker.
