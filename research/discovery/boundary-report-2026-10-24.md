# Exact boundary-word comparison: 2,415 pairs, no surviving leads

Date:2026-10-24. **Unresolved globally.** Completed bounded discovery experiment,
independently reviewed. The aim was candidate yield and fast falsification,
not a proof or a new aperiodic construction.

## Outcome

The exact library contains 126 convex hexagon congruence classes. Positive
central-symmetry omissions remove 56 monohedral tilers, leaving 70 shapes and
all 2,415 unordered pairs. The first pass produced:

| Outcome | Pairs |
|---|---:|
| Failed a seeded native radius-one disk | 2328 |
| Found a periodic tiling with at most four faces | 62 |
| Passed radius one but failed radius two | 21 |
| Passed native radius four at both seeds, no period found through four faces | 4 |

All four initial survivors then yielded exact eight-face periodic tilings.
Final discovery classification: **2,328 local failures, 21 larger finite
failures, 66 verified periodic pairs, zero surviving leads, zero UNKNOWNs**.
A failed seeded disk means failure of the requested both-seed screen; it is
not asserted to prove unrestricted pair untileability, particularly because
the target permits omitting a species. Bounded negative singleton searches
also do not prove monohedral nontilability.

The initial four survivors each had geometrically valid 61-tile native disks
around both prototile seeds. Those patches were samples from pairs that
nevertheless tile periodically. This is concrete evidence for strengthening
the periodic screen before spending effort on deeper supportive patches.

## Exact library and completeness

A boundary word `(s0,...,s5)` has integer entries in `{1,...,6}`. Its exact
successive edge directions are `(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)`,
where coordinates `(x,y)` mean Euclidean `(x,y*sqrt(3))`. Physical side lengths
are twice the native integers. All six interior angles equal 120 degrees.
Four free lengths determine the other two by

```text
k=s0-s3, s4=s1+k, s5=s2-k.
```

Check every entry's bound and group the closed polygons under all cyclic
rotations and reversals. A positive closed six-direction edge sequence is a
strictly convex hexagon. Absolute size is preserved; no tile is individually
gcd-normalized. The catalogue has 106 integer-similarity families as a separate
audit statistic. The 2,415 size-sensitive pairs represent 2,405 classes modulo
common integer scaling; every pair was nevertheless screened.

An independent verifier exhausts all 6^6 = 46,656 ordered words through the actual
retained bound, checks closure and geometry, and reproduces the complete 126
class catalogue. D6 state lists include reflections. Exact cell, polygon,
word and state definitions are retained in the JSON evidence.

This library changes the candidate representation and length coverage, not
the 120-degree angle mechanism. It contains previously studied fixtures and
makes no novelty claim. A prior three-length seed note incorrectly described
its two species' corner-pair sets as identical: A has `{12,22,13}`, B has
`{23,22,13}`; their union has all four pairs. New compatibility metadata keeps
the species separate and retains equal-length corner loops. The older note
was not edited by this experiment.

## Finite solver and declared budgets

For 120-degree hexagons, a tile corner cannot lie inside another tile side:
the remaining 180-degree half-plane cannot be filled by 120-degree corners.
Thus contacts in a plane tiling are whole edges, three faces meet at a vertex,
and all tiles share the same three unoriented edge directions. The repository's
[reviewed development lemma](../lemmas/equiangular-hexagon-honeycomb-development-2026-10-19.md)
provides the bridge between a whole infinite legal honeycomb assignment and
a plane tiling. A finite legal assignment alone does not supply that assignment.

The native model has steps `(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)`.
Each face independently chooses either species and any reflected/rotated
native word. Shared edge slots must have equal actual lengths. No requirement
forces both species into a periodic witness. Bitset arc consistency and
bounded deterministic depth-first search solve each finite domain, retaining
SAT, fully exhausted UNSAT, and budget-exhausted UNKNOWN separately.

Baseline: every noncentral singleton and all 2,415 pairs; HNF lattice generators
`(a,0),(b,c)`, `a,c>0`, `0<=b<a`, `a*c<=4` (15 domains); disk radii 1, 2, 4;
1,000 DFS nodes and 50,000 propagation revisions per solve; 600 process-CPU-second
outer cap. A fixed seed word is legitimate up to global dihedral symmetry.
The local two-seed screen precedes periodic search; deeper disks run only
when no periodic witness has appeared. All21 deeper failures occur at radius 2.

Focused follow-up was authorized after observing exactly four survivors:
HNF index <= 16 (220 domains), radii 1, 2, 4, 8, 10,000 nodes and 500,000 revisions per
solve,60 CPU seconds per selected pair. All four stopped at a positive index8
witness, so no radius eight disk was attempted. Noncentral singleton scans to 16
were repeated in each focused run; they found no witness in that finite scope.
There was no length-bound increase and no other candidate family was searched.

A native radius-r ball is defined by `max(abs(i),abs(j),abs(i+j))<=r` and has
`1+3r(r+1)` faces. These are exact native graph-ball patches, not a measured
physical disk radius, a maximal Heesch number, or an infinite-extension claim.
Fresh solutions at different radii need not extend the same saved patch.

