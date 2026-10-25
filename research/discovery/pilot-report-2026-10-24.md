# Convex-polykite discovery pilot: empty eligible catalogue

Date: 2026-10-24. **Unresolved globally.** Status: completed bounded discovery
experiment; independent witness audit passed. No aperiodic pair, promising
pair, or plane-nontilability result is claimed.

## Outcome and decision

The complete catalogue of convex whole-kite unions of at most eight cells
has six congruence classes. Each shape has an independently checked exact
periodic monohedral tiling. Consequently all 15 unordered pairs are excluded
by singleton witnesses before any mixed-pair solver or patch-growth work.
There are **zero eligible pairs, zero flags, and zero UNKNOWN outcomes**.

Stop this pilot at the declared cap. The six-cell preflight already yielded
these same six shapes; the one allowed increase to eight added none. This
small area-bounded catalogue does not justify a general polygon engine, an
interactive workbench, or automatically increasing the area bound. The next
comparison worth specifying is exact boundary-direction/length enumeration
conditioned on plausible contact compatibility. It should be assessed by
geometric diversity and useful growth yield, not raw pair counts. No such
comparison has been run. A nonretained generator timing probe during development
reached twelve cells (nine classes); no shape above eight was screened, and
that probe is outside the retained replayable census and its conclusions.

## Exact finite search

Coordinates `(x,y)` denote `(x,y*sqrt(3))`. The translation lattice is generated
by `U=(12,0)` and `V=(6,6)`. Each triangular face is split into three congruent
60/90/120/90 kites using its centroid and edge midpoints. A cell has exact ID
`(i,j,face,corner)`, with `face` in `{0,1}`, `corner` in `{0,1,2}`. Each cell
has raw shoelace double-area 24. Convexity includes collinear constituent edges;
polygon outlines remove collinear vertices.

The generator exhausts convex unions with 1 through 8 cells. It reduces
states only by translations and D6 mesh symmetries, then groups final polygons
under full Euclidean congruence using cyclic pairwise squared distances.
Scale is preserved. Grid-distinct embeddings of congruent polygons are
retained for placement generation.

| Exact cell count | Convex congruence classes |
|---|---:|
| 1 | 1 |
| 2 | 1 |
| 3 | 2 |
| 4 | 0 |
| 5 | 0 |
| 6 | 2 |
| 7 | 0 |
| 8 | 0 |

Completeness mechanism: start from a single cell, add an edge-neighbor, then
repeatedly fill every cell with positive-area intersection with the convex
hull. Any convex whole-cell target containing the current cells must contain
those forced cells. Thus closure cannot escape a target, and adjacent target
cells can build every convex target. The finite cell-intersection halo follows
from the exact triangular lattice coordinates.

An unpruned connected-polyform enumeration with a separate directed-boundary
convexity test independently reproduces all catalogue shapes and embeddings
through eight. Its connected mesh-class counts are
`1,2,4,10,27,85,262,873`; convex counts are `1,1,2,0,0,2,0,0`.
The witness-audit agent additionally cross-checked a separately constructed
mesh and independent connected enumeration through four.

The periodic solver enumerates translations, reflections, and sixth-turn grid
rotations for every supplied embedding. It exact-covers the six cell phases of
each HNF quotient, rejecting tile placements that overlap their own translates.
The configured domain cap is index four: vectors `(a,0),(b,c)` in lattice
indices, `a,c>0`, `0<=b<a`, `a*c<=4`. Search stops at its first positive witness.
All six searches succeeded at index one, so no larger domain was attempted.
Each solve has 0.1 second wall limit, 0.01 deterministic effort limit, one
worker, and seed zero. The retained run disables theorem shortcuts; every
omission has a concrete tiling witness.

| Shape | Cells | Sides | Tiles per index-one period cell |
|---|---:|---:|---:|
| K0000 | 1 | 4 | 6 |
| K0001 | 2 | 5 | 3 |
| K0002 | 3 | 3 | 2 |
| K0003 | 3 | 5 | 2 |
| K0004 | 6 | 4 | 1 |
| K0005 | 6 | 6 | 1 |

All witnesses have periods `U,V`. Exact polygon definitions, occupied cell IDs,
placed tiles, hashes, attempted domains, versions, and command are retained in
[runs/kite-n8-2026-10-24/screen.json](runs/kite-n8-2026-10-24/screen.json).
Inspect every shape in the [static gallery](runs/kite-n8-2026-10-24/gallery.html).

## Verification and reproducibility

The independent verifier does not import generator geometry or the solver.
It reconstructs the mesh, checks each polygon equals its cell union, verifies
Euclidean congruence, checks exact quotient coverage and total area, and checks
all potentially intersecting period translates using exact rational bounds.
The retained witnesses require 120 translated-overlap checks in total. It also
binds each witness to its catalogue shape and checks envelope hashes, metadata,
and the funnel. The envelope verifier intentionally accepts only the retained
all-positive, no-theorem case; it does not certify UNSAT or a general search
containing unresolved outcomes.

Verification completed: locked environment check passed; 27 discovery tests
passed; independent retained-witness check passed; fresh catalogue generation
and solver replay reproduced the stable result hash; retained evidence stayed
unchanged. Core regenerated search and verification were subsecond on this
machine, excluding interpreter/environment startup. This is a tiny empty
pilot, not a useful estimate of large-campaign throughput.

```bash
mise exec -- conda run --no-capture-output -n arisearch python -m pytest research/discovery -q
mise exec -- conda run --no-capture-output -n arisearch python -m research.discovery.verify research/discovery/runs/kite-n8-2026-10-24/screen.json
mise exec -- conda run --no-capture-output -n arisearch python -m research.discovery.replay
```

Replay operates in memory and does not rewrite retained files. To run the
same experiment to a new destination:

```bash
mise exec -- conda run --no-capture-output -n arisearch python -m research.discovery.screen --max-cells 8 --max-index 4 --solve-seconds 0.1 --deterministic-time 0.01 --no-theorems --output-dir /tmp/arisearch-kite-replay
```

Stable result SHA-256: `92e423c7ba3986fce16009f99916895df625679c1489fdc4f6ca761b86bd5ea5`.
The output destination is recorded separately from the stable search hash.
These checks are standalone; the historical repository replay registry is
unchanged.

## Limits and review

The grid alignment basis is [Appendix A, Lemma A.5 of the hat paper](https://arxiv.org/html/2303.10798v2#A1).
It applies to finite sets of disk polykites from the same grid and preserves
existence and weak/strong periodic existence. It does not assert every tiling
is aligned or put a bound on periods. The positive periodic witnesses here
are valid regardless of that alignment theorem. No absence-of-period claim
is made.

Generation, screening, and independent audit were delegated to separate Sol
agents. The audit found no unresolved generator or retained-witness defect.
Integration fixed a test import that prevented collection of the combined
suite; the final suite passes. Existing user edits to `discovery-log.md` were
preserved.

Patch-growth orchestration, complete-corona scoring, interactive manipulation,
other grids, and a second exact generator were deferred because every shape
in this finite catalogue already has a periodic omission. The generic
exact-cover primitive checks exterior conflicts, and the independent patch
verifier checks target coverage; neither is presented as a completed growth
workbench. No larger-area convex-polykite family is excluded by this pilot.
