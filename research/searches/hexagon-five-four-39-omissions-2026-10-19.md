# Exact classification of the39 retained angle-grid representatives

Domain: exactly the39 assignments in the previously declared {90,120,150} native end-side angle grid whose common closure cone admits positive pairwise-distinct five-color lengths. No grid enlargement. Budget predeclared120 seconds; exact replay takes seconds.

The certificate hexagon-five-four-angle-grid-2026-10-19.json now lists every angle tuple and an exact representative length vector. The separate certificate hexagon-five-four-39-omissions-2026-10-19.json additionally preserves exact vertices and explicit periodic carrier periods for every claimed omission kill. Field encoding [a,b] means a+b*sqrt3, with positive square root.

## Exact immediate omission criterion and proof

For each word the only equal opposite side pair is sides0,3. The reviewed H1 constructor applies exactly when their directed vectors are negatives, equivalently the end-side interior angles0,1,2 sum360. Rotate native starting vertex to4 so the pair becomes edges2,5. In the resulting coordinates q0=0 and q3=q2+q5. The two representatives Q and -Q+q1, repeated on periods a=q2 and b=q3+q4-q1, tile the plane. Boundary cancellation and determinant(a,b)=2area(Q)>0 prove coverage and absence of overlaps, as proved and independently reviewed in research/lemmas/affine-two-convex-straight-edge-resection-periodic-escape.md. The new verifier checks the exact vector identity and determinant and retains a,b,q1 for every claimed carrier.

The reviewed H2 side pattern requires an equal opposite pair (2,5) and an equal distance-two pair (1,3). A has just one repeated pair; B has opposite pair0,3 and adjacent pair1,2. Neither admits the H2 length pattern under rotation or reflection. H3 requires three equal adjacent pairs; both words fail that length pattern. These conclusions hold throughout each distinct-color cone, not merely at its representative metric. H1 depends only on the angles, so its classifications likewise hold throughout each cone.

Counts:8 cases have only A H1,8 only B H1,5 both H1,18 neither H1. Thus21 of39 cone families admit an immediate periodic monohedral omission. The other18 escape these tests; no aperiodicity or tilability claim follows.

## First both-species escape retained for targeted attack

r=sqrt3. End-side interior angles A=(90,150,90,120,150,120), B=(150,120,120,90,150,90). Exact lengths (1,4-2r,-4+3r,2-r,-6+4r). All vertices are retained in the first certificate row with empty H1_carriers in hexagon-five-four-39-omissions-2026-10-19.json; the independent verifier reconstructs and checks both strict convex polygons exactly.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_hexagon_five_four_39_omissions.py

The verifier independently reconstructs all39 polygon pairs, verifies distinct positive lengths, both closures, strict halfplanes, four support stars, all cyclic/reflected H2 length patterns and both H3 adjacent-pair partitions, then verifies every H1 carrier. No producer imports, periodic search, solver timeout or floating-point decisions occur. Software Python3.12.13/SageMath10.9. Status: exact finite geometric audit passed; H1 periodic implication uses the named reviewed explicit constructor. No fresh hostile review of this new39-case implementation yet.
