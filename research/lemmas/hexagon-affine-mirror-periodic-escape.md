# A repeated-length irrational-angle hexagon pair with a periodic escape

**Status:** exactly checked and independently reviewed as valid in the
[fresh audit](../reviews/hexagon-affine-mirror-escape-review.md), with the
explicitly imported unrestricted hexagon classification as a dependency.
This kills an explicit two-shape candidate and a proposed use of irrational
metric displacement. It is not a classification or a solution of the main
problem.

## Exact two shapes and lattice

Let w=sqrt(3)>0, h=sqrt(5)>0 and p=w*h=sqrt(15)>0. These numbers
are exactly specified in the certificate by the primitive element g=w+h,
its polynomial g^4-16g^2+4=0, and the isolating interval 39/10<g<4;
then w=(g-2/g)/2 and h=(g+2/g)/2. The following counterclockwise lists
define compact strictly convex hexagons A,B:

```text
A = [(0,0), (2,0),
     (2+(p-w)/4, (3h+1)/8),
     (1+(p-w)/4, (4w+3h+1)/8),
     (1-(p+w)/4, (4w+3h-1)/8),
     (-(p+w)/4, (3h-1)/8)]

B = [(0,0), (p/2,1/4),
     ((3p+w)/4,(3h+1)/8),
     (p/2,3h/4), (0,(3h+1)/4),
     ((-p+w)/4,(3h+1)/8)].
```

Put S(x,y)=(x,-y), and set

```text
t = (2+(p-w)/4, -(3h+1)/8),
u = (1+p/2, (2w+3h)/4),  v = (1+p/2,-(2w+3h)/4),
Lambda = Z*u + Z*v.
```

The plane is tiled by exactly these copies:

    {A+l, S(A)+l, B+t+l : l in Lambda}.                 (1)

The lattice determinant has magnitude 19w/4+3h>0. The two congruence classes
are distinct, since A has five distinct side lengths and B has three. This
whole-plane witness permits reflections and has two independent periods.
Their areas are

    area(A)=w+3h/2,  area(B)=11w/4,
    area(B)/area(A)=p/2-1.

Thus the area ratio is irrational despite the rational tile-count ratio 2:1
in a lattice cell. Both are exact assertions about the same two-shape witness.

## Geometry, repetition, and the absence of monohedral escapes

Writing q_minus=(59-9h)/32 and q_plus=(59+9h)/32, the squared
native side lengths, in displayed order, are

    A: (4,q_minus,7/4,61/16,7/4,q_plus),
    B: (61/16,q_plus,q_plus,61/16,q_minus,q_minus).

The exact inequalities 2<h<9/4 give

    0 < q_minus < 7/4 < q_plus < 61/16 < 4.

Thus both shapes are non-equilateral and noncentral. A repeats only two
sides at cyclic separation 2. B has word (u,v,v,u,z,z) with three distinct
length symbols. Strict convexity follows either from the exact half-plane
cross-product inequalities in the verifier or from the positive-determinant
affine construction below.

