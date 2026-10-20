# Fixed single Hat: symmetry-diagonal half-kite gate

Date: 2026-10-19. Status: complete finite exclusion, independently implemented
checker retained; independent human/agent hostile review pending. This is not
an impossibility result for arbitrary convex pairs.

## Predeclared domain and cap

The eight ordered standard kites are exactly those retained in
`research/certificates/hat-eight-kite-convex-cluster-gate.json`, whose source
is `source-decoration-hat-patch.py::ref_kites()`. For each ordered kite
`[v0,v1,v2,v3]`, its 60-degree vertex is v0 and its 120-degree vertex is v2.
Split it into `[v0,v1,v2]` and `[v0,v2,v3]`. These are congruent triangles
interchanged by reflection in the kite symmetry diagonal. The 16 resulting
atoms exactly partition the fixed reference Hat. Atom 2i and atom 2i+1 belong
to old kite i. All coordinates are exact integers (X,Y), representing
`(X/2,sqrt(3)*Y/2)` in the Euclidean plane.

Exhaust all 65,535 nonempty atom subsets. Retain precisely unions that are
connected, convex, and have five or six genuine corners after removal of
collinear boundary subdivisions. “Strict convexity” here means every genuine
corner has angle strictly below pi; polygons themselves are not strictly
convex sets in the curved-boundary sense. Canonicalize congruence under all
Euclidean isometries, including reflections. Enumerate every exact cover of
the 16 atoms using exactly two global classes, both present, and require
at least one piece to contain exactly one half of an old kite. This latter
condition detects the newly enabled cut mechanism; any cover containing only
whole kites already has no two-class solution by the previous complete gate.
The cap was declared as 300 seconds before execution, with no finer grid.

## Exact algorithms and result

The producer uses integer convex hulls. All triangles have equal positive
area. A subset union equals its hull exactly when its summed atom area equals
the hull area: the atoms have disjoint interiors, and any missing portion of
the hull would have positive area because the union is closed. Consequently
convexity implies connectedness; no additional connectivity filter is needed.
Integer orientation determinants decide hull turns. Squared distances in
integer coordinates are `(delta X)^2+3*(delta Y)^2`, equal to four times
Euclidean squared distance. Full pairwise distance words under all cyclic
shifts and both directions give complete congruence invariants.

There are 96 convex unions: 38 triangles, 45 quadrilaterals, 13 pentagons,
and no hexagons. The 13 pentagons form five congruence classes. The exact-cover
recursion, always selecting the least uncovered atom, exhausts 10 nodes and
finds **zero exactly-two-class covers** with both species present. Its
pruning discards only branches already using more than two classes. All
eligible masks and polygons are preserved in the JSON certificate. Producer
runtime was approximately 1.35 seconds, within the cap.

The separate checker does not import the producer or use convex hulls. It
cancels opposite directed triangle edges, requires a single simple boundary
cycle, and checks nonnegative turns, counting only positive turns. It
independently exhausts all atom subsets, recomputes congruence by pairwise
distance comparisons, and enumerates all covers. It also binds the atoms
to the reviewed whole-kite certificate. Its agreement establishes the finite
claim; an external hostile review remains a separate requirement.

## Scope and stopping point

This excludes the requested changed-atom mechanism on this exact single-Hat
scaffold. There is no candidate pair, so the conditional periodic omission
and mixed-carrier tests are not reached. It does not exclude other cuts,
multiple-Hat clusters, deformations, arbitrary two convex polygons, or prove
unrestricted forcing. No finer-grid expansion is authorized by this record.
The existence-transfer implication would be automatic for any fixed exact
Hat dissection, by applying it isometrically to every Hat of a known plane
tiling; its premise (a dissection into exactly two allowed classes) fails here.

## Replay

Run from the repository root, preserving assertions:

```text
mise exec -- conda run --no-capture-output -n arisearch python3 research/searches/hat-halfkite-convex-partition-gate.py research/certificates/hat-halfkite-convex-partition-gate.json
mise exec -- conda run --no-capture-output -n arisearch python3 research/searches/check-hat-halfkite-convex-partition-gate.py research/certificates/hat-halfkite-convex-partition-gate.json
```

Python standard library only. No randomness or solver dependency. Completion
and measured producer runtime are recorded in the certificate. This record
makes no novelty claim.
