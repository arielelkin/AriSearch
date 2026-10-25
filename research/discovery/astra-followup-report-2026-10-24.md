# Astra-directed follow-up: larger lengths and mixed obtuse angles

Date: 2026-10-24. **Unresolved globally.** Both authorized bounded experiments
are complete. Neither produced a surviving discovery lead. No growth engine
was built because the declared mixed-angle allocation gate failed.

## Why these two experiments

A fresh Astra review recommended one inexpensive length-eight calibration,
then a catalogue/contact audit that changes both angles and face topology.
The user explicitly authorized following those recommendations. Existing
Sol agents separately handled calibration, mixed exact geometry, and
independent verification. The earlier kite and length-six source files and
evidence were preserved.

## Length-eight calibration

The complete library uses positive integer native side lengths 1 through 8
at successive 60-degree headings, with exact closure and all cyclic/reflected
states. Shapes retain their sizes. It contains 330 congruence classes, of
which 120 centrally symmetric hexagons have positive monohedral omissions.
All 21,945 pairs of the remaining 210 shapes were screened. This includes
the earlier length-six shapes and pairs; the two censuses are not disjoint.

| Final finite-screen outcome | Pairs |
|---|---:|
| Local seeded-disk failure | 21,660 |
| Larger finite-disk failure | 55 |
| Exact periodic witness | 230 |
| Surviving leads / UNKNOWN / unfinished | 0 / 0 / 0 |

The periodic cutoff was eight honeycomb faces before deeper native growth at
radii 1, 2, 4. Each finite solve had 1,000 DFS nodes and 50,000 propagation
revisions; the baseline outer cap was 600 process-CPU seconds. Only survivors
would have received index-sixteen / radius-eight challenges under one shared
additional 600 CPU seconds. There were no survivors, so no stronger follow-up
or M9 run occurred.

Actual search time was 4.52 process-CPU seconds; the full wrapper including
record writing and the gallery took 5.35 seconds. The search performed
40,074 finite solves; its largest solve used 25 nodes and 1,152 propagation
revisions. These timings describe this particular, mostly locally failing
family, not general polygon-search performance.

The independent verifier exhausts all 8^6 ordered words, reproduces the full
330/120/210 catalogue split, checks every pair reference and status schedule,
and validates 273 retained patches and 230 periodic witnesses using exact
seams, holonomy, contacts, area and all potentially intersecting lattice
translates. Fresh read-only replay reproduces the result hash.

[Exact baseline](runs/boundary-m8-2026-10-24/boundary-screen.json),
[manifest](runs/boundary-m8-2026-10-24/manifest.json), and
[gallery](runs/boundary-m8-2026-10-24/gallery.html) are retained.

## Mixed-angle support catalogue

Pentagon P has cyclic angles `(105,105,105,105,120)` degrees. Heptagon Q runs
over every cyclic word modulo rotations/reflections from the three multisets
`(120^3,135^4)`, `(120^4,135^2,150)`, `(120^5,150^2)`. These give 4 + 9 + 3 = 16
heptagon angle words. The P angle palette also appears in the repository's
earlier regular-dodecagon source reconstruction; that route has a different
Q12 companion. This Q7 experiment carries no novelty claim.

Each polygon is defined by successive outward **unit** normals at 15-degree
increments and exact inequalities `n_i dot x <= h_i`, with every `h_i` in
`{1,2}`. Adjacent-line intersections are retained only when every declared
side is active, nonzero, and the polygon is strictly convex. Actual Euclidean
coordinates, normals, lengths and scales lie in Q(sqrt(2),sqrt(3)); a field
value is recorded as four rational coefficients in basis
`1,sqrt(2),sqrt(3),sqrt(6)`. Both coordinates are ordinary physical coordinates
in this field, unlike the older integer `(x,y*sqrt(3))` convention.

This generates 2,080 raw support assignments: 32 pentagonal and 2,048
heptagonal. Of these, 1,535 have inactive/zero sides and are rejected; 545
valid definitions group into **20 P + 398 Q** congruence classes. Geometric
identities use exact pairwise distances and preserve all defining data.
Rotational frames have 24 possible directions, with reflection parity also
included; asymmetric polygons can have up to 48 placements.

All angles exceed 90 degrees. Therefore two or more genuine corners cannot
fill a straight 180-degree side, and a single genuine corner cannot either:
sliding T contacts are excluded. Three corners meet at each tiling vertex.
This simplifies necessary contacts, but the 5/7-face topology is not the old
honeycomb model. No honeycomb HNF search or full growth engine was imported.

For each P/Q shape pair, every possible mixed-edge equality supplies a
relative Q/P scale `length(P edge) / length(Q edge)`. All positive ratios are
enumerated exactly. This covers this finite shape library's possible mixed
full-edge contacts without selecting approximate tuned parameters. P and Q
are never independently normalized. Common scale is removed jointly, and
source-to-representative mappings are retained in the compressed scale audit.

## Mixed-angle contact funnel

| Stage | Count |
|---|---:|
| Native P/Q shape pairs | 7,960 |
| Native pair / matched-edge scales | 158,264 |
| Common-scale duplicates | 8,038 |
| Inequivalent pair-and-scale cases | 150,226 |
| Rejected: some native corner lacks a legal star | 150,212 |
| Pass all-corner star coverage and exact star geometry | 14 |
| Rejected: rational corner-incidence infeasible | 7 |
| Pass corner incidence | 7 |
| Rejected: angular endpoint cycle around P impossible | 7 |
| Final survivors | **0** |

