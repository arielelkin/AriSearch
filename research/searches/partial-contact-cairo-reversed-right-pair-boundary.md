# Symbolic periodic boundary certificate for the reversed right-angle pair

Date2026-10-10. Python3.12.13, SageMath10.9. Exact Q(sqrt3)[u] polynomial
identities and exact algebraic real-root isolation; no numerical decisions,
random seed, timeout or unresolved solver result.

Question: does the proposed eight-face periodic motif tile for every
positive metric in the reversed-right-pair two-cross survivor family?
Words, transforms, periods and complete proof are in the linked lemma.
Finite domain:48 directed atomic native boundary edges, each native e
edge bisected. Permitted pairing is endpoint reversal plus an integer
combination of the two proposed periods. No symmetry quotient or finite
patch is assumed to extend.

A sample u4/5 supplies exact transformed bounding boxes solely to propose
integer translation indices for endpoint matches. The proof does not need
that search to exhaust arbitrary translations: a completed perfect pairing
of all48 atoms, each checked as a symbolic polynomial identity, explicitly
cancels the entire periodic boundary. Found24 pairs; none left unmatched.
The eight original face areas sum exactly to lattice covolume18u.
The producer also verifies every native isometry, side-square identity,
closure and all30 strict support determinants on1/w<u<w by exact real roots.
The global multiplicity argument in the lemma then proves both coverage
and disjoint interiors for the full interval.

    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-reversed-right-pair-boundary.py --output research/certificates/partial-contact-cairo-reversed-right-pair-boundary.json

Completion: PASS24/24 symbolic reverseboundary pairs, all48 native atoms,
area18u, full positive interval. Certificate retains all48 endpoints,
all8 face coordinates, periods, pair translations and support polynomials.
No infinite tiling is inferred from an unconnected finite patch. Review
status independently hostile-reviewed VALID at research/reviews/partial-contact-cairo-reversed-right-pair-periodic-review.md. The result supplies a periodic
escape for this explicit family, not global periodicity of all tilings.

Root proposed the motif and first checked an exact4/5 lattice fixture.
Its initial discarded period proposal had a wrong covolume; corrected
v=(3wu,3w) was used before any successful symbolic certificate. That
failure is not in the proof chain. Author first checked exposed boundaries,
then added every internal-axis boundary to retain all48 original atoms.
