# Fresh direction review: 11:00 UTC, 2026-10-15

The unrestricted two-convex-polygon problem remains **unresolved**. This cycle independently reviewed the arbitrary-split receiving-hexagon obstruction and proposes a different concrete construction gate. No discovery-log, registry or Git changes were made.

## Completed hostile review

The [independent review](../reviews/context-dependent-split-receiving-hexagon-astra-hostile-2026-10-15.md) is **VALID** for the complete stated domain of [the new theorem](../lemmas/context-dependent-split-receiving-hexagon-obstruction-2026-10-15.md). All sixteen native endpoint occurrences were reconstructed from the actual arrows. Every individual thick rhomb has a Y receiver with both retained endpoint angles72; uniqueness of this angle in the common H forces its two opposite diagonals to1/2. The same thick rhomb's X-tail receiver then has a compulsory midpoint and a strictly negative native turn. A direct independent SymPy expansion and the author's Sage checker both passed.

This includes arbitrary physical edge splits inherited by donors from their receiving neighbors. It does not require both donor parities or any equality between independent split contexts. The beta18 exception from the earlier proof disappears entirely. Do not assign another cycle to changing splits or truncation fractions in this topology. Context-dependent donor triangles are outside the theorem, but making those free would simply add another congruence system to a repeatedly failing partition. I do not recommend that as the next positive task.

## Construction recommendation: power cells of the existing three-shape Ammann tiling

Start with the reviewed exact three-shape Ammann source at

    w=exp(i*pi/5), J=1/2+(4/5)w.

Use the genuine source polygons H6,P1,P2 defined in [the forcing theorem](../lemmas/ammann-forcing-aperiodicity.md) and its reconstruction dependency. For each source tile T, place a site c_T at the arithmetic mean of its genuine vertices. This is an intrinsic interior point and commutes with every isometry. Assign weights

    weight(H6)=0, weight(P1)=a, weight(P2)=b.

The new polygon associated to T is the POWER CELL

    C_T(a,b)={x: |x-c_T|^2-weight(T)
                  <= |x-c_U|^2-weight(U) for every source tile U}.

The two real parameters are global shape-type weights. There are no donor triangles, receiving sectors, truncation fractions, prescribed opposite diagonals, original-center network edges, or whole-source fusion constraints. Boundaries are radical axes determined by competing sites. This changes the construction mechanism: convexity and whole-plane coverage are automatic, while the number of congruence classes becomes the first exact test.

The first object is therefore a specified two-parameter family of convex plane partitions, not a proposed pair with an unproved existence statement. It is NOT yet known that any member has two congruence classes. The source's aperiodicity does NOT by itself prove shape-only aperiodicity of its power cells.

### Exact small parameter domain and finite geometry gate

Let rho>0 be the minimum, over the three source polygons, of the distances from their vertex-mean site to their supporting side lines. Let R be the maximum distance from a vertex-mean site to a vertex of its source polygon. These are exact positive algebraic numbers computable directly from the given three polygons. Use the initial compact domain

    |a|<=rho^2/2, |b|<=rho^2/2.

The difference of any two weights is at most rho^2. Distinct sites have separation at least2rho, because the source tiles contain disjoint open rho-disks around their sites. Thus each site lies strictly inside its own power cell throughout the whole domain. All cells have positive area. Every x is within R of some source site, since its source tile is contained in the closed R-disk about its site. If x belongs to C_T, comparison with this nearest-distance bound gives

    |x-c_T|^2 <= R^2+rho^2.

Put C=sqrt(R^2+rho^2). Each cell is consequently bounded. At any point with |x-c_T|<=C, the constraint from a site at distance d satisfies

    |x-c_U|^2-weight(U) - (|x-c_T|^2-weight(T))
       >= d^2-2Cd-rho^2.

Hence every source site farther than

    L=C+sqrt(C^2+rho^2)

has a redundant constraint. This supplies an exact finite neighbor-radius bound without estimating an infinite tail numerically. Retain a complete local source patch around each test site out to this radius, with a certified boundary-distance margin. The existing exact source generator supplies patches; a local finite witness needs no claim that one patch contains every possible source corona.

For a site difference d=c_U-c_T and y=x-c_T, the actual constraint is

    2 d dot y <= |d|^2+weight(T)-weight(U).

The normal is fixed and the right side is affine in (a,b). Every intersection of two nonparallel supporting lines is affine in (a,b). Its feasibility against every other line is linear in (a,b). Thus a finite arrangement of exact algebraic lines partitions the parameter box into cells on which each tested polygon has a fixed cyclic list of active constraints. Evaluate the two-dimensional chambers, their one-dimensional edges and all zero-dimensional intersections; isolated coincidences must not be discarded as nongeneric.

On each such chamber the native angle word is CONSTANT: its edge directions depend on the neighboring site differences, not the weights. First delete collinear subdivisions and reject any parameter stratum with a triangle or quadrilateral output. Then test whether the observed cells have at most two angle-word classes up to cyclic shift and reversal. Three different angle words in actual source cells kill that entire stratum before metric congruence is attempted.

Before metric congruence, also use the source partition's Euler balance. In a repetitive bounded-cell power tiling with positive densities and EVERY vertex trivalent, the mean side count is6. Therefore a two-class(5,6) output using pentagons at positive density cannot occur in such a stratum; a(5,7) pair or two hexagons can. Generic power diagrams are often trivalent, but this MUST be checked for this restricted two-weight family: persistent higher-valence degeneracies can lower the mean side count. With only degree>=3 known, mean sides<=6 does not exclude(5,6). Do not silently impose a pentagon/hexagon target on this construction. Root supplied this useful prefilter during the direction review.

