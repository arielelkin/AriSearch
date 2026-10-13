# Fresh independent geometry review: rational-unit B001221 slice

Date: 2026-10-13. Reviewer: sol, distinct from root producer.
**Verdict: VALID** for the exact algebraic A/B pair and finite omission gates.
Infinite mixed covering and universal aperiodicity remain unproved.

## Exact finite defining data

Set U=(3+4i)/5. Let f be the retained monic degree12 rational polynomial
V_minpoly in
[the certificate](../certificates/two-hexagon-001221-rational-unit-slice.json).
Define V as its UNIQUE root in the rational complex rectangle

    299/1000 < Re(V) < 300/1000,
    954/1000 < Im(V) < 955/1000.

The independent verifier re-enters all13 rational coefficients directly,
checks irreducibility overQ, enumerates all12 exact QQbar roots and verifies
exactly one lies in that rectangle. Thus the decimals in the producer
certificate are not needed as defining data or for proof decisions.
Set W=-1/(UV). Exact tests give unit modulus and positive real/imaginary parts
for U,V,W, placing all three turns in(0,90) degrees. Their product is-1, so
those positive turns sum180. The defining rectangle and polynomial identify
an actual exact root, rather than a numerically selected branch.

Set S=(1+U,UV(1+V),-V(1+W)). With
D(a,b)=Im(conjugate(a)*b), define native length classes

    a=1,
    b=D(S2,S0)/D(S1,S2),
    c=D(S0,S1)/D(S1,S2).

All three are positive, real, pairwise distinct algebraic numbers. Exact A
vertices are cumulative sums of edge vectors

    (a, aU, bUV, bUV^2, -cV, -cVW).

Its native word is001122. Exact B vertices are cumulative sums of lengths
(a,a,b,c,b,a) times initial direction1 and successive turns
-1/U^2,-1/V^2,-1/W^2,-1/W^2,-1/V^2.
Its native word is001221. Both sums close exactly and all48 nonincident
support determinants are strictly positive. Consequently both are actual
strictly convex hexagons, rather than local angle/side ledgers.

## Independent closure-domain reconstruction

The checker imports neither producer nor symbolic closure source. It uses
rational functions overQ(i) to derive the B closure numerator directly from
the determinant length ratios and forced endpoint palette. That reduced
numerator is degree6 and squarefree. Its product with its coefficientwise
complex conjugate is exactly f. Therefore its six roots lie among the twelve
roots independently enumerated for f. Among those roots satisfying all unit
positive-quadrant turn tests, precisely the isolated V solves the closure
numerator. This independently verifies the producer's entire fixed-U root
census and its single retained acute-unit branch, not merely approximate
agreement with the reported branch.

The scope is one rational-unit slice, not arbitrary U. An earlier interrupted
67-degree slice supplies no exclusion or existence claim and is not used.
The precise finite domain and possible outcomes are six fixed-U complex
closure roots, tested for unit positive-quadrant geometry and actual polygons.
A nonclosing/negative/support-failing branch would fail the local candidate;
a valid branch permits subsequent native-neighbourhood testing only.

## Angle language and all reflected monohedral families

Native angle phases are A_i=-1/(U,V,W)_i and B_i=(U,V,W)_i^2. They have
arguments strictly between0 andpi. Exhausting all56 unordered triples gives
exactly the five generic ternary types. A triple phase1 cannot hide an
incorrect multiple of2pi: three positive interior angles total between0
and3pi, so only2pi is possible. Thus the star-language assertion is exact.

For EACH polygon the checker tests all12 dihedral corner reindexings against
H1,H2,H3 of the already reviewed unrestricted Zhu-Wang-Yan classification.
The reflected side map is k-i-1, matching reversed successive endpoints.
Every family test fails. Thus neither exact polygon tiles monohedrally under
that named imported theorem, including reflected and original partial-contact
tilings. The theorem is not newly proved here. Failing these two omission
gates is necessary for a two-shape candidate, not sufficient for tilability
or forcing. Exact angle-phase tests and length comparisons use QQbar/AA,
never floating-point thresholds.

## Replay and non-consequences

[Independent no-author-import verifier](verify_two_hexagon_001221_rational_unit_independent.py):

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_two_hexagon_001221_rational_unit_independent.py

Outcome: PASS. Exact degree12 root isolation, independent degree6 closure
norm, all six closure branches, two polygons,48 strict supports,56 angle
triples and24 dihedral monohedral-family cases. No solver, seed, timeout,
numerical acceptance or patch-to-plane inference. The producer writes the
retained certificate and should not be replayed against it destructively.

This does not prove an actual compatible B ring, an infinite covering,
shape-only recognizability, exclusion of unintended reflected contacts or
aperiodicity. The next concrete obligation is exact finite B-neighbourhood
extension, which can falsify the candidate cheaply before any global search.
The original research problem remains unresolved.