The only possible angle triples are `105+105+150`, `105+120+135`, and
`120+120+120`. P105 requires a Q corner; Q135 and Q150 require a P105
corner. Thus the angle lists themselves disallow a single-species escape. Each native corner has its own identity, both incident-edge
orders are allowed, and equal-length loops are retained. Exact edge lengths
must match along every ray of a three-tile star. All 357 retained star
realizations include explicit reflection, rotation, translation, scale and
polygon coordinates; pairwise interior disjointness and full radial-edge
endpoint matches are checked.

The rational incidence relaxation asks nonnegative star frequencies to
supply each native P and Q corner once. Equal normalized P/Q counts are
necessary for a trivalent 5/7 tiling; the normalized counts have F=2, E=6, V=4.
A feasible relaxation is not an actual patch or an extension mechanism.
The seven positive cases retain exact rational weights; the seven negative
cases retain exact Farkas dual certificates.

### The extra cheap obstruction

All 14 star-compatible cases belong to just two heptagon angle words:
`(120,120,120,120,150,120,150)` and
`(120,120,120,150,120,120,150)`. Both fail an angle-only cyclic-neighbor test
around P. All seven incidence-feasible cases use the first word.

The obstruction is short. With no 135-degree Q corner available, every
105-degree P corner must meet one P105 and one Q150. A Q neighbor along a
P side whose endpoints are both 105 would need adjacent Q150 corners. These
Q words have none. Thus all three consecutive P105-to-P105 sides must have
P neighbors. An interior P105 corner then has P neighbors on both sides,
contradicting its required P/Q star. Reflection does not change this argument.

The generator and independent checker also run a finite endpoint-cycle
calculation: each root edge chooses either reading of a native neighboring
edge's endpoint angles, and adjacent choices must complete 360 degrees at
the root corner. Per-first-choice reachable states and closing counts are
retained for both root species and all 16 Q words. This is a necessary local
check; it is not a general tiling decision procedure. Moving it before the
expensive metric checks is the clearest search-order improvement from this run.

The practical engine gate required at least ten inequivalent surviving pairs
across at least three Q cyclic words, each with native-corner support. The
threshold is an allocation heuristic. It already failed at seven cases / one
word before the endpoint-cycle test; that test removes every remaining case.
**No patch engine, saved-patch interface or larger support domain was built.**

The final contact preflight took 62.45 process-CPU seconds under its 540-second
cap; catalogue enumeration was separately timed at about 7.58 seconds.
The whole declared domain completed, with no unfinished scale cases. No
support offset greater than 2, extra Q angle word, or other polygon family was
searched by this preflight.

## Records and independent verification

The mixed run retains its complete [catalogue](runs/mixed-obtuse-2026-10-24/catalogue.json),
[preflight](runs/mixed-obtuse-2026-10-24/preflight.json),
[compressed scale audit](runs/mixed-obtuse-2026-10-24/scale-audit.jsonl.gz), and
[SVG gallery](runs/mixed-obtuse-2026-10-24/gallery.svg), including an empty final
result. Gzip headers have a fixed timestamp and filename so replay can match
byte hashes. Scientific-content hashes recursively exclude timing fields.

The independent mixed checker uses separate rational-coefficient field
arithmetic and certified sign intervals without importing Sage or the
generator. It independently reconstructs all 2,080 support definitions, the
418 shape identities, every one of the 158,264 raw scale rows and 8,038
common-scale mappings, all 150,226 unique cases and their complete reflected
star-incidence sets, all 357 geometric star realizations, all seven primal
and seven Farkas certificates, all 16 angular-cycle traces, and the complete
filter/gate binding. Its fresh temporary-directory scientific regeneration
matches the catalogue, preflight and deterministic gzip hashes. The original
evidence remains unchanged.

Validation completed: **74 discovery tests passed**; both independent full
audits passed; both fresh scientific replays matched. The M8 replay
independently verifies all retained positive geometry, and its fresh finite
search reproduces solver labels. The mixed replay reproduces the complete
finite preflight. These do not establish unrestricted tilability, novelty,
or aperiodicity. The historical replay registry and earlier scientific source
hashes are unchanged.

Standalone commands, from the repository root:

```bash
mise exec -- conda run --no-capture-output -n arisearch python -m pytest research/discovery -q
mise exec -- conda run --no-capture-output -n arisearch python -m research.discovery.calibration_verify --replay
mise exec -- conda run --no-capture-output -n arisearch python -m research.discovery.mixed_verify --replay
```

To repeat either experiment in a new destination:

```bash
mise exec -- conda run --no-capture-output -n arisearch python -m research.discovery.length8_experiment --output-dir /tmp/arisearch-m8
mise exec -- conda run --no-capture-output -n arisearch python -m research.discovery.mixed_angles --output /tmp/arisearch-mixed --cpu-cap 540
```

M8 result hash: `f319f48d58bc8849fbde2e52fe92eb9bd8eae36c32caae1529962757c0be8b6c`.
Mixed catalogue hash: `9000d3cabc7c7b1e3483780b8416903f2d5ce9263afcd85b4139aed56b799932`.
Mixed preflight hash: `12371eb9470c8eee718cefeca1d31b79adfa3d5658b786dc132d64fdc04afdbf`.

## Allocation outcome

Stop both declared domains. The larger length run confirms that the working
screen is cheap, with zero candidate yield in this finite calibration. The
mixed audit adds angle diversity, but isolated legal stars and feasible
corner frequencies were again weaker than a complete first neighborhood.
For a future mixed-angle proposal, apply the angle-cycle screen first and
require concrete first-surround compatibility before engine investment.
Neither empty census excludes arbitrary convex pairs or resolves the global
problem. The historical proof/review acceptance criteria remain unchanged.