For an angle-word survivor, vertices are affine functions of(a,b), so squared vertex distances are quadratic. Equality of the complete vertex-distance matrices, for each cyclic or reversed correspondence, is an exact finite polynomial congruence test. The requested output of this FIRST gate is one of:

1. an exact two-class realization on a certified complete corona atlas, including all support inequalities and exact prototype coordinates;
2. an exact finite set of source-cell witnesses excluding the entire specified weight box; or
3. an explicit residual algebraic parameter locus with the unresolved local congruences stated.

A few numerical low-class examples or bounded absence of a periodic patch are not an output of this gate. Stop on an exclusion certificate; do not add arbitrary context weights to rescue it. A larger parameter box, different fixed sites, or another source must be proposed as a separately justified changed mechanism.

### If the two-class gate succeeds

First attack both monohedral omissions and small mixed periodic carriers. A successful source partition is not enough: the older exact periodic(5,8) Voronoi pair already passes both omission tests and still tiles periodically as a pair. Apply the current hexagon restrictions immediately if both outputs are hexagons.

Only after an exact two-shape pair survives those attacks, investigate its intrinsic decoder. A concrete local test is available: transfer the reference generating-site positions into each output polygon under all its Euclidean symmetries and enumerate actual full-side pairings. For every legal pairing, test whether the two transferred sites satisfy the correct radical-axis identity on that side and whether the resulting finite local site configuration identifies one source adjacency. Multiple possible site positions under a prototype symmetry must all be included. Partial contacts and unintended vertex stars require their own exact exclusion; they are not covered by the original source theorem. If these local tests do not identify a finite source atlas, record that obstruction rather than naming global recognizability as a promised later routine step.

The central unproved construction obligations are precisely two-class closure and shape-only reconstruction. This proposal improves the first gate by making it a finite semialgebraic problem in TWO parameters with automatic convexity and plane existence. It does not assert the second obligation is easy or already reduced to a theorem.

## Cheap predecessor test executed before choosing this source

I first tested the simpler idea of power cells at the centers of the TWO Penrose rhomb species, with thin weight0 and thick weight tau. That is a different point set from the chosen Ammann-face sites. A five-deflation source has430 complete rhombs;205 source centers have numerical distance greater than3 from its rhomb-patch boundary. With tau=-1/4,-1/8,0,1/8,1/4, clipping against radius3 neighbors gives respectively75,70,70,70,70 quadrilateral cells among those205 centers. Source rhomb23 is a quadrilateral witness in all five samples. These observations are exploratory floating computations, NOT a proof over the parameter interval. They are a sufficient reason not to recommend the simplest center-only seed as a positive candidate.

The exact finite-radius justification for this exploratory parameter box is elementary: unit rhomb centers have separation at least sin36, covering radius at most cos18<1, and weight range at most1/4. Every power cell lies within sqrt(5)/2 of its center. A site farther than3 cannot cut that disk, since d^2-sqrt(5)d-1/4>0 for d>=3. All sites stay active since sin^2(36)>1/4. The numerical patch-boundary margin still needs exact certification before any observed polygon is promoted to a finite obstruction certificate. No such promotion is made here.

The source is reproduced by:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/ammann-two-class-patchdata.py 5 /tmp/astra-1100-rhombs.json

The exploratory clipping code and printed results are retained in [the diagnostic](astra-power-centers-diagnostic-2026-10-15.py). It has no registry or proof dependency. The proposal proceeds to the already available THREE convex Ammann source classes, not to arbitrary additional cut contexts in the two-rhomb donor model.

## Distinction from previous closed routes and source boundary

The [old periodic Voronoi control](../counterexamples/resumed-voronoi-periodic-nonmonohedral-pair.md) used the periodic site set Z^2+{0,d,-d}, d=(1/10,49/100). The proposed sites come from an exact aperiodic source and have different metrics. No old periodic polygon is reused. A new periodic escape may of course exist and must be attacked.

The [spoke-dual triangle obstruction](../lemmas/penrose-boundary-dual-spoke-obstruction.md) has one output face per SOURCE VERTEX and network edges joining interior source points through source-edge points. A power diagram has one output cell per SITE and new radical-axis vertices. Its edges are not those source-point connections. Likewise the fixed-point exterior-budget obstruction fixes the old ray graph; that graph is not retained here. The general exterior-budget inequality itself remains a useful filter for the new polygons.

This is not a novelty claim for Voronoi or power diagrams. The limited fresh search used the queries `Penrose rhomb centers weighted Voronoi diagram tiles` and `Penrose tiling Voronoi cells two prototiles power diagram`. The primary-source preprint [Bormashenko et al., Informational Measure of Symmetry vs. Voronoi Entropy...](https://www.preprints.org/manuscript/202109.0076) studies patterns generated from Penrose tessellations; its indexed full-text result explicitly uses rhomb centers as Voronoi seeds. The abstract page was inspected; access to its linked journal full text returned429. No exact two-shape claim or weighted-cell classification is imported from it. The [2023 patch-frequency article](https://journals.iucr.org/a/issues/2023/05/00/nv5007/) concerns exact Penrose patches and higher-dimensional Voronoi machinery, not the proposed two-weight collapse. No priority or completeness claim follows from these searches.

## Portfolio allocation

Root's common-five-length mixed repeat-separation computation is a separate structural track. Finish its small native-torus/determinism certificates and hostile review if the reported short cases close. Do not let that replace the positive construction track or infer unrestricted impossibility from a growing finite word list.

Give the power-cell family ONE exact local angle/metric gate. Its purpose is to earn or reject an actual two-shape plane partition before investing in hierarchy. Keep the main problem marked unresolved; the new receiving obstruction and current structural theorems remain restricted results.
