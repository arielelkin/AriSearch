# Pentagon/heptagon corner transport: completeness blocker

**Status: blocked before a flow LP.** This record concerns only the fixed
unit-incircle P/Q metric in the reviewed first-gate certificate. It proves
neither a mixed plane tiling nor mixed nontilability. Both monohedral
omissions remain excluded by the reviewed corner counts. No discovery-log
edit is included.
[Independent Sol hostile review](../reviews/pentagon-heptagon-corner-transport-sol-hostile-2026-10-19.md)
confirms this narrow result and its limits.

## Exact inputs and attempted certificate

P has cyclic angles (60,105,115,125,135), Q has
(150,150,120,120,120,120,120). The exact coordinates and their selected
cyclotomic embedding are in
`research/certificates/pentagon-heptagon-astra-first-gate-2026-10-19.json`.
The angular atlas, strict convexity, and omission proofs are independently
reviewed in
`research/reviews/pentagon-heptagon-astra-first-gate-sol-hostile-2026-10-19.md`.
The attempted new mechanism is a bounded-distance transport on actual
contacts/corners, with bounded transfers, a positive uniform surplus per
tile, and positive area density. Summing antisymmetric transfers over a disk
would leave only O(R) crossing transfers but require Theta(R^2) surplus.
No such transport is asserted here. In particular, the first-gate rational
frequency vector is not a stationary measure on geometric contact states.

## Complete two-tile positive-length contact parameterization

Fix an oriented native side i of a reference tile X and choose a coordinate
s along its line, putting its endpoints at 0,L. Its interior lies above the
line. A contacting tile Y has native side j of length M on this same line,
with its interior below it. Choose either chirality for Y relative to X;
for each chirality the required side direction and interior half-plane fix
the linear isometry uniquely. Its remaining translation is the scalar t,
so its endpoint coordinates, in increasing line order, are t,t+M.
For a positively oriented boundary the ordering of native endpoint labels
reverses when the determinant changes. Retain these labels explicitly.
The contact interval is

    [max(0,t), min(L,t+M)],       -M < t < L.

This includes equal endpoints, either containment, and either proper
staggering. Partition by all comparisons among 0,L,t,t+M, including the
equality cases. The discrete choices are X,Y in {P,Q}, all 5 or 7 native
side indices, and both relative determinants. Overall rigid motions and
overall reflection carry no further data. All lengths are the fixed exact
certificate lengths; t is a real parameter, not a cyclotomic coefficient.

**Proof of two-tile completeness.** Two convex polygons with disjoint
interiors and positive-length intersection have a common supporting line;
their intersection is a segment on that line. A strictly convex polygon has
one native side on a given supporting line. Interiors must lie on opposite
sides, since a relative interior point of the intersection otherwise has
interior points common to both polygons. An isometry mapping the chosen side
to that line has precisely the discrete determinant/direction choice and
the tangential translation above. Conversely these placements have disjoint
interiors by their opposite half-planes, and their intersection is exactly
the displayed nonempty interval. Thus this is an exact continuum schema,
not a complete finite geometric contact atlas.

Point contacts require the separate indexed angular-star schema from the
first gate: all ten 360-degree multisets and the two one-flat-host
multisets, all cyclic orders, native labels, and reflections. Two flats with
no corners describe a seam interior. This handles pointwise angle data but
does not establish compatibility between distinct endpoints.

## Restrictions at a partial-contact endpoint

If an endpoint of one tile falls strictly inside a side of the other, the
latter contributes a flat sector. The complete angular census therefore
forces the remaining genuine corners to be AF or AAA, with A=P0=60 and
F any of Q2,...,Q6=120. In particular B,C,D,E,G cannot terminate in a side
interior. This is a necessary local restriction, not a condition that all
remaining contacts can be completed simultaneously.

## An exact continuum surviving these local restrictions

Take Q side 2, whose two endpoint angles are both 120. Its exact length is

    L = cot(120/2) + cot(120/2) = 2/sqrt(3).

Place two copies of Q on opposite sides of a line with their respective
side-2 intervals [0,L] and [t,t+L], where 0<t<L. Such placements exist by
the preceding parameterization, with either allowed choice obtained by
appropriate reflection and endpoint labeling. They have contact [t,L].
At t the second Q supplies an F corner and the first Q a flat sector; at L
the roles reverse. Each endpoint can be completed in a sufficiently small
neighborhood by a P0 corner, since 180+120+60=360. Strict convexity places
each polygon inside its supporting half-plane/corner wedge. Choose the two
neighborhoods disjoint. This proves pointwise angular realizability at both
endpoints for every t in the open interval. It does not claim the two added
whole P tiles avoid all other tiles, or that any such configuration extends
to a plane tiling.

All members have identical native labels, endpoint order, endpoint angular
stars and chirality choices. Nevertheless their contact lengths L-t differ.
Thus any atlas retaining just that discrete data identifies unequal exact
endpoint displacement vectors. Endpoint-to-endpoint transport and geometric
closure cannot be certified merely by that quotient: along a collinear
contact chain the actual displacement includes L-t, whereas its proposed
native state is constant as t varies. This is an explicit lost variable;
it is not a proof that every conceivable discrete quotient fails.

## Precise missing completeness lemma and stop

Before a finite rational transport LP one needs a proved finite quotient of
**joint tile contact states**, not merely two-tile states or angular stars.
A sufficient lemma would supply:

1. A finite list of side partitions and corner assignments for each species,
   including all interior breakpoints, reflected copies and endpoint labels.
2. For each list item, an exact description of its jointly realizable offset
   domain; pairwise compatibility alone does not suffice.
3. A proof every unrestricted plane tiling induces one of these states at
   every tile, with all stated transition/conservation identities valid.
4. A transport assignment constant on the quotient, or an exact argument
   that its chosen offset dependence is bounded and satisfies the required
   surplus inequalities throughout each realizability domain.

A complete semialgebraic parameter domain retaining real offsets is also
possible in principle, but would require a universal exact inequality proof
or a justified finite reduction before a rational LP result can serve as a
certificate. No such reduction or universal transport inequality has been
proved in this gate. The continuum example alone does not exclude finite
cell decomposition, does not exclude an angle-only discharging proof, and
does not prove that a successful bounded-distance certificate is impossible.

The two-tile schema above is complete at its stated scope. What remains
unproved is its refinement into the complete joint states required by the
proposed finite corner-transport calculation. Therefore no flow LP was run,
no stationary geometric balance is claimed, and this branch stops at the
contact-state completeness gate under protocol section 5. Protocol section
19 leaves the overall research problem open and permits other mechanisms.
A concrete reopening step is an exact joint side-partition elimination or
a transport formula whose validity can be proved uniformly in the retained
real offsets; a larger patch radius does not supply that lemma.
