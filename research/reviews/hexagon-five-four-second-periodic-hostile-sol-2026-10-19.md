# Independent hostile review: second five/four periodic carrier

Date: 2026-10-19. Verdict: **valid** for the positive mixed periodic witness. The unrestricted two-tile problem remains unresolved. This review does not cover other angle-grid pairs or the separate monohedral classification claim.

## Claim and evidence audited

Reviewed `research/counterexamples/hexagon-five-four-second-periodic-2026-10-19.md`, `research/certificates/hexagon-five-four-second-periodic-2026-10-19.json`, and `research/reviews/verify_hexagon_five_four_second_periodic.py`. Read governing problem/protocol and restart log. Replayed the independent verifier successfully. Independently reconstructed placements by explicit orthogonal maps in the positive real embedding of Q(sqrt(3)); no producer/search functions were used.

## Exact shapes and placement reconstruction

Put r=sqrt(3)>0 and v=(3-2r,6-3r). Let A,B be the two ordered prototile lists in the certificate. The four ordered representatives are exactly:

- A;
- v-A, with the same vertex indices;
- v+diag(-1,1)B, with input index i occurring at output index 5-i modulo 6;
- diag(1,-1)B, with input index i occurring at output index 5-i modulo 6.

These identities were checked coordinate by coordinate with exact field arithmetic. Thus the B placements use reflections. Their reversed index order is essential: all four stored polygon boundaries are counterclockwise. Attempting to identify B by a rotation with the same initial vertex fails, but is not a certificate defect.

Direct squared edge lengths give A word (0,1,2,0,3,4) and B word (0,1,1,0,2,3), with positive lengths (1,4-2r,3r-4,2-r,4r-6). Their squared values are (1,28-16r,43-24r,7-4r,84-48r), respectively. They are positive and distinct at the specified embedding. Adjacent edge cross/dot data give the stated side-END angles, and the verifier checks every nonincident vertex lies strictly left of every directed representative side. This stronger halfplane check establishes strict convexity, simplicity, and positive orientation; congruence then transfers this to both prototiles. Different length multisets prove noncongruence.

The exact areas are area(A)=9r-14 and area(B)=10r-16. The period determinant is 38r-60=2 area(A)+2 area(B)>0. Positivity follows from r>30/19 (square both positive sides). Thus the periods are independent and define a discrete full-rank lattice.

## Complete boundary audit

Use representative indices 0,1,2,3 and edge indices 0,...,5. Each entry below pairs an edge with the reverse edge of another representative translated by mh+nt. These twelve pairs cover all twenty-four directed sides exactly once:

| edge | mate | (m,n) |
|---|---|---|
| 0:0 | 3:4 | (0,0) |
| 0:1 | 2:2 | (0,-1) |
| 0:2 | 1:2 | (1,0) |
| 0:3 | 3:1 | (1,1) |
| 0:4 | 2:5 | (0,0) |
| 0:5 | 1:5 | (0,0) |
| 1:0 | 2:4 | (0,0) |
| 1:1 | 3:2 | (0,1) |
| 1:3 | 2:1 | (-1,-1) |
| 1:4 | 3:5 | (0,0) |
| 2:0 | 3:0 | (1,1) |
| 2:3 | 3:3 | (0,1) |

The checker tests actual endpoint differences in the inverse period matrix, not just parallelism or equal edge lengths. Every side has exactly one reversed mate. Its mate has opposite lattice offset, so no unpaired side, repeated index, or erroneous orientation remains. A hypothetical additional coincident boundary with the same orientation is also excluded by uniqueness: its reverse mate would give a second reverse mate for this side. Partial crossings need no separate exclusion, by the multiplicity argument below.

## Global coverage and nonoverlap

Let L=Zh+Zt. Sum the indicator functions of every translated representative to obtain m. Because L is discrete and the representatives are compact, the sum is locally finite, integer-valued, nonnegative, and locally integrable. For each counterclockwise polygon its indicator distribution has gradient equal to its outward-normal boundary measure with a common overall sign. The table pairs every translated side with an exactly coincident reverse-oriented side, so all these measures cancel; vertices contribute no one-dimensional boundary measure. Consequently Dm=0 on the connected plane and m is constant almost everywhere.

Integrating over any measurable fundamental parallelogram and unfolding the lattice translates gives integral m = sum of the four representative areas = det(h,t). Hence that constant is exactly one. Any overlap of two interiors (including a representative with one of its nonzero lattice translates, or hidden duplicate tile orbits) is open and would force m>=2 on positive area, impossible. The family is locally finite, so its union of closed polygons is closed. An uncovered point would therefore have an open uncovered neighborhood, also impossible. This proves exact plane coverage and pairwise disjoint interiors, not merely an edge-balanced formal chain on a torus. Translating by either period permutes the family, giving two nonzero independent periods.

This argument does not assume embedded faces or valid vertex links in a preconstructed quotient surface. It directly establishes multiplicity one in the Euclidean plane, avoiding possible quotient self-overlap or cone-angle pitfalls.

## Defects, repairs, uncertainty

No mathematical defect found in the positive witness or its coverage proof. The compact verifier is specialized to six vertices and reads its prototiles from the certificate; this is appropriate to the retained exact witness, but by itself it does not authenticate that an externally named fixture has those coordinates. The explicit word/placement/area reconstruction above supplies that bridge for this fixture. No repair to the artifact was needed. A useful optional clarification is to state explicitly that the B copies are reflected and their stored vertex indices reversed.

Replay: `mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_hexagon_five_four_second_periodic.py`.

The finite search history, claimed enumeration counts, and imported monohedral theorem are not needed for this verdict and were not independently recertified. The positive carrier alone suffices to show this exact pair is not aperiodic.
