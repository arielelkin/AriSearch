# Independent hostile review: unequal five-length palettes, nonadjacent repeats

Date: 2026-10-15. **Verdict: VALID**, for the numerical theorem exactly as stated in [the lemma](../lemmas/hexagon-five-noncommon-nonadjacent-periodicity-2026-10-15.md). This is a restricted periodic-escape result. It neither supplies an aperiodic pair nor proves impossibility for unrestricted convex polygon pairs.

## Reviewed claim and dependency boundary

Both genuine convex hexagons have exactly five distinct numerical side lengths, their palettes differ, and each doubled length occupies nonadjacent native sides (separation two or three). Arbitrary plane tileability, with reflections and partial contacts, implies an admitted doubly periodic tiling. The proof first uses the separately reviewed defect-free full-side trivalent limit theorem. The source can omit a species; this is handled explicitly, rather than assuming both occur in every admitted source.

I read the entire new lemma and its two producers, inspected the retained certificates, and checked the precise statements and relevant arguments of the existing six/five formal-color, opposite-repeat, and private-repeat lemmas. The old private-repeat theorem is a dependency with prior independent review; its verifier was also rerun successfully. I did not reprove the general defect-free-limit theorem or the whole six/five classification in this review.

## Hostile checks of the mathematical reductions

**Pure stars and corner multiplicity.** Adjacent native side lengths differ in every normalized word. Consequently the three rays at a trivalent source vertex have three different numerical lengths. Its three corner pairs are exactly the three different edges of a triangle, so repeated occurrences of the same native corner at one vertex cannot have been omitted by using triples of distinct corner indices. The separation-two single-species corner graph is triangle-free. The opposite-repeat graph has exactly the two native triangles stated. Either actual pure triangle gives both angle sums equal to two pi, using the total four pi. I independently checked the proposed two-face side pairing: all twelve sides occur once, lengths match, and the vertex-permutation cycles are four triples, twice each native triangle. Orientability, connectedness, Euler characteristic zero and cone sums therefore give the claimed monohedral torus. In the remaining branch all actual stars are mixed and every native corner of both species occurs. Deleting pure stars, even unused metrically legal ones, is valid for that branch.

**Complete unequal-palette word domain.** Rotate a doubled slot to zero and choose a boundary reading. Separation two or three yields exactly the stated two word forms. Fixing A's five names, choosing B's shared subset, and assigning canonical fresh names to its private lengths retains every physical equality pattern. There are 120 assignments per palette and 31 unequal palettes, hence 3,720 words per separation pair and 14,880 total. No quotient, metric ordering, or probabilistic sampling is used in this gate.

**Necessary endpoint closure.** The independent checker constructs each native side's two endpoint occurrences directly. At every star ray it locates the two actual side slots and their opposite native endpoints. The actual star support survives iterative deletion inductively: every actual full side has a real far endpoint in the same actual support. All three rays are tested; repeated side slots remain distinct. Failure to cover all twelve native corners therefore contradicts the chosen mixed source. Survival is used only as a necessary condition, never as a geometric extension theorem.

**Actual seam components.** All possible fixed-atlas seam types form an upper graph. The actual seam graph is a subgraph, so its component partition refines the upper graph partition. Disconnection of a repeated pair in the upper graph implies disconnection in the actual graph. Recoloring actual components gives six formal colors on that species and at least five on the other, because a component never joins unequal original numerical lengths. This satisfies the stated six/five source theorem, including when different auxiliary colors share a physical length. The construction does not impose colors on admitted target tilings. The argument does not confuse subgraphs with component equivalence relations.

**Residual equivalences and supports.** Every one of the 20 residual raw words has its retained global color bijection and independent A/B dihedral readings checked pointwise. The induced corner map is verified on both incident side colors, including the minus-one offset for reversed readings. These operations rename numerical lengths rather than making unequal values equal. Exhausting every subset of each residual fixed atlas reproduces 64 raw supports and 22 representative supports. The actual occurring-star set equals one of these closed covering supports; no passage to only minimal supports is made.

**Deterministic opposite cases.** In each of the three A3 representatives the sole support partitions all twelve actual corners. I independently enumerated every equal-length guest native side and both ordered endpoint correspondences for each host side. Exactly one candidate survives the two endpoint star tests on each of 36 host sides. The fixed side endpoints and opposite interior half-plane determine the full relative isometry, also for reflected placements. Propagating indexed maps through connected full-side adjacency gives a framed symmetry group with finitely many tile orbits. Its discreteness and cocompactness give a rank-two translation subgroup by the previously reviewed elementary planar argument. No assumption of finitely many absolute orientations or a fixed honeycomb embedding is introduced.

**Inherited private-repeat class.** The representative is exactly A=(0,1,0,2,3,4), B=(5,3,5,2,1,4). The domain has six pairwise distinct numerical values; both repeats are private and the other four values shared. These are precisely the old theorem's hypotheses. A formal-color extension allowing physical collisions is not claimed and cannot be inferred here. Its independent verifier passed both exceptional four-face tori and all 192 generic endpoint candidates.

**Two new positive torus branches.** The independent verifier recursively pairs the greatest unused boundary dart with every same-color candidate, then walks the vertex permutation rather than using the author's endpoint union-find. It exhausts all 7,560 and 22,680 oriented four-face gluings. Counts agree exactly: 7,488/22,608 connected gluings, four/six trivalent torus candidates, and two/three distinct angle supports. Each of the five retained witnesses is checked independently for use of every side exactly once, equal lengths, connected face adjacency, and eight circular triple vertex links, with the correct native corners under each face reflection. Reverse boundary identifications give orientability and V-E+F=8-12+4=0. Exact source-angle implications, not a negative bounded search, make these positive witnesses applicable to the actual given shapes.

**All angle implications.** Every one of the ten source supports has its retained witness index and source-row list checked. Forty Fraction combinations reproduce all twelve angle coefficients AND the constant coordinate of every target equation. The two polygon total-angle rows have right-hand side four and every source/target star row has right-hand side two, in units of pi. Thus the retained identities give actual cone angle two pi. Compact nonsingular flat-torus development then supplies a Euclidean tiling by the original whole polygons with two independent deck translations. Neither metric closure nor embedded appearance of the torus patch in the source is assumed.

## Independent replay

The new [standalone verifier](hexagon-five-noncommon-independent-2026-10-15.py) imports no author modules. It uses Python integers, sets, exhaustive finite enumeration and Fraction only; it reads retained certificates as data. Commands completed with exit status zero:

```text
mise exec -- conda run --no-capture-output -n arisearch python research/reviews/hexagon-five-noncommon-independent-2026-10-15.py
mise exec -- conda run --no-capture-output -n arisearch python research/reviews/hexagon-five-length-private-repeat-verify.py
```

New-checker result:

```text
PASS: 14880 words, 20 residual maps, 22 representative/64 raw supports, 36 deterministic sides, all 30240 fixed-domain gluings, five positive tori, 40 exact augmented identities, pure-star torus
```

No revision of the mathematical claim was required. The common-palette cases are separate previously reviewed dependencies when forming the larger corollary for all nonadjacent repeats. Adjacent repeats, fewer than five numerical lengths, and polygon pairs containing a pentagon remain outside this theorem. No general impossibility or priority claim follows.
