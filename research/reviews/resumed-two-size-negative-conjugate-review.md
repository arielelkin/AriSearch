# Independent hostile review: two-size count and U metric obstruction

Date:2026-10-13. Verdict: **VALID** for the unconditional count reduction
and all94 U substitution exclusions. Monohedral periodicity and U
nonmonohedral assertions are **conditional on the cited external complete
pentagon classification**, not newly proved here. Reviewer did not develop
the reduction or metric argument.

Reviewed [artifact](../searches/resumed-two-size-negative-conjugate.md).

## Count reduction

Normalize the smaller pentagon area to1. A nontrivial first parent
partition needs at least six genuine convex pentagon children, hence area
at least6; irrational mu<6 forces one child. This is the larger prototile
B and makes B congruent to lambda A. The second image mu A has at least
six children because it cannot have one child of either available area.
Thus mu²=b+d mu with integers b>0,d>=0,b+d>=6. Irrationality excludes
b=0, and its positive root satisfies mu<6 exactly when b+6d<36.

I independently enumerated b first from1 through35, then d from0 through5,
retaining b+d>=6 and b+6d<36, and excluding square discriminants. Results:
105 integer pairs,94 irrational pairs,67 with d>0. This is a different
loop/filter order from the recorded command. The domain is analytically
bounded, so there is no cutoff extrapolation.

For d=0 the second rule is exactly a monohedral dissection of mu A into
bA copies. Iteration supplies growing convex parent regions with growing
inradii, and standard fixed-tile compactness produces an A-only plane
tiling. The additional PERIODIC monohedral consequence requires the external
classification; it is not proved by this compactness argument alone.

## Quartic field attack

Let E=Q(mu) and F=Q(lambda), with lambda²=mu and mu'<0.
Both embeddings of E have real image. If mu were a square in E, its
negative conjugate would be a square of a real number, impossible. Thus
[F:E]=2 and [F:Q]=4. The displayed quartic t⁴-dt²-b is its minimal
polynomial. Its roots comprise two real and two nonreal roots. Since
F is contained inR, it cannot contain all conjugates and is not Galois.

The uniqueness-of-quadratic-subfield claim is correct: two DISTINCT
quadratic subfields would generate a degree4 biquadratic Galois extension
inside the degree4 field F, forcing equality and contradicting its mixed
signature. This handles d=0 as well; no assumption d>0 entered the argument.

For K=Q(sqrt5), if K is not contained in F then adjoining sqrt5 to F
has degree2. The tower law gives[K(lambda):K]=4. An actual boundary
identity lambda²=a+lambda c with a,c inK would instead put lambda at
degree at most2 overK, contradiction. Hence K is contained inF and is
its unique quadratic subfield E. Then lambda is not inK, and the identity
forces c=0. This field argument does not assume disjointness of arbitrary
extensions or Galoisness of F, and no invalid positivity under a complex
embedding is used.

## Parent boundary attack

Every child is contained in the convex parent. A native child side lying
on a parent's supporting line therefore lies entirely on that parent
side; its endpoint cannot continue beyond a genuine parent corner. More
explicitly, placing a genuine parent corner in the relative interior of
an incident child side would put the child's local180-degree sector inside
a strictly smaller parent wedge, impossible. Local finite subdivision of
the parent boundary is thus a concatenation of COMPLETE native child sides.
A supporting boundary side cannot merely cut through a child interior.
Partial interior seams, reflected placements and arbitrary T-junctions do
not alter this boundary fact. Applying it to a short side of mu A gives
mu=m+n phi³+lambda(u+v phi³), with all four counts nonnegative integers.
No fixed slope, contact graph, chirality or edge-to-edge tiling assumption
has entered this step.

With c=0, positivity of1 andphi³ forces u=v=0. Hence mu=m+n phi³.
Since4<phi³<5 and mu<6, irrationality leaves only n=1,m=0 or1.
The first gives mu²=4mu+1, so(b,d)=(1,4) and only five children.
The second has positive conjugate3-sqrt5 and contradicts the earlier
negative-conjugate reduction. All94 pairs are therefore excluded without
using any monohedral classification or placement enumeration.

I independently checked the exact U vector closure, strict convexity and
phi³ polynomial using QQbar.zeta(10) and real algebraic arithmetic. The
original side directions give the stated after-side angle convention.
The definition isolating z with Im(z)>0 and .8<Re(z)<.81 selects the
correct cyclotomic root. No ambiguity in phi=z+z^-1 survives.

## Checks, repair and scope

Independent integer reconstruction and exact Sage algebraic checks both
passed. They are supporting checks; the field and boundary proof is analytic.

The original heading 'exact nonmonohedral shape' needed qualification:
nonmonohedral U and periodicity of a monohedrally tileable pentagon depend
on the externally imported complete classification, whose local filter is
explicitly conditional. The author qualified those headings, the specific U assertion and the
assumption ledger. I independently reread the amended text: its d=0 periodic
consequence and U nonmonohedral claim are now explicitly conditional, while
the94-case exclusion is unaffected and unconditional under the reviewed
six-child dissection theorem and explicitly supplied U geometry.

No counterexample or unresolved defect found in count/domain completeness,
quartic irreducibility, unique quadratic subfield, tower law, boundary
concatenation, side-count positivity or the final two arithmetic possibilities.
This does not exclude other base pentagons or all negative-conjugate
hierarchies, and gives no aperiodic pair or unrestricted impossibility theorem.

## Independent rereview of the scope repair

The amended headings no longer describe nonmonohedral U as unconditional.
The body explicitly distinguishes monohedral existence from conditional
periodic classification, and explicitly states the94 exclusion uses none
of that classification. Scope repair verdict: **VALID**. No proof step in
the unconditional count/metric exclusion changed.
