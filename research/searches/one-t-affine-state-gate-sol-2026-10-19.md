# Exact partial affine-state gate on preserved P-map 0

2026-10-19. Status: **STOP — no nontrivial merging at the completed first cut.**
The original two-convex-tile problem and the shared-angle question remain unresolved.
No additional cut or full traversal was attempted.

## Domain and predeclared limits

Input: P-map index 0 in `one-t-junction-substitution-sol-2026-10-19.json`,
SHA256 `33d0b6da814916e886daa93daee3b095519749120e42b0eaabfe6e84e550a47b`.
All native phase/reflection choices are retained: 10 per P child and 14 per Q child.
The parent cyclic coordinates are fixed. Limits were 100,000 stored states and
180 seconds aggregate computation, with no monolithic SMT retry. No SMT or LP
solver was used. The gate computation took 0.223855 seconds, storing 10 states.
A separate deterministic replay also passed; including shell startup and the
small preliminary separator diagnostic, all computation remained below 180 seconds.

## Exact state and merge theorem

Write a=(P0,...,P4,Q0,...,Q6), constrained by the common strict box
0<a_i<1 and polygon sums sum P=3, sum Q=5. Fix a parent map and a
set S of assigned children. For each native incidence (v,k) of node x, a
phase/reflection assignment supplies the exact coordinate index
j(v,k)=offset(species(v))+(phase(v)+eps(v)k) mod n(species(v)).
The host flat incidence is absent from the native incidence structure, exactly
as in the preserved map; its supplementary node has right side 1.

A completed node has all incident native children in S. An unfinished separator
node has at least one incident native child in S and at least one outside S.
Nodes with no incident assigned child are untouched. Completed nodes contribute
the exact augmented row [c_x|b_x], including subtraction of the fixed parent
coordinate at a private corner. Add the two polygon sum rows. Canonicalize the
result by rational RREF over **all thirteen augmented columns**, deleting zero
rows. This also represents inconsistent systems exactly, without relying on a
coefficient-only rank convention.

The state consists of (i) the fixed remaining child set and its full unchanged
dihedral domains; (ii) for every unfinished separator node, the individually
identified assigned native incidences (v,k,j(v,k)), with the fixed map retaining
all unassigned incidence positions; and (iii) this canonical augmented RREF.
Keep a representative prefix backpointer. No native index permutation,
coincidence quotient, separator sum, or unidentified incidence multiset is used.
The JSON retains every prefix, its explicit incidence record, and its RREF.

**Merge equivalence proof.** Consider two prefixes with the same state. Their
remaining discrete choices have an identity bijection because the remaining
children and domains agree. Fix any such suffix. At a previously completed
node the two prefixes impose identical affine solution sets because augmented
row spaces agree. At a separator node every individual assigned coordinate
index agrees and the suffix supplies identical remaining incidences, so the
completed node row is identical. At an untouched node the row depends only on
the common suffix. Thus after adjoining all future rows, the complete affine
solution sets agree, and intersecting with the identical strict box preserves
that equality. This holds for every suffix, proving equality of possible future
angle completions and permitting representative-prefix witness reconstruction.
The proof never forgets an unfinished incidence. It establishes a sufficient
merge criterion, without claiming that unequal states have disjoint solution sets.

## Smallest actual separator and exhaustive cut

To make "smallest" explicit, enumerate every nonempty proper subset S of the
13 children of P-map 0: exactly 2^13-2=8190 cuts. Minimize the number of native
separator nodes; break ties by the raw prefix domain size, then |S|, then the
lexicographic assigned-child tuple. This is a graph cut criterion, without an
assumed geometric drawing or a guessed child order. Prefix order starts with
the selected S; no remaining order is needed because the stopping gate fails.

The minimum separator size is **3**, attained by S={e0} under the declared
tie-break. The unfinished nodes are {f16,t0,t1}; completed nodes are {u1,u2}.
The native word of e0 is [t0,u1,u2,t1,f16], of species P. For phase p and
reflection e, the separator records coordinate indices p, p+3e, p+4e modulo 5
at t0,t1,f16 respectively. Equality of the first two indices determines both
p and e: 3(e-e') is not 0 modulo 5 when e differs from e'. Consequently the
separator records alone distinguish all ten branches.

| Exact quantity at the same completed cut | Count |
| --- | ---: |
| Raw phase/reflection prefixes | 10 |
| Distinct exact retained states | 10 |
| Maximum state multiplicity | 1 |
| Pruned prefixes | 0 |

Every prefix has an exact strict **partial** feasibility certificate:
P_i=3/5 for all five P coordinates and Q_i=5/7 for all seven Q coordinates.
This obeys the strict box and both sum equations. At u1 and u2 the completed
node equations identify P coordinates, hence are satisfied for every prefix.
The replay checks every row with Fraction arithmetic. This certificate makes
no claim that any suffix extends it or that a full parent is feasible.

## Stop, scope and replay

The prescribed first-cut compression gate failed: 10 raw prefixes give
10 distinct states. Stop immediately under the assessment's explicit rule.
There is no complete parent feasible-region cover, no excluded map pair, no
shared strict angle witness, no metric realization, and no plane existence or
aperiodicity claim. This negative gate applies to this specified representation
and selected cut; it does not prove that compression at another cut is impossible.
No alternative cut was traversed. The stored maps and all 48 map-pair statuses
remain unchanged.

Replay (recomputes all 8190 graph cuts and all ten exact states, comparing the
saved certificate except for elapsed wall time):

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/one-t-affine-state-gate-sol-2026-10-19.py --check

Files: this report, the adjacent `.py` replay, and the adjacent `.json` certificate.
Review status: internally checked; independent hostile review is pending.
No discovery-log or Git operation was performed by this implementer.
