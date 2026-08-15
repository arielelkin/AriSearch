# Periodic escape for three simple-cycle hexagon carriers

**Status:** Candidate under repair after hostile review.

## Claim being refuted

The following proposed compression mechanism cannot produce a strongly
aperiodic set of three convex hexagons:

1. choose a finite simple bipartite graph `G`;
2. assign a globally unique side length to every edge of `G`;
3. choose three simple six-cycles `C0,C1,C2` in `G`;
4. realize each cycle as a strictly convex hexagon whose consecutive side
   lengths encode its graph edges; and
5. arrange the angles so that any admitted tiling is an edge-to-edge
   trivalent honeycomb and the three graph edges at a physical vertex share
   one endpoint of `G`.

This is the native, uncollared version of the compatibility-graph carrier.

## Theorem

If the three hexagons above admit any tiling, then they admit a doubly
periodic tiling. This remains true when all Euclidean isometries, including
reflections, are permitted. Hence no nonempty carrier in this class is an
aperiodic protoset.

## Proof

At a physical tiling vertex let the three incident graph-edge labels be
`a,b,c`. The three incident face corners use the pairs
`{a,b}`, `{b,c}`, and `{c,a}`. A simple cycle cannot supply two of these
corners: doing so would make that cycle use all three distinct edges
`a,b,c` at their common graph vertex, whereas a simple cycle has degree two
at each of its vertices. Therefore the three corners belong to the three
different cycle types. In particular, all three tile types occur at every
physical vertex.

Take an occurrence of `C0`. Each of its six corners is a physical tiling
vertex, so each graph vertex of `C0` also lies on `C1` and `C2`. All three
cycles therefore have the same set of six graph vertices.

At any one of these vertices, the three incident active graph edges occur in
exactly two of the cycles apiece: one edge belongs to `C0` and `C1`, one to
`C1` and `C2`, and one to `C2` and `C0`. Denote these three edge classes by
`M01`, `M12`, and `M20`. Each class meets every one of the six vertices
exactly once, so each is a perfect matching. Their union is a simple cubic
bipartite graph on six vertices. Its bipartition has three vertices on each
side, and cubicity forces every possible cross-edge; hence the active graph
is `K_3,3`. Moreover,

```text
C0 = M01 union M20,
C1 = M01 union M12,
C2 = M12 union M20.
```

Label the two parts of `K_3,3` by `L_p,R_p`, with subscripts in `Z/3`, so
that

```text
M01 = {L_p R_p},
M12 = {L_p R_(p+1)},
M20 = {L_p R_(p+2)}.
```

Define the standard honeycomb explicitly by faces `F(m,n)`, `(m,n)` in
`Z^2`, and two vertex classes with incidences

```text
U(m,n) incident to F(m,n), F(m+1,n), F(m,n+1),
D(m,n) incident to F(m+1,n), F(m,n+1), F(m+1,n+1).
```

Color `F(m,n)` by `c(m,n)=m+2n mod 3`. Map honeycomb vertices by

```text
U(m,n) -> L_c,
D(m,n) -> R_(2c+1),
```

where `c=m+2n` and all subscripts are modulo three. At `U(m,n)` the three
incident face colors are `c,c+1,c+2`. At `D(m,n)` they are likewise
`c+1,c+2,c`. The three incident edges pair these colors and map respectively
to `M01,M12,M20` after the same cyclic relabeling. Consequently every face of
color `i` traces `Ci`. Both `(3,0)` and `(1,1)` preserve `c`, so the labeling
has two linearly independent periods.

Finally glue the actual polygon shapes according to this periodic labeled
honeycomb, reversing boundary orientation across every paired edge. The
quotient by the two displayed periods is an orientable topological torus.
Around each quotient vertex the same three tile corners occur as in the
assumed tiling, so their angles sum to `2*pi`; along every edge the encoded
side lengths agree. The quotient therefore has a flat polygonal metric with
no cone singularities. It is compact and hence complete. Its universal cover
is a complete simply connected flat surface, so its developing map is a
global isometry onto the Euclidean plane. The orientable torus deck group
acts by two linearly independent translations. The developed faces are thus
a genuine doubly periodic tiling by the original three hexagons, proving the
periodic escape.

## Direct verification and exact example

The smallest abstract witness is the three Hamiltonian six-cycles obtained
from the standard one-factorization of `K_3,3` above. The proof constructs a
periodic honeycomb cover for every geometric realization that has one valid
tiling; it does not depend on numerical coordinates or a bounded search.

## Dependencies

- The carrier hypotheses stated above, including the common-endpoint decoding
  property.
- Elementary facts about simple cycles, perfect matchings, and `K_3,3`.
- The developing-map argument for a compact flat polygonal torus.

## Precise scope of the failure

This theorem excludes exactly three selected simple six-cycles in a simple
bipartite compatibility graph. It does not exclude:

- carriers with repeated vertices or edges in a face word;
- multigraph compatibility data;
- additional state carried by angles or longer-range geometry;
- collared constructions with many prototiles; or
- arbitrary pairs or triples of convex polygons outside this carrier.

It is therefore a route-killing theorem, not a negative solution of the main
two-convex-tile problem.

## Adversarial-review status

The first hostile reviews found that the periodic-cover coordinates and
flat-torus step were too compressed to audit; see
`research/reviews/three-cycle-periodic-escape-review-2026-08-15.md` and
`research/reviews/extraction-scope-review-2026-08-15.md`. The proof above
contains the proposed repairs and awaits fresh independent review.

## Supporting computation

None. The result is an exact combinatorial and geometric argument.
