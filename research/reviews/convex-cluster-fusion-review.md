# Hostile review: convex-cluster fusion lemma

**Artifact reviewed:** [convex-cluster-fusion.md](../lemmas/convex-cluster-fusion.md).

**Date:** 2026-10-02
**Reviewed claim:** [research/lemmas/convex-cluster-fusion.md](../lemmas/convex-cluster-fusion.md)
**Verdict:** **Valid after repairs**, now incorporated into the lemma.

## Assumptions checked

The source protoset must be strongly aperiodic under exactly the target's
unrestricted-isometry and unrestricted-contact convention.  The residual
tile must be a member of the source set.  The cluster must be a finite legal
patch whose closed tiles have disjoint interiors and union exactly the
macro-polygon.  The witness tiling must partition at the tile level into
cluster occurrences and residual singleton occurrences.  The macro-polygon
and residual polygon must be distinct congruence classes.

## Attacks made

1. **Reflected macrotiles.**  An orientation-reversing placement of the
   cluster remains legal precisely because the source convention permits all
   Euclidean isometries.
2. **Symmetric macrotiles and nonunique dissections.**  A symmetry of the
   macro-polygon can move the seam.  This causes no defect: select one
   arbitrary placement isometry on one macrotile in each orbit and translate
   that choice through the orbit.  Canonicity is neither asserted nor needed.
3. **Orbit consistency.**  The cyclic translation action is free on bounded
   tile occurrences.  If a nonzero power fixed one, a nonempty compact set
   would be invariant under a nonzero translation.  Thus the translating
   exponent is unique.
4. **Multiple periods.**  The proof should not demand simultaneous
   equivariance under a full period lattice.  Choose one nonzero translation;
   its cyclic action suffices for the contradiction.
5. **Boundaries and partial contacts.**  Every refined subtile stays inside
   its former macrotile.  Macro-interiors were disjoint, so refinement cannot
   create interior overlap.  Shared and partial boundaries are allowed.
6. **Quantifiers.**  The special source tiling proves only existence.  The
   refinement argument begins with an arbitrary hypothetical periodic target
   tiling, so it proves universality of nonperiodicity rather than merely the
   nonperiodicity of the witness.

## Defects found and repairs

The initial statement did not spell out that the cluster union was exact,
that the source tiling's partition was at tile level and exhaustive, or that
all source isometries included reflections.  These hypotheses were made
explicit.  The proof's “choose any isometry” wording is valid but was audited
to ensure that one choice is made only for an orbit representative and then
transported, rather than silently assuming a canonical dissection.

## Remaining uncertainty

None in the conditional lemma.  Its application is unresolved: no source
set under the exact reflection convention and no convex global cluster
partition have yet been certified.
