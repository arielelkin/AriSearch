# Complementary T-junction P5/H6: first exact gate

**Status: falsified for unrestricted aperiodicity (2026-10-20).** This fixed equal-unit metric admits a periodic tiling using P alone, conditional on the standard Rao Type 2 construction as transcribed and source-audited in this repository. The stipulated first-decisive-failure rule stopped the search before enumerating the proposed midpoint and three caps. No finite patch, mixed plane tiling, or forcing claim is made.

## Exact shapes

Let `K = Q(zeta_36)` in the embedding `zeta_36 = exp(2 pi i / 36)`, and `u(d)=zeta_36^(d/10)` for the displayed directions in degrees. Set `q = u(40)+u(320)=2 cos(40°)`, `t=1+q`, and let `p` be the exact solution of

`p u(0) + u(60) + q u(140) + (1+q) u(200) + u(260) = 0`.

The two real coordinate equations have nonzero determinant and give the unique `p=3.226681596905678…`; `q=1.532088886237957…`, `t=2.532088886237957…`, `L=p+q=4.758770483143635…`. Define P by directed edge angles `(0,60,140,200,260)` and lengths `(p,1,q,t,1)`, and H by directed edge angles `(0,60,120,180,240,300)` and lengths `(L,1,L,t,p,t)`. Start both at the origin and cumulatively sum their edges. The script verifies exact closure, positive lengths and every strict-convexity cross product. The native interior angle words are respectively `(80,120,100,120,120)` and `(120,120,120,120,120,120)`. Their side counts make the two congruence classes distinct.

## Decisive omission

Use the vertex convention `side i = vertex i to vertex i+1`. Reverse the P indices with offset 4. The angle indices become `(4,3,2,1,0)`, giving the Rao Type 2 angle word `(120,120,100,120,80)` with `A+B+D=120+120+120=360°`. Reflected side indices are `(3,2,1,0,4)`, so its `c=e` condition is exactly native `P1=P4=1`. This is the relabeling `(Type 2, sign −1, offset 4)` in the repository's [reviewed Rao transcription](../lemmas/pentagrid-pentagon-monohedral-filter.md) and [table data](convex-substitution-shapes.py). The Type 2 construction is periodic and monohedral. Since admitted tilings may omit H, the pair fails the required universal no-periodic-tiling condition even if the named P/H T-junction is geometrically legal.

## Scope and comparison

The angle word and mixed P5/H6 contact proposal differ from the fixed P5/Q6 star, obtuse P5/Q7, regular-P5/heptagon and Cairo/P5/P5 records in the [shape-first deduplication audit](shape-first-dedup-audit-2026-10-20.md). The fatal equal-unit P side condition is an intrinsic monohedral escape, not a duplicate mixed construction. A changed metric with unequal outgoing P sides would require a new exact gate; this report says nothing about it. Neither a full placement enumeration nor H-only omission nor a whole-side H/H competitor was tested after the P-only failure.

Replay the exact algebra (one fixed metric, two closure checks, eleven positive-length checks, eleven convexity cross products and one explicit Type 2 relabeling):

```text
mise exec -- conda run --no-capture-output -n arisearch sage research/searches/p5h6-complementary-t-gate-2026-10-20.sage
```
