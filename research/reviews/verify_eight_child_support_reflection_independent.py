#!/usr/bin/env python3
"""Independent exact checks of the specified eight-child angle-slice exclusion.

No author imports, geometric enumeration, solver, samples, or retained outputs.
Universal inequalities are certified by nonnegative numerator and denominator
coefficients after positive-variable parametrization, in Q(sqrt(3)). The finite
angle domain deliberately permits more mates than an actual placement might.
"""
from itertools import product
import sys

from sage.all import AA, NumberField, PolynomialRing, QQ


def main():
    if sys.flags.optimize:
        raise RuntimeError("Assertions must be enabled.")
    base = PolynomialRing(QQ, "z")
    K = NumberField(base.gen()**2 - 3, "r", embedding=AA(3).sqrt())
    r = K.gen()
    ring = PolynomialRing(K, names=("T", "U", "R"))
    F = ring.fraction_field()
    T, U, R = map(F, ring.gens())
    # T>0 parametrizes 0<tan(epsilon/2)<2-sqrt(3), exactly 0<epsilon<30.
    t = (2-r)*T/(1+T)
    s = 2*t/(1+t*t)
    c = (1-t*t)/(1+t*t)
    assert c*c+s*s == 1
    c60, s60 = (c+r*s)/2, (r*c-s)/2
    c30 = (r*c+s)/2
    assert c60*c60+s60*s60 == 1

    def positive(expr):
        """Sufficient exact sign certificate on all T,U,R>0."""
        expr = F(expr)
        n, d = expr.numerator(), expr.denominator()
        # Field normalization may choose a common negative sign.
        if all(a <= 0 for a in d.coefficients()):
            n, d = -n, -d
        assert n and d
        assert all(a >= 0 for a in n.coefficients()), n
        assert all(a >= 0 for a in d.coefficients()), d
        return True

    assert positive(s) and positive(c) and positive(c30) and positive(s60)
    assert positive((2-r)-t)
    # The closure residuals come directly from the five independently expanded
    # edge directions 0,60-epsilon,180-epsilon,240,300 degrees.
    def closure(x, u, w, v, y):
        return (x+u*c60-w*c-v/2+y/2,
                u*s60+w*s-r*(v+y)/2)

    # Branch A: reflex native corner 0, hence x=y=1 and u=U>0.
    wA = (r+U*s)/c30
    vA = 3+2*U*c60-2*wA*c
    assert closure(F(1), U, wA, vA, F(1)) == (0, 0)
    # No need to assume vA>0: this proves the bound on a larger domain.
    assert positive(wA-r)

    # Branch B: reflex native corner 4, hence v=y=1.
    # Positivity of u is equivalent to 0<x<sqrt(3)*cot(epsilon).
    bound = r*c/s
    xB = bound*R/(1+R)
    uB = 2*c-2*xB*s/r
    wB = 2*xB*s60/r+2*c60
    assert closure(xB, uB, wB, F(1), F(1)) == (0, 0)
    assert uB == 2*c/(1+R)
    assert positive(xB) and positive(bound-xB) and positive(uB)
    # Check the original affine endpoint argument as an identity too.
    wdiff_at_zero = 2*c60
    wdiff_at_upper = 2*bound*s60/r+2*c60-bound
    assert wdiff_at_upper == r*(1-c)/s
    assert wB-xB == (wdiff_at_zero+R*wdiff_at_upper)/(1+R)
    assert positive(wB-xB) and positive(wB-1)

    # Angle expressions are exact affine pairs (constant, epsilon coefficient).
    angles = ((120, 0), (120, 1), (60, 0), (120, -1), (120, 0))
    a120 = (120, 0)
    assert [i for i, a in enumerate(angles) if a == a120] == [0, 4]
    # Contact side j uses vertices j,j+1; its neighboring spoke edges leave
    # j+2 and j-1, so the two parent edges meet at j+3. Check both orders.
    parent_angles = []
    for j in range(5):
        boundary_path = ((j+2)%5, (j+3)%5, (j+4)%5)
        assert boundary_path[0] == (j+2)%5
        assert boundary_path[-1] == (j-1)%5
        assert boundary_path[1] == boundary_path[::-1][1]
        parent_angles.append(angles[boundary_path[1]])
    assert tuple(parent_angles) == ((120, -1), a120, a120, (120, 1), (60, 0))

    target_words = set()
    for word in (angles, angles[::-1]):
        for k in range(5):
            target_words.add(word[k:]+word[:k])
    q_angles = set(angles)  # Superset: a similar parent must use one of these.
    assert not any(word[0] == word[2] == a120 for word in target_words)

    # Branch A w!=v and all branch B metrics: w can only match native 1 or 2.
    # Allow ANY native edge on either v-contact sector, including all aliases.
    ordinary_count = 0
    for left_w, left_v, right_v, right_w in product((1, 2), range(5), range(5), (1, 2)):
        for q in q_angles:
            word = (q, parent_angles[left_w], parent_angles[left_v],
                    parent_angles[right_v], parent_angles[right_w])
            assert word not in target_words
            ordinary_count += 1
    assert ordinary_count == 400

    # Branch A w=v: every nonreflex side match lies in {1,2,3}, permitting u=w.
    alias_count = 0
    for indices in product((1, 2, 3), repeat=4):
        for q in q_angles:
            word = (q, *(parent_angles[j] for j in indices))
            assert word not in target_words
            alias_count += 1
    assert alias_count == 324
    print("PASS: both exact closure branches, universal strict metric bounds, "
          "all five native parent-corner indices, both reflex cases, "
          "400 ordinary and 324 w=v alias parent-angle words (cyclic/reversed).")


if __name__ == "__main__":
    main()
