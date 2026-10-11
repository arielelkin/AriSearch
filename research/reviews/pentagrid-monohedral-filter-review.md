# Fresh hostile review of the pentagrid monohedral filter

Reviewed 2026-10-10 by an agent who did not develop the source filter,
its polyhedral computation, or its theorem. The reviewer previously
developed the separate angular enumeration and was assigned this audit
after the source filter had been written.

**Claim reviewed:** Under Rao's explicitly imported complete monohedral
classification, every genuine convex U-angle pentagon is individually
untileable; every W-angle pentagon is individually untileable; a genuine
V-angle pentagon tiles alone precisely when l1=l3 or l2=l4, and these
cases admit periodic tilings. Angles sit at vertex i and li joins vertices
i and i+1. All real positive lengths and arbitrary contacts are included.

**Verdict: valid conditional on the explicitly imported classification.**
The local application is exactly and independently certified. This review
does not replay or independently certify Rao's full classification search.
No mixed tilability or two-shape periodicity conclusion is supported.

## Primary source and scope

The actual [Rao primary preprint, arXiv:1708.00274v1](https://arxiv.org/pdf/1708.00274v1)
was opened independently. Table 2 is on printed page14, PDF page index13.
Every one of its fifteen known-family angle equations and length equations
agrees with the producer's transcription. The necessary side convention
is stated in Section4 on printed page10: side i joins consecutive vertices
i,i+1. Reflections are permitted in the introduction. Section2 explicitly
distinguishes full vertices from corners meeting interiors of other tile
sides, so the imported classification is not limited to edge-to-edge tilings.

The results paragraph and discussion on printed pages14–15 reduce the
additional computational types16–19 to known families and classify types
20–24 as degenerate. Thus testing the fifteen genuine known families is
the appropriate local application of the imported theorem. The theorem
and the known families' periodic realizations remain external dependencies.

## Attacks and independently checked answers

1. **A mirror can corrupt the side indices.** The checker constructs each
   transformed side from its two original vertex endpoints and looks up
   that unordered edge. This independently recovers the producer's
   incoming-side shift for reflections. All ten dihedral relabelings per
   family are retained; no extra permutation of the cyclic boundary is
   permissible or needed.
2. **Angle-compatible family gates may be missing.** The checker enters
   named scalar angle equations independently and exhausts all450 gates.
   There are exactly sixteen compatible cases: six U, ten V, zero W.
   Their keys, actual angle words, side maps, and transformed length rows
   agree with the retained certificate. No duplicate can hide an omission.
3. **An ordered-field polyhedron can misclassify arbitrary real lengths.**
   The new checker uses no polyhedron or linear-program solver. Its exact
   rowspace obstructions apply to all real nonnegative length vectors,
   including vectors outside Q(sqrt5).
4. **Closure coefficients might use the wrong corner convention.** The
   checker evaluates exact tenth roots of unity, taking real parts and
   scaled imaginary parts. These exact algebraic rows have the same
   rowspace as the independently simplified closure identities below.
5. **Zero minimum side length might be mistaken for positivity.** The two
   degenerate V Type2 cases have a nonnegative nonzero rowspace vector.
   It forces at least one side to vanish. Their retained normalized
   degenerate witnesses satisfy the equations, so their maximum minimum
   side is exactly zero rather than an empty-case result.
6. **The claimed positive optimum might be only a feasible lower bound.**
   The checker supplies a separate analytic upper bound, verifies its
   attainment, and checks the explicit positive polygon against every
   supporting side with exact algebraic coordinates.
7. **The after-side convention in the metric search might be mixed with
   the vertex convention.** Moving angle_i from vertex_i to the endpoint
   after side_i sends li to L_(i+1). Thus the gates become L2=L4 or L3=L0,
   as the theorem states. No metric certificate should use the former
   gates without this index shift.

## Independent closure and positivity certificates

Set phi=(1+sqrt5)/2 in its positive real embedding. Closure simplifies to

    U: l0=l1+phi*l2+phi*l3,
       l4=phi*l1+phi*l2+l3;

    V: l0=phi*l1+phi*l2-l4,
       l3=phi*l1+l2-phi*l4.

For each compatible case, append its exact transformed side equalities
to these two identities and compute the reduced row echelon matrix R.
For every claimed empty normalized nonnegative polyhedron, a vector in
its rowspace has all five coefficients strictly positive. Its scalar
product with any nonzero nonnegative length vector is positive, whereas
the imposed equations force that scalar product to be zero. This proves
emptiness without relying on the producer's backend.

The four U Type2 strict certificates are positive combinations of R's
three rows with coefficients respectively

| Case (word,type,sign,offset) | Row coefficients |
| --- | --- |
| (U,2,+1,1) | (1,2,4) |
| (U,2,+1,3) | (1,4,1) |
| (U,2,-1,2) | (1,8,1) |
| (U,2,-1,4) | (1,1,4) |

The other eight empty cases have rank five, hence identity reduced row
echelon matrix. The sum of its five rows is the strictly positive vector
(1,1,1,1,1). These are the two U Type8 cases and the six V Type6/8/9 cases.

The two degenerate V Type2 gates force l2+l4=0 or l1+l3=0. Nonnegative
lengths permit their retained degenerate witnesses but no strictly positive
one. Thus all fourteen negative strict-metric cases are independently
excluded, with the producer's empty versus degenerate distinction checked.

For the positive V gate l1=l3, closure implies

    l0=2(phi-1)*l1+l2.

For the positive gate l2=l4, it implies

    l0=2(phi-1)*l2+l3.

The two positive coefficients in either identity sum to sqrt5. If every
side is at least delta, l0 is at least sqrt5*delta. Under perimeter-one
normalization this gives delta<=1/(4+sqrt5)=(4-sqrt5)/11. The retained
witness l1=l2=l3=l4=(4-sqrt5)/11 and l0=(-5+4sqrt5)/11 attains the bound.
The checker verifies exact closure, positivity, all side equalities, and
strict supporting-side convexity of this coordinate polygon.

For arbitrary genuine positive V polygons satisfying either gate, the
angle and side conditions are exactly a relabeled known Type2 family.
Its imported sufficiency and periodic tiling supply the geometric conclusion.
For W the native full/half sum obstruction is elementary and independent
of the classification.

## Artifacts and actual execution

The independent checker is
[verify_pentagrid_monohedral_filter.py](verify_pentagrid_monohedral_filter.py).
It reads the root's
[retained certificate](../certificates/pentagrid-monohedral-family-filter.json)
and imports none of the producer. It uses exact Sage field matrices and
algebraic numbers, not Polyhedron, and uses explicit exception-based checks.

Replay:

```text
conda run --no-capture-output -n arisearch python3 research/reviews/verify_pentagrid_monohedral_filter.py
```

The command completed successfully: all450 source-family angle gates,
sixteen compatible cases, twelve strict rowspace obstructions, two
degenerate obstructions, and two exact positive optima with convex
coordinate witnesses passed.

No defect was found in the theorem's local application. Its dependence on
the complete external classification remains explicit. This result filters
monohedral periodic escapes; it does not establish that the user's
golden-length pair avenue is exhausted or that any surviving pair tiles.
