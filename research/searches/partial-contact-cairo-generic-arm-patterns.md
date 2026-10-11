#209 generic Cairo cross-arm patterns: exact necessary-contact classification

Date2026-10-10. **Status:** complete exact computation; mathematical conditional
filter independently adversarially reviewed VALID; see
[the fresh review](../reviews/partial-contact-cairo-generic-arm-patterns-review.md). This is not
a tiling existence or periodicity classification.

## Question and finite domain

Classify necessary e-seam corner compatibility for two Cairo-angle pentagons
whose four90-to120 arms are internally distinct, using the new two-T switch
invariant. Let native arm slots be0,1,2,3 for each species, corresponding to
a,b,c,d. A cross-arm equality pattern is a partial bijection between the
four slots of the first and second species. Its complete domain has
sum(k=0..4) binom(4,k)^2 k! =209 patterns. No dihedral/swap quotient is used.
A tiling can omit a species, but the reviewed private-arm theorem excludes
any monohedral Cairo tiling with four internally distinct arms. Thus both
species occur in any admitted tiling considered here.

## Exact encoding and generic hypotheses

All arithmetic is K=QQ(sqrt3), with positive w=sqrt3. Eight arm variables
satisfy each species' closure b-c=w(d-a), plus the indicated cross equalities.
The fifth side is e=w*c+d-2*a. Compute the exact nullspace of this linear
system. A linear form vanishes identically precisely when all its nullspace
coordinates vanish. Patterns forcing any extra internal or undeclared cross
arm equality are rejected.

For each surviving pattern, the **generic stratum** additionally excludes:

* every undeclared cross-arm equality;
* equality of any two event sums unless their difference vanishes identically
  on the closure subspace;
* equality of either e with any right-corner event sum;
* equality e_P=e_Q unless this difference vanishes identically.

These are finitely many explicit linear hyperplanes. They are intentionally
not conclusions about exceptional metrics on these hyperplanes. A strictly
positive point exists in every one of the187 remaining closure subspaces.
The open positive cone has full relative dimension: strict positivity is
an open condition on the whole nullspace. A finite union of proper linear
hyperplanes cannot cover this open set. Hence each generic stratum is
nonempty even if the retained positivity witness happens to lie on an
excluded hyperplane. This avoids falsely presenting a nongeneric witness
as a generic numerical fixture.

The exact positive-cone check uses Sage field-backend polyhedra over K.
Each of8 arms and2 e lengths is normalized to be>=1. This is equivalent to
strict positivity because all constraints are homogeneous: scale any
strictly positive solution by the inverse minimum length. Every surviving
pattern yields a retained exact parameter point satisfying these10
inequalities. No pattern is rejected for positivity, so there are no
negative LP answers needing Farkas certificates in the current output.

## Contact filter and theorem represented

Oriented90 slots are(u,r), where u is the perpendicular side length and r
the other native arm. Enumerate all8 slots and all same-u slot pairs,
including a slot paired to a second copy of itself. A paired event has bank
sum r+s. The two-T switch theorem says that an unequal arm match requires
two events with equal sums. Within each identically equal sum class, the
computation permits every pair of bank labels as an arm compatibility.
The strict switch inequalities are deliberately omitted. This is a safe
overapproximation: it may keep false local contacts but cannot reject an
actual tiling. Compatibility is a direct finite relation, not its transitive
closure.

The generic hypotheses make every e side unsplit and whole paired to an
e side. E sides can cross species only when e_P=e_Q is an identity. For
H/G with equal e, test both endpoint identifications. Preserving endpoint
labels gives exposed pairs(d_H,d_G),(a_H,a_G); reversing gives
(d_H,a_G),(a_H,d_G). Each endpoint must permit some isolated120 corner
(b,c) from either species with both rays compatible, in either order.
An e-adjacent corner cannot be the third tile because its e would face an
arm, and e has no T under the generic hypothesis.

If either species has no possible e seam under this overapproximation,
that species cannot occur; its absence is excluded by the monohedral
private-arm theorem. Therefore every generic metric in that pattern is
untileable. Passing both species' tests is only local necessary feasibility,
never plane extension.

