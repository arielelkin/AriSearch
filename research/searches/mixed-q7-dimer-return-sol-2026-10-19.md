# Mixed Q7 dimer return gate — 2026-10-19

Status: **the proposed conserved physical direction / nonnegative physical signed-turn mechanism fails**. Stop this route under protocol §5. This is an exact cocycle calculation and a local counterexample to those particular invariants, not a plane tiling, plane obstruction, or periodic carrier. All four mixed words remain unresolved.

## Domain and dependencies

Read research-problem.md, research-protocol.md §5, the latest mixed-Q7 log checkpoint, the reviewed PP purification theorem and review, the reviewed 124/128 immediate strand atlas, and the four-face UNSAT report. Work is restricted to the four words ABBCCBC, ABBCCCB, ABCBBCC, ACBBBCC. No quotient enlargement, patch growth, alpha grid, or strand embedding assumption was used. The newly reviewed fact is that one may work conditionally in a defect-free tiling with every P in a PP dimer.

Every Q has a distinguished PP dimer at its A corner: its two P neighbors on sides 0 and 6 meet along a unit PP side. In a perfect-matching tiling this pair is their unique dimer. A dimer has two A endpoints and therefore two Q owners. The calculation below concerns **Q-marked dimers**, with the axis directed from the owner's A endpoint to the other PP endpoint. Forgetting the owner produces an unoriented physical axis. There is no uniquely defined unmarked dimer successor supplied by the PP theorem alone.

## Exact induced cocycle

Write Q vertices q_j counterclockwise, q_0=0, and edge headings theta_0=0,

    theta_j = sum_{k=1}^j (180-angle_k).

For a BB side e and a CC side f, let their common necessary length be L>0. The two full-edge opposite-interior placements of a neighbor Q are exactly

    U(x)=u*x+t_u,
    u=-exp(i*(theta_e-theta_f)),
    t_u=q_e-u*q_(f+1),

    R(x)=c*conj(x)+t_r,
    c=exp(i*(theta_e+theta_f)),
    t_r=q_e-c*conj(q_f).

These formulas exhaust the two native reflection parities. They follow by mapping the CC endpoints to BB endpoints in reversed order for U and equal order for R. Let the root owner-dimer axis be v, |v|=1, and midpoint m=v/2. The induced marked-dimer frames are

    U: (v,m) -> (u*v, u*m+t_u),
    R: (v,m) -> (c*conj(v), c*conj(m)+t_r).

Thus the exact translations are (u-1)m+t_u and c*conj(m)+t_r-m. For an incoming frame G(x)=a*x+b or a*conj(x)+b, compose G with U or R; the standard conjugation in the second case gives the complete orientation/translation cocycle. This is valid for arbitrary admissible positive metrics and all real 108<alpha<126. It also covers the defect-free alpha120 limit.

The four words have (e,f)=(1,3),(1,3),(3,5),(3,5), respectively. In every case theta_e-theta_f=-108 degrees. Therefore

    u=exp(i*72 degrees)

identically, with no alpha dependence. The reflected coefficient c has heading 468-2alpha degrees for the first two words and 684-2alpha degrees for the last two. A BC seam has only the orientation-preserving endpoint-complementary placement; the same endpoint formula determines its coefficient and translation. Nothing about BC seams cancels the immediate BB/CC dimer-axis change pointwise.

## Falsification and exact certificate

A conserved physical dimer line would require u*v to be parallel to v. But u is neither +1 nor -1, so the two owner dimers across an unreflected BB-to-CC seam have different physical axes, with line angle 72 degrees. This holds universally wherever that seam is realized.

A nonnegative **physical signed turn**, oriented by native BB-to-CC succession, also fails reflection independence: reflect the entire valid immediate configuration. The native succession is unchanged, but its physical turn becomes -72 degrees. Algebraically, for any reflected frame with coefficient c,

    c*conj(u)/c = exp(-i*72 degrees).

This is a parity counterexample, not a claim that an arbitrary formal sequence of seam maps embeds. One could count a parity-compensated native turn as always +72 degrees; that quantity is a bookkeeping cocycle, not a monotone physical turning obstruction. No bound on its accumulated winding follows without a proved embedded global carrier.

For concrete geometric realizability, the replay reads the existing reviewed 124/128 strand certificate, whose five immediate seam neighborhoods and all four incoming/outgoing parity combinations are interior-disjoint. It extracts each root PP axis directly from the two common pentagon vertices, checks unit length, verifies u=z^36 for z=exp(2*pi*i/180), and retains both exact transformed dimer frames and translations. All four words pass. This reuses the old certificate, and does not enumerate any new patch. The new PP theorem cannot remove one of these local configurations merely by assigning the two A-adjacent P copies to a dimer: they already share their unique PP side. Whether the other boundary P copies admit all their partners in a plane remains an independent extension problem.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch sage research/searches/mixed-q7-dimer-return-sol-2026-10-19.sage

Output: mixed-q7-dimer-return-sol-2026-10-19.json beside this report. Exact arithmetic is CyclotomicField(180); no seed, solver, tolerance, or timeout. All assertions passed. JSON serialization initially failed on a Sage integer after the mathematical assertions; adding explicit integer serialization fixed it, and the complete replay passed.

## Stopping obligation

The PP matching adds a canonical A-dimer to each Q, but its QQ transport carries exactly the old reflected isometry cocycle; its unreflected generator already rotates the physical axis by 72 degrees. Consequently it does not supply the proposed common direction or reflection-independent nonnegative signed turn. The missing theorem remains a restriction on globally realizable reflected seam sequences, or a proved complete repeatable transverse carrier. Neither follows from local matching or finite rotational state. Stop this specific invariant route. No Git or discovery-log edits were made.
