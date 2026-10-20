# Method 3 external incidence: deterministic-continuation gate

Status: independently Sol-reviewed exact local ambiguity certificate; global chiral extension unresolved.
[Hostile review](../reviews/sugimoto-method3-external-incidence-sol-review-2026-10-19.md).
Date: 2026-10-19. No candidate pair or holonomy theorem is claimed.

## Scope

The coordinate and dissection definitions are those of
`../searches/sugimoto-method3-two-class-first-gate-2026-10-19.md`.
The primary source is Sugimoto, [arXiv:2404.00534v5](https://arxiv.org/html/2404.00534v5),
Section 2.2, Figures 15–17. It specifies a parent dissection and illustrates
one tiling. The audited coordinate fixture does not specify an exact
extendible parent-collar language. A picture alone is not such a certificate.

This note distinguishes a necessary local continuation from a continuation
known to occur in a genuine infinite chiral parent tiling. It establishes
ambiguity for the former. It does not establish ambiguity for the latter.

## Complete single-parent corner possibilities

Write d_i for the outgoing edge direction at X_i, with the 14-entry direction
word in the fixture. The parent interior angles at X1,...,X14 are

`270,120,90,120,270,120,90,240,90,240,90,120,180,120`.

At either X8 or X10, the missing 120-degree sector must be supplied by one
external parent: every nonstraight parent angle is at least 90 degrees,
so two parents cannot divide that sector. Its corner can locally be any of
X2, X4, X6, X12, X14. These correspond, respectively, to external children
A, A, B, D, H. All five alternatives have disjoint interiors from the seed
parent. Thus local geometry does not select even the child species.

At X1 or X5, the missing 90-degree sector similarly belongs to one parent,
whose corner can locally be any of X3, X7, X9, X11. The external child is
respectively A, B, C, D. All four alternatives are locally nonoverlapping.
The latter three are congruent as shapes but occupy distinct placements
and carry different surrounding parent incidences.

For each seed corner i and inserted parent corner j in these lists, the
unique orientation-preserving insertion is

`g_ij(x) = Rot(theta_ij) x + X_i - Rot(theta_ij) X_j`,
`theta_ij = d_(i-1) + 180 - d_j (mod 360)`.

Indices are cyclic. This specifies every alternative exactly in Q(sqrt(3)).
The rotations for X8, in the listed order, are 30,240,270,60,0 degrees;
for X10 they are 60,270,300,90,30 degrees. For X1 they are
120,0,330,300 degrees; for X5 they are 240,120,90,60 degrees.
No reflected parent was used in these 18 alternatives.

## Exact independent geometric check

The retained verifier is
`../searches/sugimoto-method3-external-incidence-gate-2026-10-19.py`.
It imports the exact audited t=3/5 fixture, places the whole external parent
for every listed corner, checks both sector rays, and certifies disjoint
interiors for all 25 pairs of convex children using exact separating axes.
Together the children cover their parents by the imported fixture audit.
This proves parent nonoverlap without a floating-point area tolerance.
Parent geometry is independent of t; therefore the parent-placement result
holds for every 0<t<1. The verifier uses t=3/5 merely as a convenient convex
decomposition of that fixed parent.

Replay from the repository root:

```text
mise exec -- conda run --no-capture-output -n arisearch python research/searches/sugimoto-method3-external-incidence-gate-2026-10-19.py
```

This is a finite analytic corner domain, not a growing patch census.

## Stop and exact missing gate

No deterministic transition or holonomy can be inferred from Method 3's
single-parent incidence: already its first external step has the alternatives
above. Which alternatives extend to a genuine infinite chiral source tiling
is not certified here. In particular, local parent nonoverlap is insufficient
to assert global extendibility. The present task stops at this ambiguity;
it does not turn local alternatives into fictitious source tilings.

Reopening requires an exact chiral source substitution/collar certificate
that selects the allowed ordered parent contacts at these four notches,
including any context needed to distinguish them, or a proof that every
locally admissible alternative is extendible. Only after that gate could a
finite-state saturation transition and its translation holonomy be defined.
An unbounded collar expansion without a proved finite-state reduction would
not fill this gap.

## Escape audit

No finite convex fusion cluster or two-class palette was obtained, so there
is no new monohedral or two-class candidate to audit. Any eventual deterministic
translation-equivariant fusion rule defined on the reflected periodic parent
tiling inherits a nonzero period after transport, as proved in the prior
first-gate artifact. To evade that obstruction, a concrete rule must fail on
that periodic parent source and still be forced by the final unmarked child
shapes. These 18 proper-rotation local placements do not supply either fact.
The existing parent-contained obstruction and unrestricted reflection escape
therefore remain in force.
