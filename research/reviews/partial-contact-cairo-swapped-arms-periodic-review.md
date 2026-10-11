# Independent hostile review: swapped-arm partial-contact Cairo cone

Date: 2026-10-10. Reviewer did not develop the construction and imported no author code.

**Verdict: VALID.** The full four-dimensional sufficient periodic-family theorem and its scoped partial-contact/coalescence statements have a complete proof. No unresolved mathematical defect was found. This does not classify arbitrary Cairo pairs or establish the unrestricted target.

## Exact claim reviewed

[Author theorem](../lemmas/partial-contact-cairo-swapped-arms-periodic.md): for a,c,d,D>0 and b=c+sqrt3(d-a), B=a+sqrt3(D-c), e=sqrt3*c+d-2a, f=sqrt3*a+D-2c all positive, the Cairo pentagons with words(a,b,c,d,e),(c,B,a,D,f) tile the plane periodically using the four displayed whole motifs, with both native T-contact interval cancellations and their equality boundaries.

## Assumptions and attempted failures

* Reconstructed the polygons from directed edges in directions0,90,150,240,300, rather than trusting the displayed vertex formula. Both symbolic closure equations hold over Q(sqrt3)[a,c,d,D]. Positive lengths and cyclic directions prove strict convexity over the whole cone; every adjacent turn is positive and below180. The supporting-height argument gives strict inward support for every nonadjacent vertex.
* Checked the reflection matrix orthogonality and determinant−1. Its image of the native Q side2 unit direction is the P side0 unit direction. Q motifs have clockwise native boundaries, so the positive boundary sum is p0+p1−q0−q1. Same-native-order P/Q seams cancel with this sign; P/P and Q/Q seams reverse endpoints.
* Independently checked all six full seams. They consume twelve of the twenty motif native slots, leaving exactly the eight side1/side3 slots used by the interval cancellations. No side is silently omitted or double-counted.
* Reconstructed both directed interval chains from common origins and unit directions. First-bank total is b+D, with opposite break positions D and b. Second-bank total is B+d, with opposite break positions B and d. The four component lengths are positive throughout the cone, so the chains represent equal directed boundary multiplicity for every relative break order, including b=D, d=B and their simultaneous intersection.
* Checked that the simultaneous boundary occurs at d=a,D=c and remains genuinely positive when a/sqrt3<c<sqrt3*a. A concrete a=1,c=6/5 boundary fixture passes all exact overlap checks. Coalescence changes contact combinatorics but neither face convexity nor cancellation.
* Independently expanded the periods and area identity −det(u,v)=2area(P)+2area(Q). Positive polygon areas give lattice independence over the entire cone, ruling out any hidden zero-covolume subdomain.
* Attacked the global step: a locally finite periodic sum of oriented polygon boundaries vanishes exactly as a planar chain, so its interior-count function has zero generic jumps. A finite transverse path can avoid all locally finite segment endpoints and intersection points, including split vertices. Thus the multiplicity is constant almost everywhere. Its mean is exactly1, forcing disjoint interiors. Closedness of the locally finite compact tile union upgrades almost-everywhere coverage to coverage of every point. This proves the entire plane, not merely a patch or quotient with presumed embedding.

The path argument's use of generic crossings allows avoidance of all finite boundary intersection points along a compact path; no material repair is required. The construction needs neither an imposed edge-to-edge rule nor a monohedral classification.

## Independent checker and exact finite domains

[No-author-import checker](verify_partial_contact_cairo_swapped_arms_independent.py):

    conda run --no-capture-output -n arisearch python research/reviews/verify_partial_contact_cairo_swapped_arms_independent.py

The checker is nondestructive. It reconstructs raw directed edges, motifs, orientation matrix, all six full seams, both symbolic bank chains and the area identity, then compares those expressions against the retained author certificate. It independently computes every potentially intersecting lattice translation from exact lattice-coordinate bounding boxes and checks convex separating-axis inequalities over the exact real algebraic field.

Seven fixed algebraic fixtures test all four strict break-order sign cases, each separate equality boundary and the simultaneous boundary. Complete nonidentity comparison counts are44,32,34,44,64,40,48, totaling306. The author fixture's independently generated44 comparisons equal its retained comparison list. These finite fixtures audit degeneracies and implementation; the full-cone proof rests on the symbolic boundary and convexity arguments.

Replay: Python3.12.13, Sage10.9. All assertions pass. No random seed or solver timeout. No author code imports and no retained certificate writes.

## Defects, repairs and remaining uncertainty

No substantive defect or repair. The author's noncongruence claim is correctly restricted to the exhibited fixture or separately established parameter choices; the cone may include congruent shapes and the same periodic collection still works. Partial contacts and b=D,d=B coalescences are explicitly included. The final quantifier is periodic existence throughout this cone, not every-tiling periodicity or a classification of independently chosen Cairo shapes.

Remaining uncertainty is exactly the broader target outside the stated cone; no central obligation remains inside the reviewed sufficient family. No universal novelty or priority assertion is warranted.
