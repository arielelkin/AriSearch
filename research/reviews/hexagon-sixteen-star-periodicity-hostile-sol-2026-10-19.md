# Independent hostile review: sixteen-star periodic escape

Date: 2026-10-19. Reviewer: Sol (separate review agent, not the author and not Astra).

**Verdict: PASS**, for the stated restricted family and with the explicitly imported reviewed defect-limit and monohedral-classification dependencies. No gap requiring a metric search or plane-extension assumption was found. Author lemma and producer were not edited.

Reviewed: `research/lemmas/hexagon-sixteen-star-periodicity-sol-2026-10-19.md`, its linked support producer and JSON certificate, the native upper-atlas producer, the universal strip proof, and the defect-free-limit lemma and re-review.

## Finite gate

The requested producer replay succeeded under `mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-sixteen-star-support-sol-2026-10-19.py`.

I separately enumerated all signed cyclic triples from the 24 ports, using my own incoming/outgoing-ray and remote-corner functions, and iteratively pruned unsupported seams. This independently recovered precisely the certificate’s sorted 16 stars, all twelve cover masks, and all three continuation masks per star. Exhausting all 65536 masks independently against these rebuilt masks and the certificate corona masks recovered exactly the certificate’s 190 supports. Direct proper-subset comparison recovered the six minima in order: 4740, 10372, 16772, 32936, 33924, 16598. No assumption of upward closure is used or needed.

I inspected the corona-factor construction against the ten boundary vertices of a positively handed side5 AA halfturn dimer. Ordinary factors retain the incoming and outgoing exterior side/frame; the seam-junction factor retains the single third tile’s two incident sides. Equality propagates the exterior native side and handedness along each boundary edge. Reusing an exterior tile does not invalidate any factor. Thus the relaxed corona test is necessary. Four cycles and ten factors per cycle are present. Independence limit: the numeric corona masks were consumed from the certificate in my independent exhaustive loop; their geometric definition and producer extraction were checked by inspection, not by a second separately implemented corona enumerator.

## Angle consequence

I rebuilt every augmented angle matrix directly from the signed stars; their rational ranks are 4,4,4,5,4,5. Python Fraction arithmetic independently verified each supplied row combination against (1,1,1,0,...,0;2). There is an even shorter uniform witness: all six minima include star7=((3,+),(4,+),(5,+)), forcing a3+a4+a5=2. Subtracting from the A polygon total gives a0+a1+a2=2. Hence arbitrary supersets of a minimum retain the consequence even though the gate itself need not be upward closed.

## Necessity and geometry

In the reviewed defect-free limit, both surviving species imply all twelve native corners occur. Every actual star survives atlas pruning by induction using its actual remote endpoints. Actual support consequently meets coverage and seam requirements. Color4 appears only on A side5, forcing its AA match. A reflected match would require a third corner with adjacent colors (3,3), absent from both words; the remaining opposite-side placement is the halfturn. A global reflection normalizes its handedness. The ten actual boundary stars then witness a formal corona. None of these steps asserts sufficiency of an abstract support.

For closed strictly convex A, the forced triple identity makes side3 antiparallel to side0, with equal length from their common label0. The two intermediate edges on each lateral chain have strictly monotone height because their directions lie strictly between the corresponding antiparallel directions. The linked strip proof therefore applies to every metric realization. Its shear preserves height, convexity, translations, and halfturns under conjugation. After shear the two chains lie on opposite sides of the vertical endpoint chords, have bounded periodic graphs, and the halfturn-related strips exhaust the plane without interior overlap. The transverse translation has positive horizontal component; together with the vertical strip period it gives independent translations. Undoing the shear yields actual translated/halfturned copies of the original Euclidean A. No illicit affine tile placements are introduced.

If a species disappears in the limit, the imported monohedral convex-hexagon result supplies its periodic tiling. The defect-limit re-review explicitly covers the ETE/trivalence limit, while the monohedral classification is a separate dependency of the linked lemma; these dependencies are identified rather than conflated. This review accepts those established dependencies and does not reprove the external classification.

## Dihedral extension and scope

I rebuilt the atlas on all 180 distinct permutations of 001123, rather than merely reading its cached JSON. Its full-cover 16-star rows are exactly the 12 distinct cyclic/reversed reindexings of B. The extension also follows directly by native reindexing of the same polygon; it does not assume a new metric equivalence between different shapes.

The periodic escape is permitted to omit B, exactly as stated. Partial-side contacts in the original tiling are handled only through the imported defect-free limit. The theorem remains restricted to the stated words and five distinct shared lengths.

Nonblocking correction: the producer’s exhaustion comment says “2^10 signed-star subsets”; the implementation correctly uses 1<<n with n=16, and all 65536 subsets are checked. This is a comment typo, not a mathematical or computational defect.
