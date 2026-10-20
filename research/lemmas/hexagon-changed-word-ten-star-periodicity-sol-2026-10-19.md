# Changed native word: ten-star orbit and universal periodic escape

Date: 2026-10-19. Author: Sol. Status: proved within the restricted family; [independent Sol hostile review](../reviews/hexagon-changed-word-ten-star-periodicity-hostile-sol-fresh-2026-10-19.md) PASS. This is not the original unrestricted two-polygon problem.

## Exact statement

Let closed strictly convex hexagons have native side words A=(0,1,2,0,3,4), B=(0,0,1,2,3,1), with five distinct positive common color lengths. Arbitrary reflected copies and unrestricted contacts are admitted; either species may be omitted. If this pair tiles the plane, it admits a rank-two periodic tiling. The same conclusion holds when B is any cyclic shift or reversed cyclic shift of this word, keeping A fixed. These twelve words are exactly the full-corner-cover ten-star rows of the reviewed 180-word atlas.

Dependencies: the reviewed forced-dimer atlas; the reviewed defect-free trivalent edge-to-edge limit and monohedral periodic classification imported in `hexagon-five-four-fixed-native-unrestricted-periodicity-sol-2026-10-19.md`; and the reviewed universal equal-antiparallel-side strip construction cited in `hexagon-five-four-two-more-universal-omissions-2026-10-19.md`. No new general geometric classification is claimed here.

## Exact tiny support classification

The replay script reconstructs the ten signed stars and sole formal dimer corona from the original atlas implementation. It exhausts all 1024 subsets, with no symmetry reduction, requiring twelve native corners covered, an allowed opposite-endpoint continuation for every selected seam, and the sole ten-factor corona witnessed entirely by selected stars. Exactly fourteen masks survive:

    298,303,586,591,874,879,922,927,954,959,986,991,1018,1023.

The inclusion minima are 298,586,922. Each has augmented angle rank four. Their common angle equations, in units of pi, are

    a0+a1+a2=2, a3+a4+a5=2,
    b0+b1+b5=2, b2+b3+b4=2.

Every survivor contains a minimum; exact rational row reduction verifies these implications. This finite family need not be upward closed. Formal supports are necessary upper conditions only; they are not claims of mixed geometric realizability.

## Universal strip transfer

If a mixed trivalent source existed, its actual signed-star support would pass the stated necessary predicate by the same endpoint and actual-corona argument as the fixed-word synthesis. Hence its A satisfies a0+a1+a2=2pi. Its three corresponding exterior turns sum pi, so native sides0 and3 are antiparallel and have equal color0 length. The reviewed universal strip theorem then gives a two-orbit monohedral periodic tiling by the actual polygon A for every closed strictly convex metric satisfying those equations. This transfers the new support mechanism directly: no metric specialization, patch extension, or search for a larger quotient is required. The conclusion is conditional on an actual closed metric, not on merely assigning angles.

## Stronger separation observation

In fact none of the ten retained signed stars contains both species. An actual edge-to-edge seam between A and B would give a mixed star at its endpoints, impossible in this complete upper atlas. The adjacency graph of a locally finite polygonal edge-to-edge plane tiling is connected: a path between tile interiors can be perturbed to avoid the locally finite vertex set and cross finitely many edges. Thus every trivalent source is monohedral. This does not contradict the fourteen formal full-cover supports: those predicates permit disconnected formal A and B sectors and assert no plane realization. The support-based mixed-source implication above is valid but vacuous for this word.

For unrestricted tilings apply the imported defect-free limit. A monohedral limit supplies a periodic tiling by its occurring species through the imported monohedral hexagon theorem. The mixed limit alternative is excluded as above, or already yields the universal A strip escape. Therefore the restricted implication in the statement follows. No assertion that either arbitrary input metric tiles is made; metric existence and actual tilability remain separate.

## Dihedral extension and replay

Cyclic relabeling of a polygon and reversal of its native order do not alter its physical congruence class when reflections are admitted. Normalize B to the displayed representative and apply the result. A is unchanged. The script reads the reviewed 180-row certificate and verifies set equality between the twelve full-cover ten-star B rows and the twelve cyclic/reversed shifts of this representative; the full list is retained in its output.

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-changed-word-ten-star-support-sol-2026-10-19.py

Certificate: `research/certificates/hexagon-changed-word-ten-star-support-sol-2026-10-19.json`. Exact integer subset enumeration and Sage rational linear algebra, no solver, random seed, timeout, larger patch, or new torus domain. No claim of solving the original two-convex-tile problem. The independent audit passed.
