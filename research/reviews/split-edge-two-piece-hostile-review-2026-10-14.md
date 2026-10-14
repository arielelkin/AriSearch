# Independent hostile review: one-breakpoint two-piece edge exchange

Date: 2026-10-14. Reviewer: fresh independent adversarial reviewer. Source: [the proposed template](../searches/ammann-split-edge-two-recipient-gate-2026-10-14.md), read after deriving the local obstruction. Verdict: **INVALID as a strict convex pentagon construction** for the exact template below. This is a local exclusion only, not an impossibility theorem for all split-edge interfaces.

## Claim and finite case domain

For each affected unit source edge `U V`, take one interior arrow-defined point `M`, a donor triangle `U V t` with apex anywhere strictly on the donor side, and a receiving quadrilateral `U V q p` on the other side. Divide the donor triangle by `M t`, divide the receiver by `M R` with `R=(p+q)/2`, and exchange both halves across the edge. The two proposed output boundary words are `(U,t,M,R,p)` and `(M,t,V,q,R)`. Source rhomb type is thin or thick, opposite donor-edge parity is one of two choices, and edge arrows can reverse. The finding below covers all these cases because it is invariant under rigid motions and edge reversal.

The proposed sector allocation is combinatorially complete *conditional on* valid source sectors: `U M t` and `M V t` partition the donor triangle; `U M R p` and `M V q R` partition the receiver quadrilateral when `R` lies on its opposite side `p q`. Each half of the physical edge belongs to one donor and one receiver sector, so gluing pairs uses each of these four sectors once. I checked the declared `(thin,0)`, `(thin,1)`, `(thick,0)`, `(thick,1)` parity cases: opposite-edge donor choices give the opposite role across each shared edge, while reversing the receiver's edge order swaps the interval names but preserves the physical pairings. This conditional statement does not certify the underlying asymmetric two-node source partition or global two-class congruence.

## Exact obstruction at the breakpoint

Use an isometry and unit-edge normalization to set

`U=(0,0), V=(1,0), M=(a,0), t=(b,-h), R=(r,k)`, with `0<a<1`, `h>0`, and `k>0`. No relation between `a` and `b` is needed.

The first proposed output follows `U,t,M,R,p`. Its signed turn at `M` is

`det(M-t,R-M)=det((a-b,h),(r-a,k))=(a-b)k-h(r-a)=C`.

The second follows `M,t,V,q,R`. Its signed turn at `M`, read cyclically as `R,M,t`, is

`det(M-R,t-M)=det((a-r,-k),(b-a,-h))=-C`.

Thus the two signs are opposite. If `C != 0`, at least one word has a reflex turn and cannot be strictly convex with its stated orientation. If `C=0`, `t,M,R` are collinear; because `t` and `R` are on opposite sides of the source edge, `M` lies between them, so both words are straight at `M`. The breakpoint is a fake additional corner and each output has at most four genuine corners. Reflection or reversal interchanges the two signs; it cannot make both positive. No numerical parameter search is needed.

The contradiction uses only the two-piece pairing and the degree-two junction at `M`. It remains valid for any donor apex offset, and even if all source-sector partitions, other endpoint turns, arrow cases, and global compatibility were to pass. A repair must change the incidence at the breakpoint, for example by having at least three output sectors there, or change how the pieces are paired and counted. Such changes require a new finite template and fresh edge-allocation check before another solve.

No repaired result is claimed. Universal unmarked decoding, homogeneous-carrier omission, and unrestricted tiling remain untested because the strict five-corner gate already fails.

The [small independent checker](verify_new_interface_stopping_gates_2026_10_14.py) asserts the general-apex polynomial turn identity and its zero-turn collinearity relation without importing the producer. Read-only replay: `mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_new_interface_stopping_gates_2026_10_14.py`. Result: PASS.
