# Unit-chord filter for directed-offset cross-source congruence

Date: 2026-10-14. Status: independently hostile-reviewed VALID exact **partial** obstruction for the four three-plus-one residual assignments. The other eight dihedral maps per cross-source pair are outside this lemma. See the [independent review](../reviews/ammann-directed-offset-residual-hostile-review-2026-10-14.md).

Use the four representative pentagons and strict admissibility domain of the [directed-offset gate](../searches/ammann-directed-offset-gate-2026-10-14.md). In every representative, vertices 0 and 2 are the endpoints of the receiving unit source edge. Thus their distance is exactly one. Of the ten cyclic/reversal vertex maps for a cross-source pair, precisely two map this particular chord to the corresponding particular chord: `i -> i` and `i -> 2-i (mod 5)`. This observation makes no uniqueness claim about unit diagonals.

**Lemma.** No three-plus-one assignment is realized using either of these two unit-chord-preserving maps for its required cross-source congruence.

To check the maps, take coordinates relative to the unit chord: for base `b=P_2-P_0`, record `(dot(P_i-P_0,b), cross(b,P_i-P_0))` for vertices `i=1,3,4`. Compare those coordinates to the cross-source target after the relevant index map, reversing the signed cross coordinate for the reversed map. This yields six *linear* equations in `a_X,a_Y,h_X,h_Y`, with exact coefficients in `phi=(1+sqrt(5))/2` and `t=sin(36°)`. The [checker](../searches/ammann-directed-offset-unit-chord-check-2026-10-14.py) constructs these equations directly from the gate's polygon coordinates and computes exact matrix ranks and solution sets.

| Cross pair | Same order | Reversed order |
|---|---|---|
| T0–K0 | inconsistent | inconsistent |
| T0–K1 | one-dimensional family below | inconsistent |
| T1–K0 | unique solution with `h_X=-h_Y<0` | inconsistent |
| T1–K1 | inconsistent | inconsistent |

The T0–K1 family is

```text
a_X = 1/2,
a_Y = (phi-1)(1+2t h_Y),
h_X = (phi-1)(t+2h_Y).
```

Write `E_T` and `E_K` for the edge-square half-differences in the [two-plus-two obstruction](ammann-directed-offset-two-plus-two-obstruction-2026-10-14.md). Direct exact substitution gives

```text
E_T = sqrt(5)-2 + 2(sqrt(5)-1)t h_Y > 0.
E_T-E_K = 1-2a_X = 0.
```

A three-plus-one assignment containing T0 and K1 must also contain either T1 or K0. In the first case congruence requires `E_T=0`; in the second it requires `E_K=0`. Both contradict the displayed positivity for `h_Y>0`. The T1–K0 isolated solution violates the same strict positive-height condition; all remaining chord-preserving maps are inconsistent before inequalities. This proves the lemma.

The other eight maps for each of the four cross pairs send the canonical unit chord to one of the other four diagonals. Any such congruence necessarily makes that additional diagonal unit length. They remain a 32-map conditional domain here, including all possible unit-diagonal aliases. This filter alone does **not** close the full three-plus-one residual or the directed-offset gate.

Replay:

```text
mise exec -- conda run --no-capture-output -n arisearch python research/searches/ammann-directed-offset-unit-chord-check-2026-10-14.py
```
