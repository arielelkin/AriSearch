# Independent hostile review: equiangular imbalance and one corona

Date: 2026-10-19. Reviewer: independent Sol implementation agent.
Verdict: **valid within its explicitly local/family-restricted scope**.
No plane tiling, periodic escape, or aperiodicity conclusion is certified.

## Exact claims reviewed
Reviewed `research/searches/hexagon-imbalance-cocycle-sol-2026-10-19.md`,
both companion Python scripts, and retained corona JSON. Checked closure,
phase/reflection imbalance, local triangle integrability, the generic
untileability family, exceptional b=-a obstruction, fixed b=a one-corona
certificate and no-one-species escapes. The full-edge trivalent reduction
is an explicit prior dependency, not newly established here.

## Independent algebra and endpoint attacks
Closure follows by resolving e2=e1-e0 and opposite vectors -e_i. The
A differences are (a,a,a) in the displayed convention, and B differences
are (b,b,b). For native s, s_i-s_(i+3)=(-1)^i delta, and replacing i by
r+eps*k gives (-1)^(r+k)delta for either eps. There is no missing reflection
sign. Positive closing edges in these strictly ordered six headings make
strictly convex polygons; the stated domain excludes zero lengths.

The triangle's rays have c,h,c lengths, and its corners tile exactly three
120-degree sectors. Its nonzero signed imbalance sum b therefore refutes
only a proposed local charge identity. Elementary-face telescoping supplies
integrability of a preexisting assignment; the report correctly does not
infer existence of that assignment on the infinite graph.

For generic b not in {0,a,-a}, p=c+b and m=c-b are distinct and private
to B, since p=h iff b=-a and m=h iff b=a. At a native (p,m) corner, both
other tiles must be B. Directly listing B corners gives N_B(p)={c,m}
and N_B(m)={p}, whose intersection is empty. Thus the mandatory corner
has no vertex completion. Allowing the third ray to have public length c
does not repair it. A-only stars require a proper two-color triangle and
are impossible. This is a pointwise no-tiling proof, with no finite-to-
infinite extrapolation. At b=-a the unique private c+a edge has h at both
endpoints, so its B mate requires a nonexistent (h,h) third corner.
At b=a, B-only fails by N_B(p)={c,h}, N_B(h)={p}; A-only fails as before.
These neighborhood arguments use unordered corners, so all rotations and
reflections are included. No equality exception remains for h,a>0.

## Independent corona certificate verification
Created `research/reviews/verify_hexagon_imbalance_corona_sol.py`, a small
independent verifier. It reconstructs all seven polygons from the JSON
without importing producer code, then uses exact Fraction half-plane
clipping and signed areas to check zero intersection area for all 21
pairs. This method differs from the producer's separating-axis test.
It also checks all six central seams as reversed exact segments, all six
ring seams, and absence of any vertex strictly inside another side.
All checks PASS. Thus the witness is an actual legal finite geometric
corona rather than merely an edge-incidence assignment.

The producer's side indexing is consistent: receiving side k+3 starts
at the far endpoint, hence shift q_B,k-q_neighbor,k+4. Consecutive ring
neighbors use headings k+1 and k+4. Its final last/first comparison is
correct. The separating-axis predicate is valid for convex CCW polygons
in the positively oriented oblique basis. Its collinear point-in-segment
criterion uses a coefficient-space dot product only after collinearity,
so using that auxiliary positive-definite dot product is legitimate.
Duplicate states of A are explicitly retained, not silently quotiented.
The count 5,184 is a producer enumeration of labeled states; independent
verification certifies the retained witness, not that full count by a
second enumeration. The finite domain and stopping limit are stated.

## Defects and remaining uncertainty
No mathematical defect requiring repair found. The report's statements
about arbitrary dual walks are conditional on a consistent assignment on
a simply connected complex; this hypothesis is present. Its cautious
exclusion of an automatic injective development is weaker than a possible
complete-flat-surface theorem and does not invalidate its claims.
No conclusion here establishes extension of the corona, geometric return,
a periodic carrier, or an aperiodic tiling. Those remain genuine gaps.
No novelty claim was reviewed.

## Replay

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-imbalance-cocycle-sol-2026-10-19.py
    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-imbalance-cocycle-corona-sol-2026-10-19.py
    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_hexagon_imbalance_corona_sol.py
