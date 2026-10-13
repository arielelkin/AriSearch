# Fresh hostile review: balanced whole-Ammann convex macro parity

Date:2026-10-13. Reviewer:luna, independent of terra author and root derivation.
**Verdict: VALID** for the general no180 finite convex-support lemma, its balancedG* Ammann application and the resulting two-hexagon-only compiler reduction.

## Claim and dependency scope

Reviewed [the parity artifact](../lemmas/terra-ammann-balanced-convex-macro-parity.md). The general theorem assumes finitely many whole genuine convex positive-area source polygons, disjoint interiors, exact union equal to one compact convex polygon, and no nonempty sum of source native angles equal to180. It concludes whole-side internal seams, no suppressed boundary source vertices and nM=sum n_i-2I. It requires no source-plane extension, atlas, fixed area rank, trivalent source or imposed contact rule.

The application uses the independently reviewed G* source's complete absence of180 native-angle relations and the freshly independently reviewed uniform-resection theorem. Their exact hypotheses were checked for applicability; settled source forcing/hierarchy certificates were not re-audited. General side-count and periodic quadrilateral dependencies are used only in their already reviewed scope.

## Boundary-host and internal T-junction attacks

Suppose an included source tile has a native corner atp lying inside another included tile's side. The side-host contributes a full180-degree half-disc. Ifp is on the convex macro boundary, the macro's available interior sector has angle at most180. The host already exhausts it, so the other tile's strictly positive corner cannot fit without interior overlap. If the macro sector were less than180, the host itself could not fit. Hence the boundary case is excluded by convexity alone.

Ifp is macro-interior, the complementary half-disc must be completely covered by the finite dissection. An incident tile cannot containp in its interior because that would overlap the host. Any second flat host would fill the other half-disc and leave no room for the specified native corner. Thus all tiles filling the other half-disc contribute native corners whose angles sum180, forbidden. Finiteness justifies choosing a sufficiently small disk: any tile not containingp has positive distance fromp, so no nonincident tile can intrude into the local sector argument.

Reflections preserve source angle values. No assumption about a plane source vertex atlas is needed. The argument also handles a partial-overlap endpoint where only one tile has a native corner and the other has a flat side sector.

## Whole seams, exposed edges and exact support topology

Positive-length overlap of unequal native side segments necessarily has an overlap endpoint native to one segment and internal to the other, already excluded. Thus every positive edge contact is a complete coincident native side. Opposite interior half-planes follow from disjoint convex source interiors; a third tile cannot share an open seam without overlap. Transverse interior edge crossings also force positive-area overlap.

If an open source-side point is macro-interior, a neighboring source tile fills the opposite side there, giving a positive edge overlap and therefore a full-side match. If none is macro-interior, the side is exposed on the macro boundary. A switch between exposed and shared portions would need precisely a prohibited T-junction. Here 'internal shared edge' means shared by two source tiles; its endpoints may still lie on the macro boundary, which does not affect incidence counting.

The macro boundary is a finite union of exposed full source sides. Every boundary turn is a source vertex. At a source boundary vertex, a flat host would be a prohibited T-junction against an included native corner. The included native-corner sectors fill exactly the macro interior sector. A straight180-degree sector would give the forbidden source-angle sum; hence every boundary source vertex is a genuine strict macro corner. There are no collinear consecutive exposed edges to merge after counting. Each native macro side is exactly one native source side.

Exact convex support has one simple boundary and no holes. A point-only dissection connection cannot supply the connected open interior of a convex polygon; a disconnected or holed union fails the hypothesis. Neither a convex hull of a patch nor a drawing that omits gaps is an admissible replacement for exact union. These potential counterexamples do not defeat the lemma.

Consequently each exposed native side contributes once and each shared seam twice to total source side incidences, proving nM=sum n_i-2I and its parity. No symmetry reduction, metric enumeration or topological finite-model conjecture occurs.

## Balanced contents, finite seed bounds and all-parameter scope

At every J inG*, the source no180 theorem applies to the actual H6,P1,P2 shapes. A balanced(h,k,k) whole-source patch has6h+10k source side incidences, hence any exact convex support has even genuine side count. This includes arbitrarily large finite balanced patches and all length coincidences permitted withinG*: no area-rank or generic metric independence is assumed. No balanced whole-source pentagon exists.

Two convex source polygons with disjoint interiors cannot share two different noncollinear native sides, since their convex intersection would contain a positive-area triangle. Distinct collinear source sides cannot occur in a genuine convex polygon. Thus a convex two-tile P1+P2 support has one shared side and eight boundary sides. Three source tiles share at most one side per unordered pair, so H6+P1+P2 has at least16-2*3=10 boundary sides. The tree/cycle subcounts are conditional contact counts, not claims that those geometric clusters actually occur. They correctly rule out pentagonal support without local fan enumeration.

OutsideG*, a native180 relation could allow a suppressed boundary source vertex and change parity. Cuts or fractional tiles replace native source-edge incidences and similarly escape this statement. Those are genuine changed hypotheses; larger balanced whole-source patches insideG* are not.

## Uniform resection and global reduction

The freshly reviewed uniform-resection theorem applies to every whole-source dissection of both supports whenever their unmarked pair tiles. It allows reflections, arbitrary macro contacts and omission, and forces each dissection balanced without area-rank3. Therefore parity applies separately to each target support; advertising alternate source contents cannot recover a pentagon.

A convex even-sided polygon has at least four native sides. A four-sided member gives an admitted monohedral periodic escape under the original omission convention. If both members have at least six sides and one exceeds six, the reviewed global side-count/hexagon reduction excludes an aperiodic pair; both counts above six are untileable, while a tileable hexagon-plus-higher pair has a periodic monohedral escape. Thus only(6,6) can remain potentially aperiodic among these two convex whole-Ammann-supported pairs. This does not construct or classify those two-hexagon macros, nor solve the unrestricted problem.

## Defects, repairs and continuation

No consequential defect was found; no repair or search replay is required for this analytic result. The exact-support and no180 hypotheses are essential and were not weakened to local polygon feasibility, convex hull coverage, or a finite-angle-grid representative.

The pentagon-containing whole-Ammann compiler is closed throughoutG*. A genuine pentagon construction must specify actual source cuts/fractions, changed points/source polygons or a parameter outside the currently proved source domain, with exact convex output geometry and a renewed source/forcing obligation. No larger whole-source cluster enumeration is justified. The separately retained two-hexagon structural track remains available; parity alone does not settle it.

Final verdict: **VALID on the stated mechanism scope**. No novelty or unrestricted two-convex-tile theorem is inferred.
