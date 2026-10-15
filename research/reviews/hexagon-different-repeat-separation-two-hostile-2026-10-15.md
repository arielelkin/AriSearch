# Independent hostile review: different doubled colors at separation two

Date: 2026-10-15. **Verdict: VALID for genuine convex hexagons with six actual corners.** I read the full [different-repeat theorem](../lemmas/hexagon-different-repeat-separation-two-periodicity-2026-10-15.md), its complete producer/certificate and the imported reviewed formal six-color source theorem. I independently reconstructed the entire finite domain, every pruning round and all surviving native contact graphs without producer imports. The result is a restricted periodic-escape theorem, not a resolution of the original two-convex-polygon problem.

## Exact claims and domain

The source statement assumes two fixed indexed genuine convex hexagons whose native sides use the same five DISTINCT formal colors. Each doubles one color at cyclic separation two, and the doubled colors differ between the species. Matching colors have equal positive physical lengths; the length map may be noninjective. The source already exists, is full-side and everywhere trivalent, matches colors, and includes its indexed placement maps. Reflections are allowed.

The conclusion is existence of an underlying unmarked doubly periodic tiling. It does not assert that the original unmarked geometry forces those auxiliary colors or every source is periodic. The numerical corollary applies when the five common physical lengths themselves are distinct, via the uncolored defect-free limit. Different alphabets, other repeat positions and heavier repetitions remain outside the theorem.

I requested explicit wording that the hexagons have six actual corners to match the imported source theorem and avoid any convention allowing collinear native vertices. The mathematical audit uses this intended genuine-hexagon scope throughout.

## Complete 96/48 native-word normalization

Normalize A=(0,1,0,2,3,4). Its repeated color is 0. B repeats one of 1,2,3,4 and can be written (p,q,p,r,s,t), with (q,r,s,t) a permutation of the other four colors. Thus the raw domain has 4*24=96 words. Reversal of B preserves its short-arc middle q and reverses its long three-symbol arc. Since those three colors differ, each raw word has a distinct reflected partner, giving exactly 48 forms. No A stabilizer or species exchange is used, so no further symmetry case can have been lost.

The independent checker normalizes B by generating all twelve dihedral views and filtering those with its repeated color at positions 0 and2. This independently reproduces the producer's canonical domain and checks every retained raw and normalized word, with complete and unique records.

## Native stars and endpoint pruning

Adjacent formal colors differ in both species. At a trivalent matching source vertex the three ray colors consequently differ; otherwise one intervening native corner would have equal adjacent colors. Its actual corners give the three distinct edges of a color triangle. A repeated actual corner index would repeat its same two colors, impossible in such a triangle. This excludes the apparent repeated-corner/multiset case by a mathematical argument, not by an enumeration shortcut.

The checker constructs stars from the three ray colors and independent actual corner choices on their pairs, rather than filtering three-corner subsets as the producer does. It independently builds each native side's two endpoints and each corner's two incident native side ports. Every shared star ray chooses a unique side at each corner. Their other endpoints give the actual required far corners. If those native corner indices coincide, no allowed star can hold both tile copies; otherwise some actually occurring star must hold both because the same tiles share the complete side.

Every source star survives each simultaneous pruning round by induction on these actual far-end continuations. Forty of the 48 words end with an empty atlas and cannot admit the source. Eight end with nonempty fixed points, each covering all twelve corners. Each individual species color graph is a triangle-free four-cycle with a pendant edge, so no trivalent matching source uses just one species. Thus the source necessarily uses both, and all its native corners really must occur.

The verifier checks every initial atlas, every entire current pruning atlas, every removed star's failed native demand, and the complete output of every round. It verifies the final atlas is indeed fixed. There is no inference from a surviving local atlas to a global tiling and no omission of a reflected source placement.

## All-color seam graph is a safe upper bound

For each of the eight full fixed-point atlases, inspect ALL three corner pairs in EVERY star. The pair's common formal ray color selects two actual native side slots. Add their undirected edge, keeping self-loops. This examines every side color, not only the doubled colors. The independent checker reconstructs the full retained edge set and all twelve-slot connected components by graph traversal, using a different component algorithm from the producer.

