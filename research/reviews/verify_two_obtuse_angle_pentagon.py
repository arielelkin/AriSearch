"""Independent table verifier: integer cross-products, no linear-system solver."""
from pathlib import Path
from fractions import Fraction
import json

root = Path(__file__).resolve().parents[2]
c = json.loads((root / "research/certificates/two_obtuse_angle_pentagon.json").read_text())
expected = {
    (1,4): (Fraction(4,7), Fraction(5,7), [(5,4),(6,2),(7,0)]),
    (1,5): (Fraction(3,5), Fraction(7,10), [(5,5),(6,2)]),
    (2,5): (Fraction(3,5), Fraction(4,5), [(5,5),(6,4),(7,3),(8,2),(9,1),(10,0)])}
rows = c["rows"]
assert len(rows) == 12
assert {(r["p"],r["k"]) for r in rows} == {(p,k) for p in (1,2) for k in range(6)}
for r in rows:
    p,k = r["p"],r["k"]
    assert not r.get("singular", False)
    x,y = Fraction(r["x"]),Fraction(r["y"])
    X,Y = x.numerator*y.denominator,y.numerator*x.denominator
    d = x.denominator*y.denominator
    assert k*X+(5-k)*Y == 3*d
    assert p*X+(3-p)*Y == 2*d
    legal = d < 2*X and X < Y and Y < d
    assert r["admissible"] == legal
    assert legal == ((p,k) in expected)
    if legal:
        ex,ey,ef = expected[p,k]
        assert (x,y) == (ex,ey)
        actual = [(z["n"],z["alpha_count"]) for z in r["faces"]]
        assert actual == ef
        assert actual == [(n,l) for n in range(5,11) for l in range(n+1)
                          if l*X+(n-l)*Y == (n-2)*d]
print("PASS: exact two-obtuse-angle pentagon table (12 angle rows; all retained face rows).")
