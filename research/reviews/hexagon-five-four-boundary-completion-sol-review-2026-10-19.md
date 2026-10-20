# Independent hostile review of same-strip boundary matching

Date: 2026-10-19. Verdict: **valid within the stated whole-boundary matching scope**.

Reviewed the boundary producer, search note, JSON, diagnostic SVG, reviewed translation-strip lemma and its independent verifier. The claim is failure of any isometry identifying an entire exposed periodic chain of one retained strip with an entire exposed periodic chain of the same strip, with locally opposite interiors. It concerns exactly rows 15,16,23,26,31. This review does not infer failure of general strip extensions or of unrestricted plane tilings.

## Reconstruction and independent verification

The producer reduces the certified ten-tile corona to six polygon orbits modulo the exact nonzero vector v. It orients every tile boundary with interior on the left, pairs complete edges modulo v, and follows the eight unpaired edges by unique outgoing quotient endpoints. I checked the lifting rule: successive endpoints differ from chosen representatives by integral multiples of v; the cycles lift to four-edge paths of periods v and -v. Native indexing is retained through the original polygon vertex order, including reflected polygons: reversing the traversal changes the directed endpoints but does not change which native side is present. Both recorded words are B2,B0,B5,B4. The B assertion checks the complete ordered polygon against a certified B isometry, rather than identifying species by edge lengths.

The independent checker `research/reviews/verify_hexagon_five_four_boundary_sol.py` takes its exposed-edge input from the previously reviewed translation-strip certificate, independently of the new producer's quotient and cycle algorithm. It compares the eight exact endpoint orbits with the new chains, verifies opposite periods, termwise opposite edge vectors, the four positive distinct squared lengths, and a nonzero determinant between every consecutive pair of edges, including the period junction. It passes all five metrics.

For row15 this reproduces the vectors (1-r/3,r-1), (1,0), (1/2-r/6,r/2-1/2), (2r/3-3/2,3r/2-2). The squared lengths in all five rows agree with the search note. All geometry uses the positive embedding of Q(sqrt(3)).

## Hostile orientation and completeness checks

For a determinant +1 isometry, locally opposite interiors require reversing the interior-left traversal. The cyclic length word would then equal its reversal up to shift. A cyclic four-letter word of pairwise distinct letters cannot do so: the uniquely matched first letter would have to have the same predecessor and successor. This excludes every direct isometry, without a numerical or period-line assumption.

For determinant -1, locally opposite interiors require the same traversal direction. Distinct lengths fix every native slot modulo a whole period. Mapping the same boundary type forces M to fix two independent vectors; mapping the other type forces M to negate both. Thus M is respectively I or -I, both with positive determinant. The argument excludes reflections and glide reflections, and covers all four ordered source/target chain choices. Native words are bookkeeping, not supplementary matching restrictions.

The producer's condition det(M) M(period_source) = -period_target has the correct sign. The four orthogonal maps fixing the unoriented period line are exhaustive. To justify that line reduction, a chain is contained in a bounded-width strip about v. Any nonparallel translational period would make iterates leave that strip, so every period is parallel to v. An isometry matching periodic chains carries a nonzero period to another period. A smaller period, if present, would not affect this line argument; in fact the distinct-length word rules it out here.

The finite calculation has two source types, two target types, two eligible orthogonal maps after the opposite-interior test, and four target anchor vertices: 32 cases per metric, 160 total. Integer period translations change no endpoint orbit. I also implemented a different enumeration: construct orthogonal maps from a first source edge and every length-compatible signed target edge, then enforce opposite-interior period orientation. It has four surviving cases per metric and rejects each by full endpoint-orbit equality. This does not presuppose the producer's four-map construction.

## Partial edges and rephasing

A whole-chain geometric equality cannot hide a visible corner in the interior of a straight source or target edge. The verified consecutive determinants are all nonzero, so every listed vertex is a genuine geometric corner, including the junction between periods. An isometry is locally a homeomorphism, so the converse corner correspondence holds too. Consequently each maximal straight edge maps onto a whole maximal straight edge; matching a partial segment cannot yield an extra whole-chain isometry. Arbitrary continuous rephasing reduces to the four visible vertex phases modulo v. Different local contacts with different strips, incomplete boundary matches, or interpenetrating non-whole seams are outside this claim. The result should not be cited as excluding those mechanisms.

## Provenance and replay

Replaying the producer regenerated both retained artifacts byte for byte:

- JSON SHA256: 46dadcf967a12c4f21abc7cec61e6b79a23e961cc5eb4e655b9fb2060dd91686.
- SVG SHA256: da8fcdcae10671d0c24f938a2722eabfa212efb2b1b4dff9401938a2e81d7588.

The SVG is generated directly from row15's exact chain vertices for three period translates of each chain. Float conversion is confined to drawing. Its title explicitly states its diagnostic status; it supplies no geometric equality decisions or coverage evidence.

Commands completed successfully:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-five-four-strip-boundary-completion-2026-10-19.py
    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_hexagon_five_four_boundary_sol.py

No solver, randomness, timeout, or enlarged patch domain is involved. No defect requiring repair was found. Remaining uncertainty concerns any use beyond whole periodic boundary matching, and the imported conditional source/atlas hypotheses of the parent strip lemma. Neither is settled by this review.
