"""Exact integer audit of a triangular-lattice two-hexagon power-cell fixture.

All side lengths printed here are in units of 1/(2 sqrt(3)).
"""

from collections import Counter

STEPS = ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))


def weight(i, j):
    return (i + j // 2) % 2


def sides(i, j):
    s = weight(i, j)
    neighbors = [weight(i + di, j + dj) for di, dj in STEPS]
    return tuple(
        4 + s + neighbors[k] - neighbors[(k - 1) % 6] - neighbors[(k + 1) % 6]
        for k in range(6)
    )


def canonical(word):
    return min(
        tuple(word[(j + orientation * k) % 6] for k in range(6))
        for j in range(6)
        for orientation in (-1, 1)
    )


def audit():
    words = {(i, j): sides(i, j) for i in range(2) for j in range(4)}
    classes = {key: canonical(value) for key, value in words.items()}
    assert len(set(classes.values())) == 2
    assert all(min(word) > 0 for word in words.values())
    assert all(word[0] - word[3] == word[2] - word[5] == -(word[1] - word[4])
               for word in words.values())
    assert all(any(word[k] != word[k + 3] for k in range(3))
               for word in words.values())
    assert all(weight(i + 2, j) == weight(i, j) == weight(i, j + 4)
               for i in range(2) for j in range(4))
    for i in range(2):
        for j in range(4):
            word = sides(i, j)
            for k, (di, dj) in enumerate(STEPS):
                assert word[k] == sides(i + di, j + dj)[(k + 3) % 6]

    corners = {tuple(sorted((word[k - 1], word[k])))
               for word in set(classes.values()) for k in range(6)}
    completion = {}
    for a, b in corners:
        possible = sorted({c for edge in corners for c in edge
                           if tuple(sorted((a, c))) in corners
                           and tuple(sorted((b, c))) in corners})
        completion[(a, b)] = possible
    print('classes:', sorted(set(classes.values())))
    print('site classes:', sorted(classes.items()))
    print('species counts:', Counter(classes.values()))
    print('corner completions:', sorted(completion.items()))
    print('central patch:')
    print(' (0,0)', weight(0, 0), sides(0, 0))
    for k, (i, j) in enumerate(STEPS):
        print(' side', k, 'length', sides(0, 0)[k], 'neighbor', (i, j),
              'weight', weight(i, j), 'word', sides(i, j))


if __name__ == '__main__':
    audit()
