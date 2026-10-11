#!/usr/bin/env python3
"""Finite exact angular checks for the equilateral rational-angle obstruction.

No generic root-of-unity classification is searched here: that unrestricted
classification is an imported Lam--Leung theorem in the accompanying lemma.
This script enumerates all counts in the sufficient stated domains, solves
affine theta equations with Fraction, and checks an exceptional cyclotomic
closure by integer polynomial division. No symmetry reductions or solver are
used. No stochastic seed or configured timeout/memory cap is used.
"""
from fractions import Fraction
from itertools import product
import json


def affine_solutions(target, counts, interval):
    """Angles L=180-theta, S=60+theta, P=108; count order (L,S,P)."""
    low, high, low_closed, high_closed = interval
    roots = []
    identities = []
    tested = 0
    for n, m, k in counts:
        tested += 1
        constant, slope = 180*n+60*m+108*k, m-n
        if slope == 0:
            if constant == target:
                identities.append([n,m,k])
            continue
        theta = Fraction(target-constant, slope)
        if ((theta >= low if low_closed else theta > low) and
                (theta <= high if high_closed else theta < high)):
            roots.append({"counts": [n,m,k], "theta": str(theta)})
    return {"tested_count_tuples": tested, "roots": roots,
            "identities": identities}


def polynomial_remainder(coefficients, monic_divisor):
    value = list(coefficients)
    divisor_degree = len(monic_divisor)-1
    assert monic_divisor[-1] == 1
    while len(value) > divisor_degree:
        leading = value[-1]
        degree_difference = len(value)-len(monic_divisor)
        for index, coefficient in enumerate(monic_divisor):
            value[index+degree_difference] -= leading*coefficient
        while value and value[-1] == 0:
            value.pop()
    return value


def main():
    # Acute interval: L>150, S>60, P=108. Any 180- or 360-sum
    # containing L has n<=2, m<=5, k<=3; these domains overinclude.
    acute_counts = tuple(product(range(1,3), range(6), range(4)))
    acute = {str(target): affine_solutions(
        target, acute_counts, (Fraction(0), Fraction(30), False, False))
             for target in (180,360)}
    assert all(not row["roots"] and not row["identities"]
               for row in acute.values())

    # Endpoint theta=30: angles 150,90,108. The same bounds overinclude.
    boundary = {str(target): [[n,m,k] for n,m,k in acute_counts
                             if 150*n+90*m+108*k == target]
                for target in (180,360)}
    assert boundary == {"180": [], "360": []}

    # Obtuse interval: all angles>90, hence full stars have 3 corners.
    # Classify all three-corner stars containing at least one S. The
    # closed interval [30,90] records the isolated allowable parameters.
    triple_counts = tuple((n,m,k) for n,m,k in product(range(4), repeat=3)
                          if n+m+k == 3 and m >= 1)
    triples = affine_solutions(
        360, triple_counts, (Fraction(30),Fraction(90),True,True))
    assert not triples["identities"]
    assert {row["theta"] for row in triples["roots"]} == {"60","66","84"}
    assert not any(Fraction(30)<Fraction(row["theta"])<Fraction(60)
                   for row in triples["roots"])

    # Exceptional hexagon: every possible sum containing 168 degrees
    # fits counts n=1..2, m=0..6 of 60, k=0..3 of 108.
    exceptional_counts = tuple(product(range(1,3),range(7),range(4)))
    exceptional = {str(target): [[n,m,k] for n,m,k in exceptional_counts
                                 if 168*n+60*m+108*k == target]
                   for target in (180,360)}
    assert exceptional == {"180": [], "360": []}

    # exp(2*pi*i*j/30), j in (5,6,12,18,24,25). Phi30 exact data.
    closure_polynomial = [0]*26
    for exponent in (5,6,12,18,24,25):
        closure_polynomial[exponent] += 1
    phi30 = [1,1,0,-1,-1,-1,0,1,1]
    remainder = polynomial_remainder(closure_polynomial,phi30)
    assert remainder == []
    directions = (60,72,144,216,288,300)
    turns = tuple((directions[i]-directions[i-1])%360 for i in range(6))
    assert all(0<turn<180 for turn in turns)
    angles = tuple(180-turn for turn in turns)
    assert angles == (60,168,108,108,108,168)

    mono_regular = {str(target): [k for k in range(1,4) if 108*k == target]
                    for target in (180,360)}
    assert mono_regular == {"180": [], "360": []}
    print(json.dumps({
        "claim": "finite angular checks for equilateral rational-angle pentagon-pair obstruction",
        "acute_L_corner": acute,
        "theta_30_L_corner": boundary,
        "three_corner_rows_containing_S": triples,
        "exceptional_168_corner": exceptional,
        "regular_pentagon_corner": mono_regular,
        "exceptional_closure": {"root_order":30,
            "exponents":[5,6,12,18,24,25], "phi30_coefficients_low_to_high":phi30,
            "polynomial_remainder": remainder, "turns":turns, "angles":angles},
        "scope": "bounded exact counts plus fixed exceptional closure; global polygon classification and periodic construction are proved separately",
        "verdict": "all stated angular obstructions verified"
    },indent=2))


if __name__ == "__main__":
    main()
