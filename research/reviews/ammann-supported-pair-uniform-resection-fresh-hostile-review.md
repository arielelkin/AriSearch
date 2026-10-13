# Fresh hostile review: uniform unmarked resection of source-supported macro pairs

Date:2026-10-13. Reviewer:luna, independent of sol author.
**Verdict: VALID under the stated generic unmarked Ammann source and whole-source-supported macro hypotheses, with arbitrary isometries and contacts.** It excludes a source-compiler mechanism, not arbitrary convex polygon pairs.

## Exact claim and reviewed dependencies

Reviewed [the theorem](../lemmas/ammann-supported-pair-uniform-resection-obstruction.md). At any J in reviewedG*, if two compact positive-area whole-source-supported macro shapes tile the plane, every whole-source dissection of either shape has equal P1/P2 counts; each shape has a unique content vector; those two vectors have rank2 and their nonnegative cone contains(1,phi,phi). In particular neither macro may be congruent to sourceP1 orP2.

The reviewed Ammann forcing theorem applies to EVERY admitted unmarked source tiling with reflections and unrestricted contacts, and the independently reviewed anchored count proof gives h=Theta(R^2), p1/h,p2/h->phi in every such tiling. These exact scopes were checked, not their settled forcing/hierarchy certificates redundantly rerun. The new theorem needs only the universal area identities areaH=sigma andareaP1+areaP2=phi*sigma, not area-rank3 or the algebraic perturbation certificate.

I independently substituted the reviewed affine vertex lists into the symbolic shoelace formula over Q(w)[s,t], fixing real s,t under conjugation. It returns areaH/sigma=1 and(areaP1+areaP2)/sigma=w+conjugate(w)=phi identically. These are positive unsigned areas inG*; reflection preserves them.

## Resection attack: no hidden matching convention

Choose one arbitrary finite dissection of each support. Transport it by an isometry onto every macro occurrence. Each source polygon interior is an open subset of its macro support and therefore lies in the macro interior. Distinct macro interiors are disjoint, so inserted source interiors cannot overlap; their exact support unions cover the plane. Internal source contacts and contacts across macro boundaries are all admitted by the source definition. Reflections transport source congruence classes into the same allowed classes.

The source forcing theorem may conclude that the resulting geometric resection has matching full edges, one handedness and a legal marked reconstruction. Those are consequences of its being an admitted unmarked source tiling; they cannot be used to veto a resection that already covers the plane without interior overlap. If proposed macro placements made such conclusions impossible, the macro tiling would consequently be impossible. No source arrows, matching rules, orientation restrictions or recognizer are silently assumed by this argument.

Support symmetries create no problem: any chosen isometry transports the selected source patch, and its integer content remains fixed. Arbitrary per-occurrence choices of that isometry are enough; translation covariance is unnecessary because the macro tiling need not be periodic. Omission of one macro type causes no loophole: the universal source ratio then contradicts its sole rational content direction.

## Boundary counting and annihilator quantifier

A whole-source-supported macro is a finite union of genuine source polygons, so its positive-area interior contains a fixed-radius source disk. Even nonconvex or disconnected macro supports consequently have uniform finite diameters and packing bounds under isometries. Source anchors and macro anchors move only a uniformly bounded distance in the chosen fixed patches. Thus c(R)=u*m(R)+v*n(R)+O(R), with source/source-class counts unambiguously preserved because the generic source classes are distinct. Boundary multiplicities are bounded by the fixed finite patch sizes.

For ANY rational rowa annihilatingu andv, dividea*c(R)=O(R) by h=Theta(R^2) and use the universal source ratio. This givesaH+phi(a1+a2)=0 and thereforeaH=0,a1+a2=0. The rational annihilator is at least one-dimensional and contained in span(0,1,-1), so it has exactly dimension1. Henceu,v have rank2 and both are balanced. The proof neither assumes absolute macro densities nor assumes both macro types have positive density.

The chosen dissections ofM andN were arbitrary. Given any alternate dissection ofM, hold some dissection ofN fixed and repeat the same geometric resection. The same reasoning forces its alternate count vector balanced. InterchangingM,N proves the statement for EVERY whole-source dissection. This is the consequential improvement over the earlier fixed-content theorem; no circular assertion that macro congruence already fixes content is used.

## Area uniqueness, cone and singleton escape

A balanced integer content(l,k,k) has unsigned area sigma(l+phi*k). Congruent supports have equal area. Comparing two balanced contents gives(l-l')+phi(k-k')=0, hence both integer differences0. This proves content uniqueness across all dissections without rational independence of the three individual source areas. The result does not imply a unique spatial dissection, nor exclude algebraically equal-area unbalanced contents when no two-macro tiling exists.

Positive macro/source packing givesm+n=O(R^2); h=Theta(R^2) bounds the nonnegative coefficientsm/h,n/h. A subsequence yields limiting coefficients expressing(1,phi,phi) in the closed cone ofu,v. This is a necessary count condition, not a global construction or an assertion that an arbitrary cone-compatible pair tiles.

A support congruent toP1 admits its singleton unbalanced dissection(0,1,0), including a reflected singleton if needed; P2 similarly admits(0,0,1). The universal arbitrary-dissection balance theorem therefore excludes either as a member of a tileable supported macro pair. Variable source contents cannot rescue the singleton route at anyG* parameter, including rational area-rank2 samples.

## Scope, counterexample attacks and next concrete obligation

Attacks checked: reflected macro tilings, mismatching source decoration across macro boundaries, symmetric macro isometry choices, omitted macro species, nonconvex/disconnected supports, boundary-straddling source pieces, alternate dissections with different counts, rank2 area parameters and lack of absolute frequencies. None yields a counterexample under the hypotheses. Positive compact area alone would not suffice for arbitrary pathological supports, but whole-source support supplies the finite polygon union and packing property used here.

No consequential defect or repair is needed. Cuts/fractional source transfers, a nongeneric parameter outside the reviewed universal source theorem, another source or macro shapes not whole-source-supported remain outside coverage.

The next concrete balanced two-macro feasibility obligation is geometric, not a variable-content rescue. Start with the exact P1/P2 pair across its c seam. At both K,L, the source atlas is trivalent, so any convex whole-tile cluster containing the pair must include the third incident tile. The third chi tile atK isH6 orP1, and the third psi tile atL isH6 orP2. Exact placements must determine whether an H/H fan uses one or two H copies, whether the P1/P2-added fan closes, and whether further trivalent vertices force more tiles or reflex boundaries. Balanced content and cone compatibility should be checked before convexity/forced closure. A passing finite fan would still need two prescribed convex macro supports and an actual global partition/covering; unrestricted target aperiodicity could then use unmarked source resection. This concrete fan task has been delegated separately; no duplicate enumeration was performed in this review.

Final verdict: **VALID on the stated uniform-resection mechanism scope**. Original research problem unresolved; no novelty claim follows.
