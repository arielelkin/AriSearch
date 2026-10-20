# Independent hostile review: four-face imbalance periodic carrier

Date: 2026-10-19. Verdict: **valid periodic escape for the exact pair**
A=(2,1,2,1,2,1), B=(2,2,3,1,3,2).
Reviewer independently reconstructed the witness from native words, without
importing producer code, invoking its solver, or trusting its stored lengths.
No log/Git edits. This review replaces the assigned extension design cycle
after the root reported that a periodic carrier had killed the fixture.

## Reviewed claim and complete infinite object

The certificate is `../searches/hexagon-imbalance-periodic-small-sol-2026-10-19.json`;
the search script has the same stem with suffix `.py`. Abstract face coordinates
are Z² with neighbor increments

    d0=(1,0), d1=(0,1), d2=(-1,1), d3=-d0, d4=-d1, d5=-d2.

Reduce (x,y) by q,r=divmod(y,2) to ((x-q) mod 2,r).
The resulting four representative faces carry:

|face|species|r|epsilon|lengths in headings 0,...,5|
|---|---|---|---|---|
|(0,0)|B|3|+1|(1,3,2,2,2,3)|
|(1,0)|A|0|-1|(2,1,2,1,2,1)|
|(0,1)|B|0|-1|(2,2,3,1,3,2)|
|(1,1)|A|1|-1|(1,2,1,2,1,2)|

The formula specifies an entire infinite assignment, invariant under
(2,0) and (1,2), rather than a patch with an unproved extension.

## Independent exact checks and reflection attack

Created `verify_hexagon_imbalance_periodic_small_sol.py` in this directory.
It validates the certificate state domains, reconstructs each row as
word[(r+epsilon*k) mod 6], and checks closure with the exact vectors
u_k=(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1) in the triangular basis.
All 24 directed seams satisfy L_f(k)=L_g(k+3). Opposite directions
are checked explicitly, not only inferred from producer conventions.

Both epsilon values are genuine native dihedral placements of each
equiangular shape; reflection reverses cyclic native indices. The witness
uses reflected B as well as an unreflected B. The reflected A rows coincide
with some unreflected rows through A symmetries, which is harmless. The
original problem allows every reflection, so exhibiting these allowed states
suffices; no assertion that all tilings use these states is required.

The embedding of face-neighbor coordinates uses a cyclic sequence of six
directions. It need not identify the face-neighbor vectors with the polygon
edge vectors in a regular drawing: their cyclic correspondence is what
identifies the ordinary honeycomb. Confusing these vectors would be a
potential convention error; the endpoint development below uses polygon
edge vectors only for metric coordinates.

## Endpoint cocycle and physical periods

For each row form q_f,0=0 and q_f,k=sum_(i<k) L_f(i)u_i.
The across-side translation is

    D(f,k)=q_f,k-q_g,(k+4 mod 6).

Indeed side k of f starts at q_f,k and ends at q_f,k+1, while
the oppositely directed side k+3 of g ends at q_g,k+4. Matching
lengths gives both endpoint equations. Independently summing D around
all four translates of both elementary triangles (direction sequences
(0,2,4) and (1,3,5)) gives zero exactly. These triangles generate
finite dual cycles, proving path independence on the plane.

Along paths (0,0) in direction-index notation and (0,1,1), respectively,
the checker obtains the abstract endpoints and physical displacements

    (2,0) -> P=(4,-8),
    (1,2) -> R=(9,-8).

Their determinant in the triangular basis is 40, so they are independent
nonzero physical translations. With u0=(1,0) and u1=(1/2,sqrt(3)/2),
these become (0,-4sqrt(3)) and (5,-4sqrt(3)), respectively.
State periodicity makes D periodic, so these displacements are the same
when the paths start at any face. Thus they translate the full developed
assignment, not merely the chosen base tile.

## Coverage, overlaps, and scope

Zero holonomy alone does not prove global coverage. Here the complete legal
assignment satisfies the hypotheses of the independently reviewed lemma
`../lemmas/equiangular-hexagon-honeycomb-development-2026-10-19.md`.
Both words close with positive edges, and their cyclic edge directions turn
by 60 degrees, giving strictly convex 120-degree hexagons. Full matching
edge gluings form the ordinary topological plane; each vertex has exactly
three 120-degree sectors. The resulting surface is flat. Finitely many
strictly convex shapes give a uniform bi-Lipschitz piecewise affine comparison
with the regular honeycomb, hence completeness. Complete simply connected
flat development is a global Euclidean isometry. Consequently all face
interiors are disjoint and the entire Euclidean plane is covered. This
argument addresses both potential overlap and finite-length escape; it
does not infer extension from the earlier corona.

The explicit period vectors also remove any concern that two abstract
periods could develop to collinear or zero vectors. No converse from
geometric periods to literal native-state periods is needed for this escape.
A single allowed periodic tiling disproves aperiodicity of this exact pair.
The proof makes no claim about other pairs or the original unrestricted
two-convex-polygon problem.

The producer reports UNSAT on preceding smaller HNF domains. This review
does not independently certify those negative solver answers or minimality;
none is needed for the positive carrier. Its verifier is solver-independent
and uses integer arithmetic only. No finite patch or enlarged periodic
domain was searched by the reviewer.

## Replay

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_hexagon_imbalance_periodic_small_sol.py

Output: PASS: all 24 directed seams, eight elementary triangles; physical
periods (4,-8), (9,-8), determinant 40.

No blocking defects found. Final verdict: **valid**, with the stated
reviewed development lemma as the explicit global geometric dependency.
