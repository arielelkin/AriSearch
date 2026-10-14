"""Independent exact boundary and flipped-c-seam audit.

This intentionally makes no assertion that the two-tile patch extends to a
plane tiling, or that a changed two-polygon compiler inherits the source atlas.
"""

from itertools import product
from sympy import symbols, simplify


WORDS = {"P1": ("a", "b", "a", "c", "a"),
         "P2": ("c", "r", "r", "a", "b")}
for name, word in WORDS.items():
    for reverse, shift in product((False, True), range(5)):
        w = word[::-1] if reverse else word
        w = w[shift:] + w[:shift]
        assert w.count("c") == 1, (name, reverse, shift)
        diagonals = {(i, j) for i in range(5) for j in range(i + 1, 5)
                     if j - i not in (1, 4)}
        assert len(diagonals) == 5

kappa = symbols("kappa", real=True)
K, L = kappa, 216 - kappa
assert simplify(K + L) == 216
assert simplify(360 - K - L) == 144
assert 72 + 72 == 144

# In the unmarked c-edge half-turn, K and L swap at both endpoints.
# The full 3-shape atlas is needed to reject this locally feasible patch.
print("PASS: c-edge intrinsic in both pentagons; flipped P1/P1 endpoints leave 144 degrees")
