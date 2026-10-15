# A six-color/five-color hexagon source has an unmarked periodic escape

Date: 2026-10-15. Status: independently hostile-reviewed VALID;
[review](../reviews/hexagon-six-five-formal-color-hostile-2026-10-15.md). All four existing finite component verifiers were rerun successfully during authoring. Their finite domains are unchanged; this artifact adds a geometric interpretation and an explicit indexed-state argument, not a new enumeration.

## 1. Precise statement

Let A,B be genuine compact convex hexagons with nonempty interiors. Each has a fixed reference indexing of its six sides and corners. Attach a formal color to each native side slot. Suppose:

1. A has six distinct side colors.
2. B has at least five distinct side colors.
3. There is a function ell from the used colors to positive real numbers such that every side with color c has geometric length ell(c). The function ell NEED NOT BE INJECTIVE: different colors may represent identical physical lengths.
4. There exists an edge-to-edge, everywhere-trivalent plane tiling T by indexed isometric copies of these colored reference polygons. Every full seam has the same color on its two sides. Reflections are allowed.

Then the underlying UNMARKED pair A,B admits a doubly periodic full-side plane tiling. No side-color rule is imposed on the final problem. The periodic escape may also respect some auxiliary colors, but that stronger conclusion is not needed.

The hypothesis already provides a full-side trivalent source. This theorem does not apply the uncolored defect-free limit theorem to a partially contacting colored tiling. In the contact-component application below, first take an uncolored defect-free limit, THEN assign colors from its actual native seams.

No assumption that either physical polygon is asymmetric, or that different colors have different metric lengths, occurs in the theorem. The indexed maps carried by the source tiling are part of its mathematical data. They are used only to construct an unmarked witness.

## 2. The common combinatorial and metric bridge

Number sides0,...,5 cyclically and let corner i lie after side i, between i and i+1. A side i has endpoint corners i-1 and i. Actual corner indices of A are0,...,5 and of B are6,...,11.

At a trivalent full-side vertex every ray has one well-defined COLOR, because the two incident tile sides have identical colors. The two colors adjacent at a native corner are its native arm colors. Thus the possible actual-corner stars and all their native far-endpoint tests are determined by the two color words alone. Actual physical equality of two differently colored arms does not create another star in T: its seams must match colors. Conversely, each same-color full-side match has equal physical lengths by hypothesis3.

When adjacent colors differ, the three rays at a trivalent vertex have three distinct colors: if two ray colors were equal, their intervening native corner would have two equal adjacent colors. Hence its three actual corner slots form a triangle in the union color graph. Repeated COLOR pairs represented by more than one native corner remain distinct actual slots. If B has an adjacent repeated color, repeated ray colors and the two distinct B arms at its equal-color corner must instead be retained; the existing adjacent-repeat microstate enumeration does exactly this.

An actual support is the set of native corner triples occurring somewhere in T. It covers every corner of each occurring type. Following a full matched side to its other endpoint gives another actual triple in the same support. For the adjacent-repeat branch this is imposed simultaneously on all three rays of one native-arm microstate. These are necessary properties of T, not an assumption that every locally consistent atlas extends.

All finite component computations below take integer words, equality of their labels, native indices and sets/multisets as inputs. None takes numerical lengths, angle coordinates, a metric ordering of labels or an inequality between differently named lengths. Their labels can therefore be interpreted literally as the formal colors here. The original proofs' geometric implications are checked separately in Sections3–7.

## 3. Formal-ring realization does not require unequal physical lengths

A formal four-triangle ring consists of four injective A/B native side matches, each matching the SAME source color, and a fresh private symbol on each of the remaining four slots. These fresh symbols are distinct even when their physical lengths coincide. The two resulting words each have six formal symbols. Their union corner graph consists of four triangles with disjoint edges, covering the twelve actual corner slots; each triangle's actual angles sum to2pi.

The common symbols form a four-cycle. On each cycle edge one polygon has a private symbol inserted and the other has the direct common-to-common edge. Choose reflected or unreflected B reference so the common cyclic orders are opposite. Give the four common symbols alternating bits h(c). Take A0,A1,B0,B1. Pair each private side with the same native side of the other copy of its own type, and pair a common c side of A_i with the c side of B_(i xor h(c)), reversing boundary endpoints.

