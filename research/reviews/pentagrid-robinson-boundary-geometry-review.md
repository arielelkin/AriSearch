# Fresh hostile audit of forced Robinson boundary geometry

**Reviewer:** pending_reviews, 2026-10-10. The reviewer did not develop either
root-owned geometry producer or either certificate. The reviewer previously
independently checked the source-height/wedge invariant and now audits the
exact geometry with a separately implemented intersection method.

**Verdict: valid** for the complete necessary forced-half and whole-rhomb
completion screens on the two fixed U,V fixtures. No substantive defect or
repair was needed. Neither fixture is excluded. Survivors are boundary data,
not source clusters or plane tilings.

## Exact claim, domain, and source necessity

The [diagonal producer](../searches/pentagrid-robinson-diagonal-boundary.py)
uses the fixed convex b=c=1 U,V pentagons and every positive ordered boundary
word in lengths u=1, l=phi, s=phi-1. There are 625 U and 21,801 V words in
the complete domain. It requires exact five-direction height closure,
nonnegative triangle-pair wedge counts, and open native boundary-corner fans.
For a boundary diagonal direction it counts its unique source unit-axis
pair, imposes q_ij>=d_ij and q_ij=d_ij modulo 2, and constructs the uniquely
forced interior half-triangle. It then checks parent containment and pairwise
interior disjointness of all those halves.

The [completion producer](../searches/pentagrid-robinson-boundary-completion.py)
starts from every surviving diagonal boundary, completes each forced half to
its whole source unit rhomb, and checks pairwise interior disjointness and
absence of native vertices strictly inside another rhomb side. Both exterior
and interior halves of these forced parent rhombs are tested. No claim about
the remaining six or nine whole rhombs or Penrose arrows follows from these
screens.

These are necessary tests for the stated actual edge-to-edge unit rhomb
source, cut along the specified short thin and long fat diagonals. They are
not assertions about arbitrary geometric triangle dissections. A native
boundary diagonal determines one interior triangle: for a counterclockwise
step x to x+D, its unit apex is x+z^(k+2) for D=s*z^k, or x+z^(k+1) for
D=phi*z^k. The unit apex on the left is unique. Its prescribed source mate
is the diagonal-midpoint half-turn, with apex x+(x+D)-apex. Thus the whole
rhomb is forced, including the half outside the convex macro supporting line.

Distinct macro boundary diagonals belong to distinct source rhombs, since
one prescribed source rhomb has just one cut diagonal and the simple convex
boundary cannot repeat it. Consequently overlapping completed parents are
illegal even if the overlap lies wholly outside the macro. A native vertex
strictly inside a side is also impossible in an edge-to-edge plane source:
that side's whole matching neighbor occupies the opposite local half-disk,
leaving no positive-angle sector for a third tile. This prohibition applies
even to a contact that is only a single point between the two tested rhombs.
All orientation-pair counts follow from the already checked triangle wedge
identity. Arbitrary source rotations and reflections are covered by the
fixed source frame and counterclockwise boundary convention.

## Independent exact checker

The [independent checker](verify_pentagrid_robinson_boundary_geometry_independent.py)
imports no producer. It reuses only the reviewer's earlier independent
integer word/height verifier, which itself imports no producer. It reconstructs
all ordered words and derives the height, fans and wedge vector anew, rather
than trusting the diagonal certificate's candidate list. It builds U,V and
each forced triangle/rhomb directly in CyclotomicField(10).

The geometry method differs from the producers' separating-axis tests.
The checker clips each convex polygon successively by the other polygon's
supporting halfplanes, computes the exact intersection shoelace area, and
uses equality of clipped and original area for containment. Positive
intersection area is equivalent to overlap of the interiors of these genuine
convex polygons. The checker first verifies the supporting inequalities
needed for its convex clipping assumptions. Every triangle has its two
native unit edges checked, and every completed rhomb has all four native
unit edges checked.

Cross products are divided by the positive sin(pi/5), so they lie in the
real subfield Q(phi). Their sign is determined exactly from rational
coefficients of a+b*sqrt(5), by sign cases and squared rational comparisons.
No floating embedding or tolerance decides a branch. Strict side-interior
contacts are checked independently using zero cross product and a negative
dot product (w-a) dot (w-b), rather than the producer's edge division ratio.

Every stage count and the complete retained surviving boundary-word sets
are compared, along with all coordinates of the retained first forced
triangle and completed-rhomb witnesses. The first diagonal witness's wedge
and diagonal count vectors are independently checked as well. Words are
compared as sets, so the distinct enumeration order is harmless.

## Complete results and an exact rejected word

| Fixture | All words | Height/fans/nonnegative wedge | Diagonal counts/parity | Forced halves contained | Forced halves disjoint | Full rhombs disjoint | Also no partial source contact |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| U | 625 | 30 | 28 | 28 | 28 | 28 | 28 |
| V | 21,801 | 311 | 191 | 191 | 191 | 191 | 185 |

The independent clipping checker reproduces these counts and both complete
survivor sets exactly. Every remaining U boundary has four forced halves;
every V boundary has seven. Full-rhomb exterior completion rejects no word
by area overlap but rejects exactly six V words by partial source contacts.
Neither parent is excluded.

A compact exact rejection is the V boundary

    (u), (s,s,u,u,u,l), (u), (u,s,l), (l,l).

Among its completed rhombs 1 and 6 in zero-based forced-boundary order,
a native vertex z-1 lies strictly inside the native unit side [0,z^3]. The
identity z-1=(phi-1)*z^3 and 0<phi-1<1 verify the contact exactly. The
independent checker prints this example. It is in the diagonal survivor set
and absent from the completion survivor set. No drawing or near-contact
measurement is used.

## Attacks, repairs, uncertainty, and replay

Attacks checked included using the exterior instead of the interior unit
apex, forgetting the source rhomb's outside half, duplicate completed parents,
allowing an isolated native vertex on a side interior, confusing zero
intersection area with full edge-to-edge compatibility, source reflections,
silent restriction to unordered side counts, assuming a coordinate
serialization supplied the intended physical root, and treating passed
necessary predicates as global source extendability. The fixed field
embedding, signed source frame, exact clipping, complete word enumeration,
and explicit scope address these cases. No defect or mathematical repair
was found. The checker completed the whole stated boundary domain and imported none
of the producers.

No uncertainty remains in these finite necessary geometry screens. The
residual whole-rhomb assembly, arrow rules, whole-plane macro partition,
and forcing by unmarked convex polygons remain independent obligations.
No claim of novelty, priority or aperiodicity was reviewed or is made.

The certificates are
[forced diagonals](../certificates/pentagrid-robinson-diagonal-boundary.json)
and [full-rhomb completion](../certificates/pentagrid-robinson-boundary-completion.json).
The analytic source necessity is preserved in the
[height/Stokes formalization](../lemmas/pentagrid-robinson-source-height-and-stokes.md).
This reviewer-authored formalization still requires its distinct fresh review;
the present review audits the root-owned finite geometry artifacts.

```text
conda run --no-capture-output -n arisearch python research/reviews/verify_pentagrid_robinson_boundary_geometry_independent.py
```

The command completes deterministically without a solver, random seed,
timeout, numerical decision, or producer import. It certifies the complete
stated finite boundary domain, not an unrestricted tiling theorem.
