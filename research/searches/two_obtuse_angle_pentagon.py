"""Exact twelve-row angle synthesis and finite face incidence enumeration."""
from fractions import Fraction as F
import json

rows = []
for p in (1, 2):
    for k in range(6):
        # Solve [[k,5-k],[p,3-p]] [x,y]^T = [3,2]^T.
        det = k * (3-p) - p * (5-k)
        if det == 0:
            rows.append({"p": p, "k": k, "singular": True})
            continue
        x = F(3*(3-p)-2*(5-k), det)
        y = F(2*k-3*p, det)
        admissible = F(1,2) < x < y < 1
        row = {"p": p, "k": k, "x": str(x), "y": str(y), "admissible": admissible}
        if admissible:
            row["faces"] = [{"n": n, "alpha_count": l} for n in range(5,11)
                for l in range(n+1) if l*x+(n-l)*y == n-2]
        rows.append(row)
print(json.dumps({"domain": {"p": [1,2], "pentagon_alpha_count": [0,1,2,3,4,5],
    "face_side_count": [5,6,7,8,9,10], "angle_arithmetic": "rational multiples of pi"},
    "rows": rows}, indent=2, sort_keys=True))
