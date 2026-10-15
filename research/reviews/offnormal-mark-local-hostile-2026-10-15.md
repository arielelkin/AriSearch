# Independent hostile audit: off-normal mark-local H obstruction

Date: 2026-10-15. Reviewer: y_fresh_hostile. Verdict: **VALID** for the stated construction component. This is not a solution of the unrestricted two-polygon research problem.

Final artifact-specific reread completed after the root saved the shorter four-step proof with unconditional cyclic bound and unique36/opposite-M bridge. Reviewed artifact: `research/lemmas/offnormal-mark-local-truncation-obstruction-2026-10-15.md`. I reconstructed the native source-angle transfers, same-mark head geometry, cyclic angle bound, and congruence bridge. No proof-producer imports were used. The earlier exact strict precursor fixture remains valid and is compatible with this obstruction because its receiving hexagons are not congruent.

## Native contexts and head bound

The actual thin arrows give both-tail mixed-mark source corners of 36 degrees and same-mark X-head and Y-head source corners of 144 degrees. The thick arrows give X-tail/X-tail at 72, Y-head/Y-head at 72, and the two mixed tail/head corners at 108. These reproduce precisely the endpoint angles in Section 1. Donor projections strictly inside their unit bases give acute positive base angles. Endpoint capacity forces common tail beta and X-head beta+36, with beta<36. Four other H angles exceed 108, and 36 and 72 are unique.

For a same-mark/head source endpoint U, the external and internal donor apexes have equal distance from U; their rays enclose exactly the source angle sigma. In the strict convex quad U,t,M,p, diagonal UM passes through the interior of triangle Utp until it crosses tp, and M lies strictly beyond that intersection. Thus ray tM lies strictly beyond tp away from tU inside the relevant half-plane, giving theta_head>(180-sigma)/2. This establishes X-head>18 and Y-head>54 without normal-foot or obtuse-M assumptions. The inequality agrees with the independently reconstructed exact determinant formulas in `research/searches/offnormal-strict-m-determinants-2026-10-15.md`.

## Independent exact finite check of the only cyclic bound needed

`research/reviews/offnormal-mark-local-independent-2026-10-15.py` uses only Python's standard library and exact Fractions. Reflection fixes the 36,s,t occurrence to vertices 0,1,2. It enumerates all five positions of 72, both directions for its s,t occurrence, and all five possible positions of 144: 50 native cyclic branches. Equality constraints merge the corresponding angle slots. The four large angles are relaxed to the closed interval [108,180], with total angle sum 720. Every vertex of each resulting box intersected with one affine hyperplane is enumerated exactly. Sixteen closed branches are feasible; every branch has s+t>=288, with the global minimum exactly 288. Therefore theta_tail=s+t-180>=108. This relaxation includes boundary configurations excluded by strict convexity, so cannot miss a genuine strict counterexample. It does not assume or test the stronger pair-uniqueness claim, which the simplified bridge does not require.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/offnormal-mark-local-independent-2026-10-15.py

Result: PASS, 50 branches, 16 feasible closed relaxations, minimum pair sum 288.

## Congruence bridge, including reflected aliases

Write the actual tail hexagon boundary as (T,c0,c1,M,dM,dT). Each thin tail's retained T has unique H-angle 36, so any congruence between the X and Y thin tail hexagons maps T to T. A hexagon boundary isomorphism maps the vertex three steps away to the vertex three steps away. Therefore it also maps M to M; hence mX=mY independently of any orientation or cut identification.

Normalize both receiving frames with T=(0,0), M=(m,0), receiver above the axis. The two incident rays of the hexagon at T have directions -beta and 36-beta, because the internal adjoining donor tail angle is also beta. The only plane isometries fixing both distinct points T and M are identity and reflection in their line. Reflection preserves this unordered ray pair only if beta=18. But theta_Xtail>=108 and theta_Xhead>18, together with X's total apex 144-2beta, imply beta<9. Reflection is impossible. The congruence is therefore identity in the normalized frames.

Identity fixes the external cutpoints c0 and c1 individually. The original donor apex t is recovered as the intersection of the lines Tc0 and Mc1. These are distinct nonparallel lines, since the donor triangle TtM is nondegenerate and the cuts lie strictly on its sides. Thus tX=tY, so uX=uY and hX=hY; the original unit-base head angles agree as well. Consequently gammaY=beta+36, both tail half-angles agree and are >=108, and theta_Yhead<=36-2beta<36, contradicting its strict lower bound 54.

This argument permits every cyclic/reflected prototype alias and arbitrary internal cuts. It uses genuinely six-corner strict hexagons, equal source base lengths, mark-local donor triangles/splits, and mark-local external cut geometry across thin/thick contexts. Removing any of those hypotheses requires a new argument. No conclusion concerning context-dependent cuts, different surgery incidence, or arbitrary convex P/H pairs is justified here.

## Independent assessment

The original longer common-pair uniqueness argument is also sound under its stated strict sum<306 premise; the elementary three-run case split covers all cyclic possibilities. Its uniqueness conclusion is unnecessary after using the opposite vertex M and ruling out reflection geometrically. I found no defect in either bridge. The final saved text retains the explicit beta<9 reflection exclusion and apex reconstruction, and correctly avoids treating the original apex as automatically intrinsic to the unmarked prototype. No repair is needed.
