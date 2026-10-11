# A periodic instance of the two-obtuse-angle pentagon–heptagon signature

**Status:** exact four-placement witness independently checked by a separate implementation; [fresh hostile review](../reviews/two-angle-5-7-periodic-review.md) valid. This is a counterexample to relying on this angle signature alone for aperiodicity. It does not exclude other metric choices with the same angles.

## Exact shapes and lattice

Let w be the unique root of

    w^12 - w^10 + w^8 - w^6 + w^4 - w^2 + 1 = 0

with 97/100 < Re(w) < 98/100 and 22/100 < Im(w) < 23/100. Thus w=exp(pi*i/14), i=w^7, and z=w^4=exp(2pi*i/7). For any power t of w put C(t)=(t+t^(-1))/2 and S(t)=(t-t^(-1))/(2i). These are real algebraic numbers.

Set s1=S(w^2), s2=S(w^4), s3=S(w^6), and define the seven positive lengths by

    l1=l2=l4=l6=1,
    l5=(2s2-s1+s3)/(2s3),
    l3=1+(s3/s1)(l5-1),
    l0=-sum_{j=1}^6 lj C(z^j).

Define v0=(0,0) and v_(j+1)=v_j+lj(C(z^j),S(z^j)) for j=0,...,6. Exactly v7=v0. The heptagon H has cyclic vertices v0,...,v6. Put

    d_j=v_j+v_(j+1), j in {0,2,4},
    c=d0-d2+d4,
    u=d2-d0,   v=d4-d0.

(The letter v without a subscript is a period vector.) The pentagon P has cyclic vertices

    v6, v0, d0-v2, d0-d2+v4, c-v6.

Both are genuine strictly convex compact polygons. H has seven angles 5pi/7. P has one angle 5pi/7 at its first vertex and four angles 4pi/7. Their side counts distinguish their congruence classes. Their coordinates are completely specified algebraic expressions in the isolated root w above; no numerical coordinates are used for a proof-critical decision.

Let L=Z*u+Z*v. The following four placement orbits form a tiling:

    {H+lambda, (-H+d0)+lambda, P+lambda, (-P+c)+lambda : lambda in L}.

In particular this pair has two independent translational periods. Each member individually has no monohedral tiling: H is a genuine heptagon, excluded by the global side-count theorem; P is all-obtuse and a pentagon, excluded by the all-obtuse edge-to-edge trivalent side-count theorem. Thus this is a mixed periodic escape even after both elementary monohedral filters pass.

## Exact certificate and whole-plane proof

The [certificate](../certificates/two_angle_5_7_periodic.json) lists the coordinates of the four placements and u,v as rational coefficient vectors in Q[w]/(Phi_28). The generator [two_angle_5_7_periodic_witness.py](../searches/two_angle_5_7_periodic_witness.py) emits those lists directly from the displayed definitions. The [independent checker](../reviews/verify_two_angle_5_7_periodic.py) imports none of the generator and reads only the coefficient vectors and isolated field root.

The checker verifies the following exact statements:

1. The specified complex root is unique in its rational isolating rectangle. All coordinate values are real under that embedding. All polygons have strict supporting-side inequalities: every other vertex lies strictly on the interior side of every edge. Hence they are simple and globally strictly convex, not merely locally turning in one direction.
2. Explicit half-turn sums match H with -H+d0 and P with -P+c. Nonzero determinant det(u,v) gives a rank-two lattice. Exterior turn identities give precisely the stated angles.
3. Coordinates in the (u,v) basis give a closed interval box for every polygon. For every ordered pair i,j the possible integer shifts that can produce even box intersection lie in

       ceil(a_i-b_j) <= shift <= floor(b_i-a_j)

   in each axis, where [a_i,b_i] and [a_j,b_j] are the two polygons' respective axis extents. The actual pair domains are retained in [verification output](../certificates/two_angle_5_7_periodic_verification.json). They yield exactly 34 tests after skipping a polygon against its identical zero shift. For every such test a supporting edge normal separates the two polygon interiors. The separating-axis theorem for convex polygons proves interior disjointness for all lattice translates; outside these domains even their boxes are disjoint.
4. The sum of the four polygon areas equals abs(det(u,v)) exactly.

To deduce coverage, integrate the multiplicity of these lattice translates over a fundamental parallelogram. Each tile orbit contributes its polygon area; interior disjointness makes multiplicity at most one except on a measure-zero boundary set. Statement 4 therefore leaves an uncovered set of measure zero in every lattice cell. The union of the tiles is closed because a lattice family of fixed compact polygons is locally finite. Any missing point would consequently have an open neighbourhood of missing points and positive measure, a contradiction. The tiles cover the entire plane. This argument proves infinite coverage and does not infer it from a picture or a finite patch.

The finite exact checks supply the metric incidences and separation facts; the final integration and closed-union argument establishes the unbounded tiling. It uses only Euclidean convex geometry and the lattice placement certificate.

## Replay and failure scope

```text
conda run --no-capture-output -n arisearch python3 research/searches/two_angle_5_7_periodic_witness.py
conda run --no-capture-output -n arisearch python3 research/reviews/verify_two_angle_5_7_periodic.py
```

The generator prints the certificate without overwriting it. The checker prints its independent domain/result certificate. A replay should compare parsed JSON with retained files, keeping Python assertions enabled. The [search record](../searches/two-angle-5-7-periodic.md) states the exact domain and execution record.

The failed claim is only that two specific angle values and their corner multiplicities could by themselves force aperiodicity in this family. This exact instance admits a mixed periodic tiling. Length/chirality/neighbourhood constraints for other metric instances remain unexamined, and the full two-convex-tile problem remains unresolved.
