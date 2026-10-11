# Fresh hostile review of the 5/7 metric cone and periodic rigidity

**Date:** 2026-10-10. **Reviewer:** the `periodic_counterexample_audit`
agent, independent of this construction and of its author. The root asked
for a review of the strongest shape-only statement, including local
reflections, absence of H, forced whole H orbits and unique P fillers.

**Claim reviewed:** the complete positive four-dimensional shared-order
metric cone in
[two-angle-5-7-metric-continuum.md](../lemmas/two-angle-5-7-metric-continuum.md),
its four-face whole-plane periodic tiling for every positive member, and
uniqueness of every unrestricted tiling when l0,...,l6,p are pairwise
numerically distinct. The updated broader theorem for arbitrary shared-length orders and
internally distinct side lengths is additionally reviewed below.

**Verdict: valid** for the full cone, generic shape-only uniqueness,
exactly-four-shared local classification, and the arbitrary shared-order
one-period theorem for internally distinct side lengths. This is a restricted metric-family classification, not a
classification of all alpha/beta pentagon--heptagon pairs. No defect or
mathematical proof repair was found in the reviewed statements.

## Full cone and formal geometry

The new independent checker
[verify_two_angle_5_7_metric_continuum.py](verify_two_angle_5_7_metric_continuum.py)
imports no author module. It isolates the primitive root of the degree-12
cyclotomic polynomial by rational real/imaginary rectangles, thereby fixing
the correct real embedding of t=2cos(pi/7). It derives the four closure
constraints directly from the seven heptagon unit vectors and the pentagon
closing vector e1-e3+e5-e6. Exact matrix inversion over Q(zeta28) recovers
all four claimed coefficient rows, proving both necessity and sufficiency
of the formulas in the declared shared-order family. The four unknown
closure columns have full rank, so no additional metric parameter or
unwritten equality is missing.

Independently enumerating the 56 triples of active rows in AA recovers
exactly the nine saved cone rays. Coordinates a,b,c,d are constrained
nonnegative in the closed cone, making it pointed; its exhibited strictly
positive member makes it full-dimensional. Every extreme ray therefore
has at least three independent active homogeneous constraints and occurs
in the stated enumeration. Each saved facet witness vanishes on its row
and is strictly positive on all seven others, proving all eight
inequalities irredundant. This attack did not find a missing opposite ray,
normalization error, or use of an incorrect algebraic conjugate.

The checker reconstructs all four polygons over Q(zeta28)[a,b,c,d],
checks every *physical* seam endpoint identity, and verifies the signed
shoelace identity as a polynomial identity. It reverses the pentagon's
native clockwise description to counterclockwise corners and computes a
corner-successor permutation, independently of the producer's endpoint
union-find. The quotient has exactly eight circular three-corner links,
all alpha,beta,beta, and connected face adjacency. Thus the local manifold,
orientability and no-cone hypotheses of the flat torus map are present.
Positivity of all native lengths and the once-around strictly cyclic unit
directions give globally supporting edges, so local turn signs are not
being substituted for convexity.

The continuum existence proof is global. The compact flat quotient maps
locally homeomorphically into R^2/L by the actual coordinate seams; its
image is open and closed and the target is connected. It is a finite
covering. Its total face area equals its positive lattice covolume, so its
covering degree is one. Lifting gives the full plane with disjoint face
interiors. No sampled overlap check is used to extrapolate the continuum.

As a second finite coordinate audit, the checker evaluates the retained
generic fixture (1,11/10,6/5,9/10), verifies strict support for every
nonincident vertex, and tests all possible pairwise lattice overlaps from
exact lattice-coordinate boxes. All 34 comparisons pass, with exact area
density one. Local finiteness and closedness of the periodic union turn
almost-everywhere coverage into every-point coverage, independently of the
flat-cover argument for this fixture.

## Actual shape-only uniqueness, including reflections

Both native angles alpha=4pi/7 and beta=5pi/7 exceed pi/2. A genuine vertex
cannot lie on the interior of another tile edge: a straight sector plus
one genuine angle leaves a positive angle less than pi/2, while two genuine
angles plus a straight sector exceed 2pi. Hence contacts are edge-to-edge.
Full vertices have three corners, and their angle equation forces exactly
one alpha and two beta sectors. This is a geometric consequence, not an
extra matching rule.

Each private heptagon length l0,l2,l4 occurs at just one native H side and
nowhere in P. Thus the tile across it is another same-index H. The two
possible isometries with opposite interiors are the midpoint half-turn and
the line reflection. A reflection puts two beta corners at each endpoint,
whose external edges have equal lengths. The required third alpha corner
belongs to P, which has five distinct side lengths and cannot have two
equal adjacent sides. This rules out each local reflection geometrically.
The half-turn remains, including when the initial H itself is globally
reflected.

A tiling cannot omit H. If it did, P's private side p would meet a same-
index P side. Reflection creates an alpha-alpha endpoint, forbidden by
the vertex star. The half-turn instead leaves a beta sector at each
endpoint with adjacent lengths l5,l6. P's only beta corner has adjacent
lengths p,l6, different because all eight labels are distinct. The third
sector is therefore H, a contradiction. This does not silently assume
both species are used.

Starting from any actual H, the three forced midpoint half-turns generate
translations u=d2-d0 and v=d4-d0 and force all H0+L and H1+L copies.
The formal area identity makes these periods independent. At every
side-0 seam endpoint, the remaining alpha sector has ordered adjacent
lengths l6,l1. Of P's five corners, exactly one has that unordered pair;
the labels on the two noncollinear incident rays fix their order and the
entire isometry, including whether the native reference is reflected.
Thus both P orbits are forced. They already cover the entire plane with
the forced H orbits, so no additional tile or fault-line continuation can
be present. This proves uniqueness up to one global isometry of the whole
admitted tiling, not merely existence of a favored periodic tiling.

