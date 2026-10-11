**Fresh independent status: VALID; see the corresponding root review under research/reviews.**

# Four-to-one ten-face Cairo carrier reproducibility

Status: completed exact full-cone candidate, fresh independent review pending.
Source orbit6 flat142, actual-order chamber0 from the complete remaining18
full-residual-color model certificate. Mixed frequencies0:3/5,3:1/5,9:1/5
copy atscale10 to six whole P, two split P and two split Q. All58 formal
piece darts are perfectly paired, admitting both endpoint maps and same-face
pairs, exact360-component pruning and connected final face graph. Search
stops at first witness after2221741 nodes,1 complete pairing. No exhaustive
negative implication is asserted. No random seed, numeric solver or node
cutoff is used; fixed copied-face count is the finite proposal domain.

Separate exact development has no model imports. It reconstructs original
native coordinates/closure,19 actual circular360 vertex links,10 Euclidean
frame states, every transformed endpoint/CCW direction and all58 integer
period shifts. QQ coefficient holonomy rank2 and integer Hermite lattice
produce the periods. Polynomial shoelace/covolume identity over Q(sqrt3)[a,b]
is exact. Full positivity0<b<sqrt3*a ensures all explicit cut piecespositive,
strict convexity and two independent periods. No genericity/privacy or
sample-only assertion occurs in the sufficient lemma. The multiplicity/
mean-area argument supplies full plane coverage and interior disjointness.

Replay:

    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-mixed-quotient-native-search.py --pattern orbit6 --flat 142 --scale 10 --source research/certificates/partial-contact-cairo-remaining-eighteen-residual-colors.json --output research/certificates/partial-contact-cairo-mixed-quotient-orbit6-flat142-ten-faces.json
    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-mixed-quotient-native-development.py --input research/certificates/partial-contact-cairo-mixed-quotient-orbit6-flat142-ten-faces.json --output research/certificates/partial-contact-cairo-mixed-quotient-orbit6-flat142-development.json

Environment SageMath10.9/Python3.12.13, exact QQ/quadratic field polynomial,
vertex-cycle and integer lattice arithmetic. All computation complete;
independent full-cone review pending. No seam-primal-to-surface inference.
