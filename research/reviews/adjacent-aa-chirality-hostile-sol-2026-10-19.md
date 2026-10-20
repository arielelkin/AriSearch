# Independent hostile review: adjacent-AA chirality return

Date: 2026-10-19. Scope: `AAABBACC` and `AAABCABC`, fixed strictly convex metric Q, unit regular pentagon P, arbitrary reflections, 108 < alpha < 126. Reviewed `research/searches/adjacent-aa-chirality-sol-2026-10-19.md` against the balanced-octagon purification report and reviewed complementary-angle necessary theorem.

**Verdict: PASS for the stated saturated-tiling translation theorem.** The physical incidence assertion needed for the recurrence is correct. No abstract colored-edge counterexample survives its two local equations, even after relaxing the geometric restrictions on the transverse matching. Combining the theorem with purification proves that any admitted tiling has a periodic tiling in its translation-orbit closure. It does not prove that every original, possibly defective tiling is periodic, or that either fixed metric shape tiles.

## Physical dart audit

Number a pentagon cyclically with AA-facing side 0. Its species sides are PQ, PP, PQ, PQ, PP. Write V_ij for the corner between sides i and j. The four PPA corners are V_40, V_01, V_12, V_34; the unique PBC corner is V_23. This numbering uses no orientation of Q.

Choose the marked PP side to be side 1 of P_(2k). Its owner occupies V_01, where the selected AA side 0 meets the marked edge. At the other endpoint V_12 the third tile is the isolated-A guest E_k. Across the marked edge the mate P_(2k+1) has the same owner at its selected endpoint and the same guest at the other endpoint. In a cyclic numbering adapted to that mate, the marked edge is side 4 and the guest touches side 3. Thus the guest faces side 2 of P_(2k) and side 3 of P_(2k+1). Each such full side ends at that pentagon's unique V_23. This proves that precisely the same guest appears at both PBC corners; it is not an inference from a drawing or an assumed transverse ordering.

The remaining side 3 of P_(2k) faces Q_(k-1). Indeed its other endpoint V_34 lies on the unmarked PP edge to P_(2k-1), where the latter's selected AA side ends. That Q is the owner of the previous marked dimer. Likewise side 2 of P_(2k+1) faces Q_(k+1). Consequently the PBC triples are exactly (P_(2k), Q_(k-1), E_k) and (P_(2k+1), E_k, Q_(k+1)). Reflection exchanges cyclic numbering but preserves these physical incidences.

A wording trap deserves explicit exclusion: Q_k and E_k, the owner and guest of the same marked dimer, do not share these two PBC corners. The neighboring owners Q_(k-1) and Q_(k+1) share one each with E_k. The manuscript has the correct version.

The guest corner is isolated A because neither incident side is selected AA. An endpoint A of the AAA run would force one selected AA side there; its middle A would force two. Conversely an isolated-A occurrence must sit opposite the middle AAA occurrence of a marked edge: selecting neither endpoint there means selecting both at the opposite endpoint. This gives both directions of the claimed correspondence.

## Reflections and recurrence

For both words the two external ends of the AAA chain have opposite labels, and the two neighbors of isolated A have opposite labels. Explicitly, the native AAA external pair is (B,C), while the native isolated pair is (B,C) for AAABBACC and (C,B) for AAABCABC. Reflection reverses the order of either pair and retains complementarity. No identification of an isolated-end label with a particular native AAA-end label is needed.

The preceding owner contributes its forward label s_(k-1) at the even pentagon's PBC corner. The following owner contributes its backward label complement(s_(k+1)) at the odd pentagon's PBC corner. Since PBC requires opposite physical labels, the guest labels are X_k = complement(s_(k-1)) and Y_k = s_(k+1). Its isolated pair also requires Y_k = complement(X_k). Hence s_(k+1) = s_(k-1), independently of every reflection choice and of the guest owner's location.

These labels determine the rooted placement. There is only one AAA run, and its two unit AA edges fix the root frame and occupied sector. A rigid copy has at most the two placements obtained by reversing the identification of the two native AA edges. Their forward labels differ, because B and C have distinct angles throughout the open interval, including alpha = 120. Thus equality of s at k and k+2 really is equality of the metric tile after translation, not merely of its angle word. Unknown QQ lengths can invalidate a state assignment but cannot produce an extra rooted placement.

## Counterexample search in a relaxed colored edge map

I independently tested two cyclic carriers of three marked dimers each. I allowed all 6! permutations f of guest owners among the six dimers, including maps that mix carriers arbitrarily. For each of 2^6 owner label fields s, the even PBC equations uniquely assign the first isolated flank label x to every guest owner; I then tested the odd PBC equations using the opposite second flank. This checks 46,080 assignments, accepts 2,880, and finds zero violations of s_(k+1) = s_(k-1). On these odd cycles, the accepted owner fields are precisely the four choices constant on each carrier, for each of the 720 permutations.

This is a deliberately relaxed model: it omits the additional metric relation between a guest owner's own rooted placement and its isolated flank, QQ lengths, and planar realizability. A counterexample in the actual tiling would also violate the recurrence in this relaxation. The finite check is supporting evidence; the two equations above prove exclusion for arbitrary infinite carriers and arbitrary f. No finite model is asserted to embed as a plane tiling.

## Global return and the role of matching

Marked and unmarked PP edges alternate, forcing the turn pattern ++-- up to reversal and phase. With step length 2r, the four directions 0, 36, 72, 36 degrees give the nonzero displacement w of length 4r(1+cos36 degrees). The pentagon frame and selected AA side return after four steps. Every step has strictly positive projection on w, so the center path is a proper embedded graph with bounded transverse deviation. In particular it cannot close into a finite component.

Different components have disjoint center paths: segments are inside their pentagons except at their own shared PP midpoint. A proper path with bounded deviation from an axis separates the plane, and a path with a nonparallel axis has opposite tails on opposite sides. Thus nonparallel components would intersect. All component axes are parallel; their four-step return vectors have the same norm, so they are w or -w. Invariance under either sign gives invariance under the same common vector w.

On each component the rooted dimer frame advances from k to k+2 under that vector, and the recurrence fixes its owner label. Consequently every owned Q is sent to its translated copy. Every Q has its unique AAA-owned marked dimer, so this accounts for every Q, as well as every P. Translation is a bijection on the tile family, since both positive and negative returns hold.

The matching f is genuinely a bijection: every Q supplies one isolated-A guest occurrence, and each marked dimer receives exactly one. Distinct occurrences cannot identify different physical dimers. Its bijectivity is useful for describing the incidence structure, but is not logically needed in the return proof. That proof uses only that each marked dimer's two pentagons share one guest with complementary isolated flanks. It does not need f to commute with carrier shifts, preserve a carrier, or have bounded displacement. Once all tiles return, translation-equivariance of f follows from its geometric definition.

The resonance exclusion of BBB is pointwise for these length-two non-A runs and has already been justified in the reviewed gate. The global conclusion remains conditional on saturation, with the change of tiling in the purification step explicitly retained.
