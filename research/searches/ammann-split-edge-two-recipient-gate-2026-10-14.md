# Split-edge two-recipient Ammann interface: convexity obstruction

Date: 2026-10-14. Status: **falsified as a strict-convex-pentagon topology**, independently hostile-reviewed; see the [fresh review](../reviews/split-edge-two-piece-hostile-review-2026-10-14.md). This is one bounded incidence-design cycle, not a classification of split-edge surgery and not a two-tile result.

## Finite source-sector template

Use an edge-to-edge legal marked thin/thick rhomb source from the reviewed Ammann forcing theorem, Lemmas 5–7. Label each rhomb `A,B,C,D` counterclockwise, with edge `i` running from vertex `i` to `i+1` modulo 4. Bipartite vertex coloring chooses donor parity `k=0` or `1`: donor edges are `k,k+2`, and receiving edges are `k+1,k+3`. Across each shared source edge the roles are opposite. The four cases are `(thin,0)`, `(thin,1)`, `(thick,0)`, `(thick,1)`; each has two donor and two receiving edges. Their native arrow/mark list, in edge order `AB,BC,CD,DA`, is:

| Source | Native arrows | Donors if `k=0` | Donors if `k=1` |
|---|---|---|---|
| thin | `X A→B`, `X C→B`, `Y C→D`, `Y A→D` | `AB,CD` | `BC,DA` |
| thick | `X A→B`, `Y B→C`, `Y D→C`, `X A→D` | `AB,CD` | `BC,DA` |

For each physical source edge with arrow tail `T`, head `H`, and mark `Z∈{X,Y}`, set one **interior** subdivision point `M=T+a_Z(H−T)`, `0<a_Z<1`. Its physical position is the same from both adjacent rhombs. On a donor edge `(U,V)`, put apex `t=M+h_Z n_in`, `h_Z>0`, where `n_in` is its unit normal toward the donor rhomb. The donor sector is triangle `(U,V,t)`. Its two separately assigned pieces are triangles `(U,M,t)` and `(M,V,t)`. There is exactly one mark on this edge and no additional source-edge subdivision.

Retain the prior two-node tree **inside** each rhomb. Its two donor apexes are the nodes of that tree. A receiving-edge sector, written counterclockwise, is quad `(U,V,q,p)`, where `q` is the donor node following `V` and `p` is the donor node preceding `U`. Choose `R=(p+q)/2`, on the quad's inner side `p-q`. The chord `M-R` splits this quad into `(U,M,R,p)` and `(M,V,q,R)`. Thus each source rhomb has four half-triangle sectors and four half-quad sectors. This is a finite, explicit source partition whenever the original two-node sectors are embedded; no patch growth or source-vertex census is involved.

On a shared edge, the donor's piece `(U,M,t)` goes to the receiver's piece incident to the **same physical segment** `UM`; `(M,V,t)` goes to the piece incident to `MV`. Reversing the receiving rhomb's edge order swaps the labels of those two pieces but does not change their physical assignment. Every donor half is used once, every receiver half is used once, and the two interval segments are covered once on each side. The resulting two output boundary words at a receiving edge are, after orienting `(U,V)` counterclockwise for the receiver,

```
L = (U,t,M,R,p),
R_out = (M,t,V,q,R).
```

The external donor triangle and internal receiver quad lie on opposite sides of `UV`. The four source cases above share these two boundary words; the arrow determines `M,t`, and the donor parity determines `p,q`. Both words have five *formal* vertices if no adjacent vertices coincide. The edge `t-M-R` is their entire common boundary; `M` is the only source-edge breakpoint. The area identity for each receiver is exact by dissection:

`area(L)+area(R_out)=area(U,V,q,p)+area(U,V,t)`.

Summing over all receiving edges of the infinite source counts each quad and donor triangle exactly once, hence gives an exact full-plane partition whenever the local sectors are valid. This area identity is a necessary gate; it does not imply convexity or two congruence classes.

## Exact strict-convexity gate

At `M`, the consecutive turn of `L` is

`cross(M−t,R−M)`.

The consecutive turn of `R_out` at its cyclic first vertex `M` is

`cross(M−R,t−M) = −cross(M−t,R−M)`.

Therefore both outputs cannot be strictly convex. If the cross product is nonzero, one of the two words has a reflex corner at `M`. If it is zero, `t,M,R` are collinear. Since `t` and `R` lie on opposite sides of the source edge and `M` lies on it, `M` is between `t` and `R`; it is a straight, suppressed vertex in **both** outputs. The actual output boundaries then have at most four genuine corners. The specified requirement for pentagonal or higher strict-convex outputs fails in every one of the four source-type/role cases, for all admissible `a_X,a_Y,h_X,h_Y` and every admissible internal position `R` on `p-q`. This argument does not depend on the midpoint choice for `R`.

No congruence enumeration or nonlinear solve is warranted. The failure is a topological two-sided turn obstruction at a degree-two interface point, independent of the closed directed-offset parameter classification. This template genuinely splits the old complete unit-base donor triangle into two separately assigned pieces and changes the number of output pieces, but a further incidence change is required: at the marked source-edge point, the two final output tiles cannot have the same bent interface as their only local boundary if both are to have genuine convex corners. No such alternative template is claimed here.

The source geometry and native arrows are from [the forcing theorem](../lemmas/ammann-forcing-aperiodicity.md) and [the directed-offset topology](ammann-directed-offset-gate-2026-10-14.md). The earlier whole-triangle periodic omission construction is [here](ammann-bipartite-tree-pentagons-2026-10-14.md). This gate neither reopens the closed directed-offset four-parameter family nor extends to arbitrary convex polygons.
