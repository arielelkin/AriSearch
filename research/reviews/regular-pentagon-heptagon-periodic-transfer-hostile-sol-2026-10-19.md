# Hostile review: whole-interval periodic transfer

Verdict: **PASS / valid**, precisely for existence of the specified periodic 2P+2Q tiling for every real h>-t. This excludes aperiodicity for this whole metric family. It does not resolve the unrestricted two-convex-tile problem or classify all tilings. Independent review dated 2026-10-19; no mathematical repair required.

## Independent exact audit

Read AGENTS.md, research-problem.md, research-protocol.md, the producer Markdown/Sage/JSON, and the preceding minimal-torus hostile review. The companion checker does not import producer code or use certificate assertions as inputs. It reconstructs the geometry using QQbar.zeta(20), converts to ordered exact real AA coordinates, and works in AA[x], x=h+t. Thus its coordinate representation, positivity arithmetic, and polygon construction differ from the producer's cyclotomic complex polynomial implementation. It tests identities as polynomials, covering transcendental as well as algebraic positive x.

All 50 edge/other-vertex cross products have nonnegative coefficients and at least one positive coefficient. Therefore they are positive for every x>0; this proves actual strict convexity and simplicity, beyond merely checking positive turns. Closure is independently checked as a vector polynomial identity. Edge lengths are 1,x,1,(1-k)t+kx,1,x,1 with t>0 and 0<k<1. Their directions give the stated 144/126 heptagon angles. At x=0 two edges vanish, so strict seven-sided admissibility ends there.

The checker directly builds the four displayed face placements and verifies both endpoint identities of all twelve edge pairs with their prescribed integer lattice shifts. The identities imply reversed vectors and equal lengths on the entire edge, without an extra interpolation hypothesis. Every dart occurs once. The QQ signs and native edge indices are correct. Map1 is literally obtained by permuting the two Q face names; reversing the written order of a pair reverses its displacement. This relabeling gives the entire second map and cannot change the tiled geometry.

The determinant is independently verified to equal

    sin(36 degrees)*x^2+(4+k)*x+2*t+4*sin(36 degrees).

Its coefficients are positive; hence the lattice is discrete and has rank two at every admissible parameter. The exact signed shoelace identity is 2*area(P)+2*area(Q)=det(L1,L2). There is no limiting or sampled sign decision. The reflection set identities for P and Q also hold in AA[x]. Physical reflections thus admit direct placements after native boundary relabeling. For this positive existence theorem even this reduction is unnecessary: the direct placements suffice. It must not be interpreted as completeness of a fixed native-label enumeration under reflection.

## Attack on the local-to-global argument

A possible failure would be compatible edge endpoints with folded or multiply wound vertex stars. That failure does not occur here. Let a corner dart d denote the start of a CCW edge. Gluing this edge to its mate identifies that start with the mate edge end; the next corner is next(mate(d)). Each independently computed orbit has three corners, angles APP or PBB summing to 360 degrees, and zero displacement sum. The dual face graph is connected. Thus the abstract gluing is a connected closed oriented surface with eight vertices, twelve edges and four faces. Each vertex link is a single circle, not several accidentally identified links.

More explicitly, translate the sectors incident at one abstract vertex to a common lift of its image in the target torus. The full edge equations make each shared ray coincide, with the interiors on opposite sides because both face boundaries are CCW and the paired edge directions are reversed. Traversing the link therefore advances by successive positive corner angles in one rotational sense. The total advance is precisely 2*pi. Consequently these sectors fill a sufficiently small disk once; neither a gap nor winding degree greater than one is possible. This proves local injectivity of the target map at the vertex without assuming global nonoverlap. At an edge interior the same opposite-side argument gives a disk. Rank two permits the target disk to be chosen below the lattice injectivity radius for each fixed h; no uniform radius as h approaches -t is needed.

Endpoint lattice congruences make the facewise map descend to the target flat torus. It is a local isometry everywhere by the preceding argument. Connected compact source implies a finite surjective covering of the connected target. Potential global monodromy is exactly the possible covering degree N; it is not silently assumed trivial. Local metric preservation gives source area=N times target area. The independently verified area identity forces N=1. This rules out all additional sheets and proves that projecting the representative faces gives disjoint interiors and full coverage. Lifting the target torus proves the whole-plane lattice tiling. The argument does not infer plane coverage solely from the abstract source being a torus, and it does not require the displayed representatives to be a nonoverlapping fundamental domain in the plane before taking their quotient.

Tree normalization is legitimate for an arbitrary translational quotient: recursively shift the chosen face representatives along the three tree edges, killing those gluing shifts without altering the quotient. Their lengths are constant unit lengths, so the solved rotations and translations have no parameter-dependent denominator or exceptional interior parameter. For existence this normalization is only a derivation convenience; the explicit placements and checked endpoint identities already provide the witness.

## Scope, attempted counterexamples, and replay

Attacks included wrong complex embedding, negative coefficient at large x, degeneration near x=0, self-intersection despite turning angles, QQ pair-order signs, incomplete pairing, disconnected source, multiple vertex links, folding or extra winding at a vertex, nontrivial covering monodromy, and unwarranted reflection completeness. None leaves an unresolved defect in the stated existence claim. No new construction, pairing enumeration, literature or novelty claim is involved. No Git or discovery-log edit was made.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch sage research/reviews/regular-pentagon-heptagon-periodic-transfer-hostile-sol-2026-10-19.sage

Observed output: PASS independent AA[x] geometry, 50 convexity tests, 12 full endpoint identifications, 8 stars, positive determinant and area identity; map1 follows by face exchange. Finite domain: two fixed face-label equivalent maps, 50 shared convexity polynomials, twelve pairs and eight stars; unbounded parameter conclusion follows from exact polynomial positivity and the covering proof. No solver, seed, search cutoff, numerical branch, or unresolved qualification applies to this transfer theorem.
