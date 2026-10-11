# A scalene Cairo-angle pair and its exact periodic escape

**Status:** exactly certified and adversarially reviewed; [fresh hostile review](../reviews/cairo-two-scalene-periodic-review.md) valid. The proposed family is falsified as an aperiodicity mechanism.
Monohedral tilability of either concrete member remains unclassified here.

## Exact two-pentagon object

Let w be the positive root of x^2-3, isolated by 1<w<2. Let

    p=1, r=1/2, q=w-1/2, s=2-w/2.

All four lengths p,q,r,s are positive and distinct. In counterclockwise order,
with side i joining vertex v_i to v_(i+1), define

    A = [(0,0),(q,0),(q,p),(q-w*p/2,3*p/2),(-r/2,w*r/2)],
    B = [(0,0),(p,0),(p,q),(p-w*q/2,3*q/2),(-s/2,w*s/2)].

Both are strictly convex pentagons. Their ordered side lengths are

    A: (q,p,p,q,r),
    B: (p,q,q,p,s).

The interior angle after side i is (90,120,90,120,120) degrees, for i=0,...,4.
Neither is equilateral; at either right corner the two adjacent sides have
unequal lengths p and q, so the familiar equal-right-arm Cairo construction
does not apply individually. No general monohedral exclusion is claimed.
The two polygons are noncongruent, since A has side length r and B does not.

The independent Sage checker verifies exact squared lengths, angle cosines,
strict half-plane convexity, distinct congruence classes by their side-length
multisets, and all topology below over Q(w), with no floating-point decisions.

## An entire parameter family

More generally take p>0 and 0<r<2p/w, and set

    q=w*p-r, s=2p-w*r.

Then p,q,r,s>0, q+r=w*p and s=w*q-p. The same coordinate formulas and side
patterns close exactly. The five side directions are 0,90,150,240,300 degrees,
so consecutive exterior turns are 90,60,90,60,60 degrees. Direct side-support
determinants are positive. For A, writing t=w, the nonadjacent vertex tests
for successive edges reduce to the following positive quantities:

    edge0: pq, 3pq/2, tqr/2;
    edge1: pq, tp^2/2, p(q+r/2);
    edge2: p(tp+q)/2, tp^2/2, pq;
    edge3: tqr/2, 3pq/2, pq;
    edge4: trq/2, r(p+tq)/2, trq/2.

B is the same calculation after exchanging p,q and replacing r by s,
because p=w*q-s. Thus the family supplies whole strictly convex pentagons.
Some parameter values make them congruent; the concrete parameters above do
not. The periodic escape below holds throughout the positive family.

## Four whole faces form a flat torus

Take faces 0=A0,1=A1,2=B0,3=B1, all in the displayed reference orientations.
Use corner c_i after side i. Side i has endpoints c_(i-1),c_i. Pair all twenty
whole sides by reversing endpoint order in each of the following ten seams:

    (0,0)-(2,1), (0,3)-(3,2),
    (1,0)-(3,1), (1,3)-(2,2),
    (0,1)-(3,0), (0,2)-(2,3),
    (1,1)-(2,0), (1,2)-(3,3),
    (0,4)-(1,4), (2,4)-(3,4).

Every paired side has equal exact length: the first four pairs use q, the next
four use p, and the last two pair the private lengths r and s separately.
The quotient is connected and orientable. Its six vertex classes are

    [A0c0,A1c0,B0c0,B1c0],
    [A0c2,A1c2,B0c2,B1c2],
    [A0c1,B0c3,B1c4],
    [A0c3,A1c4,B1c1],
    [A0c4,A1c3,B0c1],
    [A1c1,B0c4,B1c3].

The first two have four right angles; the other four have three120-degree
angles. Each link is circular and every cone angle is360 degrees. There are
V=6,E=10,F=4, hence Euler characteristic0. The quotient is a compact flat
orientable torus. As in the [earlier flat-torus proof](hexagon-holonomy-distinct-lengths.md),
its universal cover is Euclidean R^2, with lifted faces congruent to the
original whole A,B. Deck translations give two independent periods.

Thus this exact two-pentagon pair tiles globally, but the periodic witness
kills it as an aperiodic candidate. The same finite gluing kills the complete
positive parameter family; no bounded failure-to-find assertion is used.

## Exact evidence and the failed monohedral shortcut

[Exact coordinates and seams](../certificates/cairo-two-scalene-torus.json)
and [the verifier](../reviews/verify_cairo_two_scalene.py) retain this witness.
Replay:

```text
conda run --no-capture-output -n arisearch python3 research/reviews/verify_cairo_two_scalene.py
```

The [independent verifier](../reviews/verify_cairo_two_scalene_independent.py) also derives an explicit translation lattice and checks every possible overlap by exact lattice-coordinate bounds. It passes all48 comparisons and proves full coverage from equality of motif and lattice areas. The [execution record](../searches/cairo-two-scalene-torus.md) states the full
finite scope, exact field, and runtime conditions.

A tempting claim that each member cannot tile monohedrally by a beta-corner
length graph is invalid under unrestricted contacts. A120-degree corner cannot
be a T-junction against a straight side, but an adjacent native side can end
later in a90-degree T-junction. Its whole length need not match the whole
length of the neighboring tile's side at the original beta vertex. The exact
three-copy local patch in [the partial-contact diagnostic](../counterexamples/cairo-partial-beta-length-graph.md)
exhibits these unequal native lengths at a beta vertex. It is not asserted
to extend to a monohedral plane tiling. Monohedral tilability remains open for
these concrete polygons in the retained argument. No novelty claim is made.
