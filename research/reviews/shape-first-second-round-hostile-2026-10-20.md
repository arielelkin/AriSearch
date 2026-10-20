# Hostile review: second shape-first round, 2026-10-20

**Scope and verdict.** I reviewed the exact P5/Q8 six-template script and the
P5/Q7 self-cap report/script against the unrestricted problem definition.
The finite local claims below survive the checks stated here. Neither pair is
an aperiodic-pair solution. In particular, four P5/Q8 metrics have a
stronger **falsification**: they admit no plane tiling at all by the forced
12-ring obstruction and exact finite conflict computation described below.
The remaining two P5/Q8 metrics have branching P/P seams and no plane
existence or global forcing proof.

## P5/Q8: assumptions and independent checks

The angle words are `P=(100,110,100,120,110)` and
`Q=(150,130,140,130,140,120,140,130)`. Their sums are 540 and 1080.
Every angle exceeds 90 degrees. Thus a T-junction on a tile side is
impossible: filling its 180-degree opposite half-plane needs at least two
corners, already exceeding 180. Every tiling by these shapes is therefore
edge-to-edge. Every vertex has exactly three corners, since two corners sum
to less than 360 and four exceed 360. This argument covers reflections and
partial contacts; the latter cannot occur in a tiling.

The full angle triples are `(100,110,150)`, `(100,120,140)`,
`(100,130,130)`, `(110,110,140)`, `(110,120,130)`, and
`(120,120,120)`. Consequently each Q 150-degree corner must meet a P
100-degree and a P 110-degree corner. P-only and Q-only tilings are
impossible: their 100/110 and 130/140/150 corners, respectively, belong to
no monochromatic triple. This is a direct species-omission check and does
not depend on the imported pentagon classification.

The script constructs the P lengths from a free `t`, with `P0=P3=t`,
`P4=1`, and closes the two vector equations for `P1,P2`. For Q it fixes
`Q0=Q7=1`, puts `P1,P2` on the two sides adjacent to one of Q corners
1, 3, or 7 in both orders, chooses remaining positive rational lengths,
then solves Q sides 4 and 5 from exact closure. All six resulting length
vectors are positive, close exactly, and produce strictly convex polygons.
The linear-programming margins are floating-point discovery diagnostics;
the six selected metrics are checked by exact algebraic arithmetic after
selection. The four-tile tests account for both Q reflections and check
every pair of convex polygons by exact separating axes. The script prints
eight nonoverlap records per metric, although some placement parameter
records describe the same geometric tile. This is an existence result for
finite patches only.

The 2P+Q torus search tests two relative chirality bits after fixing the
first P face, all same-length edge pairings, and trivalent 360-degree vertex
cycles. It returns UNSAT for four chirality choices for each of six exact
metrics. This is a necessary-condition superset for edge-to-edge
translational tori, so UNSAT excludes that **specific three-face quotient**.
The solver result has no independently checkable UNSAT certificate here and
does not exclude a larger periodic tiling. A SAT result from that model
would also require planar/translation geometry validation; none is claimed.

## P5/Q8: the four forced-ring obstructions

For all six exact metrics P sides 0 and 3 share a length `t` that no Q side
has. Since every tiling is edge-to-edge, each must meet a P side 0 or 3.
I checked all four native side pairs and both relative chiralities at their
endpoints. For `(Q corner, radial reverse) = (1,yes), (3,no), (3,yes),
(7,no)`, the only completable matches are side 0 against side 3 (or the
reverse), with the same chirality and opposite edge direction. One endpoint
needs Q 150 at native corner 0, the other Q 130 at corner 1, 3, 3, or 7
respectively. The script's `P_SEAM_ENDPOINT_ATLAS` reproduces exactly
these two directed descriptions for each of the four cases. The
corner-3 exclusions are particularly transparent: side 0/0 with opposite
directions has a 150 vacancy but unequal outer-ray lengths; its reflected
version has a 160 vacancy. Side 3/3 has 130 or 140/120 vacancies whose
outer-ray lengths match no respective Q corner. The reflected 0/3 join
gives two 140 vacancies with incompatible rays. The exact endpoint atlas
performs the analogous length check for the corner-1 and corner-7 metrics.
For `(1,no)` and `(7,yes)`, 0/0 and 3/3 also have complete endpoint stars,
so the ring inference does not apply to them.

