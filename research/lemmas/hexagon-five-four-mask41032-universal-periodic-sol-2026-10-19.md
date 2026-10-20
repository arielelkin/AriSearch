# Mask41032: universal four-face periodic escape

Date:2026-10-19. Status: proved; [independent Sol hostile review](../reviews/hexagon-five-four-mask41032-universal-periodic-hostile-sol-2026-10-19.md) PASS.

## Theorem and conventions

Let A,B be closed simple strictly convex Euclidean hexagons with positive common lengths by native words A=(0,1,2,0,3,4), B=(0,1,1,0,2,3). Distinctness is optional. Let a_i,b_i denote the interior corner at the END of native side i. Suppose

    a0+b0+b1=2pi,
    a1+a2+b2=2pi,
    a3+b3+b4=2pi,
    a4+a5+b5=2pi.

These are precisely the angle equations of signed-star mask41032, indices3,6,13,15 in the reviewed atlas. Then A,B admit a doubly periodic edge-to-edge plane tiling with two copies of each per lattice cell. Reflections are permitted and used. This eliminates every geometrically feasible metric on this support from aperiodic-pair consideration.

## Complete abstract carrier

Take four oriented polygon discs: faces0,1 are A in native vertex order; faces2,3 are reflected B, stored vertex j corresponding to native vertex(5-j) mod6. Each stored boundary is counterclockwise. Its stored side j has native side j on A, and(4-j) mod6 on reflected B. Its stored vertex j has native corner j-1 on A and b_(4-j) on reflected B.

Pair the following stored sides, always identifying their boundary parameters in reverse order:

    (0,0)-(3,4)  (0,1)-(2,2)  (0,2)-(1,2)
    (0,3)-(3,1)  (0,4)-(2,5)  (0,5)-(1,5)
    (1,0)-(2,4)  (1,1)-(3,2)  (1,3)-(2,1)
    (1,4)-(3,5)  (2,0)-(3,0)  (2,3)-(3,3).

This pairing was first extracted from `hexagon-five-four-family-transfer-2026-10-19.json`; the new replay script contains the literal list and independently audits its incidences without stored lattice offsets. Each matched pair has the same native color, hence the same exact positive length. Every stored side appears once.

The vertex links, as cycles of stored face:vertex incidences, are

    (0:0,1:5,3:5), (0:1,2:3,3:4),
    (0:2,1:3,2:2), (0:3,1:2,3:2),
    (0:4,2:0,3:1), (0:5,1:0,2:5),
    (1:1,2:4,3:3), (1:4,2:1,3:0).

The endpoint identification graph consists of these eight connected degree-two triangle links. Hence each vertex has a disc neighborhood. All boundary identifications reverse direction, yielding a closed orientable surface. The face adjacency graph is connected; with V=8,E=12,F=4 its Euler characteristic is0. The surface is therefore a torus. The native angle triples of these eight links are respectively

    (a4,a5,b5), (a0,b0,b1), (a1,a2,b2), (a1,a2,b2),
    (a3,b3,b4), (a4,a5,b5), (a0,b0,b1), (a3,b3,b4).

Every link angle is exactly2pi by the theorem hypotheses.

## Euclidean development, closure, and plane coverage

The polygons in the hypotheses already satisfy their exact vector closure equations. No closure is inferred from angle sums. Equal side lengths permit a unique endpoint reversing side isometry for each listed pair. The quotient of these polygon discs carries Euclidean charts across face interiors and edge interiors. At each vertex its circular sector link has total angle2pi, so it also has an ordinary Euclidean disc chart. Thus the quotient is an everywhere nonsingular orientable Euclidean torus.

The compact quotient is complete in its length metric. Its universal cover with lifted metric is complete, simply connected and flat. Developing Euclidean charts gives a local isometry into the Euclidean plane; completeness allows every straight path to lift globally. It is consequently a covering of the plane, and since the plane is simply connected this development is a global isometry. This supplies the global step absent from mere local angle checks.

The lifted closed polygon discs tile the universal cover, with disjoint interiors and full coverage, by the cell structure of the quotient. Their images under that global isometry therefore tile the plane. Every deck transformation is an orientation preserving Euclidean isometry acting freely. A nontranslation orientation preserving isometry of the plane is a rotation and has a fixed point; thus all nontrivial deck transformations are translations. Their group is Z^2, discrete and cocompact, so its translation vectors span a rank-two lattice. Its covolume is2 area(A)+2 area(B)>0. The four original faces are its cell representatives. This proves closure, coverage, absence of overlap and two independent periods; no old coordinate period formula is assumed to persist.

## Replay and scope

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-five-four-open-metric-gate-sol-2026-10-19.py

Certificate: `research/certificates/hexagon-five-four-open-metric-gate-sol-2026-10-19.json`. Replay passed. It verifies native color matches, complete side coverage, all eight degree-two vertex links, native corner rows, face connectedness and Euler characteristic using exact finite combinatorics. It separately verifies an exact strictly convex common-length fixture and determinant; see the companion open-metric artifact.

There is no solver search or larger collar/torus enumeration. This is a conditional universal geometric theorem for mask41032 and all larger supports containing it. It makes no assertion that every formal angle point has a closed polygon realization. It makes no unrestricted classification of33416, and does not resolve the overall two-convex-tile problem.
