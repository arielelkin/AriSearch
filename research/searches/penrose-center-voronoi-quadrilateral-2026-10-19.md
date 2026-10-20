# Intrinsic Penrose rhomb sites: exact quadrilateral omission gate

Date: 2026-10-19. Status: exact certificate checked and [independently Sol-reviewed](../reviews/penrose-center-voronoi-sol-review-2026-10-19.md). This closes the earlier floating center-only diagnostic
for the specified genuine Robinson/Penrose substitution source. It is not a
classification of arbitrary site rules or a solution of the main problem.

## Statement and intrinsic-site rigidity

Let one site be assigned to each unmarked thin or thick Penrose rhomb by a
rule depending only on that tile and commuting with every Euclidean isometry.
Its site must be its center: the half-turn about that center preserves the
tile and has exactly one fixed point. In the genuine plane substitution source
constructed below, the ordinary Voronoi diagram of these sites contains the
strict convex quadrilateral certified here. Any proposed two-shape protoset
containing every output class therefore has a periodic tiling using that
quadrilateral alone. It cannot satisfy unrestricted aperiodicity. This says
nothing about context-dependent sites, marked-frame sites, weighted cells,
or selecting a different subset of output shapes.

## Primary geometry and infinite source

Jeff Preshing's [author explanation](https://preshing.com/20110831/penrose-tiling-explained/)
and [author implementation](https://preshing.com/files/penrose.py) explicitly give
the red/blue Robinson-triangle recurrence and alternating ten-triangle wheel.
The original implementation is retained at
`research/sources/penrose-preshing-author-2026-10-19.py`, SHA-256
`a5beee946b87a5084c2e7cb6ef2ae7179494935464b0fad26c8f2812d40c4c51`.
It is primary evidence for this implementation, not an original-priority claim
for Penrose or Robinson geometry. The author's discussion also describes
nesting wheel subdivisions to fill the plane. We supply an exact nesting
check rather than relying on its illustration.

Put w=exp(i*pi/5), phi=w+w^(-1), and let W be the ten triangles
(0,0,w^i,w^(i+1)), exchanging the last two vertices for even i.
This differs from the author's wheel by a common rotation of pi/10.
For a labelled triangle (colour,A,B,C), the subdivision sigma is:

* red: P=A+(B-A)/phi; children (0,C,P,B),(1,P,C,A);
* blue: Q=B+(A-B)/phi, R=B+(C-B)/phi; children
  (1,R,C,A),(1,Q,R,B),(0,R,Q,A).

These are actual subdivisions: the red segment CP divides its triangle;
for blue, the segments AR and QR give its three triangles, since Q and R
lie in the relative interiors of BA and BC. Areas add and interiors are
disjoint. Similarity commutes with sigma. Write F=phi*sigma, T_n=F^n(W).
The certificate checks all 20 labelled triangles of T_1 belong exactly to
T_5. Thus T_(1+4k) is a nested sequence under F^4. Its support is the regular
decagon phi^(1+4k)*conv{w^i}, whose inradius tends to infinity. Its union is
an actual whole-plane Robinson substitution triangle tiling. The usual
base pairing of this Penrose substitution gives its rhomb tiling; pairing
and its thin/thick interpretation are explicit in the author's source.
In T_5 the verifier independently checks that every paired base has the
same colour and ordered endpoints, the apexes are on opposite sides, all
four rhomb sides have length one, and every unmatched base lies on the
outer decagon boundary. In particular all 430 retained complete rhombs
are genuine source occurrences and remain present in the nested limit.
No inference from unrelated large finite patches is used.

## Exact witness and complete neighbors

The producer uses Q(w), w^4=w^3-w^2+w-1, with the embedding Im(w)>0.
Write h=i*sin(36 degrees), so z=x+h*y with x,y in Q(phi),
phi^2=phi+1, phi>1. Thus the geometry and metric are exact over Q(sqrt(5))
in this fixed orthogonal, unequally scaled coordinate system;
|z|^2=x^2+((3-phi)/4)*y^2. It is not claimed that ordinary orthonormal
Cartesian coordinates themselves all lie in Q(sqrt(5)).

Rhomb index 23 has center c=(5/2)+(3/2)w+2w^2. Its Voronoi cell relative
to c has the following cyclic (x,y) vertices:

| x | y |
|---|---|
| 3phi/8 | 1/4 |
| (phi-1)/4 | phi/2 |
| -3/4 | (1-phi)/2 |
| (phi-1)/4 | -phi/2 |

Their squared radii are respectively 3/16+phi/8, 1/4, 1-phi/4, 1/4,
all strictly below 1. All four turns are strictly positive. Four distinct
other centers support its four sides (indices 21,68,18,22), and every
vertex satisfies all 429 other finite-site inequalities exactly:

    (q-c) dot v <= |q-c|^2/2.

The producer clips a containing parallelogram against all these inequalities;
the final polygon is strictly inside its initial boundary. It removes straight
subdivisions before asserting four genuine sides. Consequently it is the
actual finite-site cell, not a polygon inferred only from the four supports.

The minimum squared distance from c to every exposed edge of the union of
all 430 complete rhombs is exactly 7+(37/4)phi>9. The disk B(c,3) is
therefore contained in that union: c is interior, and any path to its
complement crosses its exposed boundary. An additional rhomb in the plane
source has disjoint interior from this union, so its center q has |q-c|>=3.
For every point v of the computed convex cell, |v|<1, hence

    |q-c|^2-2(q-c) dot v >= |q-c|*(|q-c|-2|v|)>0.

Such a center cannot cut the cell. This proves completeness against the
infinite tail without a numerical cutoff or an unproved collar atlas.

## Periodic omission

Every convex quadrilateral tiles periodically by isometric copies, with
reflections unnecessary. One explicit standard construction writes its
vertices as 0,a,b,c in cyclic order and joins it to the half-turn image
a+b-Q along [a,b]. The union has boundary vertices
0,a,a+b-c,a+b,b,c and opposite boundary sides are identified by the lattice
generated by b and c-a. These side identifications are translations and
its area is |cross(b,c-a)|, exactly the lattice covolume; the paired
quadrilaterals give the usual fundamental polygon tiling. Equivalently,
placing half-turn copies successively around vertices completes the four
quadrilateral angles to 2pi and produces this lattice tiling.
Thus the witness class alone already defeats the problem's omission test.
There is no need to count the remaining Voronoi classes or test hierarchy.

## Computation record and scope

Question: does the fixed rhomb-center rule contain one genuine complete
quadrilateral in the level-5 source? Domain: the 890 labelled triangles,
430 complete paired rhombs, index 23, every finite-site constraint, every
exposed rhomb edge, and the exact 20-in-890 nesting inclusion. Arithmetic:
Sage CyclotomicField(10), with exact AA comparisons under its specified
QQbar embedding. No randomness, solver, timeout, or floating branch.
Congruence enumeration is unnecessary: a four-sided output is sufficient.

Replay from repository root:

```text
mise exec -- conda run --no-capture-output -n arisearch python research/searches/penrose-center-voronoi-quadrilateral-2026-10-19.py --check
```

The producer and JSON certificate have that same stem under `research/searches/`
and `research/certificates/`. The producer does not import the old floating
diagnostic or the existing rhomb generator. The independent hostile review
passed the scoped source and nesting claims; standard Robinson base-pairing
remains an explicit primary-source dependency. No assertion that every
nonstandard generalized or singular Penrose-like source contains this
patch is needed or made; the exclusion concerns this intrinsic rule on the
specified standard source and any source containing its patch.
