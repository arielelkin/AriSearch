# Exact mixed four-face proposal and eight-face Euclidean development

Status: completed exact candidate, fresh independent hostile review pending.

Target: obtain an actual periodic witness from the reviewed mixed necessary
frequencies, without assuming rational corner/edge balance gives a surface.
Source: orbit2 flat23, residual-color actual-order chamber0. A four-face
proposal copies P variant0 twice and Q variant9 twice. Native piece lengths
are full three-coordinate linear forms over Q(sqrt3); no numerical length
coincidences are used as colors.

Finite domain: every perfect matching of the24 atomic darts by identical
formal piece color, with both endpoint reversal and preservation for each
pair. Self-dart matching is disallowed; same-face pairs are admitted. Search
uses exact angle-component pruning (>360 or native120 mixed with90/180),
then complete360 sums and connected face adjacency. It stops on the first
candidate, which was reached after13 nodes and1 complete pairing. Thus no
exhaustive negative claim is made. The retained12 pairs cover every dart
exactly once. Search is deterministic, uses no random seed, no node bound,
no floating decisions and no external SAT solver.

Independent geometric development stage: reconstruct local atomic vectors
from exact lengths and native directions, verify closure and all native
unsubdivided coordinates, construct actual vertex flag-link circles,
develop the finite angle/sign lift by exact Euclidean maps, and retain every
transition's polynomial translation. All8 link cycles sum360. The lift
contains8 faces, four per species. Holonomy coefficient rows have rational
rank2; choose a basis, retain integral holonomy lattice via exact Hermite
normal form, and verify every transition is an integer combination of the
two resulting periods. Both transformed endpoints and opposite CCW edge
orientation are checked, not just lengths. The24 inverse pairs cancel all48
atomic edges. Shoelace area equals absolute period determinant identically
as a polynomial over Q(sqrt3)[a,b,c].

The first construction domain is ten positive original native sides
plus B>b. Positive closure proves strict convexity directly by cyclic
support heights; B>b and f=C+d make all inserted points strict interior.
The lemma gives the full global boundary-cancellation/mean-area proof,
so existence is not inferred from the combinatorial gluing or a sample.
A nonempty exact domain fixture is a=1,b=6/5,c=4/5. No generic fixture or
privacy restriction is required: the construction includes resonances.
Complementary chamber6 is also complete: scale4, variants1,1,4,4,
24 atoms,13 search nodes and1 complete pairing. Its actual eight vertex
links, exact eight-face development,48 endpoint identities and the same
period/area identities pass. It splits P_b into b-B,B and Q_f into C,d.
The two motifs agree modulo lattice translations, with only P frame(6,+)
shifted by -t. The lemma covers B=b by removing paired zero-length Q_B
subdivision segments. Thus the full positive flat is covered; no numerical
limit or degenerate original polygon is used.

Replay:

    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-mixed-quotient-four-faces.py --output research/certificates/partial-contact-cairo-mixed-quotient-four-faces.json
    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-mixed-quotient-development.py

Environment: SageMath10.9, Python3.12.13; deterministic exact QQ,
QuadraticField(3), polynomial arithmetic and integer Hermite normal form.
Producer dependencies are the retained residual-color model wrapper for
proposing native variants; geometric development has no model imports and
uses only the retained raw gluing/native linear forms. Numerical optimization
is absent from both new scripts. Completion: bounded candidate and exact
full-parameter Euclidean certificate obtained, no unresolved computation.
Construction status remains pending independent review. Artifacts:

- Lemma: research/lemmas/partial-contact-cairo-mixed-quotient-periodic.md.
- Raw producer/certificate: partial-contact-cairo-mixed-quotient-four-faces.py/json.
- Development producer/certificate: partial-contact-cairo-mixed-quotient-development.py/json.

Complementary replay:

    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-mixed-quotient-complementary.py --output research/certificates/partial-contact-cairo-mixed-quotient-complementary.json
    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-mixed-quotient-complementary-development.py --input research/certificates/partial-contact-cairo-mixed-quotient-complementary.json --output research/certificates/partial-contact-cairo-mixed-quotient-complementary-development.json

The complementary scripts use the same finite proposal/domain logic,
with default source chamber6. Original cone scripts/certificates remain
unchanged after the complementary search. Both geometric certificates
are exact candidate witnesses pending fresh review.
