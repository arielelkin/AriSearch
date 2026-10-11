# Fixed Cairo ray459 periodic witness reproducibility

Status: VALID complete exact witness after fresh independent hostile review.
Source orbit7 flat459, sole actual-order chamber0 of the remaining18 exact
full-residual-color necessary models. Scale4 copies variants0,1,10,26,
24 atomic darts withtwo odd piece-colorclasses: bounded parity failure only.
Scale8 doubles eachcopy to six P/two Q,48 actual darts. Domain all equal
symbolic piece-color perfectmatchings withboth endpointmaps, same-face pairs
allowed. Angle components are bounded360; a component withno unpaired
incidentincoming/outgoingdart and angle<360 is safely pruned because it can
never merge later. Completed candidate musthaveall360 sums andconnectedface
graph. Explicit1million-node cap; witnessfound after56277nodes and1complete
pairing, so no incomplete computation enters the existence proof.

Model-free exact Euclidean development verifies all original native vertices/
closure,16 actual circular360links,16 frame states (12P4Q), all96 original
atomic endpoint/CCW/opposite identities, integral shifts inprimitive exact
rank2/Hermite lattice, and positive area=covolume over Q(sqrt3)[scale].
No numeric solver, fixture extrapolation, seam-primal-to-surface inference
or added prototile. Fixednativecoefficientspositiveusing1<sqrt3<2;
strictconvexitybycyclicsupportheights. Global multiplicity proof explicit.

Replay:

    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-mixed-quotient-native-search.py --pattern orbit7 --flat 459 --scale 4 --source research/certificates/partial-contact-cairo-remaining-eighteen-residual-colors.json --prune-closed --max-nodes 1000000 --output research/certificates/partial-contact-cairo-mixed-quotient-orbit7-flat459-four-faces.json
    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-mixed-quotient-native-search.py --pattern orbit7 --flat 459 --scale 8 --source research/certificates/partial-contact-cairo-remaining-eighteen-residual-colors.json --prune-closed --max-nodes 1000000 --output research/certificates/partial-contact-cairo-mixed-quotient-orbit7-flat459-eight-faces.json
    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-mixed-quotient-native-development.py --input research/certificates/partial-contact-cairo-mixed-quotient-orbit7-flat459-eight-faces.json --output research/certificates/partial-contact-cairo-mixed-quotient-orbit7-flat459-development.json

Environment SageMath10.9/Python3.12.13, deterministic exact quadratic field,
polynomial, circular links andintegerlattice. No seed, numeric optimizer or
unresolved computation. Claimscopeone common-positive-scale ray only.
Otherboundedfailures are separate records.

The fresh independent review is
`research/reviews/partial-contact-cairo-mixed-quotient-fixed-ray459-periodic-review.md`.
The standalone model-free checker, with no retained certificate writes, is:

    conda run --no-capture-output -n arisearch python research/reviews/verify_partial_contact_cairo_ray459_independent.py
