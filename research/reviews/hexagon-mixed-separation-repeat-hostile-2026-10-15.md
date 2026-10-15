# Independent hostile review: common-five mixed repeat separations

Date: 2026-10-15. Verdict: **VALID**, for the exact restricted numerical and formal-source statements in [the lemma](../lemmas/hexagon-mixed-separation-repeat-periodicity-2026-10-15.md). The unrestricted original two-polygon problem is not resolved. The numerical claim uses the existing reviewed defect-free hexagon limit theorem; that dependency was not re-proved here.

## Independently reconstructed finite evidence

The [new independent verifier](hexagon-mixed-separation-repeat-independent-2026-10-15.py) imports neither the producer nor another author module. It reads the retained certificate only as evidence to check. All arithmetic is integer or exact Fraction.

It builds native side endpoint sets and corner ports, then constructs stars by choosing three ray colors and one native corner for each of their three distinct color-pair edges. This is independent of the producer's corner-triple filter. For each star it follows both specified native sides to their other native endpoints. Greatest-fixed-point pruning, all seam edges, contact components, and the twelve-corner cover test agree record-by-record on all 120 raw B words. The counts are 96 words without full cover, 16 with at least one disconnected repeated-slot pair, and eight hard words. Every hard word's retained two dihedral readings and color bijection was checked pointwise, independently of the author's equivalence finder.

The representative has exactly twelve stars. Independent exhaustive selection of all 2^12 subsets gives precisely the 30 retained full-corner-cover, endpoint-closed supports. The coverage uses the actual complete star set; no replacement by a minimal subset is made.

The verifier generates perfect matchings from permutations followed by canonical deduplication, independently of the author's recursive matching generator. It exhausts all eight sign choices and all 48,600 same-color face pairings. The side involution composed with the oriented face successor gives the vertex-link cycles directly, independently of the author's union-find test. It verifies connectedness, eight links each of length three, six surviving torus gluings, and exactly three angle-equation patterns. Every retained positive witness is separately checked for all side matches, its complete vertex links, and native-corner reading under reflections.

For the 28 covered supports, all 112 retained weighted augmented-row identities were checked directly with Fraction arithmetic, including their right-hand sides. The other two supports are exactly the displayed four-star partition S and S plus its two complementary pure-B stars. All twelve deterministic neighbor choices for S, including a far-end consistency check, pass. The explicit two-B torus was independently reconstructed: its links are twice each of native triples 012 and 345, with V=4,E=6,F=2 and all matched side colors equal.

Replay exited zero:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/hexagon-mixed-separation-repeat-independent-2026-10-15.py

## Geometric and logical audit

Adjacent colors differ in every word. Therefore three trivalent ray colors are distinct, and repeated actual corner indices cannot occur within a star: that would repeat its unordered color-pair edge. This validates the finite native-triple domain even with accidental physical equalities. All far-end tests are necessary; the proof never claims their sufficiency for a plane tiling.

The actual seam graph is a subgraph of the fixed-atlas seam graph, so its component partition refines that larger graph's partition. Components also refine the five original color classes. Disconnecting the only duplicated native slots of one shape therefore makes all six of its slots separate auxiliary colors. The other shape retains at least five auxiliary colors. The exact lemma was amended during review to cite the reviewed six/five source theorem explicitly, which proves the claimed rank-two escape. A citation solely to the arbitrary-partner theorem would have justified a nonzero translation but not its stated rank-two strengthening; that issue is now repaired.

The hard-word equivalences preserve all native incidence and angle equations, not just numerical multiplicities. The positive four-face gluings are closed orientable connected surfaces with circular vertex links and Euler characteristic zero. The checked row identities eliminate every cone defect for the actual original metrics. Compact flat-torus development therefore gives embedded plane tiles with disjoint interiors and a rank-two deck lattice. Equal physical lengths belonging to differently named colors cause no defect in this construction.

For exact S, every native corner has a unique star. A host side's color selects a unique guest corner, guest side and endpoint correspondence. Choosing the extension with opposite polygon interior half-planes fixes the complete indexed relative isometry, including reflected placements and physically symmetric reference polygons. Transport between same-type indexed occurrences propagates along connected full-side adjacency. Its framed symmetry group has at most two tile orbits, is discrete and cocompact, and the reviewed planar group argument yields rank two. Arbitrarily choosing reference frames does not create an extra ambiguity: the actual frames in the chosen source are fixed by the endpoint and interior-side data.

For Splus a pure-B star gives one complementary B triple angle sum 2pi; the polygon angle total gives the other. The explicit checked two-face torus then applies. A B-only source has such a pure-B star because B's color graph consists of exactly those two triangles. An A-only source is impossible because A's graph has no triangle. These handle monohedral sources before applying the twelve-corner cover condition.

No defect remains in the retained exact statement and proof. This is a new restricted escape class; it does not cover adjacent repeats, both-opposite repeats, fewer colors, other length sets, or pentagon-containing pairs.
