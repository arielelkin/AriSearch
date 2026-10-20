# Shape-first equiangular hexagon patches: two negative fixtures

Date: 2026-10-20. Status: exact local experiment and exact periodic counterexamples; no aperiodic pair. No novelty claim or independent hostile review. Root owns discovery-log integration.

## Prior-work exclusion gate

I inspected the current log and the 2026-10-19 three-length seed, private-dimer, alternating-binary, mixed noncentral power-cell, and five/four-word records before selecting words. Native words are compared up to the twelve cyclic/reflected forms, and the displayed pairs have side-length multisets distinct from those earlier fixed fixtures. The second construction below does not start from a periodic tiling or power diagram. A repository text search found neither of its displayed words as a previous fixed candidate. These checks do not claim exclusion from every prior parametric family.

## Fixture 1: triangular power cells, immediately periodic

At site `c_(i,j)=2i u_0+2j u_1` of the triangular lattice, with `u_k=(cos(kπ/3),sin(kπ/3))`, set `w_(i,j)=(i+floor(j/2)) mod 2`. The power cell minimizes `|x-c|²-w_c`. The weights have periods `(2,0)` and `(0,4)` in site coordinates. Nearest-site inequalities at a site of weight `s` have bounds `h_k=1+(s-w_neighbor,k)/4` in the six `u_k` directions. Its side length is

`(4+s+w_neighbor,k-w_neighbor,k-1-w_neighbor,k+1)/(2√3)`.

The eight sites in a `2×4` quotient give exactly the two dihedral side words

`C=(2,4,3,4,2,5)/(2√3)`, `D=(3,6,4,5,4,6)/(2√3)`.

Each has at least three distinct lengths, closes by `s0-s3=s2-s5=-(s1-s4)`, is strictly convex, and is noncentral. For any more distant lattice site at distance `d≥2√3`, its half-plane lies at distance at least `(d²-1)/(2d)≥11/(4√3)` from the candidate center. The six nearest half-planes put the candidate inside the radius `5/(2√3)` disk, so no distant site cuts it. Thus the power cells are the exact polygons and tile periodically. At the central site `(0,0)`, the six neighbors in native side order have species `D,C,D,D,D,C`; the exact side matches and all eight quotient classes are printed by the checker. The corner graph has exactly two numerical triangles, `(2,4,5)` and `(3,4,6)`, each giving a unique third length at every corner. This local forcing does not help: the source field already supplies rank-two periods.

Replay: `mise exec -- conda run --no-capture-output -n arisearch python research/searches/triangular-power-hexagon-pair-2026-10-20.py`.

## Fixture 2: direct native words and patch assembly

Take unscaled side words, successive directed headings `0,60,...,300` degrees,

`A=(1,3,2,3,1,4)`, `B=(2,5,3,4,3,5)`.

Their vertices are the six cumulative sums `v_0=0`, `v_(k+1)=v_k+s_k u_k`. Both sums return to zero. All sides are positive, each exterior turn is `60` degrees, so both are strictly convex 120-degree hexagons. Their opposite-side difference triples are both `(-2,-2,-2)` in the closure convention `s0-s3=s2-s5=-(s1-s4)`; hence neither is central. Their side multisets are distinct, so the polygons are noncongruent.

The combined numerical corner graph has precisely two triples capable of making a 360-degree trivalent vertex: `(1,3,4)` with two A corners and one B corner, and `(2,3,5)` with one A corner and two B corners. Every native corner belongs to one of these triples. Neither species alone has a legal corner triple, so there is no monohedral tiling. The private length-1 A edges force A neighbors, and the private length-5 B edges force B neighbors, giving competing local propagation.

I assembled the dual honeycomb directly: at a site `(i,j)`, a state is a species plus any cyclic/reflected native side sequence; its side `k` must equal side `k+3` at the neighboring site in direction `(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)`. For either fixed seed, exhaustive native states give **one** complete six-neighbor ring. Each unique ring extends to at least one 19-face radius-two assignment. This is finite patch evidence only.

The first-ring forcing is killed by an exact four-face periodic carrier. Set `t=i-j mod 4` and assign the following globally oriented words:

| `t` | Species | Six side lengths by global heading |
|---|---|---|
| 0 | A | `(1,3,2,3,1,4)` |
| 1 | A | `(3,1,4,1,3,2)` |
| 2 | B | `(5,3,4,3,5,2)` |
| 3 | B | `(3,5,2,5,3,4)` |

For each of 24 directed seams, the words have equal opposite side lengths; the checker verifies this directly. Complete flat development of this global honeycomb assignment yields a plane tiling (see the independently reviewed `research/lemmas/equiangular-hexagon-honeycomb-development-2026-10-19.md`). In coordinates `(x,y√3)`, the site periods `(1,1)` and `(4,0)` develop to vectors `(9/2,-9√3/2)` and `(0,-12√3)`. Their determinant has absolute value `54√3`, exactly the area of two A plus two B cells: `2(15√3/2)+2(39√3/2)`. Hence the pair has an explicit rank-two periodic mixed tiling and is falsified for aperiodicity. The 19-face sample is a portion of this carrier, explaining its clean growth.

Replay: `mise exec -- conda run --no-capture-output -n arisearch python research/searches/native-shape-hexagon-patch-2026-10-20.py`.

## Limit and next change

The first fixture repeats a prior power-cell mechanism with new metric words. The second is a genuinely direct native-word patch experiment, but its locally unique corona conceals a four-state periodic carrier. Neither fixture supports plane-only aperiodicity. A next direct pair needs a forcing feature that survives the smallest exact periodic carrier audit; merely enlarging these uniquely determined rings would repeat the same killed branch.
