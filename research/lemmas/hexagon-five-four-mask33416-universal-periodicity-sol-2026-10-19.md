# Mask33416 has a universal four-face periodic carrier

Date: 2026-10-19. Status: proved with exact carrier check and [independent Sol hostile review](../reviews/hexagon-five-four-mask33416-universal-periodicity-hostile-sol-2026-10-19.md) PASS. Author mechanism: Sol, explicit combinatorial construction, no bounded search.

## Theorem

Let A,B be closed strictly convex Euclidean hexagons with native cyclic side words A=(0,1,2,0,3,4), B=(0,1,1,0,2,3). Sides carrying the same number have equal length. Native corner i is the end of side i and start of side i+1 modulo6. Let alpha0,...,alpha5 be A angles and alpha6,...,alpha11 be B angles. Assume

    alpha0+alpha6+alpha7 = 2pi,
    alpha1+alpha8+alpha9 = 2pi,
    alpha2+alpha3+alpha10 = 2pi,
    alpha4+alpha5+alpha11 = 2pi.

Then A,B admit a plane tiling invariant under two independent translations. No genericity, extra angle equality, or metric specialization is required. Thus every realizable metric of support33416 has a periodic escape and cannot be an aperiodic pair in the original unrestricted problem.

## Literal carrier and verification

Use faces0,1 as positively oriented A copies and faces2,3 as negatively oriented B copies. The following native-side pairs use every side once:

    (0,0)-(2,0), (1,0)-(3,0),
    (0,1)-(3,2), (1,1)-(2,2),
    (0,2)-(2,4), (1,2)-(3,4),
    (0,4)-(3,5), (1,4)-(2,5),
    (0,3)-(1,3), (0,5)-(1,5),
    (2,1)-(3,1), (2,3)-(3,3).

Glue by the unique boundary-direction-reversing segment isometry, orienting face boundaries positively on the abstract surface. For opposite native handedness this identifies native start with native start and native end with native end. For equal native handedness it exchanges native start and native end. Every pair has matching side color, so all gluings are metric isometries.

The eight circular vertex links, listed as (face,native corner), are

    [(0,0),(2,0),(3,1)],
    [(0,1),(3,2),(2,3)],
    [(0,2),(2,4),(1,3)],
    [(0,3),(3,4),(1,2)],
    [(0,4),(3,5),(1,5)],
    [(0,5),(2,5),(1,4)],
    [(1,0),(3,0),(2,1)],
    [(1,1),(2,2),(3,3)].

These lists partition all24 corners. Each is a genuine link triangle: its successive edges are the two endpoint identifications from its incident sides. In particular all links are circles, so the quotient is a closed surface. The side pairings reverse the positively oriented face boundaries, hence extend a consistent surface orientation. The dual graph is connected (the displayed A-B edges already connect all four faces). Thus the quotient is a connected closed orientable surface with F=4,E=12,V=8 and Euler characteristic0, hence a torus. Each of the four stated angle triples occurs exactly twice.

## Geometric development and periodicity

The quotient carries the length metric obtained by gluing the four actual Euclidean hexagons. Polygon interiors are Euclidean. Edge interiors have two Euclidean half disks. At every quotient vertex its link is a circle and its sector angles add to2pi by hypothesis, so its neighborhood is also an ordinary Euclidean disk. The quotient is therefore a compact flat oriented Riemannian surface without cone points.

Its universal cover with the lifted metric is complete, connected and simply connected and locally Euclidean. Development gives a global isometry with the Euclidean plane: equivalently, the complete simply connected surface of zero curvature is Euclidean. The lifted polygon cells therefore tile the entire plane with disjoint interiors; this step does not assume extension of a finite planar patch. The universal cover map and the quotient construction supply it directly.

Deck transformations are orientation preserving Euclidean isometries acting freely. A nontrivial orientation preserving Euclidean isometry with a rotational component has a fixed point, so every nontrivial deck transformation is a nonzero translation. The torus deck group is Z^2 and the quotient is compact; its translation vectors consequently span two dimensions (a collinear subgroup would have noncompact plane quotient). Thus the developed tiling has a rank-two lattice of periods. Reflected B copies are allowed by the original problem.

## Discovery mechanism

The four signed identities force, within a connected handedness component, A+ to B- across native pairs A0-B0,A1-B2,A2-B4,A4-B5, together with same-handed A3-A3,A5-A5,B1-B1,B3-B3. Use two copies of each species. Let s exchange the two copies. Choose cross copy bijections id,s,id,s in that order, and use s on every same-species pair. The four vertex triangle conditions close successively; the literal carrier above records the result. This is a construction, so it refutes any proposed obstruction for arbitrarily large carriers.

## Reproducibility and exact scope

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-five-four-mask33416-carrier-sol-2026-10-19.py

Certificate: research/certificates/hexagon-five-four-mask33416-carrier-sol-2026-10-19.json. The checker verifies one literal12-pair gluing over24 native sides, all colors, all links, all four triples, connectivity and Euler characteristic. It uses only integer arithmetic and Python standard library, with no solver, random seed, search timeout or symmetry reduction. Replay passed. The independent human proof above explains orientability and geometric development.

This excludes the complete feasible support33416 family as an aperiodicity source. It does not classify unrelated side words, establish impossibility for arbitrary convex pairs, or solve the original unrestricted problem. No unresolved mathematical obligation remains in this carrier construction.
