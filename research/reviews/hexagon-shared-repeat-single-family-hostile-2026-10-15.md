# Independent review: the first shared-repeat word family is untileable

Date:2026-10-15. Verdict: **VALID** for the complete stated all-metric, unrestricted-contact exclusion. This reviewer proposed the cyclic-word family, but did not author the root's obstruction proof or producer. The independent computation below was derived from direct side matching before reading the producer. No producer imports are used.

## Claim and assumptions checked

Reviewed [the author proof](../lemmas/hexagon-shared-repeat-single-family-2026-10-15.md), its twelve-star JSON certificate, and its producer. The family is

    A=(r,x,r,y,z,t), B=(r,y,r,z,x,t),

with five pairwise distinct positive lengths and genuine convex hexagons. Reflections and unrestricted initial contacts are allowed. The reviewed defect-free hexagon limit supplies an edge-to-edge trivalent tiling if any unrestricted tiling exists. Neither native word has equal adjacent lengths. At a trivalent vertex all three ray lengths therefore differ. Each single-type corner graph is a four-cycle with a pendant edge, so neither species can be the only type in that limit. An A occurrence, and hence its side2, must exist.

## Independent direct eight-match contradiction

Examine A side2, length r, with endpoint corners A1,A2. Their other arms are x,y. Every full mate must be one of A0,A2,B0,B2, and either endpoint correspondence is allowed. These four slots times two endpoint modes exhaust all reflections and rotations at the native-segment level. At either endpoint the two non-r arms must be different and joined by some native corner. The complete results are below. An empty entry means that endpoint cannot be completed; native B indices are offset by6.

| Mate | Guest corners paired with (A1,A2) | Third-corner choices at those endpoints |
| --- | --- | --- |
| A side0 | (A5,A0) | ({B4}, empty) |
| A side0 | (A0,A5) | (empty, empty) |
| A side2 | (A1,A2) | (empty, empty) |
| A side2 | (A2,A1) | (empty, empty) |
| B side0 | (B5,B0) | ({B4}, empty) |
| B side0 | (B0,B5) | (empty, empty) |
| B side2 | (B1,B2) | (empty, {A3}) |
| B side2 | (B2,B1) | ({B3}, empty) |

No match has both endpoints legal. These are necessary length conditions independent of the numerical angles, so no omitted angle choice can repair them. Thus A side2 has no mate, contradicting the full-side limit. This independently proves the stated theorem without depending on the author's selected three-star argument.

## Certificate and implementation review

The independent checker constructs the star atlas by choosing triples of actual native CORNER INDICES and checking that their three distinct arm pairs form a triangle. This differs from the producer's triples-of-ray-labels and corner-product construction. It recovers exactly the twelve retained stars. It then independently follows the r arms from the three A1 stars and recovers exactly the author's far pairs (0,2),(2,7),(2,6), all unsupported. Full endpoint pruning independently reduces the atlas12 ->1 ->0.

[Independent checker](hexagon-shared-repeat-single-family-independent-2026-10-15.py):

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/hexagon-shared-repeat-single-family-independent-2026-10-15.py

Result: PASS, exit0. Its only certificate access is read-only comparison with independently reconstructed data. It imports no author module and uses only the standard library. The producer itself correctly retains actual corner indices and enumerates the complete relevant domain. No finite-model assumption, solver assertion or numerical tolerance enters either proof.

## Counterexample attempts and remaining uncertainty

Checked same-type mates, cross-type mates, both repeated slots of each species, both endpoint orientations, monohedral disappearance in the defect-free limit, and accidental angle equalities. All are covered. Extra side-length aliases would change the graph and are explicitly excluded by the five-distinct-length hypothesis. Nontrivalent or partial contacts in the original tiling are covered by the existing defect-free limit dependency, whose validity is inherited rather than re-proved here. No defect or repair was needed.

The result is an all-metric exclusion of this word pair only. It gives no classification of other A5/B5 words and no solution of the unrestricted two-polygon problem.
