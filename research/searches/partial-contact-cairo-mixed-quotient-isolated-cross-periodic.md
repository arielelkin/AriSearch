# Second mixed-quotient carrier reproducibility record

Status: completed exact full-cone candidate, fresh independent review pending.
Source: orbit7 flat12 residual-color native actual-order chambers0 and1.
Each candidate copies two P and two Q exact native variants. Chamber0
variants1,1,7,7; chamber1 variants4,4,12,12. Each has24 atomic darts.
Both endpoint maps are admitted on every identical symbolic piece-color
pair, including same-face pairs. Complete angle components are checked,
then connected face graph and actual vertex flag-link cycles. Search stops
on the first complete candidate: respectively20 and19 search nodes,1
completed pairing each. No exhaustive negative implication is asserted.

Development has no model imports: it reconstructs original native pentagon
coordinates from retained full side forms, checks strict native closure,
both edge endpoints and opposite CCW boundary direction, all8 actual circular
vertex links360, and8 Euclidean frame states. QQ coefficient holonomy rank2,
exact Hermite lattice, all48 integer transition shifts, and total original
face area/covolume equality are verified exactly over Q(sqrt3)[a,b,c].
The full metric domain is original10 positive native sides, split by D>d
orD<d. The lemma explicitly handles D=d by deleting paired zero pieces.
No privacy/event genericity assumption or numerical fixture drives geometry.
Motifs agree modulo lattice, except Q frame(face3,9,+) shifts by -t.

Replay:

    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-mixed-quotient-native-search.py --pattern orbit7 --flat 12 --chamber 0 --scale 4 --output research/certificates/partial-contact-cairo-mixed-quotient-orbit7-flat12.json
    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-mixed-quotient-native-search.py --pattern orbit7 --flat 12 --chamber 1 --scale 4 --output research/certificates/partial-contact-cairo-mixed-quotient-orbit7-flat12-complement.json
    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-mixed-quotient-native-development.py --input research/certificates/partial-contact-cairo-mixed-quotient-orbit7-flat12.json --output research/certificates/partial-contact-cairo-mixed-quotient-orbit7-flat12-development.json
    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-mixed-quotient-native-development.py --input research/certificates/partial-contact-cairo-mixed-quotient-orbit7-flat12-complement.json --output research/certificates/partial-contact-cairo-mixed-quotient-orbit7-flat12-complement-development.json

Environment: SageMath10.9, Python3.12.13. Deterministic, no seed, numeric
optimization or resource cutoff. Search uses retained residual-color model
only for proposing concrete native subdivisions; geometric proof uses exact
raw side coordinates, polynomial identities and explicit multiplicity proof.
Scope: full sufficient periodic cone, not an arbitrary gluing sufficiency
rule. All computations complete; independent mathematical review pending.
