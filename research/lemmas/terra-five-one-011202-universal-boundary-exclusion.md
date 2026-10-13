# A011202 on B5+1: universal boundary-row angle obstruction

Date: 2026-10-13. Status: [independent hostile review VALID](../reviews/terra-five-one-011202-universal-boundary-fresh-hostile-review.md); exact native checks PASS. The [full-interval scope review](../reviews/five-one-full-strict-convex-angle-line-extension-review.md) extends this coverage mechanism to 108 < x < 126, x != 120. Restricted-family result, not the original research problem.

## Theorem and dependencies

Let x in (112.5,126), x!=120, y=720-5x, z=4x-360, r=360-2x, s=360-2y. If actual strictly convex A with native angle word (x,y,y,z,x,z) and actual strictly convex B with angle word (s,r,r,r,r,r) admit an unrestricted plane tiling, the same pair admits a periodic tiling. A and B side lengths may have arbitrary equality specializations. Every saturated defect-free field for this word omits B; the conclusion is a periodic pure-A escape, not a construction of a mixed tiling.

Imported dependencies are the independently reviewed saturation extraction/palette, actual honeycomb development, the [opposite BB row lemma](five-one-middle-mask-b-rows-and-bounded-a-strips.md), and settled unrestricted convex-hexagon monohedral periodic escape. Original partial contacts and reflections are handled by those reductions; the original tiling is not assumed to be a native row field. No no-AAA binary-lift theorem or positive closure search is needed.

The complete native star language is AAA(x,y,z), AAB(x,x,r), AAB(y,y,s), ABB(z,r,r). Saturated B has two B neighbours. A endpoint palettes are (01,11,12,02,02,02), with no22 edge, so the two outer BB masks are unavailable and the only possible BB mask is native{1,4}. Its opposite sides force full parallel B rows in the reviewed cell lattice, with A rows separating B rows.

## Width-one exclusion

B's AB endpoint palettes in this mask are02/12. Hence native A sides0(01) and1(11) both must be AA. They are adjacent. An A in a width-one strip between B rows has AA neighbours only in its two opposite row directions. No rotation or reflection maps adjacent private native sides0,1 to these two opposite positions. Thus each B-row face borders an A strip at least two rows wide, or an A half-plane, and the boundary A row has AAA inward and AAB outward vertices.

## Exact two-face boundary gate

Index row-direction AA sides by global2,5. For a boundary A row with B above, adjacent AB sides0,1 meet at global corner1, which must be z by ABB. For C=(0,1,1,2,0,2), the four of twelve native placements having z at corner1 are:

| State | Rotation/sign | Global corner colours0,...,5 |
|---|---|---|
| 0 | (0,-) | 0,2,0,2,1,1 |
| 1 | (2,+) | 1,2,0,2,0,1 |
| 2 | (4,+) | 0,2,0,1,1,2 |
| 3 | (4,-) | 0,2,1,1,0,2 |

For neighbouring left/right boundary A copies sharing side2/5, outward AAB A colours are (left corner2,right corner0); inward AAA A colours are (left corner3,right corner5). The former must be equal0/0 or1/1, the latter distinct. The complete16-pair gate accepts exactly:

| Directed states | Outward colours | Inward colours | Required native AA equality |
|---|---|---|---|
| 0→0 | x,x | z,y | a3=a0 |
| 1→0 | x,x | z,y | a4=a0 |
| 2→2 | x,x | y,z | a0=a3 |
| 2→3 | x,x | y,z | a0=a4 |

Every accepted outward vertex is x/x; there is no y/y option. The only bi-infinite native row paths are constant state0 or2, requiringa0=a3. This exact transfer information is preserved, but global exclusion uses only the x/x property, not the metric relation or periodic boundary.

The opposite boundary is checked directly, with AB sides3,4 and global z corner4. Its four placements are (1,+),(1,-),(3,-),(5,+), with corner profiles respectively(1,1,2,0,2,0),(1,0,2,0,2,1),(2,1,1,0,2,1),(2,0,1,1,2,0). Outward pair (left corner3,right corner5) and inward pair (left corner2,right corner0) give exactly the same directed graph and metric equalities. Thus both B-row faces universally require x/x, with reflections included and without assuming an intrinsic symmetry of A.

## B-angle contradiction and periodic escape

Every B has exactly two AAB vertices, on its two row faces, and four ABB vertices. Both boundary rows demand x/x, so both its AAB corners must be r. ABB also requires its B corners to be r. Thus every one of its six native corners would have to be r, leaving no place for its unique mandatory s corner. Equivalently, native AAB corners0 and3 of the {1,4} mask are s and r, so the s face cannot meet the forced x/x boundary. No mixed saturated B row exists.

If the actual pair tiles, reviewed extraction must give an all-A plane tiling. The settled monohedral convex-hexagon classification gives a periodic A-only tiling admitted by the same pair. No length distinctness, metric enumeration, local extension assumption, or finite-model theorem enters this conclusion. In particular every coarsening of the six A side lengths is covered by the same angle-only proof.

## Finite domain and replay

Before computation the domain was stated as2 faces*12*12 native A orientation pairs plus12 width-one poses. Possible outcomes were a missing y-facing boundary (then a uniform B exclusion), or a surviving boundary requiring exact metric/positive closure next. The uniform exclusion occurred, so203 length partitions and geometric closure were unnecessary and were not searched.

Producer, exact certificate and independent checker are:

- research/searches/terra-five-one-011202-boundary-transfer.py
- research/certificates/terra-five-one-011202-boundary-transfer.json
- research/reviews/verify_terra_five_one_011202_boundary_transfer.py

    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python research/searches/terra-five-one-011202-boundary-transfer.py
    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_terra_five_one_011202_boundary_transfer.py

The independent checker imports no producer code. It constructs native edge identities from consecutive native vertex indices, scans all288 orientation pairs directly, verifies all exact side equalities and cyclic states, and checks all12 opposite-AA width-one cases against the certificate. MISE_AUTO_INSTALL=0 skips installation of unrelated tools without waiving provenance verification.

A legal boundary cycle remains only local compatibility; no global strip, mixed tilability or aperiodicity is inferred from one. This theorem does not cover other native words, other angle strata/multiplicities or the original global acceptance criteria. The root portfolio retains genuinely different construction and structural routes after this family checkpoint.