Every pairing has equal physical lengths. The quotient is connected, closed and orientable. At each inserted private symbol between common colors c,d, the two A corners and the corresponding B corner belong to one circular three-sector link, since h(c) and h(d) differ; the same holds with A/B exchanged. There are two copies of each of the four prescribed corner triples, so V=8,E=12,F=4 and Euler characteristic zero. All vertex angles are2pi. This is a compact flat torus, whose universal cover develops isometrically onto the Euclidean plane. Its deck group is a rank-two translation lattice, giving the unmarked periodic witness.

This construction is exactly Section2 of [the distinct-length proof](hexagon-holonomy-distinct-lengths.md), which already expressly permits different formal symbols to have equal numerical lengths. No geometric symmetry or accidental additional equality invalidates an indexed gluing.

## 4. Six colors on B: audit of every component

Both color graphs are simple six-cycles. Each is triangle-free, so T cannot use only one type. Every actual corner occurs. Private A colors have two neighbors in its cycle; their required triangle shortcut must be a B edge. Thus private colors are isolated, and three private colors would force a triangle in B's six-cycle. Consequently the number k of shared colors is at least4.

For k=4 the union is the formal four-triangle ring directly. For k=5,6 the complete integer-word classification in [hexagon-holonomy-distinct-lengths.md](hexagon-holonomy-distinct-lengths.md), Sections4–6, applies unchanged: normalize A=(0,1,2,3,4,5), with360 normalized words for k=5 and60 for k=6. The thirty surviving words form four classes:

    k5: B=(0,2,1,3,6,4), B=(0,2,6,3,1,4);
    k6: B=(0,1,5,3,4,2), B=(0,2,4,1,5,3).

In the first class, actual corner coverage selects complementary A/B choices for the duplicated corner pair, giving a legal ring after splitting one common COLOR. In the second, four triangles are forced by uniquely represented actual corners and give a ring. In the third, two independent two-set matchings select each duplicated actual corner once and give a ring after two color splits. In the fourth, the octahedral graph has the two four-triangle edge partitions F,H recorded in that proof. A corner-covering legal set either contains one partition directly or contains three triangles of one partition; the sum of all twelve native angles is8pi, forcing its fourth triangle to sum to2pi. This too gives a ring.

These steps use only color incidence, actual angle equations from T and the universal polygon angle sum. They do not use distinct physical lengths. Section3 supplies a periodic witness in every case. The existing independent verifier checks all420 normalized words,54 explicit four-face gluings and95 covering angle-support cases.

## 5. Five colors on B: adjacent repeated slots

Normalize B=(p,p,q,r,s,t), with five distinct COLORS. Its color graph is a five-cycle plus the loop p-p. A cannot occur alone. B alone cannot tile a trivalent source: its repeated-ray pure-B stars can involve only its loop and the two neighboring p-color corner pairs, or only the loop; the native q-r corner cannot occur in a pure-B star. Thus both types occur and all twelve actual corners occur.

The adjacent-repeat proof's private-color argument is unchanged: an A-private color u has two different A neighbors; at least one is not p, and the corresponding corner must use a three-distinct-color triangle, forcing both its neighbors shared. Three private A colors would force a triangle on distinct colors in B's five-cycle, impossible. Hence k>=4.

Use [hexagon-six-five-adjacent-periodicity-2026-10-15.md](hexagon-six-five-adjacent-periodicity-2026-10-15.md), Sections2–4, as the exact finite combinatorial lemma. Its complete3780-word domain retains132 words, in twelve dihedral classes. Its native-arm microstates allow repeated ray colors and both independently indexed equal-color B side slots. Simultaneous all-ray far-end closure retains eleven actual-corner-cover supports, each containing a formal four-triangle ring. All matching tests are color equality. Every actual support of T survives the pruning and belongs to this domain for the original proof's stated reasons. The four selected stars therefore have angle sums2pi, and Section3 gives the periodic unmarked escape.

No deterministic branch occurs here. In particular, no physical distinction between the two equal-color B sides is assumed by the microstate algorithm: their native indices, arm choices and both endpoints are retained explicitly.

## 6. Five colors on B: separation two

Normalize B=(p,q,p,r,s,t). Adjacent colors differ. Its simple color graph is a four-cycle with a pendant edge, the latter having two actual corner occurrences. Both this graph and A's six-cycle are triangle-free, forcing both types and all actual corners to occur. The private-color shortcut argument gives k>=4.

