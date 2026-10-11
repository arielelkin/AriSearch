# Fresh hostile review: exact four-face Cairo witness

Reviewer: `primary_literature`, 2026-10-09. The reviewer did not construct or
modify the author proof. Reviewed
[the Cairo family and concrete witness](../lemmas/cairo-two-scalene-periodic.md),
[the exact certificate](../certificates/cairo-two-scalene-torus.json),
[the author's verifier](verify_cairo_two_scalene.py), and
[the partial-contact diagnostic](../counterexamples/cairo-partial-beta-length-graph.md).
A separate reviewer checker is retained at
[verify_cairo_two_scalene_independent.py](verify_cairo_two_scalene_independent.py).
It imports neither an author generator nor an author verifier.

## Exact claim and hypotheses

Let w be the root of x^2-3 in (1,2). For p=1,r=1/2 put
q=w-1/2 and s=2-w/2. The two whole pentagons have side words
A=(q,p,p,q,r), B=(p,q,q,p,s), and corner-after-side angle word
(90,120,90,120,120). The claim is a genuine periodic plane tiling using
both noncongruent convex shapes, certified by four whole faces. It therefore
refutes this pair as an aperiodic candidate.

The same ten full-side seams also give a periodic tiling throughout the
family p>0, 0<r<2p/w, q=wp-r, s=2p-wr. Members of the general family need
not be noncongruent. Neither the proof nor this review claims that either
individual concrete pentagon fails to tile monohedrally under unrestricted
contacts. No novelty claim is made.

## Exact geometry and family closure

The polynomial x^2-3 has precisely one root in (1,2); its other real root is
negative. Both checkers use the positive exact algebraic embedding. The
concrete p,q,r,s are positive and pairwise unequal; r occurs in A's length
multiset and not B's, while s occurs only in B's. The shapes are noncongruent.

Independently derive A from its edge vectors

    (q,0), (0,p), (-wp/2,p/2), (-q/2,-wq/2), (r/2,-wr/2).

Their sum is ((q+r-wp)/2, (3p-w(q+r))/2)=(0,0).
They have the stated positive lengths and directions 0,90,150,240,300
degrees. Consecutive exterior turns are 90,60,90,60,60 degrees. This gives
the required interior angle word in the **corner-after-side** convention.
The generated coordinates exactly equal every retained certificate entry.
B follows by p<->q and r->s: p+s=wq, so the same derivation closes it.

The parameter restriction implies s>0 and q>p/w>0. Local turn signs alone
would not certify genuine convexity; the independent checker instead
checks every other vertex strictly to the interior side of every supporting
edge, for both concrete polygons. It additionally verifies the displayed
symbolic support determinants for the general A family in a polynomial ring
over Q(w). Every determinant reduces to a positive expression in p,q,r:

    edge0: pq, 3pq/2, wqr/2;
    edge1: pq, wp^2/2, p(q+r/2);
    edge2: p(wp+q)/2, wp^2/2, pq;
    edge3: wqr/2, 3pq/2, pq;
    edge4: wrq/2, r(p+wq)/2, wrq/2.

For B the same identities use the positive variables q,p,s, which satisfy
p+s=wq. Thus neither star polygons nor degenerate boundary vertices are
being passed by a merely local convexity check.

## Corner links, orientation, and torus topology

All twenty native side occurrences appear once in the ten retained seams.
Each seam identifies equal full lengths and reverses its two endpoint roles.
All four reference faces are unreflected and counterclockwise. These
reversals therefore give a globally oriented quotient, with no boundary.
The face graph is connected.

The reviewer does not infer manifold links merely from the sizes of corner
equivalence classes. Instead, the independent checker walks each vertex
link through its incoming edge, then through the predecessor corner of the
matched edge. This exact corner-successor permutation has two length-four
cycles, consisting respectively of all four c_0 and all four c_2 corners,
and four length-three cycles:

    A0c1,B0c3,B1c4;
    A0c3,A1c4,B1c1;
    A0c4,A1c3,B0c1;
    A1c1,B0c4,B1c3.

Every link is one circle. The quadruples have four right angles and the
triples have three120-degree angles; every cone angle is360 degrees.
There are six vertices, ten edges and four faces, so the connected closed
orientable surface has Euler characteristic0 and is a torus. With the actual
polygon metrics it is flat everywhere. Thus no nonmanifold vertex, reflected
boundary seam, angle deficit, or unpaired corner invalidates the surface.

A compact flat torus is complete. Its simply connected complete flat
universal cover develops isometrically onto the Euclidean plane: geodesics
continue for all time, giving a surjective local isometry, and the plane's
simple connectedness makes the covering one-sheeted. Its deck transformations
preserve orientation and act freely. A nonidentity rotation fixes a point,
so every nonidentity deck transformation is a translation. Compactness
forces their discrete group to have rank two. This supplies the global
tiling conclusion, rather than only a locally angle-legal patch.

## Independent direct plane witness and lattice rank

The reviewer also developed a dual spanning tree and checked every remaining
seam's exact affine holonomy. All residual orthogonal parts are identity.
The nonzero seam vectors generate the explicit lattice with basis

    u=(w,-3), v=(2w-3/4,-w/4).

Their determinant is 6w-3>0. Every retained seam period has integer
coordinates in this basis, and both basis vectors actually occur as seam
periods. Thus the computed periods have genuine rank two, rather than a
formal pair of dependent or zero vectors.

The four developed motif faces are, writing R90(x,y)=(-y,x),

    A;
    (-r/2,wr/2)-A;
    R90(B)+(q,-p);
    -R90(B)+(-q-r/2,p+wr/2).

Their total exact area equals det(u,v)=6w-3. The reviewer checker checks all
possible overlaps between these faces and their lattice translates. It
derives each finite integer shift range from the **exact** bounding boxes
of polygon vertices in lattice coordinates, and checks both polygons'
supporting-edge separating axes for every candidate. All48 ordered
comparisons pass. This domain includes every possible interior overlap;
it is not an arbitrarily bounded lattice search.

For coverage, integrate the sum of translated tile indicators over a lattice
fundamental parallelogram. Its integral is the total motif area, equal to
the parallelogram area. Interior-disjointness bounds that sum by1 almost
everywhere, so it equals1 almost everywhere. The union of translated compact
motif faces is locally finite and closed. Any uncovered point would lie in
an open uncovered neighborhood of positive area, contradicting the almost
everywhere result. Consequently this explicit motif and lattice tile the
whole plane. This provides a separate direct global check in addition to
the flat-torus proof.

## Partial contacts and the failed monohedral shortcut

The independent checker also verifies the exact three-A diagnostic

    T1=A, T2=(-r/2,wr/2)-A, T3=R90(A)+(p,-q).

They meet at120-degree native corners at the origin. Exact supporting-cone
inequalities put them in the respective sectors0..120,120..240,240..360,
so they are interior-disjoint and fill a neighborhood of the origin. On the
0-degree and240-degree rays, a native length-q edge meets a native length-p
edge only for its initial length-p segment. Since q>p, the shorter edge
ends at a right corner on the longer edge's interior. This verifies that
a three-beta native-corner star need not equate its three incident whole
native lengths. The observed local patch is not asserted to extend to a
monohedral plane tiling.

The statement that the private side is shorter than twice the minimum
native length excludes subdivision into two **complete** opposing sides;
it does not exclude opposing fragments, or force full matching on the
adjacent beta-to-right sides. Any individual untileability argument using
that shortcut would fail. The current proof correctly leaves those
monohedral questions unclassified.

## Reproduction, defects, uncertainty, and verdict

Both commands were freshly executed with assertions enabled:

```text
conda run --no-capture-output -n arisearch python3 research/reviews/verify_cairo_two_scalene.py
conda run --no-capture-output -n arisearch python3 research/reviews/verify_cairo_two_scalene_independent.py
```

Independent result:

```text
PASS independent Cairo audit: exact positive-root closure; all supporting halfplanes; six circular angle-flat links; connected orientable chi=0; all seam holonomies translations with rank-two span.
exact lattice area: 6*w - 3 ; bounded-domain overlap comparisons: 48
```

Certificate SHA-256:
`d05ffcae5478d61145435e3d6a20ea78f445fd19e03adc196ec7dc1a83798da1`.
The independent checks use exact arithmetic throughout, including lattice
bounding-range rounding by real algebraic numbers. No search cutoff,
sampling, floating-point sign decisions, or negative search conclusions
support the witness.

No defect or counterexample to the periodic witness or stated positive
parameter family was found. No proof repair was made by the reviewer.
The only failed inference discussed here is the already retracted whole
native-length beta-star shortcut for individual monohedral untileability.
Those individual questions and any novelty question remain outside the
verified conclusion.

**Verdict: VALID periodic witness and VALID periodic escape for the stated
positive parameter family.** The concrete pair is not aperiodic.
