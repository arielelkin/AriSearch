# Off-normal split points: an exact surviving receiving-H angle gate

**Later status:** the full stated off-normal mark-local receiving-hexagon
component is excluded by the independently reviewed
[combined congruence obstruction](../lemmas/offnormal-mark-local-truncation-obstruction-2026-10-15.md).
The narrower calculations below retain their explicitly stated scope.

Date:2026-10-15. Status: exact necessary-angle witness, independently checked
by a small Fraction verifier. This is not a geometric two-class candidate,
not a plane-tiling existence proof, and not the main-problem solution.

## Genuine changed hypothesis and declared finite gate

Keep the three-sector source incidence, arrow-indexed mark-local unequal
ray fractions and thick cap split on edges0/3, but detach the split point M
from the normal projection of donor apex t. Both t and M remain mark-local;
M lies strictly inside the unit source edge and t lies strictly on its
donor side. The donor apex projection stays inside its edge, so its two
base angles are acute. No cap/P congruence or metric search is run here.

For each mark Z introduce positive external half-apex angles theta_ZT,
theta_ZH with

    theta_ZT+theta_ZH=180-b_ZT-b_ZH,
    0<b_ZT,b_ZH<90.

These are exactly the angle-sum conditions for the two subtriangles split
by ray t-M. They replace theta_ZT=90-b_ZT, which required M to be the normal
foot and powered the preceding obstruction. The two cut angles in each
half remain mark-local and must sum180+theta, with each strictly between
theta and180. Original receiving split-point angles are now merely in
(0,180), with no compulsory obtuse restriction.

The declared gate has22 real angle variables: six H angles, four donor
base angles, four half-apex angles, and eight external cut angles. It
models all16 receiving hexagons from thin/thick source species, both donor
parities, and both endpoints of each receiving edge. Every receiving H
has all12 dihedral prototype aliases available. It includes the actual
source-arrow endpoint-angle formula, strict precursor-quad angles, and
the general truncation inequalities. It is a NECESSARY H-only subsystem;
P/cap matching and metric ray closure remain outside this first gate.

A single Z3 exact-linear-arithmetic call with a declared60000ms timeout
returned SAT. The witness is rational (in fact integral degrees) and is
verified independently without Z3 below. No further metric or quotient
search was launched.

## Exact witness and all actual vertex correspondences

Use the prototype H angle word

    H=(36,156,144,156,72,156).

For BOTH marks X,Y, set

    b_tail=6, b_head=42,
    theta_tail=120, theta_head=12,
    tail cut pair=(156,144),
    head cut pair=(156,36).

Then theta_tail+theta_head=132=180-6-42. Tail cut sum300=180+120,
head cut sum192=180+12, and every cut angle exceeds its original half-apex
angle and is below180. The H word sums720 and every entry lies in(0,180).

The correct source endpoint values are

    thin Xtail=thin Ytail=36;
    thin Xhead=thin Yhead=144;
    thick Xtail=thick Ytail=72;
    thick Xhead=144, thick Yhead=72.

This uses the same actual arrow table as the preceding obstruction; it
does not merge X-tail and Y-tail before their equality is verified.
Every context uses ONE of these four complete six-vertex correspondences:

| Retained source angle / incoming role | H indices in receiving boundary order | Original internal donor-node angle |
|---|---|---:|
|36 / tail|(0,1,2,3,4,5)|48|
|144 / head|(2,1,0,5,4,3)|48|
|72 / tail|(4,3,2,1,0,5)|12|
|72 / head|(4,5,0,1,2,3)|120|

The receiving boundary order is retained source vertex, two external donor
cut vertices, split point M, two internal donor cut vertices. For all four
rows M=156. The uncut internal donor angle is

    inner=360-source_angle-theta_incoming-M,

and is strictly in(0,180). The last two H angles sum180+inner and are each
strictly greater than inner: respectively (72,156), (72,156), (36,156),
and (144,156). Thus all strict quad and corner-truncation angle conditions
of the declared gate hold.

The JSON certificate lists all16 contexts, each actual native receiving
edge/endpoint, exact angle values, and its D6 alias. The independent verifier
reconstructs that full context list and verifies each correspondence from
the source arrows. Therefore the four-row compression is not hiding a
missing parity, mark, or reflected occurrence.

## Exact replay and interpretation

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/offnormal-cap-h-angle-gate-2026-10-15.py
    mise exec -- conda run --no-capture-output -n arisearch python research/searches/offnormal-cap-h-angle-witness-check-2026-10-15.py

The producer prints JSON by default and writes a certificate only with
explicit --output. The retained witness is
`research/certificates/offnormal-cap-h-angle-gate-2026-10-15.json`.
The verifier uses only the standard library, reconstructs the actual arrow
contexts independently, and checks exact Fractions; it imports no producer
code and invokes no solver. Observed result: PASS.

The witness proves that the FULL declared16-context necessary H-angle gate
survives the changed split rule; it is stronger than evading one old cyclic-
word inequality. It does not prove the selected angles come from one actual
ray-fraction/coordinate realization. The common P5 word, all cap/child vertex
identifications, general cap+neighbor angle equations, disjoint sectors,
metric closure, and two-class congruence must still be checked before any
geometric candidate or existence claim. Omission attacks and universal
shape-only forcing are further independent obligations. The next authorized
step should therefore be the remaining P/cap angle gate, with the current
H witness as an exact starting point, rather than a metric census.
