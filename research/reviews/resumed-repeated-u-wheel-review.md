# Independent finite audit: repeated-angle U boundary wheel

Date:2026-10-13. Reviewed computation: research/searches/resumed-two-size-repeated-u-wheel.md, producer research/searches/resumed_intrinsic_repeated_u.py and certificate research/certificates/resumed_intrinsic_repeated_u.json. Exact finite claim: all7680 necessary outer-boundary matrices are nonsingular for μ=1+√5, λ=√μ, the stated U angle word,4small+2large children, one center/five single-corner children and exactly two complete child edges on each parent side. This audit does not establish new U-family coverage; the candidate route is already superseded by the reviewed unrestricted at-most-two-U theorem.

## Independent native-index and domain reconstruction

Edge directions are0,144,216,252,288 degrees. Their consecutive exterior turns, labelled BEFORE the outgoing side, are72,144,72,36,36. Subtracting from180 independently yields before-side native angle word(108,36,108,144,144), i.e.(3,1,3,4,4)π/5. The after-side word is correspondingly(1,3,4,4,3), agreeing with the producer. Thus this is a cyclic rotation of the earlier two-U obstruction's(36,108,144,144,108) word, not a new angular family.

A parent corner i can use any native child corner j with equal angle. There are two choices at each of the two108 parents, one at the36 parent and two at each of the two144 parents:2×1×2×2×2=16 native maps. These choices are independent, not restricted to permutations; distinct children may choose the same native corner. The producer includes all16, an important completeness point.

I reconstructed each corner's two-ray block separately. For chosen native j, incoming/outgoing columns are(j−1,j) if direct, and(j,j−1) if reflected. They contribute scale t_i to parent rows(i−1,i), respectively. This yields exactly the producer's start/end boundary equations, including the wraparound at corner0. Unlike the unique-angle case, C need not be symmetric; the independent checker correctly does not impose symmetry here.

A small center leaves2 large corners:10 choices×32 reflections=320. A large center leaves1:5×32=160. Multiplying by16 gives7680, subdivided5120 center-small and2560 center-large. No rotational symmetry quotient or hidden chirality condition is used. Central orientation and isolated extra point contacts need no enumeration because the necessary boundary equations do not depend on them. The equations exclude all compatible inner arrangements if already nonsingular.

## Exact independent coefficient verification

Minimal polynomial t⁴−2t²−4 is irreducible, by the negative conjugate of μ and the degree-four argument in the prior wheel review. The interval(1,2) identifies its positive real root λ uniquely. A nonzero exact determinant therefore remains nonzero in that real embedding, excluding nonzero real length vectors, not just vectors in Q(λ).

The independent verifier research/reviews/resumed-repeated-u-wheel-independent.py imports only Python standard-library modules. It reconstructs every case and matrix from the corner convention above, computes each determinant by120-term Leibniz expansion using integer polynomial4-tuples reduced by λ⁴=2λ²+4, and compares all four coefficient values against the retained JSON. It does not import Sage or the producer and does not call a matrix determinant routine. Rational-string certificate coefficients are parsed exactly with Fraction; all are verified integral.

It checks all16 native maps, exact case keys with no duplicates, five legal reflection bits, allowed large-corner indices and center sizes, all7680 full coefficient vectors, the5120/2560 subdivision, and empty singular/positive lists. Every determinant is nonzero. Exact replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/resumed-repeated-u-wheel-independent.py

Observed result: PASS: all7680 repeated-angle wheel coefficient vectors independently verified;16 native maps and5120/2560 central-size cases.

This is the complete stated finite domain, with no sampling, solver, seed, numerical tolerance, timeout or global-tiling search. No closed global family enumeration was rerun.

The native closure rows were independently checked symbolically: cos144=cos216=−φ/2, cos252=−(φ−1)/2, cos288=(φ−1)/2; sin144=sin36, sin216=−sin36, sin252=sin288=−φsin36. These yield exactly the two stated real/imaginary closure equations. They are not needed for the nonsingularity result. No singular case was found, so augmented-kernel and positive-polyhedron code branches were never reached; their implementation is not certified by this review and no theorem here relies on them.

## Hostile attacks and scope verdict

Checked omitted repeated-angle assignments, incoming/outgoing indexing after reflection, accidental symmetry assumption inherited from unique-angle matrices, repeated certificate labels, coefficient parsing, arbitrary real metric scope, and isolated point contacts at side joints. The stated necessary boundary model permits an extra child touching a joint only at a native corner; such a contact changes local angular filling but not the exact two-segment boundary length equation. Therefore the finite nonsingularity claim does not secretly rely on the stricter two-sector wheel model.

Optional angular observation is consistent: a native36 corner has native108 neighbours; a strict two-sector parent-side junction cannot fill108 with any other U corner, whereas108+36+36=180 could fill a three-sector joint. This is neither used as a global existence claim nor needed for the determinant certificate.

**Verdict: VALID finite nonsingularity computation over all7680 stated necessary boundary cases.** No repair was needed. The U construction route is **SUPERSEDED** for candidate coverage by research/lemmas/pentagrid-two-asymmetric-u-obstruction.md, whose reviewed statement already excludes every at-most-two-U pair at arbitrary metrics and unrestricted contacts. That global theorem was read for the exact hypothesis match; its proof and dependencies were not independently re-reviewed or replayed in this finite audit. No new U coverage, novelty, aperiodicity or unrestricted impossibility follows from this computation.