An actual seam appears at an actual source vertex and therefore supplies one of these retained port pairs. Consequently the ACTUAL seam graph is a subgraph of this full fixed-point graph, even if some formally possible star or edge fails another global consistency condition. Such extraneous edges only make the bound weaker. They cannot create a false disconnected conclusion. The actual equivalence partition E is its component partition and hence refines the full graph's components. I asked the author to distinguish this partition from the literal seam graph; the corrected proof now does so.

All retained graph edges preserve the original source color; the verifier checks this on every edge and every component. Self-loops affect neither connectivity between different slots nor its implication. In each of the eight full fixed-point graphs, at least one species has its two repeated native slots in DIFFERENT components. The independent verifier reproduces the whole table and the repeated-pair join flags. Deleting edges cannot connect disconnected vertices, so the same split holds for every actual admitted source in that row. No assumption that the full atlas itself occurs or extends is made.

Physical equality of different original colors does not invalidate this conclusion. The source hypothesis explicitly matches colors at every seam; actual paths therefore remain within one ORIGINAL color even when different colors happen to prescribe the same physical length. In the numerical corollary, the five physical lengths are distinct and give this color matching automatically.

## E-component recoloring and periodic witness

Give every native side slot its component of the ACTUAL seam graph as a new formal color. This is a global finite relation on the twelve native slots, not a bounded-patch guess. It has a well-defined geometric length because each generating actual seam identifies equal lengths. The same source remains matching under the new colors by definition.

At least one species' only repeated original color has been split between its two slots. The other four native slots had distinct original colors and cannot join any of each other or the repeated pair through source paths. Hence that species now has SIX distinct formal colors. The other species has at least its original five, and at most six. Interchanging species if needed, these are exactly the hypotheses of the already independently reviewed six-color/five-or-six-color source theorem. The source retains its indexed placement data, so physical polygon symmetries create no hidden framing assumption. Its length map may be noninjective exactly as that theorem permits.

That imported result constructs an unmarked rank-two periodic escape through positive flat-torus witnesses or complete indexed-neighbor determinism. It uses no generic finite-model property or bounded negative period search. Applying it to this single recolored actual source proves the source statement here. Colors are auxiliary proof data and impose no rule on the final unmarked witness.

For the numerical-length statement, the reviewed defect-free-limit theorem first gives an uncolored full-side trivalent tiling of the same original genuine hexagons. Native physical lengths supply the five colors, and every seam matches them. A disappearing species would give a monochromatic triangle-free color graph and is impossible. Thus the source statement applies. The separately reviewed same-repeat theorem covers the complementary case when the doubled values agree; this combination validly closes the stated slice sharing the same five physical lengths with both repetitions at separation two.

## Supplementary 36-support check and replay

For completeness I independently enumerate every subset of each full fixed point, retaining exactly coverage of all twelve native corners and all far-end continuations. Exactly 36 such supports survive across the eight words. I reproduce every support mask, actual star list, all-color seam graph, components and repeated-pair flags. This stronger certificate check is supplementary: the full fixed-point graph disconnection already proves the needed split for every actual subset.

Run:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/hexagon-different-repeat-separation-two-independent-2026-10-15.py

Observed result: PASS 96 raw words, 48 dihedrally normalized forms, 40 empty fixed points, eight complete native graphs with a repeated-pair split, and 36 exact endpoint-closed corner covers. The checker uses only standard-library finite integer sets, tuples and graph traversal; it imports no producer, calls no solver, makes no floating-point geometric decision, and enumerates no periodic quotient.

I attacked native far-end errors, repeated-corner multiplicities, lost reflected modes, omission of unique-color cross-species contacts, omitted self-loops, transitive connections via another original color, accidental physical length coincidences, treating an overapproximate atlas as realized, an unproved finite periodicity principle, and illicit preservation of colors through an uncolored limit. The stated hypotheses and the graph-refinement proof survive. Apart from the noted graph-versus-partition clarification and explicit genuine-corner scope, no repair was needed. The theorem is VALID within that scope; the unrestricted main objective remains unresolved.
