# Exact angle projection on the preserved one-T maps

2026-10-19. One decomposition design cycle. This concerns necessary angles only,
not metric realization, plane existence, recognition, or aperiodicity.

## Domain

Exactly the saved eight P-parent and six Q-parent maps in
`one-t-junction-substitution-sol-2026-10-19.json`. Each P child has all ten
cyclic/reflected assignments, each Q child all fourteen. The complete domain is
48*10^20*14^5 assignments. No quotient by coincident angles is taken. The parent
word order remains fixed. Shared angles a=(P0,...,P4,Q0,...,Q6) satisfy
0<a_i<1, sum P=3, sum Q=5, in units pi. These strict bounds encode strict
convexity at the angle level only.

## Exact projection lemma

Fix a parent p, map d, and a complete child dihedral assignment sigma.
For child v of species s and native position k, define its shared-angle column
index j(v,k)=offset(s)+(phase(v)+eps(v)*k) mod n_s, with offsets 0 and 5.
For each node x define a 12-entry integer row c_x by summing the unit rows
at j(v,k) over all native incidences of x. At a private parent corner u_r,
subtract the parent unit row at offset(p)+r and set b_x=0. At ordinary interior
nodes b_x=2. At transitions and at the T set b_x=1. In particular the host
flat incidence is absent from native slots, and the other two T angles are
exactly supplementary. Append the two polygon sum rows.

The exact projected parent region is

    K(p,d,sigma) = {a in (0,1)^12 : C(p,d,sigma) a=b(p,d,sigma)}.

Proof: the original fixed-branch slot equations identify every native slot with
exactly the indicated entry of a. Substitution in every node equation gives
precisely these rows. Conversely any a obeying the rows extends uniquely to
all native slots by those identifications; the omitted host contributes its
explicit flat angle 1. All original equations and strict bounds then hold.
No inequality is weakened or closed. Thus there is no Fourier-Motzkin loss,
exceptional boundary case, or existential slot variable left in this projected
representation. If an actual homogeneous cone is desired, homogenize b with
h>0 and replace 0<a_i<1 by 0<a_i<h; h=1 is the normalization used here.

The full exact shared-angle question is whether

    union_{dP,sigmaP,dQ,sigmaQ} K(P,dP,sigmaP) intersect K(Q,dQ,sigmaQ)

is nonempty. This is an exact finite union of open affine polyhedra. It is a
symbolic projection description, not a materialized enumeration of its huge
branch set. `branch_rows` generates any member using integer/Fraction arithmetic;
`rref` gives its exact affine equation reduction. Concatenating the two parent
row sets before RREF implements intersection on the identical angle word
coordinates. RREF alone does not certify strict feasibility.

## Solver decomposition

For the single bounded solve, eliminate native slots before finite branching.
At each node choose the last native slot y and replace it by
b_x minus the sum of other slots; at private parent corners use the appropriate
shared parent angle in place of b_x. The sets of native slots at distinct nodes
are disjoint, so these eliminations commute and introduce no consistency
condition. The T is in particular y=1-z. A private corner is y=a_parent.
All remaining slots occur only in child dihedral identification disjunctions.
For each child use exactly one Boolean among all 2n choices and equate its
substituted native slots to the corresponding shared word. Inactive map
branches impose no constraints. This formulation is equivalent to the projected
union above. It uses a different syntactic decomposition from the previous
integer-selector gate, without changing any mathematical case.

The script writes the SMT-LIB formula and hashes it before `check`, addressing
the previous post-check serialization caveat. Seed 0, timeout exactly 180000ms,
Z3 version retained in JSON. There is no timeout escalation. A SAT branch would
retain exact rational a, both chosen maps, all child assignments, and the joint
Fraction RREF; `--check` independently recomputes the integer incidence rows and
checks every strict inequality and row, without Z3 solving. This checker does
not verify topology again; the previously reviewed fixed maps are its input.

## Replay

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/one-t-angle-decomposition-sol-2026-10-19.py

