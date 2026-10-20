# Last B orbit: eight-star intrinsic determinism and analytic-branch escape

Date: 2026-10-19. Status: independently hostile-reviewed valid for its stated conditional periodic escapes; see [review](../reviews/hexagon-thirtytwo-star-support-determinism-hostile-sol-2026-10-19.md). No larger torus enumeration.

## Statements

Use A=(0,1,2,0,3,4), B=(0,1,2,0,3,1), with five pairwise distinct positive lengths. Corner i is at the END of side i. Signed star indices refer to the retained 32-star upper atlas in `hexagon-thirtytwo-star-candidate-gate-sol-2026-10-19.json`.

1. Every edge-to-edge everywhere-trivalent plane tiling whose signed stars lie in S={2,5,13,15,17,20,22,23} has two independent translation periods.
2. For every sufficiently small positive parameter t on the corrected **end-corner** analytic branch of `hexagon-thirtytwo-star-end-corner-analytic-metric-sol-2026-10-19.md`, if the pair admits any plane tiling with unrestricted contacts and reflected copies, it admits a tiling with two independent translation periods.

Statement2 gives a periodic escape conditional on existence; it does not construct an actual plane tiling. It is restricted to this analytic branch, not all metrics or all angle supports for these words.

More generally, statement1 and the defect-free limit apply to **any** strict closed metric on these words for which every angle-compatible signed star in the full 32-star upper atlas lies in S. The four displayed support equations plus exclusion of the other 24 stars provide one such locus; the corrected IFT branch shows this metric locus is nonempty, without proving it contains a plane-tileable metric.

## Exact structural mechanism

A signed port (c,h), c=6f+i, has ordered incident native sides (c,6f+(i+1) mod6) when h=+1, reversed when h=-1. In the atlas circular order, the outgoing side of a port p matches the incoming side of its successor q. Read all three adjacent pairs in the eight retained stars. Every one of the 24 signed native side states has exactly one possible neighbor side state. In species-native notation the involution is

    (A0,h) <-> (B3,h)
    (A1,h) <-> (A1,h)
    (A2,h) <-> (B2,h)
    (A3,h) <-> (B0,-h)
    (A4,h) <-> (B4,h)
    (A5,h) <-> (A5,h)
    (B1,h) <-> (B5,-h).

Here h ranges over both signs. These seven rows cover all24 signed native sides, with the two fixed-side rows each covering two states. The exact audit reconstructs this table from all24 adjacent-port incidences and checks involutivity.

For fixed reference polygons, neighbor species, side index, and relative handedness uniquely specify the complete isometry across a full side with interiors on opposite sides. The two endpoint bijections have opposite orientation parity; specifying handedness selects one. Thus a tile state consists of its species and handedness, giving four finite intrinsic states. For each state and native side the table specifies its unique neighbor state, native side and complete relative isometry. No absolute orientation is included in the state.

The full-side adjacency graph of an edge-to-edge locally finite plane tiling by these convex polygons is connected: choose interior points of two tiles and a path between them avoiding the locally finite vertex set and crossing edges transversely. Its finite compact image meets finitely many tiles, giving a full-side adjacency path.

All hypotheses of the adversarially reviewed [intrinsic geometric determinism theorem](hexagon-five-length-intrinsic-determinism.md) now hold. It gives two independent translational periods. This proves statement1. It uses complete geometric neighbor maps, rather than a finite symbolic-state count alone.

## Isolation of the corrected analytic branch

Let alpha(t) be the end-corner branch in the corrected metric lemma. Each signed atlas star r has analytic residual R_r(t)=sum(alpha_c(t))-2pi. Every residual vanishes at t=0. For r in S, it vanishes identically by the four defining support identities. Exact differentiation gives R'_r(0), in atlas order0..31:

    -1, -2sqrt(3)-1, 0, -2sqrt(3),
    -1, 0, -2sqrt(3)-1, -2sqrt(3),
    -2+2sqrt(3), -1+2sqrt(3), -2+2sqrt(3), -1+2sqrt(3),
    -2, 0, -2, 0,
    1, 0, 2, 1, 0, 2, 0, 0,
    -1, -1, -1, -1, 1, 1, 1, 1.

Precisely the eight indices S have zero derivative. Each of the remaining24 residuals is nonzero on a sufficiently small punctured parameter interval, since R_r(t)/t tends to its nonzero derivative. Intersect these finitely many intervals with the corrected metric lemma's positive convex distinct-length interval. For every resulting t>0, the only angle-compatible stars in the upper atlas lie in S.

Start from any unrestricted tiling by such a pair. The reviewed defect-free limit theorem in [hexagon limits](hexagon-limit-and-periodicity.md), with [valid rereview](../reviews/hexagon-defect-limit-rereview.md), supplies an edge-to-edge everywhere-trivalent tiling by the same pair; species omission is allowed. All its actual signed stars belong to the reviewed native upper atlas: exact length matching is necessary, and every actual remote edge endpoint supplies the continuations used by atlas pruning. This applies even if a species disappears. The angle residual exclusion forces every actual star into S. Statement1 then makes that limit tiling periodic. This proves statement2 without using monohedral classification or a finite-to-infinite extrapolation.

## Evidence, dependencies, and scope

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-thirtytwo-star-support-determinism-sol-2026-10-19.py

Certificate: `research/certificates/hexagon-thirtytwo-star-support-determinism-sol-2026-10-19.json`.

The complete finite audit domain is24 signed side states,24 port adjacencies in eight stars, and32 residual derivatives. Exact rational/quadratic SymPy arithmetic; no search solver, timeout, randomness, or symmetry quotient. The script asserts the unique involution and the exact zero-derivative index set. The proof additionally uses the corrected analytic metric lemma, the upper-atlas necessity proof, intrinsic determinism, and defect-free limits. Its imported global theorems have the reviewed status recorded in their linked artifacts; this application and corrected metric still need independent hostile review.

Protocol section5: this closes the periodic-escape question for the corrected one-parameter branch conditional on the listed dependencies. General metrics of the last B orbit remain unresolved. Extending the result requires deriving deterministic support or another periodic construction for the other angle supports. The present argument provides no unrestricted finite-model theorem and no permission to infer global extension from a formal corona.
