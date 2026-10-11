# Alternate Cairo final-stratum search record

The pre-existing reviewed reduction left k in{sqrt3,1+sqrt3,1+4sqrt3/3}.
The work in this record keeps every native a/b cut choice and every whole/T
choice of the resonant fifth side. Native slot identities and reference
endpoint parities are retained across both geometric ends of a seam.

|Ratio|Full variants|Typed corners|Cyclic oriented stars|Seam features|New outcome|
|---|---:|---:|---:|---:|---|
|fac: k=sqrt3|16|104|8253|1045|Exact rational dual, all tile charges-1|
|e2c: k=1+sqrt3|12|76|5006|567|Exact rational dual, all tile charges-1|
|eac: k=1+4sqrt3/3|16|104|15913|1037|Marginals feasible; actual periodic escape constructed|

The producer partial-contact-cairo-alternate-slot-edge-resonances.py adapts
the reviewed f2a mechanism to these three domains. e2c carries W12/Y166
nonzero rational entries. The fac full exact primal run remained unfinished
and was terminated only after a separate rational dual passed all exact
checks. Its unfinished result is UNKNOWN, not UNSAT. A separate numeric
primal-support attempt also failed to finish exact solving and was canceled;
it supplies no conclusion.

For fac, partial-contact-cairo-alternate-slot-edge-dual-discovery.py uses
HiGHS only to propose real coefficients, then rational reconstruction and
exact Fraction inequalities on all8253 stars and16 tile variants. The
reconstructed vector has W35/Y413 nonzero entries and every tile charge-1.
No numerical infeasibility judgment appears in the proof.

The eac raw seam primal uses Pwhole,P(b-T,e(a,c)-T),Qwhole in equal thirds.
Its six supported vertex types suggest a six/twelve-face domain but do not
by themselves give an assembly. A reflection-consistent version of the
same necessary model returns a different primal: only P(a-T,e(c,a)-T)
and Qwhole, with each reflection flag of each state frequency1/4, and
eight supported three-corner stars each frequency1/4.

Reflection consistency is not an independent linear strengthening here.
Global reflection reverses cyclic star order and flips every corner flag,
while preserving the unordered seam key and reference-end sign. Any old
merged primal can be averaged with its reflected copy to meet the oriented
corner equations with each tile flag half its previous frequency. Its
usefulness was discovery of a more constructive primal.

Directly assigning one face to each of the four oriented states would
reuse four same-typed-slot edges. Two copies of each state remove this
ambiguity. The exact pre-stated lifted domain has8 faces, ten nonself
seam types each with two pairings, four forced same-slot seams:1024 lifts.
At attempt278, the face pairing has24 edges and16 single circular vertex
links of angle360, with connected dual graph. This is a compact orientable
flat torus. The retained positive certificate is
partial-contact-cairo-alternate-eac-eight-face-lift.json.

Exact independent face development obtains periods
U=(2+sqrt3,2+sqrt3), V=(4sqrt3/3,-4-10sqrt3/3), every side holonomy
translational, full integral translation module rank2, and covolume
22+40sqrt3/3=4area(P)+4area(Q). Geometry, links and motif area are carried
in partial-contact-cairo-alternate-eac-eight-face-development.json.
The flat torus universal cover supplies the global periodic tiling;
neither marginal feasibility nor finite neighborhood coverage does so.

All new producers default to read-only replay; explicit --output is
required for writes. No original reviewed f2a artifact was modified.
No period bound was used in the obstruction. Failed earlier four-face
searches remain only their stated finite domains and are superseded by
this positive eight-face quotient where applicable.

Root independent hostile review and no-producer-import reconstruction are
required for promotion of the new fixed-ratio lemmas. If accepted, these
results complete the internally distinct-arm alternate family: outside
k=1 the only tileable parameter is k=1+4sqrt3/3, which is periodic. k=1
has repeated arms and is excluded from this family claim. The main target
is not resolved by this classification.
