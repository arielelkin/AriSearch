# Periodic tiling for the AABBAABB octagon continuum

**Theorem (restricted family).** Let `w=exp(2*pi*i/20)`. Let `P` be the regular unit pentagon with vertices `p_i=sum_{j<i}w^(4j)`, `i=0,...,4`. For any real `h>0`, let `Q(h)` be the octagon whose consecutive interior-angle word is `AABBAABB`, with `A=144°`, `B=126°`, whose two BB sides (native edges 2 and 6) have length `h`, and whose six other sides have length one. Start edge 0 in direction 1 and turn by 36° at A and 54° at B. Then `Q(h)` closes and is strictly convex. The unmarked pair `{P,Q(h)}` admits a doubly periodic tiling of the entire Euclidean plane. Therefore no member of this family is aperiodic under the [research problem](../../research-problem.md).

The theorem is for every real `h>0`, including transcendental values. It asserts one permitted periodic tiling, not a classification of every tiling or every convex octagon.

## Exact carrier

Use representatives `F0=P`, `F1=1-P`, `F2=1+w^4-w^4 Q(h)`. Let

`L1=w^6+w^4+w^2`,

`L2=(w^7-w^5+w^3-w)h+2w^6-1`.

Number F0's edges 0–4, F1's 5–9 and F2's 10–17. Pair the nine edges as

`(0,5),(2,7),(1,10),(3,13),(4,15),(6,14),(8,17),(9,11),(12,16)`.

The corresponding start-minus-opposite-end shifts are respectively

`(0,0),(1,0),(0,0),(0,1),(-1,1),(-1,1),(-1,0),(0,0),(-1,0)`

in the lattice basis `(L1,L2)`. Both endpoints of every paired edge obey these identities exactly in `Q(w)[h]`; opposite edge vectors and the entire-edge gluing follow. The two private BB edges of Q self-pair in this one-Q quotient. The six vertex links are the single three-cycles

`(0,6,15),(1,11,5),(2,8,10),(3,14,7),(4,16,13),(9,12,17)`.

Four have corner types `P,P,A` and two have `P,B,B`; all have total angle 360°.

## Proof of admissibility and full coverage

The octagon edge directions occur in opposite pairs, as do their lengths, so its walk closes for every h. The [exact producer certificate](../searches/regular-pentagon-octagon-minimal-carrier-sol-2026-10-19.sage) and [independent checker](../reviews/regular-pentagon-octagon-minimal-carrier-hostile-sol-2026-10-19.sage) verify all 48 nonincident vertex/edge supporting inequalities for Q as strictly positive polynomials in `h>0`; this proves strict convexity and simplicity. At `h=0` two edges collapse, so the theorem excludes it.

The nine paired edges make an abstract compact connected oriented surface `X` without boundary. The six vertex links are single circles and have exactly 360° of positively oriented sectors; with 3 faces and 9 edges, `X` has Euler characteristic zero. The exact edge shifts define a continuous map from `X` to the flat torus `T=R²/(ZL1+ZL2)`. The opposed face sectors along each shared edge and the single 360° winding at each vertex make this map a local Euclidean isometry everywhere, without presuming global nonoverlap.

Exact signed shoelace and lattice arithmetic give

`cross(L1,L2)=2 area(P)+area(Q(h))`

`=(-w^6+w^4+2)h-7w^7/2+2w^5-w^3/2+4w`.

Both the constant and linear coefficients are strictly positive in the distinguished real embedding. Thus the lattice has rank two and positive covolume for every h>0. The compact local isometry `X->T` is a finite surjective covering; its degree is `area(X)/area(T)=1`. It is a homeomorphism. Lifting its faces proves that all lattice translates of the three displayed polygons cover the plane with disjoint interiors. Both `L1` and `L2` are periods.

The proof permits rotations, reflections and partial contacts as in the original problem: a single tiling using direct isometries suffices to defeat aperiodicity. No assertion is made about the separate isolated `AAABBABB` octagon.

## Finite gate, independent review and limits

The [search report](../searches/regular-pentagon-octagon-minimal-carrier-sol-2026-10-19.md) explains why star counts and pentagon saturation make `2P+1Q` the smallest possible full-edge translational quotient. Its deterministic exact enumeration includes both Q reflection parities and all 4,320 normalized pairings per word. Four AABBAABB maps survive; the displayed map alone proves the theorem. The [independent Sol hostile review](../reviews/regular-pentagon-octagon-minimal-carrier-hostile-sol-2026-10-19.md) is **PASS** for the continuum tiling and finite enumeration. Its separate analytic observation proves that `AAABBABB` cannot self-pair its nonantiparallel QQ sides in a one-Q torus. That narrow obstruction does not address a larger periodic quotient or plane tilability.

Replay both exact SageMath 10.9 programs from repository root:

```sh
mise exec -- conda run --no-capture-output -n arisearch sage research/searches/regular-pentagon-octagon-minimal-carrier-sol-2026-10-19.sage
mise exec -- conda run --no-capture-output -n arisearch sage research/reviews/regular-pentagon-octagon-minimal-carrier-hostile-sol-2026-10-19.sage
```

No solver, random seed, parameter sampling or timeout enters the theorem. The unrestricted two-convex-polygon objective remains unresolved.
