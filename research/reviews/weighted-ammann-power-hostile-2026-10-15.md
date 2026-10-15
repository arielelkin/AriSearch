# Independent hostile review: the fixed Ammann weighted mean-site box

Date:2026-10-15. Verdict: **VALID** for the exact small weight-box obstruction in [the construction gate](../lemmas/weighted-ammann-power-small-box-obstruction-2026-10-15.md), including occurrence of the three witness contexts in every legal Ammann source through the reviewed composition theorem. The claim is at least three congruence classes throughout the specified box. It excludes this construction family on this box; it proves no impossibility for general convex pairs, unrestricted weights, changed sites, or changed source metrics.

The [independent exact checker](weighted-ammann-power-independent-2026-10-15.py) imports neither new author checker. It explicitly depends on the already reviewed Robinson/Ammann source generator, [ammann-two-class-reconstruct.py](../searches/ammann-two-class-reconstruct.py), for substitution, rhomb pairing and placement. This shared source dependency is not described as an independent re-proof of the original Ammann theorem.

## Independent geometry

The checker writes its own three reference polygons from J=1/2+(4/5)w and reconstructs their genuine vertex means, support-line distances and vertex radii. All predicates use exact algebraic real arithmetic. It finds rho²=0.0466681472606..., R²=0.493755685157..., L=1.50135452420... as diagnostics only, and checks L+2R<3 exactly.

From the reviewed source's five-subdivision rhombs, it independently rebuilds the decoration graph. Unlike the author's existing face-tracer dependency, the new verifier sorts rays by exact half-plane and determinant predicates, using no numerical angles. It traces all faces, verifies the complete positive-area sum against the source rhomb area in the exact cyclotomic field, checks strict convexity, and classifies every complete source polygon by its full pairwise squared-distance matrix under every cyclic and reversed correspondence. All650 polygons, their types and genuine mean sites agree with the retained certificate. Source indices43,44,45 are respectively P1,H6,P2.

The power geometry uses independently implemented exact half-plane clipping, with duplicate and collinear subdivisions removed. It does not reuse the producer's pair-intersection enumerator or its retained active pairs. At zero weights the three clipped polygons have respectively7,6,5 strictly convex genuine corners. An independent active-line pair is chosen for each vertex. At all four corners of the closed weight box, the resulting affine vertices satisfy every one of the650 reconstructed source-site inequalities, not only the retained near-neighbor constraints. Independently clipped polygons at these corners have exactly those vertices.

Every cyclic edge is parallel to its corresponding zero-weight edge with strictly positive projection at all four box corners. Every vertex has squared norm at most C², and all turns are strict. These tests certify genuine corners, rather than graph vertices lying collinearly on a side. Affine slack and edge-projection dependence extends the statements over the entire closed box, including its edges and isolated parameter strata.

Persistent ties are handled correctly. In particular the heptagon has a four-site power vertex. A nonincident slack that vanishes at the box center and is nonnegative at all four corners must vanish identically, since the center is a strict convex combination of those corners. No generic trivalence assumption or strict-slack requirement is imposed.

## Finite versus infinite competitors

The open rho-disks about source means lie inside their respective source polygons, so distinct sites are separated by at least2rho. Weight differences are at most rho². Sites therefore remain strictly active, while every point has a source mean within R. A true global power cell lies in the C-disk, where C²=R²+rho². For a competitor at distance d>L, its worst possible power improvement there is bounded by d²-2Cd-rho²>0, so it is redundant.

A genuine gap in the preliminary checker was repaired during review: bounding the true global cell by C does not alone bound a finite half-plane intersection. The author added, and the independent checker verifies, the C-disk bound on every affine candidate vertex at every weight-box corner. Convexity of squared norm extends that bound throughout the box. The fixed feasible nonzero edge cycle describes the entire local intersection, since its edges remain supporting constraints; its bounded recession cone is independent of weights. Thus the computed finite polygon itself lies inside the C-disk, and all omitted distant competitors are redundant on it. Local and global cells coincide.

For each witness, exact point-to-segment distances put every original rhomb boundary segment farther than L+2R and farther than3. A missing complete source tile cannot have its mean within L: if it reaches that boundary, its diameter at most2R would violate the margin. The retained near-neighbor list is independently reconstructed by exact distance comparison. This excludes boundary truncation and missing-competitor artifacts.

## Positive source occurrence and every-source bridge

Finite legal patches were not assumed extendable merely because they came from a sun seed. In particular, centered nesting of scaled sun subdivisions was not assumed. The additional retained certificate gives137 complete decorated rhomb frames and their explicit embedding into the ninth subdivision of one red Robinson triangle. The independent checker reconstructs the selected137 frames and the target supertile directly, then verifies every transformed frame is present, including its native decoration orientation. It does not repeat an unbounded search or infer occurrence from failure to find an obstruction.

Every unit rhomb has diameter strictly less than2. Any rhomb meeting one of the radius3 witness disks has a vertex within5 and is therefore among the selected137. Those disks lie strictly inside the original patch, and L+2R<3. Consequently the matched decorated patch determines all required witness and competitor source cells, not merely some nearby point coordinates. The ninth-level supertile check uses rhombs paired entirely from halves inside that supertile, so an unspecified outside completion cannot change those frames.

The extension to EVERY legal source needs the reviewed global hierarchy, not a generic assertion of Penrose minimality. By Lemma6 of the [reviewed Ammann forcing theorem](../lemmas/ammann-forcing-aperiodicity.md), each legal marked-rhomb source admits composition through ten levels, and substitution of those parents exactly recovers the source. Each parent half, red or blue, has a red child: the displayed Robinson rules give respectively one red plus one blue, and one red plus two blue. A level10 half has scale phi^10; its red child is a level9 half of scale phi^9. Its nine unit-scale subdivisions are isometric to precisely the red supertile used in the positive137-frame certificate. This checks the level index rather than assuming a level9 parent must itself be red.

All red halves have the same indexed reference geometry up to isometry; reflections are allowed. The matched frames fix the decoration, and mean sites and shape-type weights commute with these isometries. Thus every legal source contains all three required mean-site contexts. For a source initially presented as an Ammann polygon tiling, the reviewed reconstruction and converse decoration identify it with this legal marked-rhomb source. No new all-corona enumeration or external minimality theorem is used.

Three different genuine corner counts imply three different Euclidean congruence classes, including reflected congruences. The whole specified box is therefore excluded as a two-class power partition. This says nothing about shape-only reconstruction or aperiodicity of a hypothetical successful changed family.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/weighted-ammann-power-independent-2026-10-15.py

## Final promoted-artifact reread

The reviewer reread the exact promoted lemma at `research/lemmas/weighted-ammann-power-small-box-obstruction-2026-10-15.md`, including its revised every-source statement, ten-level composition paragraph, ninth-level red child indexing, reviewed status, replay scope, and retained geometry/embedding links. The obsolete minimality qualification has been removed and replaced by the explicitly reviewed hierarchy argument above. These final changes introduce no new geometry or finite-domain claim. Verdict remains **VALID** for the promoted artifact as written.
