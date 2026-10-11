#!/usr/bin/env python3
"""Exact twelve-case equal-private closure classification for regular unit P.

Q has alpha corners0,d, d in2,3,4. One private side is incident to each;
all other native lengths are1. No period search or solver is used.
"""
import argparse
import json
from pathlib import Path
from sage.all import AA, QQbar, CyclotomicField

K = CyclotomicField(10)
z = K.gen()
phi = z+z**-1


def classify():
    rows = []
    for d in (2, 3, 4):
        directions = [j+int(j >= d) for j in range(8)]
        missing_sum = z**d+z**9
        assert sum(z**j for j in directions) == -missing_sum
        for i in (7, 0):
            for j in (d-1, d):
                coefficient = z**directions[i]+z**directions[j]
                row = {"alpha_gap": d, "private_sides": [i, j]}
                if coefficient == 0:
                    row["closure"] = "all L" if missing_sum == 0 else "inconsistent"
                    row["positive_nonunit_admissible"] = missing_sum == 0
                else:
                    value = 1+missing_sum/coefficient
                    real = QQbar(value).imag() == 0
                    row["closure"] = str(value)
                    row["real"] = real
                    row["positive_nonunit_admissible"] = bool(real and AA(QQbar(value).real()) > 0 and value != 1)
                    row["L_cyclotomic_coefficients"] = [str(q) for q in value.list()]
                rows.append(row)
    admitted = {(row["alpha_gap"], *row["private_sides"])
                for row in rows if row["positive_nonunit_admissible"]}
    assert admitted == {(2, 0, 1), (3, 0, 2), (4, 7, 3), (4, 0, 4)}
    by_key = {(row["alpha_gap"], *row["private_sides"]): row for row in rows}
    for key, expected in (((2, 0, 1), phi), ((3, 0, 2), (5-(2*phi-1))/2)):
        row = by_key[key]
        assert K([int(q) if q.lstrip("-").isdigit() else q for q in row["L_cyclotomic_coefficients"]]) == expected
    return {"status": "complete exact twelve-case closure classification",
            "domain": "d=2,3,4; i in{7,0}; j in{d-1,d}; both private lengths L>0,L!=1; other6 lengths1",
            "field": "Q(z), z=exp(pi*i/5), z^4-z^3+z^2-z+1=0",
            "reduction_dependencies": "all-obtuse forcing; private sides alpha-beta, one incident to each nonadjacent alpha corner",
            "equation": "(L-1)*(z^k_i+z^k_j)=z^d+z^9; k_j=j+1[j>=d]",
            "cases": rows,
            "admitted_rows": [list(key) for key in sorted(admitted)],
            "distinct_geometry_classes": ["d2 private0,1 L=phi reflection", "d3 private0,2 L=(5-sqrt5)/2 reflection", "d4 private3,7 any L>0,L!=1 central;0,4 reflected equivalent"],
            "search_scope": "closure only; does not establish plane tilability",
            "software": {"SageMath": "10.9", "Python": "3.12.13"}}


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run without Python -O")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(classify(), indent=2)+"\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")
