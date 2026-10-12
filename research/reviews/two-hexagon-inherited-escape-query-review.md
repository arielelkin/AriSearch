# Review of the inherited low-rank escape query

**Status:** code and mathematical soundness review, 2026-10-12. The review
covers `research/searches/two-hexagon-inherited-escape-query.py` and the
called support, symmetry, implication, and query routines. It does not
assert a final solver outcome or joint polygon realisability.

## Extraction and relabelling

The library reads all retained torus labellings, recomputes the actually
used triples U and side pairs E with the separate global checker, and
compares E with the stored record. It checks U in the original angle
closure and E in the equivalence closure of F. Using U,E directly gives a
valid torus clause on the full type lattice. Deduplicating identical U,E
preserves every inherited clause; one source is sufficient for provenance.

The 288 relabellings apply independent dihedral corner maps to both
species and optional species exchange. Their side map correctly contains
the reflection offset -1: side i joins corners i,i+1, hence reflection
r-i sends it to side r-i-1. Applying the corner and side maps to U,E
therefore gives another valid escape support. No lattice reflection is
needed: the native-symbol chirality changes to compensate for a native
corner relabelling. The group is closed and contains inverses.

## Refinement logic

The initial query treats triple variables as independent Boolean values.
The patch extraction uses only actual patch triples U and actual glued
pairs E. Its minimal side type is eqclosure(E), which is contained in the
solver's transitive side relation. Thus if closure(U),eqclosure(E) activates
an inherited support V,F, all its side variables are already true. At
least one triple of V must be false in the solver assignment; otherwise
the existing blocking clause was violated. The assertion of a nonempty
missing set is sound.

A greedily reduced subset S of U implying every missing triple is checked
with exact rational elimination. Adding S=>tau, together with all symmetry
images, is valid for every exact geometrically realisable angle type.
This removes the relaxed assignment without excluding an actual type that
could matter. The refinement does not need to assert every closure triple
immediately: it learns only consequences necessary for inherited escapes.

On a residual return, the extracted patch is legal in
X(closure(U),eqclosure(E)), and that type activates no retained escape under
any of the 288 symmetries. This is a sound finite residual obligation.
It does not imply that the patch extends, that the polygons close with the
required length data, or that there is no other periodic escape.

An UNSAT result is correspondingly stronger: the relaxed query contains
every exact type admitting a patch and avoiding the library, because every
added implication is sound. UNKNOWN and the iteration limit remain
unresolved outcomes. No formally checkable CP-SAT infeasibility proof is
produced.

## Practical limits

The recorded rank is the augmented rational rank minus the two polygon
sums. Consistency is automatic here because the all-120-degree vector
satisfies every triple equation. Coverage and rank are descriptive output,
not evidence of infinite tilability. A residual may be noncovering or fail
the corner-balance condition, so those tests should precede expensive
geometric or large-patch work.

The refinement records retain S and targets, so their validity can be
independently replayed even without the full relaxed triple assignment.
For an independent residual review, recompute U,E from the saved patch,
then closure, equivalence closure and support avoidance using a separate
checker; do not trust only the recorded booleans or rank.
