# Independent hostile review: AA/BB immediate seam atlas

Verdict: PASS for the fixed finite geometry and its stated limitations. No plane tilability, obstruction, universal nonperiodicity, or propagation theorem is certified.

Reviewed the problem definitions, protocol §§5 and 19, the regular P5/Q7 first gate and its exact certificate, and the atlas source, report and regenerated certificate. The producer completed successfully under the required environment wrapper. The independent checker is `aa-bb-strand-atlas-independent-sol-2026-10-19.sage` in this directory.

The checker separately reads exact certificate coordinates over Q(zeta_180), verifies strict convexity of Q, its native turns, the four unit edges and AA/BB length equality, and reconstructs all four forced exterior regular pentagons by clockwise edge walks. It checks their nonoverlap and the two shared vertices at Q144. Exact signs use certified intervals with precision doubling, with exact field zero tests.

It independently enumerates all 18 endpoint/parity possibilities per metric. Precisely five survive: both parities AA-to-BB, both parities BB-to-AA, and the orientation preserving AB-to-AB (or BA-to-BA) seam. A mixed seam with reflection has wrong endpoint sums. An isometry of each parity is uniquely fixed by its two endpoint images; hence this enumeration covers all whole-edge native seams, including reflected copies. Exact reconstructed complex maps, real matrices, translations and unit modulus agree with the certificate.

For every surviving seam the checker independently constructs the two Q and eight incident P placements. Exactly the two endpoint P pairs coincide, leaving eight distinct geometric tiles; all distinct tile interiors are disjoint. Separation is checked by independently comparing exact projection intervals along every edge normal, rather than using the producer's inward-side test. For every one of the four AA/BB parity combinations at each of the four metrics, the three Q and twelve incident P placements leave eleven distinct tiles after the four required endpoint identifications, with all distinct interiors disjoint. Thus no additional coincident tiles are being silently accepted by deduplication in these tests.

The formal holonomy statements follow directly from composition: (c conjugation+t)^2 has translation t+c conjugate(t), whereas the direct step has rotation order five in these four records. These are group identities for specified rigid motions. Repeating a selected motion has not been proved to produce an embedded infinite strand, and arbitrary admitted parity sequences need not repeat that motion. Consequently neither a forced parity, a global return constraint, nor transverse completion follows from this atlas. This is a limitation of the established argument, not a proof that no future invariant exists.

The stopping statement accords with §5: a new unbounded restriction on parity sequences or a construction with proved transverse completion is missing. §19 requires redirecting the overall investigation; this finite review does not authorize growth to larger strands or carriers. Necessary torus count balances have no extension consequence here.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch sage research/searches/aa-bb-strand-atlas-sol-2026-10-19.sage
    mise exec -- conda run --no-capture-output -n arisearch sage research/reviews/aa-bb-strand-atlas-independent-sol-2026-10-19.sage

Both cover exactly AABBAB, AABBBA, ABAABB, BAAABB, five immediate seams and four two-seam combinations per metric. No larger search was performed.
