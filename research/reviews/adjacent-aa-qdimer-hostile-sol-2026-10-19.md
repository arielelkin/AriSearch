# Independent hostile review: adjacent-AA q-dimer carrier

Date: 2026-10-19. Verdict: **VALID within the stated saturated, full-edge, orientable translation-quotient domain.** Both the AAABCABC existence family and the AAABBACC finite 4P+2Q obstruction survive review. Neither conclusion classifies arbitrary inventories or unrestricted tilings.

Reviewed the search note, Python affine-angle screen, Sage contact enumeration, and both JSON artifacts. Independently reconstructed the exact member at alpha=117 degrees without executing either search program. The accompanying `adjacent-aa-qdimer-hostile-sol-2026-10-19-check.sage` prints PASS under the required repository wrapper.

## Exact member and coverage

The independent checker constructs the regular unit pentagon from fifth roots in Q(zeta40), constructs Q using directions (0,36,72,135,180,216,279,324), and solves its two private lengths by the two-dimensional closure equations. It verifies both lengths positive, exact closure, and strict left-of-edge convexity for every nonincident vertex. Each stored placed polygon is exactly its reconstructed native polygon under the recorded rotation and a translation.

All 36 darts occur exactly once in the 18 pairs. For every pair, both reversed endpoint equations hold with precisely the stored integer combination of the two lattice vectors. This verifies opposite edge vectors and equal lengths, rather than just lengths or approximate endpoints. Recomputing successor-after-mate gives exactly the twelve stored three-dart cycles. Each is APP or PBC, so its angle sum is 360 degrees. Face adjacency is connected, and 12-18+6=0 gives genus one for the orientable glued surface.

Every face has positive signed area. The two stored lattice vectors are independent, every edge shift belongs to their integer span, and the absolute lattice determinant equals the total positive face area exactly. Area equality alone would not suffice: here the polygonal quotient is locally Euclidean at edges and vertices. The endpoint identities induce a local isometry to the lattice torus. Compactness makes it a finite covering; the verified area ratio is one, hence it has degree one. Thus no positive-area overlap or hole is hidden in the placement certificate.

## All-real-alpha continuation

The public-vector sum is s u(18), s=2cos54. With theta=252-alpha and phi=396-alpha, the proposed closure coefficients are exactly the solution of x u(theta)+y u(phi)=-s u(18), since phi-theta=144 and sin144 is positive. Their numerator angles are 198-alpha and alpha-54. For 108<alpha<126 these lie respectively in (72,90) and (54,72), so both private lengths stay strictly positive. The denominator is a fixed nonzero number. There is no singular length solve at any real parameter in the interval.

The cyclic exterior turns are positive, strictly below 180 degrees, and total 360 degrees. A closed polygon with positive edges in this cyclic direction order is strictly convex: its directed edge directions go once around the circle and each side supports the resulting convex boundary. This justifies extending the exact convexity check to the entire interval.

The six public directions remain constant. The fixed face rotations and all PP/PQ matches therefore persist; the QQ mates use equal corresponding private lengths and a half-turn. The same combinatorial vertex cycles remain APP or PBC, whose angle sums remain 360 because A=144 and B+C=252. Consequently every parameter gives a connected compact smooth Euclidean genus-one surface. Completeness develops its simply connected cover isometrically onto the Euclidean plane; its orientable deck transformations are translations and form a rank-two lattice. This proves coverage and absence of overlaps for the entire open interval. It does not assume that the particular stored lattice basis remains a basis away from alpha117, or infer nonsingularity merely from a homotopy of pictures. The persistent local Euclidean metric supplies the missing global control directly.

## Obstruction and census domain

The two private Q directions differ by 144 degrees. They cannot pair within one Q because a translation self-identification needs opposite directions. With exactly two Q faces each private dart must therefore meet the other Q. The two bijections and two relative chiralities exhaust the possibilities after fixing the first Q and allowing global reflection. Equal chirality leaves the corresponding pairing and a half-turn. Opposite chirality leaves the swapped pairing with relative angle 648-2alpha modulo360, strictly between36 and72 degrees.

Under the stipulated saturation each of the four P faces has one distinguished Q-AA edge, normalized to pentagon side1; its PP edges are0 and2. The two P faces anchored to either Q have orientations differing by36 degrees. Neither can self-pair a PP edge, and their two PP edges cannot both pair internally, so a cross-group PP match is compulsory. Its direction equation forces relative Q rotation to be a multiple of36 degrees. This excludes the opposite-chirality interval above. Reflections of the pentagon add no missing case because a regular pentagon has no independent chirality once rotation is allowed.

In the remaining half-turn case all P edges have directions in36Z. For AAABBACC, public Q side4 has direction432-2alpha and must meet P, forcing alpha in18Z. There is no such alpha strictly between108 and126. This is a valid necessary-direction contradiction independent of private-length coincidences or placement offsets.

The Python artifact contains eight QQ cases across both words, four QQ-compatible cases and 4*105=420 PP perfect matchings. Its four survivors split two per word, all equal chirality; the two AAABBACC survivors are only PP survivors and are rejected by the public-Q direction argument. They are not metric counterexamples to the obstruction. The finite root window used for affine equations is amply larger than needed for the bounded coefficients and alpha interval in this specific screen; it is not an arbitrary-alpha solver.

The Sage census for AAABCABC has four QQ cases, two QQ-compatible cases, and 2*(4!)^2=1152 PQ assignments. Fixing P labels by their unique AA mate removes only face relabeling. The AB/AC and BA/CA assignments enforce the endpoint colors required by APP/PBC stars. One assignment survives directions, its105 PP matchings leave two direction-compatible candidates, and exactly one has the required stars. The code includes reflected Q placements; the affine-angle argument independently excludes that chirality throughout the interval. This is exhaustive in the declared saturation domain, including repeated face neighbors and quotient edge identifications; it is not a census of all possible contacts without that saturation premise.

## Limits

AAABCABC supplies an actual one-parameter family of congruent-octagon/regular-pentagon periodic tilings. AAABBACC is excluded only from the specific orientable saturated translation quotient with four pentagons and two octagons. Larger quotients, different inventories, unsaturated contacts, and unrestricted nonperiodic tilings remain outside this review. No defect found requiring a correction to the stated claims.
