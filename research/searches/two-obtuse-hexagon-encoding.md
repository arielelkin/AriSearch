# Exact formulation: two obtuse hexagons as a matching-rule compiler

**Status:** general mechanism remains open; the full Walton one-block
transcription is falsified. No surviving exact two-hexagon pair is selected.

For type \(t\in\{0,1\}\) and slot \(i\in\mathbb Z/6\mathbb Z\), introduce
side lengths \(\ell_{t,i}>0\) and angles
\(\alpha_{t,i}\in(\pi/2,\pi)\).  Put
\(\beta_{t,i}=\pi-\alpha_{t,i}\) and
\(\theta_{t,i}=\sum_{j<i}\beta_{t,j}\).  Exact polygon existence is

\[
 \sum_i\beta_{t,i}=2\pi,
 \qquad
 \sum_i\ell_{t,i}e^{\mathrm i\theta_{t,i}}=0.
\]

Positive lengths and positive turns below \(\pi/2\) then give a genuine
strictly convex closed hexagon.  Side compatibility is necessarily equality
of lengths, hence an equivalence relation on the twelve side slots.  At a
vertex, three placed corner slots are geometrically legal exactly when their
incident edge-length classes match cyclically and

\[
 \alpha_p+\alpha_q+\alpha_r=2\pi.
\]

Reflections reverse the ordered endpoint data, so the local language must be
closed under that reversal.  A proposed finite honeycomb rule language is
realizable by this mechanism precisely when these equations have a positive
solution and every unwanted compatible corner triple has angle sum unequal
to \(2\pi\).

For fixed desired triples, their angle equations and the two per-tile sums
define an affine space.  An unwanted triple can be generically excluded near
the regular point only if its sum is not identically \(2\pi\) on that affine
space.  Length equality classes plus the two complex closure equations form
a finite linear feasibility problem after angles are fixed.

## Fast obstructions

* Length matching gives equality cliques, never a directed complementary
  relation.  Endpoint angles must eliminate unwanted self-matches.
* Angle rules cannot distinguish triples with the same multiset of angle
  values.
* If three corners of one hexagon sum to \(2\pi\), the complementary three
  do also because all six sum to \(4\pi\).
* Both reflected local languages are automatically admitted.
* Either resulting hexagon lying in a monohedral Reinhardt family kills the
  pair by monohedral escape.

The Walton–Whittaker incidence transcription and finite compiler searches
are complete: [reconnaissance](walton-encoding-reconnaissance.md) records the
regular-hexagon collapse, and [the one-block obstruction](../lemmas/walton-one-block-obstruction.md)
states the precise excluded class. Reopening this route requires a different
source language, a proved extendible strict sublanguage, or an encoding beyond
the excluded compiler family; repeating the transcription is unnecessary.