For a saved SAT result only:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/one-t-angle-decomposition-sol-2026-10-19.py --check

Result and exact remaining obligation are appended after the single solve.


## Supplementary coordinate elimination and exact pruning

For an individual projected branch let its T row be t*a=1 (two native
incidences counted with multiplicity). Choose any pivot i with t_i>0 and set

    a_i = (1 - sum_{j != i} t_j*a_j)/t_i.

Replace every row c*a=b by the row c-(c_i/t_i)t with right side
b-c_i/t_i and delete coordinate i. Impose 0<a_j<1 for every retained coordinate
and 0<(1-sum_{j != i}t_j*a_j)/t_i<1. This is an exact projection and a unique
extension, including the repeated-angle case t_i=2. The function
`supplementary_projection` returns precisely these rational rows, the affine
extension expression, and its strict bounds. To intersect two parents that
eliminate different coordinates, lift each by its unique extension or simply
concatenate their original 12-column row systems. Independent choice of parent
projections never permits independently permuting the shared polygon words.

Two elementary exact pruning lemmas can reduce future explicit cone enumeration:

* If both T pairs use P angles and their two distinct-index pairs are disjoint,
  no branch is feasible. Their four P angles sum to 2, so the fifth P angle
  equals 1 by the P polygon sum, violating strict convexity. This assertion is
  deliberately limited to four distinct indices; repeated-index pairs require
  the full affine test.
* In any species mix, an ordinary triple node cannot contain the supplementary
  pair as a multiset of shared angle coordinates. Subtracting its sum 1 from
  the triple sum 2 forces the remaining angle to equal 1. This works with
  repeated indices as well.

Neither lemma alone decides the complete phase domain. They do not justify
replacing strict inequalities with non-strict ones.


## Scheduling scope

The 21:22 assessment's later instruction asks for at most 30 seconds per
unresolved branch within the 180-second aggregate budget. This single
aggregate disjunctive check had already launched when that instruction arrived;
the parent explicitly permitted it to finish. It keeps its original 180-second
cap and makes no per-branch coverage claim. It is a deviation from the later
branch scheduling rule, not an extension of the total timeout. No second
check or branch retries are performed in this cycle. The coverage ledger must
therefore report all individually undecided map pairs as unresolved unless a
joint witness or a complete aggregate UNSAT answer is obtained.


## Completed result and stop

**UNKNOWN (timeout)** after 180.01853186800145 seconds, Z3 4.16.0, seed 0,
fixed timeout 180000ms. No rational witness, excluded map pair, or UNSAT
certificate was obtained. All 48 pairs remain individually unresolved in the
JSON coverage ledger. Pre-check formula SHA256 is
`410501398f4478e0a77f066c0950afd618b5aa1dec9e4579cc52db5ae0a82265`.
The full pre-check SMT-LIB formula is retained beside this report. The JSON
also separately hashes that file, which appends a check-sat command to the
hashed assertion serialization. Source input SHA256 is
`33d0b6da814916e886daa93daee3b095519749120e42b0eaabfe6e84e550a47b`.

The exact remaining system is the displayed finite union of intersections of
the two strict projected parent affine regions, over exactly the saved maps
and all child phases/reflections. Its emptiness is undecided. The slot
elimination and supplementary-coordinate projection are complete algebraic
reductions, but the enormous discrete union has not been explicitly exhausted.
The elementary pruning lemmas do not decide the surviving overlap cases.
Stop this design cycle under the assigned §5 limit; no timeout extension,
new map, metric gate, or aperiodicity conclusion follows. Reopening should
supply an exact branch-cone enumeration with independently checked
infeasibility certificates or a simultaneous strict rational angle witness,
using a materially stronger finite-domain decomposition rather than repeated
aggregate timeouts. No Git or discovery-log edit was made by this implementer.

Review status: internally checked derivation; fresh hostile review requested
through the parent. The projected formulas must not be described as an
independently reviewed feasibility or infeasibility result.