The unrestricted monohedral convex-hexagon classification is imported from
Zhu--Wang--Yan, [*Hexagonal Tiling of the Plane*, arXiv:2508.01404v2](https://arxiv.org/html/2508.01404v2),
Main Theorem and the H1,H2,H3 systems in Section 1. Under cyclic relabeling
or reversal, H1 requires an equal parallel opposite-side pair; H2 requires
an equal opposite pair and an equal pair at separation 2; H3 requires a
partition into three equal adjacent-side pairs.

A has no equal opposite pair and no three adjacent pairs. B has only one
equal opposite pair, sides 0,3; those vectors are (p/2,1/4) and
(-p/2,1/4), which are not parallel. B has no repeated side at separation
2 and cannot partition its six positions into three equal adjacent pairs.
Neither satisfies any Reinhardt system. Consequently neither shape alone
admits an unrestricted plane tiling. No monohedral pentagon classification
or imposed contact rule is used.

At least one B angle is an irrational multiple of pi. Otherwise all native
edge-direction differences would be rational multiples of pi. Put
theta=arctan(1/(2p)). The difference between B's side directions 0 and 3 is
pi-2theta, so exp(2i*theta) would be a root of unity. Its trace would be

    exp(2i*theta)+exp(-2i*theta) = 118/61.

A rational algebraic integer is an integer, whereas 118/61 is not. This
contradiction establishes irrationality without evaluating an angle.

## Direct infinite tiling verification

Let the three finite motif polygons be A,S(A),B+t. For any pair of motifs,
any lattice translate is n*u+m*v, whose coordinates are

    (L*(n+m), H*(n-m)),   L=1+p/2, H=(2w+3h)/4.

If their bounding boxes intersect, q=n+m and k=n-m lie in explicit finite
closed intervals derived from those boxes. Their parity must agree. The
[exact verifier](../reviews/verify_hexagon_affine_mirror_escape.py) enumerates
all these intervals using exact algebraic floor/ceiling operations. There
are 18 ordered candidate comparisons other than identical copies. For each,
one of the native edge-normal projections separates the two polygon
interiors, allowing equality at shared boundaries. All other translated
pairs have disjoint bounding boxes. Thus every two distinct copies in (1)
have disjoint interiors.

The sum of the three motif areas is exactly 19w/4+3h, equal to the lattice
covolume. Passing to a lattice fundamental parallelogram, the disjoint
interiors occupy its full area. The lattice union of these compact bounded
polygons is closed and locally finite. If any point of the plane were
uncovered, an open disk would be uncovered, contradicting full area in the
fundamental parallelogram. Hence (1) covers the entire plane. The finite
comparison domain therefore proves an infinite tiling, rather than relying
on an unproved finite-patch extension.

## Why this affine construction stays at exactly two congruence classes

This is the substantive mechanism behind the witness; an arbitrary affine
image of a Euclidean tiling can create more tile classes. Let R_b denote
rotation through b, let cos(a)=p/4 and sin(a)=1/4, and put D=diag(2,1).
Start with the equilateral triangle-orbit references A0=H(a), B0=H(2a)
whose directed unit sides have angles respectively

    A0: 0,60+a,120,180+a,240,300+a,
    B0: 0,60-2a,120,180-2a,240,300-2a.

Closure follows by grouping their alternating sides into two equilateral
triangle orbits. The inequality 1/p<1/w gives 0<a<30 degrees, so both
references are strictly convex. In the reviewed three-face torus of
[the two-triangle hexagon lemma](new-angle-two-equilateral-hexagons.md),
the three developed motif orientations are A0, R_(-a)A0, R_a B0. The first
whole-side seam places the second A0 motif precisely at S(A0): rotation
R_(-a) followed by its seam translation equals S(A0) as an unindexed set.
This identity follows from A0's reflection axis at angle a/2 and is also
checked directly from the six coordinates. D commutes with S. Therefore
both deformed A motifs belong to the same Euclidean congruence class.
The sole B motif becomes B=D*R_a B0. All further placements in the source
development are translations, and D carries translations to translations.
The result uses only A=D*A0 and B, with precisely the reflected A copy in
(1). The direct overlap-and-area verification above is independent of this
construction history.

## Replay, limitations, and restart state

```text
conda run --no-capture-output -n arisearch python research/reviews/verify_hexagon_affine_mirror_escape.py
```

The [exact certificate](../certificates/hexagon-affine-mirror-escape.json)
contains all coordinates, lattice vectors, motif translation, source seams,
and translation coefficients. The [execution record](../searches/hexagon-affine-mirror-escape.md)
states the finite domain and versions. This pair has no monohedral escape,
noncentral geometry, repeated non-equilateral lengths, and an irrational
angle, yet its two-shape tiling is doubly periodic with tile counts 2:1.
Even an irrational area ratio added to these properties cannot enforce
irrational tile-count frequency or exclude translations. No statement about arbitrary stretched hexagons, generic
stripe dynamics, or novelty is made.
