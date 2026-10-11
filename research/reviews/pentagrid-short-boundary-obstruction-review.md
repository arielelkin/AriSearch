# Fresh review of the pure-phi boundary obstruction

Reviewed 2026-10-10 by an agent who did not develop the exact metric family
or this boundary-corner argument.

**Verdict: valid.** For the b=c=1 area-compatible U/V pair, no parent
(m*phi)U, with positive integer m, can be finitely partitioned into whole
U/V copies, including reflections and arbitrary interior partial contacts.
The derived necessary lower bound lambda>=phi^3 for a general real
homothetic U-parent subdivision is also valid. No subdivision is asserted
to exist at phi^3 or at any larger scale.

Reviewed theorem:
[short boundary obstruction](../lemmas/pentagrid-golden-metric-short-boundary-obstruction.md).
This review also checks the lower-bound derivation communicated by root:
the side alphabet has nonnegative coefficients in (1,phi), q=1 is
impossible, q=0 would be a forbidden U-only reptile, and p=0 is excluded
by the pure-phi boundary theorem. The exact area-compatible geometry has
its [separate valid audit](pentagrid-area-compatible-family-review.md).

## Whole sides and exact coefficient sums

The supporting-line proof of whole child sides on a genuine convex
parent's boundary is valid, including internal partial seams. It is
independently detailed in
[the generic metric review](pentagrid-generic-metric-substitution-review.md).
The four numerical child-side lengths are

    1, 2phi, 1+2phi, 1+3phi.

Each has a nonnegative integer coefficient pair in (1,phi). A parent
short side has length m*phi. Uniqueness of rational coefficients in this
basis forces the sum of its constant coefficients to be zero. Therefore
every child side in that boundary word has length2phi. There are exactly
m/2 of them; odd m is impossible without any geometric search.

## Terminal-corner attacks

For even m, choose a144-degree U parent corner between two of its short
sides. The terminal complete edge on each parent side is a V side of
length2phi. Such an edge has endpoint angles108 and144, because V's
two2phi edges are sides3 and4 in after-side conventions. They meet each
other at the unique108-degree V corner. No endpoint of either is72.

A child containing this genuine parent corner must have a native corner
there: a straight child sector would have angle180 and could not fit in
the parent144 aperture. The boundary terminal-edge endpoints are thus
actual child corners, not interior points of their sides. This remains
true even if other children meet the same parent corner.

If the two terminal edges belong to different children, their two sectors
at that point already total at least108+108=216 degrees. Their interiors
must be disjoint inside the144 parent aperture, so this is impossible.
Additional corner pieces only worsen the inequality.

If they belong to the same child, they lie on the two distinct parent
boundary rays and are that child's two adjacent native edges at this
corner. They cannot be nonadjacent sides meeting at a point of a genuine
convex pentagon, or the same straight native side on two different rays.
The only adjacent2phi edges of V meet at108 degrees. A rotated or reflected
child preserves that angle, whereas the two fixed parent rays bound
144 degrees. Thus the same-child alternative is impossible as well.

These cases exhaust the two terminal boundary edges. Partial contacts
inside the parent do not change which complete edges end at its corner.
No edge-to-edge hypothesis is used.

## Lower bound for every possible scale of this fixed pair

Suppose lambda U has a finite U/V subdivision for any real lambda>1.
A unit parent side is a sum of complete child sides from the above
alphabet, so

    lambda=p+q*phi, with p,q nonnegative integers.

Every child-side phi coefficient is0,2,or3, so q=1 cannot occur. If q=0,
lambda is an integer, hence lambda^2 is an integer and area conservation
forces an all-U subdivision. Iteration and compactness would produce a
monohedral U tiling, contradicting the explicitly imported reviewed Rao
exclusion. If p=0, lambda=q*phi is excluded by the terminal-corner theorem.

Thus p>=1 and q>=2, giving lambda>=1+2phi=phi^3. At that boundary scale,
area conservation requires5U+8V for the U parent and8U+13V for the V
parent, totals13 and21. The count and boundary tests are necessary only;
they supply no actual placements, extension, or hierarchy. The equality
case remains a geometric question.

The proposed2phi scale has parent counts4U+4V and4U+8V. These exact area
counts do not overcome its boundary-corner contradiction. The proposal
is excluded before any placement solver is needed.

No substantive defect or repair was found. The obstruction and scale
bound are analytic integer-coefficient and corner-sector arguments; no
bounded search, numerical threshold, finite-orientation convention, or
unproved universal substitution principle supports them. Arbitrary plane
tilings of this pair remain a separate unresolved problem.
