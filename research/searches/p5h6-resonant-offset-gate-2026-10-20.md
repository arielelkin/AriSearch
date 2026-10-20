# Resonant q=1/2 P5/H6: first omission gate

**Status: falsified for unrestricted aperiodicity (2026-10-20).** The proposed equality `q=1/2` would close the second contact of the prior offset split, but it also makes P a periodic monohedral Type 2 pentagon. The pair fails the universal aperiodicity condition because H may be omitted. The search stopped before mixed placements or H-only classification.

Work in `K=Q(zeta_36)`, `u(d)=zeta_36^(d/10)`. Fix P directions `(0,50,150,200,280)` and lengths `(p,1,1/2,s,1/2)`. Solve its exact vector closure for `p,s`. Put `L=p+1/2`; H has directions `(0,50,100,180,230,280)` and lengths `(L,1,1,c,1/2,e)`, with `c,e` fixed by vector closure. The [Sage replay](p5h6-resonant-offset-gate-2026-10-20.sage) proves uniqueness of both linear solves, exact closure, positive lengths and strict convexity. It gives `p≈1.14209163605`, `s≈1.53102259277`, `L≈1.64209163605`, `c≈2.03102259277`, `e≈1.38893095672`.

P's native angle word is `(100,130,80,130,100)`. With the identity relabeling, Rao Type 2 is satisfied exactly: `A+B+D=100+130+130=360°` and `c=e` in the classification's side notation is native `P2=P4=1/2`. The replay exhausts all 15 stored Rao families and 10 dihedral relabelings and returns only `(Type 2, sign +1, offset 0)`. The standard Type 2 construction gives a periodic P-only plane tiling, conditional on the repository's [reviewed source transcription](../lemmas/pentagrid-pentagon-monohedral-filter.md). This is a positive periodic witness mechanism, not an inference from bounded negative search.

This metric differs from the [nonresonant offset fixture](p5h6-offset-t-gate-2026-10-20.md) and the earlier [equal-unit fixture](p5h6-complementary-t-gate-2026-10-20.md). Their failures do not imply this one; the Type 2 equality is checked anew. No plane-tiling or aperiodicity assertion is made for any changed side-length choices.

```text
mise exec -- conda run --no-capture-output -n arisearch sage research/searches/p5h6-resonant-offset-gate-2026-10-20.sage
```
