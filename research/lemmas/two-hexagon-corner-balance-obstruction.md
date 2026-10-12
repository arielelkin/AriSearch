# Two hexagons: a corner-balance obstruction independent of side lengths

**Status:** internal proof, 2026-10-12. This is a necessary-condition
filter, not a higher-rank census or a periodicity theorem for balanced types.
It uses the reviewed global SFT reduction and the imported unrestricted
monohedral convex-hexagon classification.

Let T be any allowed corner-triple set and let m_t in Z^12 count the
multiplicity of each corner in t. Write 1_A and 1_B for the two disjoint
six-corner indicator vectors. Define the corner balance system

    w_t >= 0, a > 0, b > 0, a+b=1,
    sum_t w_t m_t = a 1_A + b 1_B.                 (CB)

**Proposition.** If (CB) is infeasible, no geometrically realisable pair
with triple set T is aperiodic, regardless of its side-equality relation.

**Proof.** Suppose X(T,e) is nonempty. Averaging translates of a point
over growing lattice squares and taking a weak limit gives an invariant
probability measure mu supported on X. Put a=mu(q(x_0)=A), b=1-a.
There are two honeycomb vertices per cell. Count the types of these two
vertex stars with multiplicity, and denote their expected counts by w_t.
Every cell contributes each of its six native corners exactly once to
those vertex incidences. Translation invariance therefore gives, for
each native corner c,

    sum_t w_t m_t(c) = a   (c in A),
    sum_t w_t m_t(c) = b   (c in B).

Also sum_t w_t=2, as follows either from the two vertices per cell or by
summing the twelve balance equations. If (CB) is infeasible, one of a,b
must vanish. In the zero-A case, translation invariance gives zero
probability of A at every site. The countable union over all sites has
zero probability, so mu is supported on monohedral B configurations.
The zero-B case is identical. Thus X contains a monohedral point. For
actual convex hexagons, the monohedral classification supplies a periodic
tiling by that species. The pair consequently has a periodic tiling.
If X is empty the pair does not tile, by the global reduction. QED.

The proof does not assume that a mixed configuration has positive density
of both species. Sparse occurrence is precisely why a monohedral limit,
instead of a claim about the original configuration, is used.

## A directly checkable certificate

A rational corner potential d in Q^12 is sufficient when

    sum_{c in t} d_c >= 0                for every t in T,
    s_A = sum_{c in A} d_c <= 0,
    s_B = sum_{c in B} d_c <= 0,
    s_A+s_B < 0.                                  (D)

Pairing the corner-balance equations with d gives

    0 <= sum_t w_t sum_{c in t} d_c = a s_A + b s_B.

This excludes a,b>0. More precisely, every species whose s_q is negative
has zero frequency in every invariant measure. If both species sums are
negative, X is empty for every e; otherwise any nonempty X has a
monohedral configuration of the species with zero sum. Finite rational
arithmetic verifies this certificate without trusting an LP or SAT
infeasibility verdict.

[The exact verifier](../reviews/verify_two_hexagon_corner_balance.py)
uses Z3 only to find rational primal weights or a dual potential normalized
to s_A+s_B=-1. It independently validates each returned potential by
Python rational arithmetic. A feasible (CB) is only a necessary condition
for mixed recurrence; it proves neither a legal patch nor periodicity.
The filter is compatible with the global encoding lemma's warning about
frequency proofs: it removes types lacking recurrent mixed tilings,
whereas balanced types still require nonconvex spatial information.

## An exact minimal covering rank-five obstruction

The [retained certificate](../certificates/two-hexagon-corner-balance-obstruction-example.json)
has exact triple set

    T = {(0,9,11), (1,6,9), (2,8,8),
         (3,5,7), (4,5,10), (5,8,9)}.

Its first five equations have rank five modulo the polygon sums. The sixth
is their sum minus both polygon-sum equations. Independently enumerating
all 364 triple vectors against the exact rational nullspace finds no other
implied triples. The flat has a generic point arbitrarily close to the
all-120-degree point; this asserts exact angle feasibility, not joint
polygon and side-length realisability.

This is a **minimal covering flat**: corners 0,1,2,3,4 respectively occur
only in the first five triples. Every covering closed subset of T must
therefore contain those five equations and consequently all their closure,
which equals T. Every proper ancestor is noncovering. This explicitly
shows why retaining only the covering rank-at-most-three parents misses
higher-rank roots, independently of whether this example is geometrically
realisable.

Take the integer potential

    d = (0,0,0,-2,-1,2,0,0,0,0,-1,0).

The sums for the six displayed triples are respectively 0,0,0,0,0,2,
and both species sums equal -1. Hence X(T,e) is empty for every e,
by (D), without any solver infeasibility claim.

More broadly, put T_d = {t : sum_{c in t} d_c >= 0}. It contains exactly
195 of the 364 possible triples. The same proof gives

    X(T',e) is empty whenever T' is a subset of T_d,

for every e and even for triple sets T' that are not rationally closed.
Thus the potential is a reusable analytic empty record on an entire
half-space region, together with all 288 native relabelling images.
The region also has an explicit finite empty-patch certificate. A hexagonal
patch of radius R has N=1+3R(R+1) cells and 6R^2 complete vertex stars.
There are 6N-18R^2=18R+6 corner incidences at incomplete boundary stars.
The total d-sum over all tile corners equals -N, since each tile contributes
-1. Complete stars contribute nonnegative sums. Each remaining incidence
contributes at least -2, so necessarily N<=2(18R+6). At R=12 this would
require 469<=444, a contradiction. Thus X(T_d,e) has no radius-12 patch,
for any e. This is a finite analytic empty record in the sense of the global
encoding lemma; it requires no invariant-measure or polygon assumptions.

A descendant of the rank-five example remains excluded provided every
new triple has nonnegative d-sum. Adding a negative-sum triple requires
new analysis. The finite certificate can be verified by exact rational
arithmetic; the current verifier also checks rank, full closure, and the
unique-corner minimality argument independently of the census code:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_two_hexagon_corner_balance.py --example

## Interaction with higher-rank continuation

The condition is monotone in the useful direction: adding allowed triples
adds nonnegative weight variables and can restore feasibility. Therefore
an obstructed parent cannot be pruned from the all-flat enumeration;
a descendant may become balanced and covering. For a fixed potential,
all descendants whose added triples still have nonnegative d-sum inherit
the same obstruction. This yields a reusable half-space certificate in
triple-set space, independent of side-equality data.

All 316 stored covering rank-at-most-three types pass (CB): six at rank
two and 310 at rank three. Thus this filter does not retrospectively
replace the low-rank torus census. Higher-rank usefulness requires explicit
examples or a census; no complete higher-rank count is asserted here.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_two_hexagon_corner_balance.py --registry
    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_two_hexagon_corner_balance.py INPUT.json
