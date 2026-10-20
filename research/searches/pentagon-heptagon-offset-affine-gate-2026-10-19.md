# Offset-uniform affine contact gate: pairwise relaxation fails

Status: exact scoped falsification; [independent Sol hostile review](../reviews/pentagon-heptagon-offset-affine-sol-review-2026-10-19.md) passed.
This gate concerns the fixed unit-incircle P/Q metric of the first-gate
certificate, not arbitrary pentagon/heptagon pairs. It gives no plane
existence or mixed nontilability result.

## Declaration before computation

Use zero initial tile charge and conservative contact transfers. For every
ordered native-side pair, relative chirality, and native endpoint ordering,
allow the rational ansatz

    f(t) = a + b*t + c*h(t),
    h(t) = min(L,t+M)-max(0,t).

Coefficients are rational, degree at most one on each endpoint-order cell;
no radius beyond two contacting tiles and no additional corner charge.
The two receivers must assign opposite values to a shared contact. Seek
net incoming charge at least 1 on every tile over the product relaxation
of its pairwise contact domains, requiring covered native sides. A unit
lower bound is harmless under rational rescaling of any strict uniform
surplus. This is a sufficient but deliberately strong certification gate.
Its failure does not exclude rules using jointly realizable corner states.

## Complete pairwise domain

For X,Y in {P,Q}, every native side i,j, both relative determinants,
and both endpoint orders, place X side on [0,L] with interior above the
line and Y side on [t,t+M] with interior below. Retain native endpoint
labels, so reflection never silently identifies opposite corner labels.
Positive-length contact has exactly -M<t<L. Split at 0 and L-M, retaining
the singleton equality cases and all nonempty open cells. Equivalently
partition all comparisons among 0,L,t,t+M. The outer values -M,L are
excluded point contacts; this declared ansatz assigns them zero transfer
separately, without requiring the positive-length formula's one-sided
limits to vanish.

This covers proper staggering, containment, equal endpoints and identical
segments, including reflections. Convexity supplies the proof: every
positive-length intersection of disjoint convex polygon interiors lies on
a common supporting side line, the interiors occupy opposite half-planes,
and the remaining isometry freedom is this tangential translation. See
the previously reviewed corner-transport blocker for the complete argument.
Since h is affine on every cell, all candidate inequalities are affine
there. Universal nonstrict inequalities can be checked at cell endpoint
limits and at equality cells. No finite sampling of sliding offsets is
being substituted for this continuum domain.

## Cheap exact falsification

For each native side choose the contacting tile to be a copy of the same
species reflected across that very side, with identical endpoint labels
at the same positions. This is an allowed two-tile contact, t=0, M=L,
h=L. The pair of tiles is interchanged by the reflection across their seam.
The rooted contact data (including relative determinant -1 and native
labels) are unchanged on exchanging the two tiles and applying that
reflection. Any isometry-equivariant conservative scalar transfer therefore
satisfies f(0)=-f(0), hence f(0)=0. In the declared ansatz this is the exact
linear equality a+c*L=0. It is independent of the value of b and does not
require rounding any algebraic length.

Assign this contact independently on every side of P, and separately on
every side of Q. Each whole side is covered, so these are states of the
product pairwise relaxation. Each tile has net incoming charge exactly 0.
Its required inequality is 0>=1. This single exact equality-cell witness
falsifies universal feasibility across the complete interval domains;
there is no need to enumerate or optimize coefficients on other cells.
The adjacent deterministic verifier checks the rational involution and
this zero-row contradiction for five and seven sides.

These are formal independent-side states, NOT geometric coronas. In
particular two 115-degree P corners at a reflected side endpoint leave
130 degrees, which cannot be filled by the complete angular palette.
Consequently this witness is not a tiling, not a stationary geometric
measure, and not a failure of all offset-uniform discharging rules.

## Boundary-versus-area obligation and stop

If a conservative local flux were bounded, every tile had positive uniform
surplus, and valid plane tilings induced the tested joint states, summing
over tiles contained in a radius-R disk would leave O(R) uncancelled
transfers while demanding Theta(R^2) surplus. Congruent compact tiles of
positive area bound the number of tiles in a fixed-width annulus by O(R).
The number of neighbors is uniformly bounded: any contacting neighbor lies
in a fixed-radius disk and their disjoint positive-area interiors give a
packing bound. Thus bounded flux gives the required boundary estimate.

The declared product relaxation fails its positive-surplus inequality.
Removing its explicit spurious reflected-side states requires a specified
joint angular/contact domain or an independently proved sound stronger
relaxation. Those constraints were not supplied by the complete two-tile
schema. No mixed nontilability contradiction is established. Stop this
ansatz here; no degree, radius, metric or patch-size escalation is claimed.
A material reopening would give explicit simultaneous corner-completion
and side-partition constraints and a concrete revised conservative charge
formula. Simply solving a larger pairwise LP cannot remove this witness.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/pentagon-heptagon-offset-affine-gate-2026-10-19.py
