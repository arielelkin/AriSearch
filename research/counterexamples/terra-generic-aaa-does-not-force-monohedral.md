# A generic ternary AAA star need not permit a monohedral escape

Date: 2026-10-13. Status: independently adversarially reviewed VALID;
[fresh review](../reviews/terra-generic-aaa-counterexample-fresh-hostile-review.md). No plane tiling of the two-type problem is asserted.

## Claims falsified

Outside opposite-angle native012012, a metrically realizable pure AAA star
need not force central symmetry, and need not imply that A tiles monohedrally.
This invalidates extending the new012012 mechanism merely by retaining its
AAA premise. It does not refute the global two-tile impossibility conjecture.

## Exact polygon

Let z be the primitive360th root exp(2pi i/360). Finite defining data are
Phi_360(z)=0, Re(z)>99/100 and 1745/100000<Im(z)<1746/100000; these isolate
the specified root. Set I=z^90 and define

    cross(P,Q)=(conjugate(P)*Q-P*conjugate(Q))/(2I),
    S0=1+z^67, S1=z^126+z^185, S2=z^239+z^293,
    v0=cross(S1,S2), v1=cross(S2,S0), v2=cross(S0,S1),
    a=1, b=v1/v0, c=v2/v0.

The vertices are p0=0 and cumulative sums of edge vectors

    (a, a*z^67, b*z^126, b*z^185, c*z^239, c*z^293).

The sum is zero by the two-dimensional determinant kernel identity.
The exact checker proves a,b,c strictly positive and pairwise distinct,
and checks all24 strict nonincident support determinants. Hence these data
specify a strictly convex hexagon with angles

    (113,113,121,121,126,126)

and side word(a,a,b,b,c,c). For orientation only, b is approximately
0.811500595570514 and c approximately0.847341668454972. These decimals do not
define the polygon or decide any equality/inequality.

Corners0,2,4 have respective arm pairs(c,a),(a,b),(b,c), so three direct
copies admit a ray-matched AAA star with angle sum113+121+126=360. Each copy
lies in its convex corner wedge; the three wedges have disjoint interiors,
so the three whole copies give an actual disjoint finite patch, rather than
only formal ray compatibility. Opposite side lengths are not equal, so A is
not centrally symmetric.

## It is outside every monohedral hexagon class

The current primary source Zhu, Wang and Yan, *Hexagonal Tiling of the Plane*,
arXiv2508.01404v2, dated28 April2026, states the unrestricted three-family
classification, with reflections and original partial contacts included.
The Introduction gives these conditions up to cyclic relabelling/reflection:

* H1: angle0+angle1+angle2=360, side2=side5;
* H2: angle0+angle1+angle3=360, side1=side3 and side2=side5;
* H3: angles0,2,4 each120, side0=side1, side2=side3, side4=side5.

[Primary source](https://arxiv.org/html/2508.01404v2), refreshed13 October2026.
The separate checker exhausts all12 dihedral relabellings and verifies exact
failure of each family condition. Thus by this named imported theorem A does
not tile the plane monohedrally. The classification is not proved anew here.
The fixture angle triple is generic for the complementary ternary star
language: the existing single-cross-palette artifact exhaustively verifies
the five triple types for six angles(113,121,126,134,118,108).

## Replay, scope and next obligation

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_terra_noncentral_aaa_hexagon.py

[Exact checker](../reviews/verify_terra_noncentral_aaa_hexagon.py) imports no
search producer. Its domain is one exact polygon,24 support inequalities,
one AAA star and12 dihedral relabellings for the three monohedral criteria.
It uses CyclotomicField360 and a specified QQbar embedding with AA sign tests.
No solver, seed, timeout, floating-point acceptance or infinite extension is
involved. The output is PASS. Independent hostile review and a separate whole-copy ray checker have passed.

The next justified obligation is to examine whether a mixed isolated-B
neighbourhood can surround this specific actualAAA mechanism, using exact
local geometry first. A local star supplies neither an infinite mixed field
nor a universal aperiodicity mechanism. A broad AAA=>monohedral assertion is
now falsified and should not be used as a replacement missing lemma.