Baseline search counters: 4,699 finite solves, 11,490 nodes, 166,834 propagation
revisions, largest solve 25 nodes / 2,192 revisions. Initialization work is counted;
duplicate local/growth records do not double-count the same solve. The
retained final baseline took2.44 seconds of process CPU time. All five
retained runs together took13.41 seconds, excluding environment/interpreter
startup and independent verification. These measurements describe this mostly
locally failing family; they do not predict performance for general polygons.
Repeated whole-library singleton scans dominate the focused-run overhead and
are an obvious cache opportunity if this solver is used further.

## The four false positives

Each eight-face carrier has HNF`(2,0,4)`. The following exact period vectors
use coordinates `(x,y*sqrt(3))`. Each witness uses both species.

| Follow-up | Native word A | Native word B | Period vectors |
|---|---|---|---|
| 1 | `(1, 3, 2, 2, 2, 3)` | `(2, 4, 4, 3, 3, 5)` | `(0, -12)`, `(40, -12)` |
| 2 | `(1, 3, 3, 2, 2, 4)` | `(3, 4, 4, 4, 3, 5)` | `(0, -12)`, `(32, -12)` |
| 3 | `(2, 4, 3, 3, 3, 4)` | `(3, 5, 5, 4, 4, 6)` | `(0, -16)`, `(52, -16)` |
| 4 | `(2, 4, 4, 3, 3, 5)` | `(4, 5, 5, 5, 4, 6)` | `(0, -16)`, `(44, -16)` |

Pairs 1/3 and 2/4 are related by adding one to every side length of both shapes;
they are not four independent angle mechanisms. No general family theorem
is claimed here.

The [baseline gallery](runs/boundary-m6-2026-10-24/gallery.html) intentionally
shows the initial four radius-four survivors at its four-face cutoff.
Their stronger periodic resolutions have separate galleries:
[1](runs/boundary-m6-2026-10-24/followup-01/gallery.html),
[2](runs/boundary-m6-2026-10-24/followup-02/gallery.html),
[3](runs/boundary-m6-2026-10-24/followup-03/gallery.html),
[4](runs/boundary-m6-2026-10-24/followup-04/gallery.html).
Those galleries render repeated periodic motifs with a dashed period cell.
The [manifest](runs/boundary-m6-2026-10-24/manifest.json) binds the complete
baseline and every focused challenge; their JSON contains every pair outcome,
exact polygon and placement, attempted domain, budget, source hash and command.

## Independent checks and replay

The solver-free verifier reconstructs the geometry from boundary words and
checks both endpoints of every matched edge, every development cycle, and
all stated origins. Patch verification checks the full native domain,
seed species, all-pair interior disjointness, and absence of unintended
nonnative contacts. Periodic verification checks every wrapped seam, exact
period-area coverage, independent period vectors, and all potentially
intersecting lattice translates using rational coordinate bounds.

It verifies 103 retained patch certificates and 66 periodic certificates,
binds them to their library species and finite-search summaries, checks full
or explicitly focused pair coverage, verifies source/data hashes, and checks
the funnel. SAT summaries whose smaller witnesses were replaced by stronger
ones remain solver reports. Negative labels are recomputed by fresh replay;
no independent UNSAT proof object or unrestricted exclusion is claimed.
Tiny torus instances were also checked against brute-force assignments, and
a known four-face periodic mixed fixture passed as a control.

Validation: locked environment passed; 57 discovery tests passed;
all five independent evidence-envelope audits passed; fresh replay reproduced
all five stable hashes without writing any retained files. The existing kite
pilot and historical replay registry remain unchanged.

```bash
mise exec -- conda run --no-capture-output -n arisearch python -m pytest research/discovery -q
mise exec -- conda run --no-capture-output -n arisearch python -m research.discovery.boundary_replay
```

For independent positive-geometry/coverage verification without rerunning
finite searches:

```bash
mise exec -- conda run --no-capture-output -n arisearch python -m research.discovery.boundary_replay --verify-only
```

Baseline reproduction to a new destination:

```bash
mise exec -- conda run --no-capture-output -n arisearch python -m research.discovery.boundary_screen --max-length 6 --max-index 4 --radii 1 2 4 --node-budget 1000 --propagation-budget 50000 --cpu-seconds 600 --output-dir /tmp/arisearch-boundary-m6
```

Focused searches use`--pair ID_A ID_B` and the retained command. `--grow`
requests a fresh larger native disk for that pair; it does not lock a saved
patch. Fixed-patch manipulation was deferred because all four leads were
resolved by periods.

Baseline hash:`8bfef360d999f8b25bb98e4f2d5c971a452d1e2b0a30d09cba63dd61b507376a`.
Experiment manifest hash:`3436cdfbc9fb2c4f702087b2395772424cd68a8586b53ed621483c23e76bb0bc`.

## Comparison and stop/go decision

The first small-area kite census had six monohedral shapes and no pair work.
This length library generated 70 noncentral shapes and exercised 2,415 pair
screens, including nontrivial growth and periodic falsification. The search
loop is cheap on this family; candidate yield remains zero.

Stop this declared length-six experiment. Do not automatically spend on length seven
or larger native disks. For another campaign in this same angle family, move
the cheap periodic cutoff to at least eight faces before ranking deeper
patches. The more informative next generator comparison should vary angle
sequences or exact direction libraries, with its placement-mode limitations
explicit, rather than interpret more size variants as new mechanisms. No broader candidate family was searched.
