# Fresh hostile review: proper Penrose window exclusion of the Robinson boundaries

**Verdict: VALID in the stated source-compiler scope.** Fresh independent
review completed 2026-10-10. The reviewer did not develop the membership
producer, its certificate, or the source lemma. No substantive defect was
found. This review accepts neither an unrestricted U/V untileability claim
nor an aperiodicity claim.

Reviewed claim:
`research/lemmas/pentagrid-robinson-penrose-window-exclusion.md`.
Producer: `research/searches/pentagrid-robinson-penrose-window.py`.
Certificate: `research/certificates/pentagrid-robinson-penrose-window.json`.
Independent replay:
`research/reviews/verify_pentagrid_robinson_penrose_window_independent.py`.

## The claim actually established

Every one of the 28 U and 185 V surviving mandatory boundary objects is
absent from every proper Penrose rhomb tiling, regular or singular, when
the macros are the specified unions of whole thin/fat Robinson triangles
from a common unit rhomb source. Mandatory whole source rhombs include
the halves outside the macro. This excludes alternate residual fillings
of these same boundary words: their obligatory boundary objects already
fail the membership test. The 28 U and 168 V retained full assemblies give
a separate, weaker confirmation; one retained assembly per word would not
by itself exclude alternate fillings.

Completeness of the upstream necessary boundary-word screens is an
explicit dependency. It was independently checked in
`pentagrid-robinson-height-boundary-review.md` and
`pentagrid-robinson-boundary-geometry-review.md`; residual witness soundness
and the 17 rejected V residual domains were independently checked in
`pentagrid-robinson-residual-rhombs-review.md`. No membership sufficiency,
Penrose-arrow test, global macro extension, or unrestricted plane tiling is
inferred here. Noninteger-intercept generalized Penrose sources and
arbitrary unmarked unit-rhomb sources remain outside the claim.

## Primary-source boundary and singular transfer

