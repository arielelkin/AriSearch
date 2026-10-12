# Interior-T hat cut: side inventory and strict geometry

Verdict: VALID for this explicit two-pentagon/two-hexagon cut and a strictly interior straight-side junction.

The independent checker reconstructs all four midpoint boundary words, their squared side inventories, both exact branch ideals, and the positive sample partition. It imports the earlier independent hat boundary reconstruction, never the new producer.

The finite reduction is exhaustive before polynomial solving. Let W=h4+s(V-h4), with 0<s<1, and let L,F,G,J denote the actual positive lengths in the feature note. Hexagon congruence gives `{2,sL,F}={b,G,L}` after cancelling one b and two unit sides. Pentagon congruence gives `{b,G}={(1-s)L,F}` after cancelling the fixed J, unit side, and b. Substitution and cancellation of F give `{2,sL}={(1-s)L,L}`. Since sL<L, the right-hand L must match the left-hand 2. Thus L=2 and s=1/2. The remaining identity `{b,G}={1,F}` yields exactly the two branches `(b=1,F=G)` or `(G=1,F=b)`. Multiset cancellation remains valid when lengths coincide; no cyclic orientation or reflection is discarded.

At the forced midpoint, the independent squared equations reproduce both dimension-zero ideals and their exact Groebner bases. Each has two real points. All four have positive b and satisfy their necessary equations, but independently evaluated full supporting-line determinants rule out strict convexity at every point. Therefore no strict two-class realization survives even this necessary side inventory test; full congruence checks are unnecessary for exclusion. This replay shares Sage's exact ideal/real-algebraic engine with the producer, while reconstructing its equations independently.

At `(b,u,v)=(1,9/5,0)`, every piece has strictly positive supporting inequalities, all six pairwise intersection areas vanish, and atomic boundary cancellation reconstructs the source outline. W is exactly the strict midpoint of a nonzero h4-V segment, hence lies in P1's side interior. The positive feature exists before imposing congruence, and the gate fails at the two-class metric requirement.

The independent artifacts are `check_hat_interior_t_two_class_gate.py` and `hat-interior-t-two-class-check.json`. The checker has optional `--output PATH` and otherwise writes no artifact. The result covers these four words with this straight-side interior-T topology, not arbitrary cuts, source recognition, plane existence, or unrestricted forcing. Straight/zero degenerations do not satisfy its strict polygon hypothesis.
