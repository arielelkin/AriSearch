# Independent hostile review: iterable affine substitution obstruction

Date: 2026-10-13. Reviewer: contact_structure, independent of author.
Artifact: [theorem](../lemmas/affine-two-convex-iterable-obstruction.md).
Verdict: VALID under its explicit equivariant-iterability hypothesis. The
minor orientation wording clarification requested below has been applied.

## Attacks and checks

1. **Orientation hypothesis.** The condition M^n R M^(-n) orthogonal is
assumed for dissection placements, not purported to follow from arbitrary
self-affine substitution. I attempted to use orientation-dependent child
replacement or polygon symmetry to refute necessity. Such constructions are
expressly outside the theorem; they do not refute this conditional result.
The condition is sufficient: transporting the replacement of RQ by M^n
produces child orthogonal part (M^n R M^(-n)) times a base orthogonal part,
which remains orthogonal. Products therefore remain congruent children.

2. **Finite orientation group.** The orthogonality equation for M R M^(-1)
is exactly R^T(M^T M)R=M^T M. A nonsimilarity has two distinct singular
values, so its symmetric matrix has two distinct eigenlines and its
orthogonal centralizer consists of four sign matrices. Products and inverses
preserve all conjugation conditions; H is a group. Conjugation maps H into
itself, and injectivity plus finiteness makes this a permutation. No
orientation closure assumption is missing.

3. **Boundary directions and partial seams.** Finitely many children cover
a parent side. Away from their finitely many vertices, coverage forces a
child side segment on that boundary line. Internal seams or partial side
contacts cannot replace the parent boundary by an unsupported direction.
Consequently M D0 is contained in H D0. Conjugation invariance of H then
makes M D a subset of D. An invertible projective map on a finite set is
bijective, so every side direction has a periodic projective orbit.

4. **Real spectrum cases.** For distinct eigenvalue moduli a periodic
non-eigenline would imply (lambda1/lambda2)^k=1, which is impossible.
Opposite-sign eigenvalues cause no exception unless moduli are equal.
A nontrivial Jordan block accumulates shear and has only one periodic
projective line; one side direction cannot enclose positive area.
A diagonalizable repeated real eigenvalue is scalar and hence a similarity,
already outside the hypothesis. Equal opposite eigenvalues square to a
positive scalar even for a nonorthogonal eigenbasis.

5. **Complex spectrum and finite order.** Real conjugacy to a scaled
rotation preserves projective periodicity. A periodic line forces k theta
in pi Z; thus M^k is a nonzero real scalar. Conversely irrational theta
has no finite projective orbit. The sample M=((0,-2),(1,0)) has eigenvalue
moduli sqrt(2)>1, is nonsimilar, and squares to -2I, so it correctly blocks
any attempted unrestricted anisotropic conclusion. Iterating k times is
valid by the explicit hypothesis and yields finitely many isometric children.

6. **Quantifiers and endpoint.** The proof applies to any finite collection,
not merely two shapes. The parallelogram conclusion gives an admitted
monohedral periodic tiling under the target convention, which allows a
species to be omitted. It excludes only the specified substitution mechanism,
not arbitrary plane tilings or hierarchies.

## Minor requested clarification

The phrase “ordinary scalar inflation, possibly orientation reversing at the
first power” can be read as claiming a scalar map reverses orientation.
Every nonzero real scalar matrix in dimension two has positive determinant;
a negative scalar adds a half-turn. The first map M can reverse orientation
in the equal-opposite-real-eigenvalue case, but its scalar power cannot.
Suggested replacement: “ordinary similarity inflation (a negative scalar
includes a half-turn).” This wording issue does not affect the theorem proof.

No proof-relevant computation or unretained counterexample is used.

## Resolution

The author replaced the ambiguous scalar orientation clause. Scalar powers
are similarities, negative scalars include a half-turn, and the original M
may itself reverse orientation. No unresolved objection remains.
