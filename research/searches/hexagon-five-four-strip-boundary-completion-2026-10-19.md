# Same-strip boundary completion gate

Date: 2026-10-19. Status: internally proved exact obstruction; independent hostile review requested. Scope: only the same six-tile quotient strip for rows15,16,23,26,31, not arbitrary complementary strips or unrestricted tilings.

## Result

Neither exposed boundary of any of the five strips can meet any exposed boundary of an isometric copy of that SAME strip along its whole native edge chain, with opposite interiors. Thus the requested one-strip-to-one-strip stacking method has an exact obstruction. No plane tiling, untileability, or aperiodicity conclusion follows. No larger quotient or patch search was performed.

## Reconstructed exact boundary data

The certificate stores both oriented four-edge boundary chains, including all five vertices in Q(r), r²=3, r>0, native species and side, exact edge vectors, squared lengths, and quotient face indices. Boundary directions have the strip interior on the left. Both chains have native word B2,B0,B5,B4; their periods are respectively v and -v. Their vectors are termwise negatives. The finite native word denotes the actual metric edges, and does not impose an artificial marking rule.

For row15, writing the first chain vectors in its stored order, these are

    (1-r/3,r-1), (1,0), (1/2-r/6,r/2-1/2), (2r/3-3/2,3r/2-2).

The first chain starts at (2+r/6,r-3/2). The second starts at (r/6,7r-17/2) with the termwise negative vectors. The other exact chains and all coordinates appear in the JSON, without numerical reconstruction.

The four squared lengths in the order B2,B0,B5,B4 are:

* row15: (16/3-8r/3, 1, 4/3-2r/3, 43/3-8r).
* row16: (16-8r, 1, 52-30r, 37-20r).
* row23: (73-40r, 1, 31-12r, 37-20r).
* row26: (21-12r, 1, 37/3-20r/3, 43/3-8r).
* row31: (21-12r, 1, 37/4-5r, 19/4-2r).

In each row these are four distinct positive numbers. The first and second vectors are not parallel. Distinct consecutive directions ensure the four chain vertices are geometrically visible corners; no hidden subdivision or arbitrary phase along a straight segment creates an extra correspondence.

## Complete obstruction proof

Each oriented chain has the same cyclic sequence of four distinct lengths. An orientation preserving isometry placing the strip on the other side of a seam must reverse the boundary traversal. Hence its length sequence would have to be cyclically equivalent to its reversal. A cyclic word of four pairwise distinct symbols is not equivalent to its reversal: matching the unique first symbol forces its successor to equal its predecessor, which are distinct. This excludes translations and, for completeness, halfturns.

For an orientation reversing isometry the chain traversal agrees with the target traversal, since reflection reverses the interior-left convention. The unique edge lengths force equal native slots to correspond. On the same boundary type, the linear map would therefore fix each edge vector. On opposite boundary types, it would negate each vector, because the two chains have termwise negative vectors. The first two vectors are independent, so the linear map would be I or -I respectively. Both have determinant +1, contrary to reflection. This excludes reflected and glide placements. This proof applies to each choice of source and target boundary. Since no whole-chain geometric match exists, interior overlap and positive transverse displacement never arise, and a strip-area coverage argument is not applicable.

## Exact finite verification domain

The deterministic script reconstructs six quotient tile representatives from the previously certified ten-tile corona, identifies shared full-edge orbits exactly, and follows the eight exposed directed edges modulo v. Every quotient vertex has exactly one next boundary edge. It obtains exactly two four-edge cycles, with lifts closing by ±v. It checks the termwise-negative relation, distinct lengths, independent first two vectors, and B native-side identities.

For an independent mechanical cross-check of the word argument it enumerates all four orthogonal linear maps preserving the period line: I, -I, reflection parallel to v, and reflection perpendicular to v. For each source/target boundary pair it keeps only maps with det(M)M(period_source)=-period_target and tests the four possible image vertices for source vertex0. This is 32 exact cases per metric, 160 total. Translation by an arbitrary integer multiple of v is factored out. Edge equality is checked through exact canonical endpoint pairs modulo v, including vertices and full edges. All 160 cases fail. Any isometry mapping one whole periodic chain to another must preserve the period line and sends a visible corner to a visible corner, so this finite domain is complete for the specified method. Native side labels are not used to reject a geometric match.

No solver, randomness, timeout, floating-point branch, larger patch, or larger quotient is involved. Arithmetic is Sage QuadraticField(3). Float conversion is used only to render the explicitly diagnostic SVG from the certified coordinates.

## Artifacts and replay

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-five-four-strip-boundary-completion-2026-10-19.py

Producer: research/searches/hexagon-five-four-strip-boundary-completion-2026-10-19.py.
Certificate: research/certificates/hexagon-five-four-strip-boundary-completion-2026-10-19.json.
Diagnostic: research/figures/hexagon-five-four-strip-boundaries-row15-2026-10-19.svg.
Inputs: retained 39-omissions metric certificate and five-residual-coronas certificate. Conditional strip-packing validity and its native propagation remain covered by the parent strip lemma and its separate review. This gate itself only analyzes those explicit exposed chains.

The discovery log was not edited. Fresh hostile review should attack boundary reconstruction, the four-map completeness argument, reflection orientation, hidden vertices, and the distinction between failure of same-strip stacking and unrestricted nonextension.
