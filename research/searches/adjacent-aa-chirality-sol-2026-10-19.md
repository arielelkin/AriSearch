# Adjacent-AA octagons: reflected endpoint return closes the carrier

Date: 2026-10-19. Analytic derivation; independent review pending. Scope: fixed strictly convex Q with word AAABBACC or AAABCABC, A=144, B=alpha, C=252-alpha, 108<alpha<126, and unit regular pentagon P. All reflections allowed. This note concerns saturated tilings, where every P receives one AA edge. The balanced-octagon necessary theorem excludes BBB exactly even at alpha=120.

**Conclusion.** Every such saturated tiling has a common nonzero translation. The transverse matching of dimers need not be classified: the two PBC equations on each dimer force the owner's reflected placement to repeat after two dimers along every backbone.

## 1. Physical dimers and transverse matching

A P with its AA-facing side numbered 0 has PP sides 1,4 and its other PQ sides 2,3. Its unique PBC corner is the meeting of sides 2,3. Every PP component is a doubly infinite chain; the geometric return below also excludes finite components.

Write the triple-A run of Q as A0,A1,A2, and its isolated A as I. Its two AA sides face two P tiles sharing a PP edge at A1. Call this the marked edge and its pair the owned dimer. Every P belongs to exactly one such dimer: its AA-facing edge belongs to a unique Q, whose other AA-facing P is its mate. PP edges alternate marked and unmarked.

At a marked edge, the endpoint adjacent to both selected AA-facing sides has the owner's middle corner A1. At its opposite endpoint neither P's selected side is adjacent. The third tile must therefore have an isolated A corner. Indeed an end of a triple-A run would put an AA-facing side against one of these P tiles, and its middle would put one against both. Conversely an isolated A corner has neither incident Q side AA; the PP edge between its two P neighbors cannot be unmarked, because at an unmarked edge each endpoint is selected by exactly one P. This last statement follows directly from the selected ends: both selected ends at one endpoint makes that edge marked; neither selected there makes the opposite endpoint selected by both.

Thus every marked dimer has exactly one guest Q at the endpoint opposite its owner. Every Q supplies exactly one guest occurrence, at I. If dimers are identified with their owner Q, define f(D) to be the dimer at which owner(D)'s isolated A sits. Then f is a bijection on all physical dimers. The guest at D is owner(f^{-1}(D)). This is a matching of MARKED edges, not unmarked edges. No commutation of f with any shift is assumed.

## 2. Backbone return

Let r=1/(2 tan36 degrees), the P apothem. Successive P centers are distance 2r apart. Because their two PP sides have outward normals separated by144 degrees, the signed turn at each P is plus or minus36 degrees. Across a PP edge, selecting the same physical endpoint on both P tiles gives equal successive turn signs; selecting opposite endpoints gives opposite signs. Marked edges select the same endpoint; unmarked edges select opposite endpoints. Hence, up to cyclic shift and reversal, the turn sequence is ++--.

Index P along one backbone so dimer k is (P_{2k},P_{2k+1}), with owner Q_k. Successive displacement directions can be normalized to 0,36,72,36 degrees. Therefore

    P_{n+4}=P_n+v,
    v=2r(1+2 exp(i36 degrees)+exp(i72 degrees)),
    |v|=4r(1+cos36 degrees)>0.

This is equality of physical polygons with their selected AA edges, since their PP-side and AA-side frames also repeat. Each center path is a proper embedded graph over its v-axis and stays within bounded distance of that line. The same local calculation rules out finite PP components.

## 3. Complete reflected endpoint recurrence

A Q anchored on a marked dimer has exactly two possible physical placements, allowing reflection: its triple-A unit-side chain is already fixed, and its two orientations exchange the B and C at the ends of that chain. They are distinct because B is not C anywhere in the open interval (equality would occur only at126).

For Q_k define F_k as its non-A endpoint on the triple-run flank toward P_{2k+2}; define H_k as its non-A endpoint on the flank toward P_{2k-1}. Put s_k=label(F_k). In BOTH words,

    label(H_k)=complement(s_k),  complement(B)=C.

The two non-A neighbors of the isolated A are also opposite labels in BOTH words. For guest E_k=owner(f^{-1}(D_k)), let X_k be its isolated-flank non-A endpoint incident at the PBC corner of P_{2k}; let Y_k be the analogous endpoint at P_{2k+1}. Then label(Y_k)=complement(label(X_k)). These are physical endpoint definitions, so they include reflections without any native counterclockwise assumption.

At the unique PBC corner of P_{2k}, the other tiles are Q_{k-1} and E_k. At that of P_{2k+1}, they are E_k and Q_{k+1}. Consequently

    label(X_k)=complement(s_{k-1}),
    label(Y_k)=s_{k+1}.

Combining with the isolated-flank complement relation gives

    s_{k+1}=s_{k-1}.                         (R)

Explicit exhaustive binary table:

| s_{k-1} | s_{k+1} | forced (X_k,Y_k) | isolated-A flanks legal? |
|---|---|---|---|
| B | B | C,B | yes |
| B | C | C,C | no |
| C | B | B,B | no |
| C | C | B,C | yes |

Reflection reverses the physical association of native endpoints with F,H or X,Y, but preserves each complementary pair and therefore preserves this table. The two words differ in which native QQ side carries the resulting pair, not in recurrence (R).

For completeness, the QQ connections are exactly those already used at these PBC vertices. Each Q has two QQ sides, each joining one triple-run terminal to one isolated-run terminal. AAABBACC has native QQ sides BB and CC, which must meet CC and BB respectively. AAABCABC has two BC sides, each meeting BC with complementary physical endpoint labels. At dimer k the guest's two QQ sides meet Q_{k-1} and Q_{k+1}. Equality of their actual native lengths can restrict the remaining binary states further, but cannot remove (R). No additional Q-only corner or QQ connection remains: every non-A corner is at one of these PBC stars.

Thus s_{k+2}=s_k. Translation by v sends the rooted dimer frame k to k+2 without reversing its forward direction. Its terminal label s fixes which of the two rooted placements occurs, proving

    Q_{k+2}=Q_k+v.

Every owned decorated backbone is invariant under v. This result does not require f itself to be selected in advance, bounded in chain coordinates, or proved to commute with a shift. Once every tile has been proved to return, its geometrically defined incidence map f necessarily returns as well.

## 4. One period for the whole plane

Center paths of different PP backbones are disjoint: each lies in its P interiors except at shared PP midpoints, and a shared midpoint would merge the components. Proper paths with nonparallel axes intersect, because either tail of the second eventually lies on a different side of the first graph. Thus every backbone axis is parallel. Their return vectors have the same length above and differ only by sign. All owned decorated backbones therefore share the translation v of either sign. Every P and every Q belongs to an owned backbone, so the entire saturated tiling has this nonzero period.

## Scope and audit

The essential finite-state return is (R), not a hypothesis about the transverse matching. No plane extension of an arbitrary state field is claimed, and no patch growth, torus search, or numerical alpha sampling is used. The proof applies at120 because balanced octagon words have no BBB corner. To pass from an arbitrary admitted tiling to a saturated one, the usual nonnegative AA-capacity deficit and translated compactness argument is needed; that purification is an input here rather than reproved. The crucial audit is that both PBC corners of a marked dimer see the SAME isolated-A guest, and that the neighboring owners are Q_{k-1},Q_{k+1}; section1 and the explicit side numbering give these incidences.