The exact finite lemma in [hexagon-six-five-separation-two-periodicity-2026-10-15.md](hexagon-six-five-separation-two-periodicity-2026-10-15.md), Sections1–3, has3780 normalized words,90 surviving words, eight classes and sixteen endpoint-closed corner-cover supports. Fourteen supports contain rings. The two exceptions are disjoint partitions of the twelve actual corner indices:

    class2: {(0,1,6),(2,3,7),(4,8,10),(5,9,11)};
    class8: {(0,1,11),(2,3,10),(4,7,9),(5,6,8)}.

Each support uses only three-distinct-COLOR ray stars. The ring cases are handled by Section3. The two partition cases are handled by the indexed deterministic argument in Section8 below. The old assertion that the physical polygons have no symmetry, based on unequal numerical lengths, is NOT imported; it is replaced by that explicit argument.

## 7. Five colors on B: opposite repeated slots

Normalize B=(p,q,r,p,s,t). Adjacent colors differ. Its graph consists of two triangles sharing p. If any pure-B star occurs, its actual native corners are {0,1,2} or {3,4,5}, using B-local indices in this paragraph. That triple sums to2pi, and B's total angle4pi makes the other triple sum to2pi too.

The existing two-B torus is still valid. Take two B faces. Within each face pair native side0 with native side3, reversing boundary endpoints; these have the same color p and hence equal geometric lengths. Pair each remaining side1,2,4,5 with the same native side in the other face. This yields a connected orientable closed surface with four circular three-corner vertex links: two of each displayed triple. Thus V=4,E=6,F=2, all angles are2pi, and it is a compact flat torus. Accidental equalities between other sides have no bearing on these specified pairings.

Otherwise every actual star is mixed, because A's graph is triangle-free. Both types and all native corners occur. The complete finite lemma in [hexagon-six-five-opposite-repeat-periodicity-2026-10-15.md](hexagon-six-five-opposite-repeat-periodicity-2026-10-15.md), Sections2–3, contains1890 normalized words,66 surviving words, eight classes and twelve endpoint-closed corner covers. Ten contain rings. The remaining two are disjoint partitions:

    class3: {(0,1,6),(2,7,10),(3,4,9),(5,8,11)};
    class7: {(0,1,11),(2,7,10),(3,4,8),(5,6,9)}.

All these enumerations concern color words and actual indices only. Section3 gives the ten ring escapes; Section8 gives the two partition escapes. The pure-B branch above covers a source that uses B alone as well as a mixed source containing one B-only vertex.

## 8. Indexed determinism, including physically symmetric polygons

This replaces the only geometric step in the source component proofs that used unequal numerical lengths to infer absence of polygon symmetries.

Suppose the actual support is one of the four partition supports in Sections6–7. Each actual corner slot c occurs in precisely one actual-star triple {c,d,e}; the three ray COLORS are distinct. Fix an indexed placed tile U with reference placement g_U and a native side i. Choose one endpoint corner c. Its star identifies d,e. The color of side i selects exactly one of d,e as the neighbor corner across i, since in a triangle just one other corner contains this ray color. That neighbor corner's two incident colors differ, so it also selects one native side j of its reference polygon. This fixes the neighbor type, native side and one endpoint correspondence. The other endpoint corresponds along the full side.

For the actual given polygon metrics, this ordered segment identification has exactly two Euclidean isometric extensions from the neighbor reference plane. Exactly one puts the neighbor interior opposite U's interior. Strict convexity gives the whole polygon a definite interior side at that boundary edge. Call the resulting complete relative map h_(type(U),i). Actual occurrence supplies existence and consistency at the far endpoint. The reference h depends only on U's TYPE AND NATIVE SIDE, since its support and color data do; it does not depend on absolute location, orientation, physical length inequalities or a choice among physically symmetric images.

Every occurrence already carries its indexed placement g_V from the colored source data. The determined corner and side are its ACTUAL indices; therefore

    g_V = g_U composed with h_(type(U),i).

This is an equality of complete indexed placement maps, not merely an equality of the unindexed polygon image. If the physical neighbor polygon has a symmetry, composing with that symmetry changes native index images unless it is the identity on all vertices. The derivation has fixed the image of two distinct reference endpoints and the interior half-plane, so there is no residual isometry ambiguity. Equivalently, six distinct colors on A and four singly occurring colors on B destroy any nontrivial color-preserving reference symmetry, even if the uncolored polygon is symmetric. No arbitrary extra state needs to be inferred from physical geometry.

