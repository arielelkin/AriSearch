# Independent hostile Sol review: mask33416 universal periodicity

Date: 2026-10-19. Verdict: **PASS**. Reviewer: independent Sol agent (not Astra).

Reviewed the lemma `research/lemmas/hexagon-five-four-mask33416-universal-periodicity-sol-2026-10-19.md`, exact producer `research/searches/hexagon-five-four-mask33416-carrier-sol-2026-10-19.py`, and its JSON certificate. No author artifact was edited. Producer replay regenerated its certificate successfully.

## Independent incidence reconstruction

I reconstructed the quotient from oriented polygon boundaries rather than copying the producer endpoint formula. Give each face an abstract counterclockwise boundary parameter k. Its native start-vertex is k on A and -k modulo six on reflected B. Native side i runs from native vertex i to i+1; reflection reverses that ordered interval. Reverse the abstract boundary direction at every gluing, union the corresponding abstract boundary endpoints, and convert native start-vertices v back to the paper's corners v-1.

This independently yields the following eight unordered corner classes:

```
(0,0) (2,0) (3,1)
(0,1) (2,3) (3,2)
(0,2) (1,3) (2,4)
(0,3) (1,2) (3,4)
(0,4) (1,5) (3,5)
(0,5) (1,4) (2,5)
(1,0) (2,1) (3,0)
(1,1) (2,2) (3,3)
```

All 24 native sides occur once in the 12 pairs; all paired colors agree. Every corner has two endpoint adjacencies, and on each class the adjacency graph is precisely a triangle, not merely a three-element union-find class. Thus the links are genuine circles. Conversion to species angle indices gives (0,6,7), (1,8,9), (2,3,10), (4,5,11), each twice. The certificate agrees exactly, including the reflected B indices. These are the mask33416 rows stated independently in the existing open-metric-family lemma.

## Hostile geometric checks

Orientability is not established merely by the certificate's hardcoded boolean. It follows directly from using the reflected native boundary ordering on B and reversing the resulting abstract oriented boundary at every identification. This extends the chosen face orientations across all edges. The dual edges connect face 0 to 2 and 3 and face 1 to 2 and 3, so connectedness holds even before the same-species identifications. With V=8, E=12, F=4, the closed connected orientable surface has Euler characteristic zero and is a torus.

No extra side-length equation is hidden in the carrier. Each segment gluing requires only the equality attached to its side color. There is no need to realize four faces simultaneously as a finite planar patch. Arbitrary closed strictly convex realizations supply genuine Euclidean disks as faces, positive edge lengths, and positive sector angles. All edge interiors have disk neighborhoods, and the triangle links with total angle 2pi make the vertices ordinary Euclidean points. Consequently the compact quotient has an actual flat metric, without a cone or a singular link.

The universal-cover step is valid: the lifted metric is complete because the base is a compact flat surface. A complete simply connected flat surface develops globally isometrically to the Euclidean plane. This gives both exhaustive coverage and disjoint interiors of lifted polygons, excluding overlap or a merely local development. No numerical closure, genericity, parallel-side relation, or extra metric condition is used.

Each deck transformation preserves orientation and acts freely, so a nonidentity Euclidean rotation is impossible; all nonidentity deck maps are translations. Compactness forces their translation vectors to span the plane, and the torus deck group supplies the rank-two lattice. Reflected B tiles are expressly permitted in the problem as scoped by the lemma. Thus the argument proves existence of a periodic tiling for every actual metric satisfying the four rows, including nongeneric metrics and metrics having additional angle or length coincidences.

## Replay and checker limits

Executed successfully:

```
mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-five-four-mask33416-carrier-sol-2026-10-19.py
```

Also executed an independent Python reconstruction using reflected abstract-boundary coordinates as detailed above; it checked side coverage/colors, every link triangle, the exact row multiset, and agreement with the JSON corner classes. It printed `Independent reflected-boundary reconstruction PASS`.

The producer itself does not mechanize the flat universal-cover theorem or independently compute orientability; its boolean is a declaration. Those are proved by the accompanying mathematical argument and checked here. This is a limitation of what the executable alone certifies, not a gap in the combined proof.

No counterexample or unresolved obligation was found within the stated universal mask33416 theorem. The result does not classify other supports or solve the unrestricted two-convex-tile problem.
