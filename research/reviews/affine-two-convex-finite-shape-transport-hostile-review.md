# Hostile review: finite transported shape affine obstruction

Date: 2026-10-13. Independent reviewer: contact_structure.
Artifact: [theorem](../lemmas/affine-two-convex-finite-shape-transport.md).
Verdict: VALID after the scope correction recorded below.

The finite transported-shape assumption is stronger than mere existence of
a base dissection and is expressly stated. Images of fixed vertex-difference
vectors have lengths in a finite set, even though vertices may be permuted
under congruences. A fixed pair of independent vectors bounds the full linear
operator, so there is no hidden orientation compactness assumption.

For unequal real moduli the upper offdiagonal grows unbounded unless zero;
then finite squared-distance values force the quadratic polynomial in the
other offdiagonal decay parameter to be constant, forcing that coefficient
zero. Negative eigenvalues and an oblique eigenbasis cause no exception.
Jordan normalization removes only a scalar; boundedness of the conjugation
polynomial forces the commutator zero. No finite distance step is needed there.

In the irrational complex case the orbit is dense. A continuous squared
length function taking values in a closed finite set on that orbit must be
constant everywhere. Three noncollinear polygon vertices supply v,w,v-w,
so their three norms determine a preserved Gram matrix. All conjugates are
therefore orthogonal, and their membership in the four-element centralizer
of M^T M forces the continuous curve to be constant. This proves commutation.

Commuting orthogonal placements commute with M^T M, so the generated group
is finite and commutes with M. Boundary side covering with partial contacts
then proves finite projective direction closure. The real, Jordan and complex
projective classifications and parallelogram consequence are valid. The
scalar-power exception is necessary; it is not a counterexample to the core.

## Requested scope correction

The final sentence asserts that the scalar-power regime “returns an ordinary
similarity inflation after finitely many levels.” The weaker transported-shape
condition does not supply dissections for extra transported congruence species
and does not supply actual recursive iterability. Thus only the MATRIX has
a scalar power. An ordinary scalar substitution follows if an actual compatible
hierarchy is independently supplied, as in the stronger equivariant theorem;
it does not follow from the current hypotheses. Remove that conclusion or
state the additional hypothesis. This objection does not invalidate the core
matrix/commutation and periodic escape alternatives.

No computation is used. Review tests were analytic and address all spectral
cases of invertible real 2 by 2 matrices.

## Resolution and rereview

The repaired final sentence identifies only a scalar-power matrix exception
and explicitly requires independent actual iterability before inferring an
ordinary similarity substitution. It states why extra transported species
may have no rules. This resolves the objection; no unresolved findings remain.
