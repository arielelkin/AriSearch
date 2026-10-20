# Obtuse P5/Q8 six-template shape-first gate, 2026-10-20

**Result.** All six prescribed two-end templates from the [12:59 Astra assessment](astra-shape-first-assessment-2026-10-20-1259.md) admit a strictly convex exact metric and a nonoverlapping four-tile patch. None of the six representative metrics has a monohedral P tiling under the stored Rao Table 2 filter, a Q-only tiling, or an oriented trivalent 2P+Q torus. Four of the six exact representatives are in fact **plane-nontilable**: their forced P seams close a twelve-P ring whose twelve required inner Q tiles cannot coexist. The two other representatives have alternative P/P seams, so this ring proof does not cover them. No aperiodic pair or plane tiling is established here.

Replay: `mise exec -- conda run --no-capture-output -n arisearch sage research/searches/astra-obtuse-p5q8-six-template-gate-2026-10-20.sage` from the repository root. The script uses Sage `AA` for every metric and geometric comparison, Z3 for the bounded 2P+Q quotient, and SciPy only for exploratory positive margins. Its printed `TEMPLATE`, `TORUS_2P1Q`, `INNER_Q_RING`, and `P_SEAM_ENDPOINT_ATLAS` lines are the finite certificates.

## Checked finite domain

The native angle words are P=(100,110,100,120,110) and Q=(150,130,140,130,140,120,140,130). Both have the correct angle sums. The only trivalent angular stars are (100,110,150), (100,120,140), (100,130,130), (110,110,140), (110,120,130), and (120,120,120). All corners exceed 90 degrees, so a tiling cannot have side-interior T contacts; four corners cannot meet. Q's unique 150 corner can only join P100 and P110.

The assessment's seam indexing is correct: join P side 0 to P side 3 with P corner 0 opposite P corner 4, leaving 150 degrees; the far endpoint joins P corners 1 and 3, leaving 130 degrees. At the 150 endpoint the exposed sides are both P side 4, so Q sides 7 and 0 both have length 1 after normalizing P4=1. At the far endpoint Q corner 1, 3, or 7 can meet P sides 1 and 2 in either radial order. These are six templates. An earlier exploratory calculation used the angle at the wrong vertex when advancing side directions; the replay script corrects that error and is the only result used here.

For Q corner 1 or 7, one adjacent side coincides with Q0 or Q7. The exact closure system therefore additionally forces P1=1 or P2=1. The script solves for the P seam length algebraically before testing Q closure. The following table gives one exact metric per template by listing the rational free coordinates; all unlisted lengths are the unique `AA` solutions of the two vector-closure equations and the named side equalities. Each representative passes exact positivity, strict convexity, and pairwise separating-axis nonoverlap for a four-tile patch. Reflected and unreflected placements are enumerated.

| Q corner | Radial reversal | P0=P3 | Q free lengths | P/P seam atlas | Inner-ring result |
|---|---:|---:|---|---|---|
| 1 | no | unique root P1=1 (~0.5976724775) | Q2=Q3=Q6=1/5 | P0/P0, P0/P3, P3/P3 | no forced ring |
| 1 | yes | unique root P2=1 (~1.6328715747) | Q2=Q3=Q6=1/5 | P0/P3 only | 0 of 4096 Q choices |
| 3 | no | 1/2 | Q1=Q6=1/5 | P0/P3 only | 0 of 4096 Q choices |
| 3 | yes | 1/2 | Q1=Q6=1/5 | P0/P3 only | 0 of 4096 Q choices |
| 7 | no | unique root P2=1 (~1.6328715747) | Q1=1/5,Q2=1/2,Q3=2 | P0/P3 only | 0 of 4096 Q choices |
| 7 | yes | unique root P1=1 (~0.5976724775) | Q1=Q2=1/5,Q3=3/2 | P0/P0, P0/P3, P3/P3 | no forced ring |

Here P0/P3 includes the reciprocal naming P3/P0. The seam atlas tests both reflection parities, both endpoint orders, every P side of the seam length, every possible third-corner species and index, exact adjacent side lengths, and both endpoints. It is a necessary endpoint test, not a full continuation proof. In the four ring-forced representatives, P sides 0 and 3 are the only native sides of their common length across both species. Their only fully completable seam is the prescribed P0/P3 pairing. Iterating that edge isometry rotates the next P by 30 degrees. The twelfth copy returns exactly to the first, and the twelve P interiors are pairwise disjoint. Each of the twelve 150-degree ring vertices requires a distinct Q tile, since Q has exactly one 150 corner.

At each ring vertex the script constructs all reflected and unreflected Q placements with exact adjacent sides and discards placements overlapping the P ring. Exactly two distinct Q placements survive at each of twelve vertices. It checks all resulting Q/Q pairs with an exact convex separating-axis test and exhausts all 2^12 choices. No assignment is nonoverlapping for any of the four ring-forced metrics. This proves those **specific exact pairs** do not tile the plane. It does not prove that every metric in a continuous template family fails; changing a free Q length can change ring conflicts.

## Immediate omission and carrier attacks

The stored fifteen-type Rao Table 2 implementation finds no monohedral P hit for any representative, under the imported convex-pentagon classification. Q alone is locally impossible: in an edge-to-edge trivalent Q-only tiling every corner would have to belong to a three-Q star, but any 130-, 140-, or 150-degree Q corner plus two Q corners exceeds 360 degrees. The complete 2P+Q oriented trivalent edge-pairing search tries both orientations of each second P and Q, exact native side-length equality, angle-sum closure at every trivalent vertex, and all edge involutions. All 24 cases are UNSAT. This excludes that particular minimal periodic carrier only; it does not exclude larger periods.

The two branching representatives have no compulsory twelve-P ring: their P0/P0 and P3/P3 alternatives have complete endpoint stars. The four-tile patch and bounded torus UNSAT do not supply an infinite extension or a forced hierarchy. Further fixed-metric patch growth would need a new return rule. Deduplication against the [shape-first audit](shape-first-dedup-audit-2026-10-20.md) and the discovery log found no prior use of these exact angle words; this is a repository check, not a literature novelty claim. The older P5/Q8 work uses a regular pentagon and a different construction.
