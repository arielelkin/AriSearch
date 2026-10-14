"""Finite combinatorial audit of one intrinsic Ammann pentagon seam feature.

This does not decide polygon congruence or planar tileability.  It verifies
that the distinctive c edge survives all unmarked dihedral relabelings and
retains all five possible pentagon diagonals as alternate chord candidates.
"""

from itertools import product


WORDS = {
    "P1": ("a", "b", "a", "c", "a"),
    "P2": ("c", "r", "r", "a", "b"),
}


def dihedral_words(word):
    n = len(word)
    for reverse, shift in product((False, True), range(n)):
        seq = word[::-1] if reverse else word
        yield (reverse, shift), seq[shift:] + seq[:shift]


def diagonals(n):
    return tuple((i, j) for i in range(n) for j in range(i + 1, n)
                 if (j - i) not in (1, n - 1))


def main():
    for name, word in WORDS.items():
        labeled = list(dihedral_words(word))
        assert len(labeled) == 10
        assert all(w.count("c") == 1 for _, w in labeled)
        # The asymmetric side cycle can name vertices and diagonals.
        # This audit proves no particular diagonal is the source cut or
        # a forced decoder; all five remain in the candidate list.
        assert len(diagonals(5)) == 5
        print(f"{name}: 10 dihedral labelings, unique c edge in each, "
              "5 retained undirected diagonals")
    print("PASS: boundary recognizability only; contact forcing unproved")


if __name__ == "__main__":
    main()
