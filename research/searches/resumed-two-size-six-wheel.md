# Exact six-piece wheel test in the quartic size field

Date: 2026-10-13. Status: exact480-matrix exclusion, independently reviewed VALID;
[review](../reviews/resumed-two-size-wheel-review.md). This excludes one precise dissection
scheme, not all six-piece dissections and not the unrestricted problem.

## Concrete scheme and hypotheses

Set mu=1+sqrt5 and lambda=sqrt(mu)>1. Seek a convex pentagon P with five
pairwise DISTINCT native interior angles and arbitrary positive real native
side lengths l_0,...,l_4 (in particular lengths spanning the full quartic
Q(lambda) are allowed). Parent mu P is to be partitioned into4 copies of P
and2 copies of lambda P. Writing A=P and B=lambda P, an ordinary substitution would use
the other one-child rule lambda A -> one copy of B.

The tested contact scheme is a wheel: one central child plus five corner
children, each occupying exactly one original parent corner with one native
corner equal to the entire parent angle. Each parent side is exactly the
union of the complete boundary sides of its two neighboring corner children;
no extra boundary child, partial truncation or corner subdivision is present.
Every corner child has two full consecutive sides on the two parent rays.
Its other boundaries may meet the center/neighbor children in any compatible
way; we use only necessary outer-boundary equalities. Reflections are allowed.
This scheme is an explicit proposed construction topology, not a theorem
that every six-pentagon partition has this topology.

Write t_i=1 or lambda for the scale of corner child i. The central child is
small or large. If central is small, exactly2 of the5 corner children are
large; if central is large, exactly1 is large. Native angles are distinct,
so corner child i must use native vertex i at parent vertex i. Its placement
on the two parent rays has exactly two isometry choices: direct, or reflection
that interchanges its incoming and outgoing side lengths. Let r_i in {0,1}
record this reflection (not an externally enforced placement rule).

For parent side i, the child at its start contributes

    t_i l_i if r_i=0, else t_i l_(i-1),

and the child at its end, vertex i+1, contributes

    t_(i+1) l_i if r_(i+1)=0, else t_(i+1) l_(i+1).

All indices are modulo5. Exact covering would therefore require

    mu l_i = [start contribution]+[end contribution], i=0,...,4.  (W)

No supplementary length rule is imposed: these are necessary Euclidean
length equations for the stated wheel scheme, with every permitted reflection
included.

## Finite exact domain and result

The corner-scale/reflection domain is precisely

    central small: C(5,2)*2^5=320 configurations;
    central large: C(5,1)*2^5=160 configurations.

No symmetry reduction is used; total480. For each case construct the5x5
matrix M in (W), with diagonal mu and the two negative corner contributions
in their appropriate native columns. The exact number field is

    F=Q(a), a⁴-2a²-4=0,

with a identified mathematically with the positive root lambda. This
polynomial is irreducible: a²=1+sqrt5 has negative quadratic conjugate and
cannot be a square in Q(sqrt5). No floating-point embedding is used to
calculate determinants.

**All480 determinants are nonzero in F.** Thus every corresponding matrix
is nonsingular in its positive real embedding. Its kernel contains no
nonzero real length vector at all, irrespective of the metric field.
Consequently the proposed wheel has no exact geometric realization by a
five-distinct-angle pentagon, even with arbitrary real positive lengths.
This excludes the specified full-quartic attempt before vertex coordinates,
closure or inner contacts need to be searched. It is stronger than merely
checking a single arbitrary quartic metric fixture.

Producer: [resumed_intrinsic_two_size_wheel.py](resumed_intrinsic_two_size_wheel.py).
Certificate: [resumed_intrinsic_two_size_wheel.json](../certificates/resumed_intrinsic_two_size_wheel.json).
Each record retains central size, both large-corner choices/reflections and
the four integer coefficients of the exact determinant in the basis
1,a,a²,a³. The complete480-case certificate is reproducible.

Read-only replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/resumed_intrinsic_two_size_wheel.py --check research/certificates/resumed_intrinsic_two_size_wheel.json

SageMath exact rational number-field arithmetic; deterministic complete
domain, no seed, solver, tolerance, timeout or parameter grid. The replay
passed. The [independent verifier](../reviews/resumed-two-size-wheel-independent.py)
reconstructs corner blocks and every determinant by integer polynomial
Leibniz expansion, compares all certificate coefficients, and checks complete
320/160 case keys. It passed without importing Sage or the producer.

## Exact blocked obligation

This count/geometry scheme is killed. Reopen it only by changing a hypothesis
actually used: repeated native angles permitting a different corner-to-native
assignment; subdivided parent corner sectors; additional boundary children;
or a different count/size/contact scheme with an explicit geometric proposal.
No generic point enumeration is justified by this negative result. The
remaining general task is a complete exact convex-parent dissection at a
surviving count and metric, followed separately by extension and shape-only
recognition/aperiodicity. No one-child rule or absence of this wheel supplies
those missing lemmas.