## Replays and limits

The author replay was run in-memory and its parsed JSON was exactly equal
to the retained certificate; neither the certificate nor producer was
changed. The independent replay is:

```text
conda run --no-capture-output -n arisearch python3 research/reviews/verify_two_angle_5_7_metric_continuum.py
```

Environment: Python 3.12.13, SageMath 10.9. No configured timeout, memory
cap or random seed. The finite cone domain is all 56 triples of the eight
inequalities; the polynomial geometry statements are symbolic identities;
the generic fixture overlap domain is the complete exact-box-derived 34
comparisons, including nonzero self-translates.

**Counterexamples attempted:** opposite ray orientations, other real
embeddings, disconnected/noncircular quotient links, side-slot reuse,
clockwise/counterclockwise seam mismatch, reflection across private sides,
all-P tilings, ambiguous reflected P fillers, missed overlap translates,
and fault-line tilings outside the generated orbits. Each was excluded by
the exact calculations or the local/global arguments above.
**Remaining uncertainty:** metric pairs outside this shared-order cone
and coincident labels are outside the cone uniqueness statement. They are
not silently excluded or classified here.

## Updated arbitrary-order and five-shared statements

I reread the updated source, including “Local constraints force the
shared-order family” and “A nonzero period for every internally distinct-
side pair.” **Verdict: valid without repair.** The new result excludes
every aperiodic pair in this angle family when each shape's own side
lengths are distinct. It does not classify repeated lengths or the full
metric feasibility of the five-shared case.

The exactly-four-shared reduction is sound. A private H side forces a
same-index half-turn H neighbor. The remaining alpha sector at each
endpoint is P, so the two neighboring H side lengths must occur in P.
Thus private H sides form an independent set in the seven-side cycle,
of size at most three. At most three shared values is impossible. With
exactly four shared values the private sides have cyclic gaps (2,2,3),
so cyclic renumbering/reflection gives private indices 0,2,4. The three
required P-alpha side pairs are {l6,l1},{l1,l3},{l3,l5}. Distinct P sides
make these a path through all four shared lengths, and the private P side
joins the ends. The unique beta corner is one of its endpoints. The
reflection j -> 4-j exchanges the two choices, so the shared-order cone
really exhausts this declared case.

For five shared values I attacked the potential gap between periods of
individual half-turn chains and a period of the entire tiling. There are
at least two H lengths absent from P, since H has seven distinct lengths
and P only five. Fix those native side indices once and for all. Their
midpoints M,N are distinct, so U=2(N-M) is nonzero. Every H copy supplies
one chord between their images, whose open segment lies in H's interior.
A forced side-midpoint half-turn maps the next chord to a straight
continuation, not merely a parallel translated segment. Two steps give a
translation of length |U|; hence every component is a complete straight
line with no finite end or geometric cycle.

Two different chain lines cannot intersect. An intersection in a chord's
open segment would be an overlap of H interiors. At a chord endpoint,
the point is in the interior of a private whole-side seam, not a vertex;
only its two paired H copies occur in a sufficiently small neighborhood,
and both have that same chord line. Thus an intersecting other chain would
be the same chain. Coincident distinct chains are excluded by the same
argument. All chain lines are therefore parallel. Every chain has the
same two-step translation magnitude |U|, including reflected H references.
Choosing the same direction on every parallel line gives one vector u,
not independent chain-specific directions or irrational drifts. Each
chain's H set is invariant under both signs of u, so the entire H set is
invariant under u. This is an exact geometric period, not a limiting
average or a bounded period search.

I independently checked the P-transfer step as well. A P-P contact on an
alpha--alpha side would make two alpha sectors at an endpoint. On a
beta--alpha side, the same-index reflection is likewise forbidden at its
alpha endpoint; the half-turn gives alpha+beta at both endpoints. At P's
beta corner, the necessary alpha belongs to another P. The other beta
cannot be a second P beta, because these two beta corners would share a
same-index beta--alpha side with reflected endpoint order, producing an
alpha--alpha other endpoint. The beta star is therefore P-beta, P-alpha,
H-beta. This forces exactly one P-P side per P and four H neighbors; three
of its alpha corners are H-H-P. None of this assumes P has a private side.

Translate an actual H-H-P alpha corner by the common H period u. The
translated two H copies exist and delimit the same unfilled alpha sector.
The tiling must fill it by P. Its incident side lengths determine a unique
native P corner because its five side lengths are distinct; the ordered
noncollinear rays determine a unique placement, including a reflection.
That tile is exactly P+u. The same reasoning with -u proves invariance in
both directions. Hence the entire admitted tiling has the nonzero period.
The transfer is pointwise for every P, so unanchored fillers or fault-line
exceptions cannot invalidate it.

As an additional hostile cross-check, each P's four H neighbors are joined
by H-H seams at its three H-H-alpha corners. The P-P pairs are dimers,
and an endpoint H of the P-P seam touches both members, joining their
H-neighbor components. Connectedness of the full face adjacency graph
then makes the H-H graph connected; every H-H gluing is a same-index
half-turn by the same unequal-adjacent-sides argument. This independently
excludes variable H orientations modulo pi. The source's parallel-chain
proof already establishes the period without needing this strengthening.

No broad metric classification is inferred from the four-dimensional
certificate: the arbitrary-order period theorem is analytic and rests on
the private midpoint chains and unique P anchors. Repeated side lengths
are the precisely stated remaining loophole; the argument genuinely uses
internal distinctness at both steps. The updated scope is correctly kept
separate from the original unrestricted two-convex-polygon target.
