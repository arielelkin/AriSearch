# A prescribed mirror-V dimer plus W torus search

**Status:** witness found; matching domain not exhausted. The result has
been expanded into an explicit real-parameter family in
[the continuum theorem](../lemmas/pentagrid-v-w-periodic-continuum.md), now with a VALID fresh whole-family review.

## Finite domain and constraints

The prescribed domain has one eight-sided mirror-V dimer face Q and two
congruent equiangular108-degree pentagon faces W. Q's side labels are
(b,E,E,b,b,E,E,b), and its vertex angles in pi/5 units are
(4,4,3,4,4,4,3,4). The two W faces have unknown positive native lengths
(w0,w1,w2,w3,w4); the second face is processed in each relative reflection
parity. Positive b is normalized to1; E>phi*b encodes the c>0 family
E=phi*(b+c). All full sides are paired, reversing endpoints. Same-face
pairs are allowed; no period coordinate bound is imposed.

Before constraints, there are2*17!!=68,918,850 matchings including the
relative W parity. W0 can be fixed unreflected using the Q reflection
symmetry and reflection of the full quotient; no reflection assignment
is silently excluded from this stated dimer ansatz.

The recursive search merges corner endpoints and rejects partial vertex
angle totals above10. It separately merges unknown equal-length classes,
rejecting any pairing forcing b=E. Completed candidates must have six
vertices each with native total10 and connected face adjacency. The
ordered links are subsequently checked by the explicit family producer.

Every surviving length partition gets exact W closure equations from
its two real vector components in Q(sqrt(5)). Sage's exact field-backed
polyhedron imposes b=1 and a positive margin delta for every length class
and E-phi*b;0<=delta<=1. A vertex with delta>0 supplies a positive exact
metric witness. Length-partition feasibility results are cached. This is
an existence search, and no necessary cone is declared sufficient without
the complete positive polygon quotient and its global verification.

The first witness was found in the unreflected second-W case after6258
recursive pair branches and151 complete angular matchings. There was
one distinct completed length partition requiring an exact metric check.
The second parity and all later matchings were not processed. This is
not an UNSAT result or a classification.

The retained matching has W lengths(b,H,b,E,E) with H=phi*E-b/phi.
The explicit family has positive H for all b>0,E>phi*b. Its four native
V/V/W/W motifs, independent periods, full seam map, ordered links,
area/covolume identity, and exact sqrt2 fixture are verified in the
separate family producer. The six-polygon dimer argument alone does not
establish plane extension.

## Replay and certificates

No randomized solver or seed is used. Arithmetic uses Sage exact
quadratic and cyclotomic fields plus the field polyhedron backend.

```text
conda run --no-capture-output -n arisearch python research/searches/pentagrid_v_w_dimer_torus.py
conda run --no-capture-output -n arisearch python research/searches/pentagrid-v-w-periodic-continuum.py
```

Search certificate: `research/certificates/pentagrid-v-w-dimer-torus.json`.
Global witness certificate:
`research/certificates/pentagrid-v-w-periodic-continuum.json`.

The fixture's exhaustive overlap domain is32 nontrivial ordered
motif/lattice comparisons, derived from exact lattice-coordinate boxes,
plus exact total area equality. The full real-parameter theorem uses
formal seams and a degree-one map, not sampled metric checks.
