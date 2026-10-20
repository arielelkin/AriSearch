# Hostile audit of three equiangular-hexagon trials

Status: **the three fixed-pair verdicts survive independent checks**. Trial 1 and trial 3 cannot tile the plane; trial 2 has an explicit rank-two periodic tiling. The source report has two editorial errors noted below. This audit does not support any claim about other metrics or a larger search family.

Independent replay: `mise exec -- conda run --no-capture-output -n arisearch python research/reviews/shape-first-fresh-hostile-2026-10-20.py`. The checker rebuilds all six polygons from their side words, checks every turning cross product, counts native corner types, and develops a 17-by-17 window of the trial-2 honeycomb through all six neighbors of every interior face. It does not call the producer script or reuse its selected rhombus loops.

## Geometry and the first correction

All six words close and are strictly convex: each side is positive and each successive directed edge turns 60 degrees. Their opposite-side differences are `-2` for **trial 1 A** and `-1` for the other five words. Thus the producer's sentence “All displayed words close with opposite difference `-1`” is false, although the closure conclusion is true. The heading “The two trials” should read “The three trials.” Neither error affects a verdict.

## Trial 1

The unique length-1 side of A forces an AA full-side seam. Its two endpoints each demand the sole `(4,4)` corner, which belongs to B. The A word has length-2 sides beyond both length-4 arms; the B `(4,4)` corner has length-2 and length-3 sides beyond its two arms. Hence either reflection choice gives a far endpoint with two length-2 edges and demands a `(2,2)` third corner. Neither species has one. This argument allows both orientations and uses full-side incidence only after the 120-degree angle rule forces edge-to-edge tilings.

B alone is impossible: its private length-5 side forces a BB seam. The two endpoint matchings yield either `(2,3)` at both endpoints or `(2,2)` and `(3,3)`. B lacks `(2,3)` and `(2,2)`. Therefore every plane tiling would need A, while no plane tiling can contain A.

## Trial 2

The finite-window development checked 289 labeled faces and 1,600 directed seam traversals. Every shared edge had the same length and opposite direction from its two copies, and every face origin reached by multiple paths agreed exactly in integer triangular coordinates. The symbolic HNF states repeat under `(2,0)` and `(1,2)`. Their developed displacements were respectively `(4,-12)` and `(13,-10)`, at every applicable face in the window; the determinant is `116`. Combined with the independently reviewed complete-flat-honeycomb development lemma, this proves an actual Euclidean plane tiling with two independent translation periods. The local six-tile patch is not needed for this verdict.

## Trial 3

The complete native-corner inventory confirms that a star containing `(1,4)` has only third side label `2`: the shared corner set admits `(1,2)` and `(2,4)`, and no other common third label. A contributes `(1,4),(1,2),(2,4)` counts `(2,2,0)`; B contributes `(1,0,1)`. In a radius-`R` disk, all stars away from a fixed-width boundary annulus demand both a `(1,2)` and a `(2,4)` corner. Thus `2N_A+N_B <= 2N_A+O(R)` and `2N_A+N_B <= N_B+O(R)`, giving `N_A+N_B=O(R)`. Bounded positive-area tiles covering the disk require `Omega(R^2)` tiles. The contradiction applies to unrestricted plane tilings because three 120-degree corners must meet at each vertex and T-junctions are impossible.