The full-side adjacency graph is connected. With finitely many genuine compact polygon types, a compact set meets finitely many tiles; a generic compact path between two tile interiors avoids vertices and crosses finitely many full sides. For same-type tiles U,W set I=g_W g_U^(-1). The fixed h rules imply that I maps every indexed neighbor of U to the corresponding indexed neighbor of W. Propagate over the connected graph: I maps every source tile with its indexed placement to a tile of T with the corresponding placement. These images cover the plane, so the image collection is the whole tiling. Thus I preserves the entire FRAMED tiling.

Let G be its framed symmetry group. It has at most two tile orbits, and acts cocompactly. It is discrete: a sequence of symmetries converging to the identity must eventually fix a selected tile containing a fixed interior point; a bounded polygon has finitely many physical symmetries, and indexed framing is an additional restriction. Let N be its translation subgroup. If N were trivial, the orientation-preserving subgroup would inject into SO(2), be abelian, and consist of commuting rotations about one center; discreteness makes it finite. G would be finite, contradicting cocompactness. If N had rank one, its primitive vector would be preserved up to sign by the linear parts of G. Only four orthogonal maps preserve that axis, so G would be at most four cosets of a rank-one lattice and could not act cocompactly on the plane. Hence N has rank two.

Its two independent translations preserve T and therefore its underlying unmarked tiling. This is the [reviewed intrinsic determinism theorem](hexagon-five-length-intrinsic-determinism.md) with its hypotheses proved for these indexed source states. It does not assume that every unmarked tiling has unique neighbors. Only the chosen colored source must obey the derived rules.

Sections4–7 exhaust six or five B colors and all cyclic positions of the latter's repeated color. This completes the theorem. QED.

## 9. Actual-contact-component corollary

Let an unmarked pair of convex hexagons admit a full-side trivalent tiling T. Give each occurrence an indexed reference placement. Make a graph on the twelve native side slots, with an edge for every native slot pair occurring across some full seam anywhere in T; loops are permitted. Its connected components define E. Each E-class has one physical length, because every generating seam has equal lengths. Color each native side by its E-class. Then T satisfies the source-color matching rule.

If no E-class contains two A slots, A has six colors. If E restricted to B has at least five classes, the theorem applies and gives an unmarked doubly periodic escape. In particular, if physical B has at least five distinct numerical side lengths, its formal E-colors automatically number at least five, because an E-class cannot join unequal physical lengths.

Consequently, for a hypothetical aperiodic A5/B5 pair, in EVERY admitted defect-free tiling and EVERY chosen indexing of its occurrences, the two repeated A slots must belong to one E-class, and the two repeated B slots must belong to one E-class. Otherwise apply the theorem, exchanging species if appropriate. This is stronger than merely observing a repeated numerical side length. It asserts connectivity by seam types that actually occur. A compatible but nonoccurring seam cannot be used to establish a component.

The uncolored defect-free limit theorem is used only to obtain T from unrestricted tileability. Its original source tiling need not retain any coloring during passage to the limit. This corollary imposes no rules on the admitted tilings in the original aperiodicity definition.

## 10. Verification, dependencies and limits

The four independent existing verifiers were rerun with exit status0 during authoring:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/hexagon-holonomy-verify.py
    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/hexagon-six-five-independent-2026-10-15.py
    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/hexagon-six-five-adjacent-independent-2026-10-15.py
    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/hexagon-six-five-separation-three-independent-2026-10-15.py

They verify the SAME retained integer-word and native-index domains as the original theorems. No retained certificate was intentionally written, no registry entry was added, and no new solver or geometric enumeration was run. Successful replay certifies those finite lemmas; fresh hostile review of the new proof interpretation and symmetry treatment is still required.

Dependencies are exactly the four linked finite component proofs/certificates and their independent verifiers; formal-ring flat-torus realization; compact flat-surface development; the elementary indexed determinism argument reproduced here; and, only for the unrestricted contact-component application, the reviewed defect-free hexagon limit theorem. The arbitrary-B periodic-chain/SFT theorem is NOT used.

This proves a conditional periodic escape from a color-compatible SOURCE tiling. It supplies neither an aperiodic pair nor a classification when both species' repeated slots are joined by actual seam chains. No claim about pentagon-containing pairs follows. The main unrestricted problem remains unresolved.