**Complete outcome:**22 patterns force extra arm equalities;147 remaining
patterns have this generic beta obstruction;40 are local necessary
survivors. There are8 survivor patterns with2 cross-arm equalities and32
with3. The contact test by itself makes no tilability conclusion for those40.
The later exact symmetry/subset audit maps32 of40 into two independently
constructed sufficient periodic cones, as recorded below. The retained JSON lists
every pattern, nullspace dimension, exact positive point, quotient arm/e
forms, permitted e seam cases and final status. The22 equality rejects,
147 necessary obstructions and40 survivors exhaust209.

## Reproducibility

[Producer](partial-contact-cairo-generic-arm-patterns.py),
[retained output](../certificates/partial-contact-cairo-generic-arm-patterns.json).
Exact deterministic Sage10.9/Python3.12.13 computation, no SAT/SMT,
randomness, timeout, numerical tolerance or truncated enumeration.
Replay is nondestructive:

    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-generic-arm-patterns.py

Explicit output production:

    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-generic-arm-patterns.py --output research/certificates/partial-contact-cairo-generic-arm-patterns.json

Completed output counts:

    forced-extra-arm-equality22; generic-beta-obstruction147; local-survivor40.

Dependencies: independently reviewed
[private-arm theorem](../lemmas/partial-contact-cairo-private-arms.md), and
[two-T switch invariant](../lemmas/partial-contact-cairo-two-t-switch.md).
The two-T invariant's root hostile review is separate. This finite producer and conditional classification passed the separately
retained independent audit, with all209 patterns and187 exact positive
fixtures reconstructed.
No literature priority claim is made.

## Periodic-survivor synthesis and exact remaining gaps

One k=2 survivor matching P0=Q2,P2=Q0 has already produced a changed periodic
four-face fixture with actual partial contacts, retained separately in
[partial-contact-cairo-swapped-arms-periodic.py](partial-contact-cairo-swapped-arms-periodic.py).
The full4D positive metric-cone coverage proof is now retained in the
[swapped-arm theorem](../lemmas/partial-contact-cairo-swapped-arms-periodic.md).
All8 k=2 survivors are exactly the two reflection/species-swap orbits of
{(0,2),(2,0)} and{(1,3),(2,0)}. The latter maps to the already reviewed Y
criterion after native normalization P_Y=(b,c,d,e,a). 24 of32 k=3 survivors
contain one of these8 subsets;8 do not. The producer verifies every subset/map and
retains the sufficient pattern and family. Hence the two global cone proofs,
not local feasibility, give periodic existence for32 survivors.8 additional
k=3 survivors form one five-label-path orbit and are excluded by native-slot
anchoring below. The
[scoped generic dichotomy](../lemmas/partial-contact-cairo-generic-periodic-dichotomy.md)
is internally proved; the209 computation and new full-cone theorem still
require independent audit.

The209 conditional classification does not cover arm repetitions inside a
species, or extra event-sum/e hyperplane collisions, and does not classify
exceptional non-generic metrics' infinite extensions. These are explicit remaining strata.

## Stronger actual native-slot anchoring

For each actual arm slot i its perpendicular seam at90 must match the
other arm of that same native90 corner. Its possible event sums are
S_i={arm_i+arm_j:other_i=other_j}. A ray opposing unequal original slots
i,j requires S_i intersection S_j, not an arbitrary equal-sum group containing
the same bank labels. Dropping strict offset inequalities is still a safe
overapproximation, but original slot anchoring is mandatory. No transitive
closure is used. Repeating the same e endpoint tests with this relation
yields22 forced extra equalities,155 generic obstructions and32 survivors.
Every final32 survivor has one of the8 sufficient periodic subsets.

The producer preserves old status/allowed_e_seams fields147/40 and adds
anchored_status/anchored_allowed_e_seams/anchored_slot_compatibility fields
155/32. Each positive pattern retains an actual8-arm/2-e witness as well
as its nullspace parameter point. The open-cone hyperplane argument above
certifies generic strata without pretending these specific witnesses
avoid every excluded equality.

The independent root checker
[verify_cairo_generic_arm_patterns_independent.py](../reviews/verify_cairo_generic_arm_patterns_independent.py)
uses a different reduced label basis, without author imports, and returns
155/32 with all32 sufficient-cone maps. Its old147/40 comparison also passes.
The new swapped-arm cone has a separate author-independent review in progress.
These are the final strongest counts; they do not overwrite the narrower
unanchored output semantics.
