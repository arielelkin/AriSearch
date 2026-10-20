# Independent hostile review: mixed-Q7 owner-dimer transport

Date: 2026-10-19. Verdict: **PASS within the stated local cocycle and route-stopping scope.** No plane-extension, plane-obstruction, or periodicity theorem is established. The physical-axis invariant fails as an identity of admissible immediate seam geometry; whether a particular seam extends to a whole purified tiling is not proved.

Reviewed the producer Markdown/Sage/JSON, the PP purification theorem and hostile review, the earlier exact 124/128 gate and review, and the immediate AA/BB strand atlas source and certificate. Replayed the producer exact script successfully.

## Independent reconstruction and side indexing

Use native counterclockwise Q vertices q0,...,q6, q0=A=144 degrees, and unit side 0 along the positive real axis. Let B=alpha, C=252-alpha. Sides 0,2,4,6 face P in the defect-free reduction. The QQ slots are 1,3,5. Directly reading the four words gives:

| word | BB side e | CC side f | theta_e | theta_f |
|---|---:|---:|---|---|
| ABBCCBC | 1 | 3 | 180-alpha | 288-alpha |
| ABBCCCB | 1 | 3 | 180-alpha | 288-alpha |
| ABCBBCC | 3 | 5 | 288-alpha | 396-alpha |
| ACBBBCC | 3 | 5 | 288-alpha | 396-alpha |

Thus theta_e-theta_f=-108 degrees without specializing alpha. The indexing agrees with the older atlas after its A=124,B=128 are renamed B,C and the initial 144 is prefixed. The producer selects the older AA slot, correctly the new BB slot. Its four-row ordering agrees with the certificate; zip relies on that ordering rather than independently asserting word identity, a minor robustness limitation rather than a present error.

Across BB-to-CC, opposite interiors and preserved orientation force q_(f+1) to q_e and q_f to q_(e+1). Their difference gives u=-exp(i(theta_e-theta_f))=exp(i72 degrees), and t_u=q_e-u*q_(f+1). With reversed orientation the endpoint order agrees: q_f maps to q_e. Hence c=exp(i(theta_e+theta_f)), t_r=q_e-c*conj(q_f). These are exactly the producer formulas. Equal BB/CC lengths cancel in both coefficients. Translations retain the full metric dependence. Therefore the proof applies to every admissible positive metric and every real 108<alpha<126, conditionally on defect-free QQ slots at resonance.

In the reverse CC-to-BB direction the preserving map has coefficient exp(-i72 degrees); its translation is -conj(u)*t_u. The reversing map has the same linear coefficient c and inverse translation -c*conj(t_r). Thus a universal +72 statement must specify the native BB-to-CC direction. The producer does so. Reflected seams themselves do not universally turn by 72 degrees.

## Owner frame, both physical parities, and composition

The pentagons attached to sides 0 and 6 meet along the PP edge from 0 to v=exp(-i108 degrees). This follows from the regular pentagon on side 0: its vertex after the second side is -exp(i72 degrees). The A-star forces the other pentagon on that same PP edge. Its directed owner axis is therefore v, and its midpoint is m=v/2, independent of alpha or the remaining edge lengths. The two possible owners of an unmarked dimer give opposite directions. The producer explicitly retains the owner, so there is no hidden choice of a canonical unmarked successor.

For G(x)=a*x+b the two transported axes are a*u*v and a*c*conj(v), with midpoints obtained by applying G to the stated local midpoints. For G(x)=a*conj(x)+b they are a*conj(u)*conj(v) and a*conj(c)*v. More generally composition has coefficients a*d or a*conj(d) and translation a*t+b or a*conj(t)+b according to the incoming parity, with output parity the XOR of the two parities. This verifies the required conjugation rather than commuting a reflection with a rotation.

Relative to the incoming owner axis, a preserving BB-to-CC step turns +72 degrees in an orientation-preserving physical frame and -72 degrees in an orientation-reversing physical frame. For a reversing step the native relative angle is theta_e+theta_f+216 degrees: modulo 360 this is 324-2alpha degrees for the first two words and 180-2alpha degrees for the last two. An incoming reflection negates that angle. These formulas cover both incoming physical parities and both seam parities; alpha120 causes no algebraic exception. Changing owners only adds 180 degrees and cannot turn the preserving 72-degree line change into parallel axes.

## Exact certificate and locality attack

Replay completed with exit status zero:

    mise exec -- conda run --no-capture-output -n arisearch sage research/searches/mixed-q7-dimer-return-sol-2026-10-19.sage

It printed PASS for all four words and regenerated the neighboring JSON. The script uses exact CyclotomicField(180) arithmetic. It reads, rather than regenerates or independently verifies, the prior atlas certificate. I inspected that atlas source: it constructs closed positive metric polygons, places every forced adjacent pentagon, deduplicates identical tiles, and tests every remaining pair for strict interior overlap by exact separating supporting lines. Its five seam neighborhoods and four two-seam parity combinations per word all pass. This is adequate inherited finite evidence at alpha124; the symbolic coefficient derivation supplies the all-alpha statement and does not assert all-alpha local embedding.

A local owner dimer already has its full PP side and cannot be reassigned by perfect matching. Boundary pentagons of the finite atlas need not have all their partners present. The producer expressly leaves their completion open. Accordingly the exact finite patch refutes an invariant asserted solely from immediate seam geometry plus the owner assignment. It does not exhibit a patch completed to an infinite perfect-matching tiling. A hypothetical global theorem excluding all BB/CC seams, or excluding these local configurations from all plane extensions, is untouched. Conditional on even one BB/CC seam in a plane tiling, however, physical axes change by 72 degrees, so matching itself cannot make that seam preserve a physical line.

The nonnegative signed-turn proposal also fails as a reflection-independent local physical quantity: global reflection preserves native BB-to-CC succession and negates its signed angle. A parity-compensated native count can be +72 at every forward preserving step, but no embedded carrier, winding bound, or global monotonicity follows from that count. At reflection-changing seams the full formulas above must be used.

## Scoped conclusion

No substantive error found in the final claims. The conclusion correctly stops the proposed common-axis/nonnegative-physical-turn mechanism. It neither settles plane existence nor rules out periodic tilings, larger carriers, or alternative global invariants. The purification theorem is conditional and supplies a perfect matching in some tiling; it supplies no seam-word extension theorem. Formal isometry powers, finite rotational state, and immediate interior disjointness do not supply one either. All four mixed words remain unresolved for the original aperiodicity objective. No Git or discovery-log changes were made by this reviewer.
