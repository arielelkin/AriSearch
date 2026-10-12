# Fresh review of the prescribed Ammann H dissection gate

Date: 2026-10-11. Verdict: **PASS for the stated varying-angle family exclusion.** The main two-convex-tile problem remains unresolved.

The reviewed family keeps the reconstructed shapes `H(J), P1(J), P2(J)` fixed as functions of one complex point `J=s+t*w`. It attempts to replace each convex H with exactly two convex pieces congruent to prescribed P1/P2, allowing all rotations and reflections. It does not introduce new pentagon words or extra coordinates.

For two convex polygons with disjoint interiors covering convex H, a separating line forces them to be the two half-plane intersections with H. Their common interface is therefore one straight chord. For two strict pentagons the hexagon must have six actual corners, each piece must contain three old corners, and both cut endpoints must lie inside opposite edges. In particular the entire chord is one full side of both pieces. If H has at most five corners, or an endpoint is an old corner, the total number of piece corners is at most nine; at least one piece has at most four corners and supplies the problem's admitted monohedral periodic escape. Flat prescribed pentagons also supply that escape.

I reconstructed the coordinates independently in a polynomial ring over `Q(w)`, taking complex conjugates coefficient by coefficient. Direct products with conjugates give all side squared norms; the exact conjugate shoelace sum gives all areas. This independently confirms

```
H:  a b b r r a
P1: a b a c a
P2: c r r a b
```

The sum of piece perimeters minus the outer perimeter is twice the chord length. It gives `a+c` for P1+P2, `2a+c-r` for two P1 copies, and `r+c` for two P2 copies. Positivity rules out chord length a or c in the mixed case, so the necessary P1 side is b. In the two-P1 case all a/b/c possibilities are retained; in the two-P2 case positivity rules out r/c and leaves a/b. The additional mixed r case is a redundant looser superset and does not undermine completeness. Side coincidences are covered.

The independently derived scaled signed areas satisfy `AH=2` and `A1+A2=1+sqrt5`. Hence the mixed dissection is impossible throughout its real geometric domain regardless of polygon orientation:

```
|A1| + |A2| >= |A1+A2| = 1+sqrt5 > 2 = |AH|.
```

This unsigned inequality is stronger than the original signed-area unit-ideal control and avoids relying on an admissibility convention. Both original mixed ideals were independently recomputed as unit ideals.

For each same-shape dissection the physical area condition is `Ai=+1` or `Ai=-1`. I independently rebuilt and recomputed all ten side/area ideals, including the five added negative-orientation supersets. Every ideal is zero-dimensional and every saved Groebner basis matches. Each leading ideal contains a positive pure power of each of the six variables s,t,a,b,r,c, independently confirming a finite-dimensional quotient. Therefore only finitely many complex J values can satisfy even these necessary equations. Imposing realness, positive lengths, convexity or actual cut geometry only removes points; it cannot create an angle-varying family. Arbitrary rotations/reflections of the dissection pieces do not alter these area or perimeter necessities.

As an extra independent control, exact SMT queries show that strict positive H turns already imply A1>0 and A2>0. The final negative conclusion does not depend on those SMT queries because both orientation signs were explicitly included. The prescribed uncut shape family does have actual angle freedom: at the exact strictly convex samples `(s,t)=(1/2,4/5)` and `(1/2,3/4)`, I checked every other vertex lies strictly to the left of every oriented polygon edge, for all three shapes. P1's angle at vertex 1 has different exact squared cosines at the two samples. The failure comes from the dissection equations reducing that freedom to finitely many possible J values.

No varying-angle candidate reaches the periodic-escape or reconstruction stages. This is a legitimate early negative gate, rather than an aperiodicity claim from an unsuccessful periodic search. Isolated same-shape necessary specializations have not been classified as actual dissections or periodic/aperiodic tile pairs. The result excludes no family with other final boundary words, more pieces, neighbour-dependent attachments, or a cluster involving H and surrounding pentagons.

The computation shares Sage/Singular with the producer; it independently reconstructs geometry and equations, but is not a proof-assistant audit of the algebra engine. The independent replay takes about 0.35 seconds after startup. All twelve producer rows, exact pure-power controls, and the producer hash were checked.

Artifacts: [independent verifier](boundary-attachment-ammann-h-gate-review.py), [certificate](../certificates/boundary-attachment-ammann-h-gate-review.json), and the two replayable orientation SMT files beside it.

```
conda run --no-capture-output -n arisearch python research/reviews/boundary-attachment-ammann-h-gate-review.py
```

The P2 audit execution record was also checked while doing this review: `kite-dart-exclusion-audit.json` now contains `retained_bounded_faces_and_classes_independently_verified: 1194`, and its manifest records the same count with current independent-script hashes. The reported earlier missing-field observation preceded the completed strengthened rerun.
