# A002112: complete native AAA corner availability and strip gate

Status: exact finite corner certificate and independent replay; conditional spatial implication awaits root's parallel-B-row lemma and no-AAA periodic-lift review. No infinite extension or periodicity is established merely by legal corners.

Domain declared before search: all42 actual non-H1 side partitions admitting some AAA cycle, including all coarsenings and the four four-class partitions, against all64 corner/arm-order choices. A legal star satisfies the three native arm equalities exactly. The question is whether a whole A tile can have all6 AAA corners, or whether any three consecutive corners are individually AAA-eligible. Absence of three consecutive eligible corners can obstruct any two-row A strip in the saturated parallel-B-row geometry; presence supplies a precise remaining obligation, not evidence of a tiling.

The exact finite return is22 partitions with no consecutive3 run,12 with all6 corners eligible, and8 with a proper corner subset containing a3-run. Among the ten geometry-positive three-class A/B/BB families, six have no3-run:

| Partition | Eligible native A corners |
|---|---|
| 001102 | 1,2,4 |
| 001121 | 0,2,3 |
| 010122 | 0,2,4 |
| 010220 | 0,3,5 |
| 011202 | 1,3,5 |
| 012110 | 1,4,5 |

All four four-class cases likewise have no3-run:

| Partition | Eligible native A corners |
|---|---|
| 001232 | 0,2,3 |
| 010223 | 0,3,5 |
| 012130 | 1,4,5 |
| 012203 | 1,2,4 |

Conditional spatial implication: in a whole-side saturated field whose B cells form parallel complete lattice rows, an A strip of at least two rows has a boundary A row with three consecutive inward AAA vertices. Its A corner word can be rotated or reflected, but the existence of a consecutive3 run is dihedrally invariant. Any no3-run partition therefore permits only width-one A strips; every vertex of that alternating row field contains B, so AAA is absent. A separately reviewed no-AAA periodic-lift theorem then yields a periodic escape for an actual tiling pair. This implication neither requires positive closure of the four-class kernels nor discards their necessary equality ancestors: all actual specializations were checked independently among42 partitions. Root must confirm the imported row-geometric statement and whole-field conclusion before this conditional result is promoted.

Exactly four geometry-positive three-class partitions remain after the conditional strip gate:

    001202, 010112, 010120, 012202.

All6 native corners are AAA-eligible in each. The color-preserving reflection of A002112 is corner i→1-i and edge j→-j; it exchanges001202 with010120 and010112 with012202. Thus only two metric orbits remain, with all their further specializations already classified. This is a shape-class identification between reflected polygons, not an intrinsic reflection symmetry of every A in the orbit.

Next concrete obligation: derive a stronger native full-A neighbourhood obstruction or a periodic mechanism for the parallel B-row strips in these two metric orbits. There is no automatic reason to enlarge a torus search. The fact that nonmonohedral A has no pure-A tiling gives a compactness bound on A-only strip width, but bounded width by itself does not prove periodicity of an entire field.

Producer, certificate, and independent checker:

    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python research/searches/terra-five-one-002112-aaa-corner-strip-gate.py
    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_terra_five_one_002112_corner_strip_gate.py

Certificate: research/certificates/terra-five-one-002112-aaa-corner-strip-gate.json. The checker independently builds all64 arm pairings directly against each partition, rather than trusting the producer's previously retained equality relations. The closure ledger and independent checker are research/lemmas/terra-five-one-002112-complete-aaa-closure-ledger.md and research/reviews/verify_terra_five_one_002112_chebyshev_gate.py.

## Subsequent stronger result

The fresh independent native interface review `research/reviews/terra-five-one-002112-universal-interface-fresh-review.md` verifies root's all-metric obstruction: a boundary A row cannot have another A row on its inward side. Combined with opposite saturated B seams, this forces alternating A/B rows and removes every AAA-used branch, including the residual three- and four-class cases above. The earlier computational returns are retained as necessary-condition evidence and exact counterexamples; they are no longer the active extension blocker for A002112. The separately reviewed no-AAA binary lift then supplies periodic escape for the actual pair.
