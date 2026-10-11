# Full exact metric cone for the four-shared-length(5,7) family

**Question.** Determine the entire positive metric deformation cone of the
retained two-H/two-P lattice gluing, and whether unrestricted local geometry
forces its metric ordering for distinct-side-length pairs.

**Result.** A four-dimensional homogeneous cone with eight irredundant
positive inequalities and nine closure rays, parametrized by
(a,b,c,d)=(H1,H2,H4,H6). All metrics in the cone tile by the same twelve
seam-pair torus. At pairwise distinct union lengths every tiling is exactly
that periodic source. A fresh local reduction places every tileable
H/P pair with distinct lengths on each polygon and exactly four shared
length values in this cone, up to dihedral renumbering. Three or fewer
shared values are untileable. A separate analytic midpoint-chain theorem
forces a nonzero period also with five shared values, excluding every
internally distinct-side pair in this angular family. Repeated lengths
remain outside the result.

**Exact finite computation.** Q(t), t^3-t^2-2t+1=0 with
18/10<t<181/100, for the eight homogeneous coefficient rows. Enumerate
all 56 triples of active rows, solve kernels exactly, retain nine feasible
rays, and verify each facet's three-dimensional span and relative-interior
witness. A generic rational parameter quadruple gives eight positive
and distinct union lengths. Universal seam, vertex-link and area identities
are checked formally in Q(zeta28)[a,b,c,d], with twelve seam pairs and eight
three-corner links. No parameter grid, torus-bound increase, stochastic seed,
LP/polyhedron backend, float decision, or solver extrapolation is used.

**Artifacts.** `research/lemmas/two-angle-5-7-metric-continuum.md`,
`research/searches/two-angle-5-7-metric-continuum.py`, and
`research/certificates/two-angle-5-7-metric-continuum.json`.
The default producer prints JSON nondestructively; --output deliberately
writes a named certificate.

```text
conda run --no-capture-output -n arisearch python research/searches/two-angle-5-7-metric-continuum.py
```

The complete replay passed in the arisearch environment, using exact Sage
number fields and polynomial rings. No configured resource limit, timeout
or incomplete result occurred. The global theorem uses the exact side/link
identities to obtain a degree-one flat-torus covering, and the local rigidity
proof uses actual unmarked edge-length equality. Fresh hostile review is
requested; no claim about the original unrestricted aperiodic-pair problem
is made.
