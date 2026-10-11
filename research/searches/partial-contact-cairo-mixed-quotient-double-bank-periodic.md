# Double-bank Cairo carrier exact reproducibility

Status: complete full-cone candidate; fresh independent review pending.
Source orbit0 flat23, residual-color actual-order chambers0 and8. Initial
scale3 proposal (variants0,0,8) has18 darts and two odd formal piece-color
classes, retained bounded parity certificate only. Scale6 chamber0 uses
variants0,0,0,0,8,8; chamber8 uses1,1,2,2,5,5. Both have36 darts,
19 search nodes and1 completed pairing before finding the candidate.
Proposal domain is all formal-color perfectmatchings with both endpoint
maps, same-face matches allowed, and exact360 corner-component pruning.
No exhaustive negative geometric implication is made.

Actual original pentagon coordinates and closures are reconstructed in
separate exact Euclidean development, with no model imports. All12 true
vertex links are circular360, both endpoints/opposite CCW orientations and
integer-period coefficients are checked. Chamber0's Euclidean frame lift
has12 original faces (8P4Q),72 atomic directed transitions; chamber8 has
6 faces (4P2Q),36 transitions. Exact QQ coefficient holonomy rank2 and
integer Hermite primitive lattice give displayed periods, whose determinant
is precisely original motif shoelace area. Full positivity proves convexity
and period independence. Cut signs are linked by B-b=w(D-a)=w(2a-e).
The lemma explicitly handles e=2a by removing paired zero boundary atoms.
No privacy or genericity condition restricts the sufficient domain.

Replay:

    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-mixed-quotient-native-search.py --pattern orbit0 --flat 23 --scale 3 --output research/certificates/partial-contact-cairo-mixed-quotient-orbit0-flat23-three-faces.json
    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-mixed-quotient-native-search.py --pattern orbit0 --flat 23 --scale 6 --output research/certificates/partial-contact-cairo-mixed-quotient-orbit0-flat23-six-faces.json
    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-mixed-quotient-native-search.py --pattern orbit0 --flat 23 --chamber 8 --scale 6 --output research/certificates/partial-contact-cairo-mixed-quotient-orbit0-flat23-complement-six-faces.json
    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-mixed-quotient-native-development.py --input research/certificates/partial-contact-cairo-mixed-quotient-orbit0-flat23-six-faces.json --output research/certificates/partial-contact-cairo-mixed-quotient-orbit0-flat23-development.json
    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-mixed-quotient-native-development.py --input research/certificates/partial-contact-cairo-mixed-quotient-orbit0-flat23-complement-six-faces.json --output research/certificates/partial-contact-cairo-mixed-quotient-orbit0-flat23-complement-development.json

Environment SageMath10.9, Python3.12.13. Deterministic, no seed, numeric
optimizer, node cutoff or unresolved result. Exact quadratic field,
polynomial identities, vertex links and integer lattice arithmetic carry
all consequential decisions. Frequency balance was used only to propose
copied native variants; actual geometric/global proofs supply existence.
Independent full-cone review remains pending.
