# Fresh hostile review: saturated five-plus-one B field with A012012

Date:2026-10-13. Independent reviewer:sol, distinct from terra author.
**Verdict: VALID** for the conditional actual-saturated-field row lift and
its periodic-escape corollary using the independently reviewed saturation
reduction. This closes A012012 on the stated5+1 B line, not the other eight
remaining saturated A words or the general problem.

## Dependencies and angle scope

Input is an ACTUAL connected defect-free mixed field, in the exact four-star
language AAAxyz,AABxxr,AAByys,ABBzrr with every B having two B neighbours.
The parameter interval112.5<x<126,x!=120 gives genuine distinct angles and
positive fixed polygon shapes. The capacity reduction's uniform deficiency
O(R)/clean saturation limit has a fresh VALID review by luna and was checked
for applicability here, not repeatedly re-audited. Its pureA alternative
already gives a monohedral escape; pureB would need forbiddenBBB. Thus the
conditional result suffices for arbitrary original partial-contact tilings.

The existing AAA=>centrality lemma for A012012 uses only A's closure kernel,
one corner of each colour and positive exterior turns summing180, not the
old two-of-each B counts. It therefore applies unchanged to this four-star
family. If A is central there is an immediate omission escape. If not, AAA
is impossible, and each opposite length difference is nonzero; in particular
a0!=a3. No nongeneric line outside the stated interval is inferred covered.

## Private edges and global row alignment

Of the three saturated B masks, only native{1,4} has AB pair demands present
in A012012; the other masks require22, absent in A's palette. Its AB pairs
are02 and12, so native A01 sides0,3 cannot be AB and are AA. Every A0/A1
vertex, absentAAA, is AAB and has exactly one AA/AB arm; its01 arm is already
AA. Every A2 vertex is ABB and has two AB arms. Thus0,3 are EXACTLY A's
AA sides; no extra A adjacency survives a length specialization.

In the standard triangular cell lattice, these opposite AA flags give each
A two opposite A neighbours. Following a component propagates the same
primitive lattice direction at the next cell, making it a complete bi-infinite
integer line. Any two of the three available primitive directions have
absolute determinant1, so any two differently directed such integer lines
intersect at a cell regardless of their offsets. That cell would need four
A neighbours, contradicting its exact degree2. Hence all A lines are parallel.
After indexing this common directionD0, any row containing one A is whollyA;
all others are whollyB. Two adjacentA rows would increase A degree beyond2;
two adjacentB rows would add two B neighbours to the two within its own row,
violating saturation. All rows therefore alternate globally. This argument
excludes finite B cycles here and supplies the backbone rather than assuming
arbitrary saturated chains align or become periodic.

## Exact B metric symmetry

At B's AAB0 corner, the two A0 corners have native AA arms a0 or a3. Their
matching and a0!=a3 force both to use the same native slot, so their remaining
02 arms have equal length. The special AAB1 corner similarly forces equal
12 arms. Thus B's native length word is(m,p,n,n,q,m), with all lengths positive.
Its first edge direction1 and remaining turnsR=180-r give unit directions
1,E,...,E^5, E=exp(iR),45<R<72. Conjugating closure and multiplying byE^5
reverses the length word. The two BB columnsE,E^4 have determinant sin3R,
nonzero in this interval exceptR=60 (x=120), expressly excluded. Unique real
solutions forcep=q as stated.

An independent simpler check gives the same conclusion directly: subtract
the reversed closure from the original to obtain(p-q)(E-E^4)=0. Since3R lies
in(135,216), E^3!=1, so E!=E^4 andp=q. This uses exact conjugation and real
lengths, not a reflection assumption or numerical trigonometry. It makes no
extension of the entire four-star theorem to x=120. Positivity and convexity
of the B whose metrics are used are actual input assumptions.

## Full native row transitions and canonical metric transfer

I independently derive side maps from the two mapped endpoint indices,
rather than using the producer's direct r-k-1 formula. Among all12 indexed
A placements, AA flags at global sides5,2 mapping to native0,3 leave exactly
four. Full AA native-index equality (forced by a0!=a3) and same-colour endpoint
matching give the two unique two-cycles in the lemma. Therefore each A row's
FULL indexed labels repeat under2D0, with the same common period across all
rows, even if their transverse phases differ. A0/A1 colour equality alone
would not have proved this; the native length distinction is consequential.

Four indexed B row states map global sides5,2 to native1,4. All have common
BB lengthp and r corners at global0,2,3,5. The supplemental checker tests all
16 possible ordered BB state pairs: their side lengths and both endpoint
colours agree regardless of choices. All four A states also have A2 at their
remaining global1,4 corners, so each ABB vertex retains z+2r=360. No hidden
B-B label interaction is left to force a nonperiodic alias pattern.

For each occurring ordered four-A tuple, the actual source field supplies a
nonempty finite set of compatible B states at the FIXED actual A/B metrics.
The tuple repeats under2D0 because all four full A labels do. Choosing one
state per tuple preserves its AB side/endpoint matches and AAB stars. Across
BB seams any independently selected pair remains legal by the commonp/r
checks. Across AA seams the full A two-cycles are retained. Thus the replacement
is a complete native metric-legal field with period2D0. No formal tuple is
assumed to extend; the actual field provides the occurrence and compatibility.

This is a new NATIVE field, not a claim that a different B can be inserted at
the unchanged Euclidean coordinates of the original source. The reviewed
metric-development theorem supplies its actual plane embedding and nonzero
translation, squaring a glide if necessary. It applies to this general
trivalent angle language once whole-side equality and angle sums are valid;
the old one-B species coset is neither assumed nor required.

## Combined original-tiling corollary and replay

An admitted original tiling first supplies the reviewed saturated limit or
pureA escape. In the mixed limit, central A escapes immediately; otherwise
the preceding full-native row lift escapes. Hence every tileable pair with
actual A012012/B5r+1s in the stated angle line admits a periodic tiling,
including original partial contacts, reflections and omission. The argument
does not assert every original tiling is saturated or periodic.

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_terra_five_one_opposite_a_row_lift.py
    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_five_one_row_transfer_independent.py

Both outcomes:PASS. All12 placements/four permittedA/fourB, unique fullA
two-cycles,16BB transfers, exact four-star equations and symbolic closure
reversal. No solver, sample geometry, chain bound, timeout or numerical
acceptance. Global row topology and positivity/trigonometric implications
are proved analytically above, not extrapolated from those finite tests.
The original problem and other surviving five-plus-one native words remain
unresolved.
