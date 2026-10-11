# Six-face bank-transfer carrier reproducibility

Status: complete exact full-cone candidate, fresh independent review pending.
Source: orbit0 flat11 residual-color actual-order chambers0 and7.
Scale3 proposal variants0,2,5 has17 darts and three odd formal piece-color
classes: bounded parity obstruction only, retained certificate. Scale6
copies variants0,0,2,2,5,5 for B>b; variants0,0,5,5,12,12 for B<b.
Each has34 darts. Exhaustive perfectmatching proposal admits both endpoint
maps among identical formal piece colors and same-face pairs. It stops on
first exact360 connected candidate:74/40 nodes,1 complete pairing each.
Thus no negative global conclusion or bounded-resource claim is made.

Actual Euclidean proof stage reconstructs original native coordinates,
11 genuine circular360 links (one four90 star),6 frame states, both endpoints
and CCW directions for all34 atom transitions, integer primitive lattice
shifts via exact coefficient rank2 and Hermite normal form, and full
shoelace area/covolume equality over Q(sqrt3)[a,b,c]. Both strict metric
order domains are explicit; B=b removes paired zero atoms. All original
side lengths stay positive and strict convexity is proved from cyclic
support heights. No genericity, privacy or frequency-to-surface inference
appears in the sufficient statement.

Replay commands (all complete, deterministic, no seed or numeric solver):

    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-mixed-quotient-native-search.py --pattern orbit0 --flat 11 --scale 3 --output research/certificates/partial-contact-cairo-mixed-quotient-orbit0-flat11.json
    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-mixed-quotient-native-search.py --pattern orbit0 --flat 11 --scale 6 --output research/certificates/partial-contact-cairo-mixed-quotient-orbit0-flat11-six-faces.json
    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-mixed-quotient-native-search.py --pattern orbit0 --flat 11 --chamber 7 --scale 6 --output research/certificates/partial-contact-cairo-mixed-quotient-orbit0-flat11-complement-six-faces.json
    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-mixed-quotient-native-development.py --input research/certificates/partial-contact-cairo-mixed-quotient-orbit0-flat11-six-faces.json --output research/certificates/partial-contact-cairo-mixed-quotient-orbit0-flat11-development.json
    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-mixed-quotient-native-development.py --input research/certificates/partial-contact-cairo-mixed-quotient-orbit0-flat11-complement-six-faces.json --output research/certificates/partial-contact-cairo-mixed-quotient-orbit0-flat11-complement-development.json

Environment SageMath10.9, Python3.12.13. Proposal imports retained model
wrapper only to propose native copies; geometric development imports no
model/author proof, only raw native side and pairing data. Exact QQ, quadratic
field, polynomial, vertex-cycle and integer lattice checks decide all
consequential outcomes. No unresolved computation; review pending.