The primary article's Section 2.3, Definition 2 selects integer unit
2-facets inside a regular strip E+[0,1]^5. Its subsequent proper-Penrose
specialization imposes an integer coordinate sum on the intercept. The
Introduction gives the common finite-pattern language of proper Penrose
tilings. These statements were inspected directly in the
[Fernique--Lutfalla primary PDF, arXiv:2211.08239v2](https://arxiv.org/pdf/2211.08239v2).

The distinction between proper and generalized sources is essential.
The integer-sum hypothesis supplies the four strict integer layers. A
singular proper tiling is excluded by transferring any alleged finite
unmarked whole-rhomb patch to a regular proper tiling with the same finite
pattern language. A finite boundary object, although it need not fill its
interior, can be extended within the alleged source to a finite rhomb
patch, so that transfer applies. We do not apply the regular strip
selection rule directly to arbitrary singular closed-window selections.
In particular, the zero-margin examples below are not an unqualified
singular-window contradiction.

Regular integer-sum sources exist: in the two-dimensional internal
star-coordinate space, each integer-point facet-boundary condition is a
nontrivial affine line. Avoiding their countable union gives a regular
intercept. The independent facet reconstruction confirms that every
facet has a nonzero star-coordinate normal, so fixing an integer sum does
not make one such condition identically true.

## Lift and isometry audit

Put z=exp(i*pi/5) and rho=z^2. A physical native source edge of direction
+rho^j has lift +e_j, and the opposite direction has lift -e_j. The
independent checker determines these lifts by exact physical field
equality, traverses each complete finite unit-edge graph, and requires
agreement on every repeated vertex. Macro unit steps connect the
mandatory boundary rhombs. All retained graphs are connected. The lift
therefore has only one global integer translation gauge; independently
adding physical-kernel vectors at individual vertices is not allowed.

For the author's z-basis H, the identity
z^i=(-1)^i*rho^(3i) gives

    N_(3i mod 5)=(-1)^i H_i,
    kappa=sum N_j=sum (-1)^i H_i.

The checker constructs N directly and separately verifies this formula
and both physical projections. The physical kernel relation
(1,-1,1,-1,1) in H becomes (1,1,1,1,1) in N, a uniform layer shift by 5.
It cannot repair a layer span.

After aligning one source direction, allowed source-frame rotations act
by a permutation of the rho basis or a uniform negative permutation;
reflections permute it. The corresponding cube is preserved up to a
single integer translation. Thus kappa changes by a sign and a constant,
and the arbitrary internal shift absorbs the window translation. This
covers rotations and reflections of the macros and source together,
without a separate window search for each frame.

## Window and exact rejection audit

The internal coordinates are

    I(N)=(sum N_j,
          sum N_j*cos(4*pi*j/5),
          sum N_j*sin(4*pi*j/5)/sin(pi/5)).

They are independent and annihilate the physical slope, so they are an
invertible coordinate system on its internal quotient; orthonormality is
unnecessary. In Q(sqrt(5)), with phi=(1+sqrt(5))/2, their generator lists
are

    cos:  (1,-phi/2,(phi-1)/2,(phi-1)/2,-phi/2),
    sin:  (0,1,-phi,phi,-1).

The window is the zonotope generated by
(1,cos_j,sin_j). The checker independently reconstructs all 20 support
facets by cross products of pairs of generators, with the support offset
given by the sum of negative generator projections. It verifies exact
positive-proportional agreement with the retained facet list.

For integer intercept sum m, strict strip membership forces
kappa-m in {1,2,3,4}; endpoints 0 and 5 require all cube coordinates to
be 0 or 1 and lie on its boundary. Thus the only possible integer m are

    max(kappa)-4 <= m <= min(kappa)-1.

Every survivor has span 3, so only one m remains. For each vertex and
facet the independent reconstruction gives an inequality
C-ha*A-ht*T>0. A common positive margin is equivalent to these finitely
many strict inequalities. The author's margin cap at 1 does not alter
whether any positive margin exists.

The checker does not import the producer, a polyhedron backend, or an LP
solver. It clips the shifted-window inequalities exactly in Q(sqrt(5)).
The initial rectangle [-phi,phi] by [-phi^2,phi^2] follows from requiring
the rooted height-zero vertex in the window; it is a proved bound, not a
search bound. Clipping handles empty, segment, and point intersections.
Because all star normals are nonzero, strict feasibility would give a
positive-area intersection. Every candidate has zero area or is empty.

It also checks all 21 selected-row Farkas obstructions: each selected row
must occur in the independently derived constraints; weights are
nonnegative and not all zero; their weighted star normals vanish; and
the weighted constants are nonpositive. These conditions contradict
simultaneous strict inequalities. A zero constant proves only lack of
strict acceptance. The separate clipping calculation verifies the
certificate's stronger closed-empty classifications, while explicit
reported shifts independently verify the boundary-feasible cases.

## Independent exact results

| Object domain | Count | Layer spans | Four-layer passes | Closed-empty among passes | Closed-boundary among passes | Strict passes |
| --- | ---: | --- | ---: | ---: | ---: | ---: |
| Full U | 28 | 3:3,4:19,5:6 | 3 | 2 | 1 | 0 |
| Full V | 168 | 3:6,4:27,5:33,6:39,7:42,10:21 | 6 | 6 | 0 | 0 |
| Mandatory U boundaries | 28 | 3:4,4:20,5:4 | 4 | 2 | 2 | 0 |
| Mandatory V boundaries | 185 | 3:8,4:32,5:44,6:36,7:42,10:23 | 8 | 8 | 0 | 0 |

The checker reconstructs every object from the prior boundary words and
full rhomb geometry, then compares complete domains, all retained vertex
lifts, and physical coordinates. It confirms the author's first full U
and V layer intervals, [-3,1] and [-4,3], respectively. Completing a
boundary diagonal has the predicted midpoint layer at either apex; all
completion vertices are actually included in the tested graphs.

The full U row 8 has words
(l,u,l),(u,s,l,u),(u),(u),(u), with a closed feasible shift

    m=-4, A=1-sqrt(5)/2, T=(sqrt(5)-1)/2.

Its common margin is zero. The mandatory-only test also has this row and
U row 14 on the closed boundary. The latter has words
(u,l,s,u),(l,u,l),(u),(u),(u), and shift

    m=-2, A=7/4-3*sqrt(5)/4, T=3/2-sqrt(5)/2.

All reported shifts satisfy every closed inequality and at least one is
tight. These cases explain why the proper-Penrose finite-pattern transfer
is a necessary logical step rather than a dispensable numerical detail.

Replay completed successfully:

```text
conda run --no-capture-output -n arisearch python research/reviews/verify_pentagrid_robinson_penrose_window_independent.py
```

The replay imports only reviewer-owned independent geometry/height/residual
checkers and the input certificates. It uses exact algebraic signs, no
floating tolerance, timeout extrapolation, or expanded search domain.
No repair to the authored lemma or certificate is needed.

## Independent resume audit, 2026-10-10

A separate agent re-read the analytic source/window argument, the producer,
and the independent checker, then inspected the primary article directly.
The [primary HTML, Section 2.3](https://arxiv.org/html/2211.08239v2#S2.SS3)
specifies the regular whole-unit-facet strip construction and the integer
coordinate-sum specialization. The Introduction gives the common finite
pattern language for the arrow-legal Penrose tiling space; the Section 2.3
window discussion distinguishes generalized intercepts from that language.
The integral sum is therefore a source hypothesis supplied by the proper
Penrose specialization, not an assumed geometric consequence of an arbitrary
unit-rhomb tiling.

Mandatory boundary objects need not themselves be simply connected. If
one occurred in a source, it could be included in a finite whole-rhomb
patch by taking all source tiles meeting a sufficiently large disk and
filling bounded complementary components. Local finiteness makes this
finite. Common-pattern transfer applies to that patch and therefore to
the mandatory object inside it. It does not assert that an arbitrary
closed-window choice at a singular intercept is arrow legal.

The independent replay again passed all 196 retained full assemblies and
all 213 mandatory boundary objects with the exact counts above. No scope,
finite domain, mathematical result, certificate, or verifier changed.
The lemma's former “fresh hostile review pending” status was stale and has
been reconciled with this VALID review. The proper source compiler is
excluded before any residual choice, so extending the same 28 U / 185 V
boundary words into a proper Penrose source is no longer an open task.
Generalized noninteger intercepts, different source cuts/scales, and
non-source macro constructions remain separate mechanisms.