Following P side 0 to its forced P side 3 neighbor, and then that tile's
side 0, defines a deterministic same-chirality isometry. Its twelfth
iterate returns the starting placement exactly; the first twelve
placements are distinct and have pairwise disjoint interiors. Thus every
P belongs to such a closed 12-P component in any putative plane tiling.
This global inference relies on the proved edge-to-edge property and on
the complete local seam atlas, not on assuming that a generated finite
patch extends.

Each of the twelve 150-degree seam endpoints then requires a Q corner 0.
Its two length-1 incident sides can be assigned to the two P rays in two
geometrically distinct ways, including the reflected Q. A Q has only one
150-degree corner, so these twelve required Q tiles are distinct. The
script retains both options at every endpoint, rejects any option
overlapping a P in the closed ring, checks all pairs of Q options by exact
separating axes, and backtracks over all `2^12` assignments. For both
corner-3 metrics it reports 144 conflict entries, for `(1,yes)` 192, and
for `(7,no)` 180; all four have zero assignments. I replayed the frozen
script. A separate verifier at
`research/reviews/p5q8-ring-independent-2026-10-20.py` rebuilds the four
length vectors, full P/P seam endpoint atlas, ring placements, reflected
Q choices, exact conflicts, and all 4096 assignments without importing
the author program. Subject
to these exact finite checks, these four metrics are **falsified for plane
existence**, not evidence for aperiodicity. The conclusion does not
transfer to the two branching metrics.

## P5/Q7 self-cap: assumptions and checks

The stated number-field formulas give positive side lengths, exact vector
closure, and positive consecutive edge crosses for both polygons. The
prescribed Q/Q seam across Q side 0 has two isometric choices, half-turn
and reflection. At either endpoint the P 60-degree corner has two ways to
assign its equal length-1 arms. Hence the eight 2P+2Q base patches cover
that **prescribed full-edge seam**. For each base the script tests both
half-turn and reflected Q attachment across Q side 2, yielding sixteen
case records. This does not enumerate every possible local continuation
of either shape. All eight bases are collision-free. Four cap-assignment
patterns allow both Q side-2 mates immediately; four block both by overlap
with the far P. The earlier apparent universal blockage is therefore false.

The full-edge 2P+2Q translational-torus exclusion is sound within its
domain. Q side 0 must pair Q side 0: pairing a P length-`d` edge leaves
an impossible 75-degree endpoint vacancy. This forces the two Q and the
two P 60-degree caps into one of the eight bases. Exact directed-edge
balance fails six of the eight. The `(H,0,1)` survivor has a required Q
side-2 mate overlapping a P. The `(H,1,0)` survivor has two forced period
vectors from the unique Q side-2 and side-4 pairs. Their parallelogram
area divided by the four-face tile area lies strictly between 1 and 2,
contradicting its required positive integer lattice index. I replayed the
exact inequality and all sixteen orientation records. This excludes only
a four-face edge-to-edge translational quotient. It leaves larger and
partial-contact periodic tilings, plane existence, and global forcing open.

Q-only tilings are independently excluded: its only angles are 120 and
150, no T-junction can form, and a 150 corner belongs to no Q-only
360-degree star. P-only exclusion relies on the imported complete
monohedral convex-pentagon classification and its exact 15-type filter;
I did not reprove that classification.

## Repairs and remaining uncertainty

No author file was edited. The P5/Q8 author report states the automatic
edge-to-edge lemma and identifies all four plane-nonexistence obstructions.
No present
bounded torus result establishes universal aperiodicity. The live
`(1,no)` and `(7,yes)` P5/Q8 metrics still need either an infinite-plane
construction or a global contradiction. The P5/Q7 self-cap metric needs a
new extension or contact invariant before further bounded patch growth is
probative.

**Final verdict:** four P5/Q8 exact pairs: falsified for tilability by
the exact finite Q-ring check; two other exact pairs: unresolved. The
six-template and 2P+Q finite claims are valid in their stated domains.
P5/Q7 self-cap: finite
claims valid in their stated domains; unrestricted objective unresolved.
