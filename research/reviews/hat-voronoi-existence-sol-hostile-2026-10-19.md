# Hat prescribed-disk Voronoi gate: independent hostile review

2026-10-19. Verdict: scoped pass. This excludes the prescribed unweighted site disk, not arbitrary site rules, weights, or the main two-convex-tile problem.

Reviewed the producer, certificate and matching report, together with research-problem.md and prior actual-support/proxy caveats. Independently replayed the producer through its successful uniform obstruction status: targets 509/519/516 have 5/6/7 sides, neighborhood sizes 21/23/22, accepted box counts 287/97/553 and maximum subdivision depths 16/11/16. No sampling predicate supplies the conclusion.

## Native geometry and actual supports

Independently recomputed all 13 exact squared boundary distances from native p0. They agree with the report; their minimum is 25/64. Independently recomputed all exact vertex squared distances; maximum is 301/16. Hence delta=5/8 and the stated R are correct. Independently extracted the native eight-kite union boundary: it has 14 split edges; every exposed segment lies exactly on a native Hat outline segment. Its signed doubled area and the sum of kite doubled areas both equal 16sqrt(3). This checks the reference decomposition against the actual Hat rather than an auxiliary metatile polygon.

The producer checks every transformed primitive sector against the six standard sectors of one common hex-center lattice. Distinct sector centroids therefore identify distinct, interior-disjoint primitive grid faces, and thus disjoint Hat interiors. This is substantially stronger than testing unique centroids of arbitrary polygons. Full-edge multiplicity at most two and exact cancellation recover every exposed actual-union edge, including hole boundaries. Because each target p0 is interior, all boundary distances strictly greater than 10 prove containment of its closed radius-10 disk: any exit segment would meet that boundary. Proxy outline areas are irrelevant to this argument.

## Infinite source and normalization

Freshly compared retained initialization, the 29 placement rules, all four child selections, recentering, and geometric recurrence with the creator [hat.js](https://raw.githubusercontent.com/isohedral/hatviz/main/hat.js). They match. The [Hat paper](https://arxiv.org/html/2303.10798v3), Sections 2 and 5, supplies the hierarchy/existence theorem input. Counting H children in the four retained selections gives 3/1/2/2. Thus an infinite hierarchy containing level-4 supertiles contains the exact level-3 H used here. This relies on the published legal hierarchy, not on deducing infinite extension from this finite patch. The report states that dependency correctly. No fixed similarity ratio for proxy outlines is assumed.

The factor two compensates for half-size source frames. Reflections are retained in each affine frame; the shared parameter disk is invariant under orthogonal changes of frame. Reflections of resulting polygons cannot equate different intrinsic side counts.

## Uniform Voronoi certificate

A closed rho disk about native p0 remains strictly interior to its Hat, giving separation at least 2(delta-rho)=15/16. Convexity of the Euclidean norm on the Hat vertex hull proves covering radius R=sqrt(301)/4+5/32. Uniform separation and covering establish bounded finite-sided Voronoi cells in a genuine plane source.

The exact cutoff is sound: 2R+2rho=sqrt(301)/2+5/8<10. Every omitted infinite-source p0 site lies outside the covered radius-10 disk, since its site is interior to its omitted Hat. Every site can move at most rho, so the finite lists include all possible sites within 2R. Equality cases at the radius-10 cutoff cannot matter because the cutoff inequality has strict slack.

Interval operations use exact rational endpoints and a verified enclosing interval for sqrt(3). The subdivision tree covers the whole closed parameter square; discarded boxes are strictly disjoint from the closed disk. The remaining boxes cover every disk point, including its circular boundary. Bisector intersections are algebraically exact before interval enclosure. Nonzero determinants, strict nonincident inequalities, and strictly positive oriented edge lengths certify a feasible convex cycle with exactly the advertised genuine sides. The nonincident strictness excludes competing sides passing through vertices. The vertex radius check puts the whole convex polygon inside B(site,R), so omitted sites cannot trim it. SciPy proposes orders only; it cannot make an invalid order pass these predicates.

The report therefore gives a valid uniform three-congruence-class obstruction for the specified disk. It gives neither global palette enumeration nor a two-tile construction, and claims neither. Replay of the full producer, rather than a separate independent interval engine, is the computational check used here; the native geometric distance and decomposition checks were recomputed separately.

Final certificate inspection confirmed serialization of all 937 accepted rational boxes (287/97/553), preserving the complete retained cover. Creator source snapshots and SHA256 provenance are retained alongside the certificate.
