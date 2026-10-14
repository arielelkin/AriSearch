# Independent review of the polygonal-parent perimeter bound

Date: 2026-10-14. **Verdict: VALID for the stated finite simple-polygon
dissections and fixed-atomic iterative consequence.** The reviewer did not
develop the [submitted lemma](../lemmas/nonconvex-parent-hexagon-perimeter-bound.md)
or its repaired sector count. No author artifact was changed during review.
No classification of arbitrary two-hexagon tilings follows.

The claim is: a compact simple polygon M with p genuine corners, dissected
into finitely many compact convex children having at least six genuine
sides, satisfies perimeter(M)≤(2p−6)L, where L is their largest native side
length. The parent may have reflex corners; partial contacts and reflections
of children are permitted. The union must be the full disk-support M,
with pairwise disjoint interiors. Holes and disconnected supports are
explicitly outside this statement.

I independently reconstructed the planar count. Planarizing at every native
child corner and parent corner captures contact endpoints: a positive-length
contact cannot end in the relative interiors of both native sides unless
the sides are collinear and continue there. Crossing native sides would
give an interior overlap. Redundant degree-two points can therefore be
suppressed. The resulting graph is connected and has precisely the t child
faces inside its simple parent boundary, so V−E+t=1.

Count every incident child sector at each retained graph vertex, including
an angle-π sector when the vertex lies inside a child side. If S is this
total and F counts the flat incidences, N=S−F is exactly the number of
native child corners. A reflex parent corner may indeed lie inside a child
side; F must include it. That does not invalidate the degree count: each
sector is a positive-angle interval between consecutive incident rays.
There are m+1 rays at a boundary vertex with m child sectors, and m rays
at an interior vertex. Distinct coincident rays do not create extra sectors.

At a parent corner m≥1. In a parent-side interior a retained vertex has
m≥2: one flat child sector would give a suppressed degree-two point,
while one strict convex child corner cannot fill the parent half-disc.
At an interior retained vertex m≥3: two sectors fill2π only if both are
flat, which again is a suppressed point. Thus, writing b,i for the two
non-parent vertex counts and X≥0 for all excess sector incidences,

    S=p+2b+3i+X,
    2E=S+p+b,
    2t=2+b+i+X,
    6t−N=6−p+b+2X+F.

These identities were rederived from degree counting and Euler; they do
not assume a convex parent or omit flat sectors at parent corners. Since
N≥6t, they imply b+2X+F≤p−6, hence b≤p−6. Each of the p+b elementary
boundary segments lies in one native child side and has length at mostL.
Therefore perimeter(M)≤(p+b)L≤(2p−6)L. If p<6 the inequalities instead
prove that the assumed dissection cannot exist, as expected.

The attacks considered were a T-junction, a flat child sector at a reflex
parent corner, a degree-two boundary subdivision, multiple incidences on
one ray, a child contacting the parent only at an isolated vertex, and an
incorrect Euler correction for holes. The sector convention handles the
first five, and the explicit simple-parent hypothesis excludes holes.
No unresolved defect was found in the stated finite theorem.

For the iteration consequence, finitely many fixed atomic shapes give one
fixed finite L. A similarity leaves a parent's p unchanged while expansion
by λ>1 multiplies its perimeter by λ. Iterating genuinely compatible
substitution rules would dissect λᵏM into the same unit atoms: compose
the rules and then replace each smallest parent with its defining finite
atomic patch. The bound prohibits those dissections for arbitrarily largek.
No bound on the number of atoms is needed. A valid one-generation rule
below the stated numerical threshold is not itself excluded; rather it
cannot be iterated in the claimed fixed-atomic hierarchy. Rescaled atoms,
infinitely changing parent boundaries, and other hierarchy mechanisms
remain outside this consequence.

This is an analytic review, not a finite numerical or solver census.
The proof requires only the explicitly stated planar cell decomposition
and finite polygonal geometry; no external classification or literature
novelty claim is used. The broader aperiodic-pair target remains unresolved.
