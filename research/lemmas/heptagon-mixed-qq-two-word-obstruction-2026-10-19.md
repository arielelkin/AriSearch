# Two mixed-QQ complementary-angle heptagons are untileable with a regular pentagon

## Theorem

Let `P` be the unit regular pentagon. Let `Q` be any strictly convex heptagon whose cyclic angle word is `ABBBCCC` or `ABBCBCC`, up to rotation and reversal, where `A=144°`, `B=α`, `C=252°−α` and real `108°<α<126°`. Then `{P,Q}` does not tile the plane, even with arbitrary reflections and unrestricted contacts. This includes `α=120°`.

## Proof

The [reviewed complementary-angle necessary theorem](complementary-angle-flow-necessary-theorem-2026-10-19.md) forces full-edge trivalent contacts. Off `α=120°`, all stars are PPA or PBC. At `α=120°`, BBB stars are additionally possible, but for these balanced `b=c=3` words its square-window incidence count bounds their number by `O(R)` in a side-`R` square. Each tile touching BBB is defective, and there are `O(R)` such tiles in an enlarged square. For each fixed radius `r`, their `r`-neighborhoods have area `O_r(R)`; hence arbitrarily large defect-free disks exist. Translate disks of increasing radii to the origin and take a locally convergent subsequence of tilings by the same fixed shapes. Fixed positive areas and bounded diameters give local finiteness and compactness of the relevant isometries; the limit has no BBB stars. Thus a hypothetical tiling at resonance yields a defect-free tiling of the same pair. Pentagon-only tilings are excluded by the same vertex-star theorem, so Q occurs in that limit.

Index Q vertices from 0 to 6 with vertex 0 of type A and side `j` leaving vertex `j`. In the defect-free tiling, the A corner has no QQ side and each B/C corner has exactly one. Propagation along the six non-A corners forces sides `1,3,5` to meet Q and sides `0,2,4,6` to meet P. The latter four intrinsic Q lengths are therefore one. In both words side 1 is BB and side 5 is CC. At a QQ endpoint, B must meet C, regardless of reflection, so a BB side must mate a CC side. As Q has one of each, their lengths agree; call that positive length `x`. Call the positive side-3 length `z`.

Set `d=126°−α`, with `0°<d<18°`, and `e(θ)=(cos θ,sin θ)`. Orient Q side 0 at heading 0°. The headings of sides 0 through 6 are respectively

```text
ABBBCCC:  0, 54+d, 108+2d, 162+3d, 216+2d, 270+d, 324
ABBCBCC: 0, 54+d, 108+2d, 162+d,  216+2d, 270+d, 324.
```

The four unit-side vector sum is `S=e(0)+e(108+2d)+e(216+2d)+e(324)`. Let `U=e(162+d)`. The sum of the two length-`x` side directions is `V=e(54+d)+e(270+d)`, which is parallel to U. A direct sine identity gives

```text
cross(U,S)=2(cos18°+cos54°) sin d > 0,
cross(U,V)=0.
```

For `ABBCBCC`, side 3 is parallel to U. Taking `cross(U,·)` of Q's closure equation `S+xV+zU=0` gives a contradiction. For `ABBBCCC`, side 3 has heading `162+3d`, so the same closure equation yields `0=cross(U,S)+z sin(2d)` and therefore `z=−(cos18°+cos54°)/cos d<0`, contradicting positivity. Reflection changes all oriented cross signs together and cannot repair either contradiction. Hence neither pair tiles.

## Scope and review

The [producer report and exact Sage verifier](../searches/heptagon-mixed-qq-mechanism-sol-2026-10-19.md) check the vector identities symbolically over the full interval. Replay:

```text
mise exec -- conda run --no-capture-output -n arisearch sage research/searches/heptagon-mixed-qq-mechanism-sol-2026-10-19.sage
```

The [independent Sol hostile review](../reviews/heptagon-mixed-metric-hostile-sol-2026-10-19.md) passed the metric and resonance arguments. This excludes two restricted angle words, not arbitrary convex pairs. The other four mixed-QQ heptagon words remain unresolved.
