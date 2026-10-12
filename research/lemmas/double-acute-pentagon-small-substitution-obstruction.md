# Double-acute pentagons: an angle cross-check for small dissections

Date: 2026-10-12. Status: independently hostile-reviewed VALID; see [fresh review](../reviews/double-acute-pentagon-small-substitution-review.md).

Consider any strictly convex pentagons whose native angle multiset is
{60,60,120,150,150} degrees, with arbitrary lengths, native order and reflections.
A convex pentagon with this angle multiset cannot be dissected into two or three
such pentagons. Consequently any ordinary geometric substitution using only
these shapes, whose inflated parents have that same angle multiset, must use
at least four children in every nontrivial parent image. This is a dissection obstruction,
not a proof against all substitutions or against aperiodic tiling.

This angle-specific argument is weaker than the already reviewed
[general six-piece theorem](pentagrid-golden-metric-small-substitution-obstruction.md),
which excludes all nontrivial convex-pentagon dissections with fewer than
six children. It is retained as an independent angle cross-check, not as
a new enlargement of that existing obstruction.

## Corner inventory

For N children there are 2N native 150-degree corners. A 150-degree parent
corner must contain precisely one child corner of 150 degrees: no sum of
60- and 120-degree corners is 150. No child 150-degree corner can occur at
a parent 60- or 120-degree corner. Nor can it occur at a flat boundary
point, since the remaining 30-degree sector cannot be filled by the
available corner angles (and a child side interior contributes 180).
Thus precisely 2N-2 such corners are interior to the parent.

At an interior point carrying a 150-degree corner, the remaining 210 degrees
can only be another 150 plus a 60. A side-interior contribution of 180 would
leave 30, and all combinations using just 60 and 120 have sum divisible by
60. Therefore these corners occur in exactly N-1 interior junctions, each
formed by three distinct children, with star (150,150,60).

For N=2 this is impossible because there are only two children. For N=3
it requires two interior junctions common to all three children. The next
convexity fact excludes that possibility, independently of side subdivisions.

## Three convex pieces have at most one common interior junction

Suppose three compact convex pieces with disjoint interiors all contain two
distinct points x,y in the interior of the parent. Convexity places their
common segment [x,y] in all three pieces. Choose z in its relative interior.
Each full-dimensional convex piece containing this segment has interior
points arbitrarily close to z on at least one of the two sides of the
supporting line. Two pieces must choose the same side. Their convex hulls
of a small segment around z and respective off-line interior points contain
an overlapping open region near z on that side, contradicting disjoint
interiors. Thus the three pieces cannot share two points. In particular,
they cannot supply the two required (150,150,60) junctions. QED.

This proof allows reflected children, different lengths and partial contacts.
It does not assume edge-to-edge subdivision. No finite solver failure enters
its conclusion. A route based on larger images, multiple parent regions or
non-substitution infinite constructions remains open.


## Conditional inflation-factor consequence

For an ordinary substitution on a finite set of convex pentagons, assume
EVERY parent image contains more than one child and that all use the same
positive similarity ratio lambda>1. The existing general six-piece theorem
gives lambda>=sqrt(6): choose the smallest-area prototile, with area a_min.
Its image has at least six children of area at least a_min, so
lambda^2*a_min>=6*a_min. The weaker angle proof alone would give lambda>=2.

The hypothesis about every image is essential. A parent may instead be
replaced by one differently sized similar prototile; finiteness alone does
not exclude such individual one-child images. No unconditional inflation
bound is asserted for such substitutions. Parent regions differing from
the individual pentagons also lie outside this claim.
