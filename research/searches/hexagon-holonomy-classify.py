#!/usr/bin/env python3
"""Exact finite side-order classification for the distinct-length theorem.
Domain: k=5: 6*60 normalized cyclic words; k=6: 60 words.
No geometric coordinates, solver, tolerance, randomness, or resource cutoff.
"""
from itertools import combinations, permutations
from collections import Counter
import json

A = tuple(range(6))

def cycle_edges(word):
    return {frozenset((word[i], word[(i+1)%6])) for i in range(6)}

def triangles(edges):
    vertices = set().union(*edges)
    return [tuple(t) for t in combinations(sorted(vertices), 3)
            if all(frozenset(e) in edges for e in combinations(t, 2))]

def cycle_normal(word):
    return min(w[i:]+w[:i] for w in (word, tuple(reversed(word)))
               for i in range(len(w)))

def orbit_normal(word):
    private = sorted(set(word)-set(A))
    return min(cycle_normal(tuple((sign*x+shift)%6 if x<6 else mapping[x]
                    for x in word))
               for sign in (-1, 1) for shift in range(6)
               for vals in permutations(private)
               for mapping in [dict(zip(private, vals))])

def split_stars(word, retained):
    retained = set(retained)
    words = {name: tuple(('C',x) if x in retained else (name,x) for x in w)
             for name,w in [('A', A), ('B', word)]}
    edges = set().union(*(cycle_edges(w) for w in words.values()))
    ts = triangles(edges)
    if not all(any(e <= set(t) for t in ts) for e in edges):
        return None
    assert len(edges) == 12 and len(ts) == 4
    assert all(v == 1 for v in Counter(e for t in ts for e in combinations(t,2)).values())
    lookup = {}
    for name,w in words.items():
        for i in range(6):
            edge = frozenset((w[i],w[(i+1)%6]))
            assert edge not in lookup
            lookup[edge] = (name,i)
    result = [sorted(lookup[frozenset(e)] for e in combinations(t,2)) for t in ts]
    assert sorted(c for row in result for c in row) == [(n,i) for n in ('A','B') for i in range(6)]
    return result

def main():
    output = {'domain': {'k5':360, 'k6':60}, 'survivors': []}
    for k in (5,6):
        examined = 0
        for shared in combinations(A,k):
            vertices = shared + tuple(range(6,12-k))
            for tail in permutations(vertices[1:]):
                word = (vertices[0],)+tail
                if word[1]>word[-1]:
                    continue
                examined += 1
                edges = cycle_edges(A)|cycle_edges(word)
                ts = triangles(edges)
                if not all(any(e <= set(t) for t in ts) for e in edges):
                    continue
                choices = []
                for retained in combinations(shared,4):
                    stars = split_stars(word,retained)
                    if stars is not None:
                        choices.append({'retained':retained, 'stars':stars})
                assert choices
                output['survivors'].append({'k':k,'B':word,
                    'orbit':orbit_normal(word),'shared_corner_edges':len(cycle_edges(A)&cycle_edges(word)),
                    'triangles':ts,'splittings':choices})
        assert examined == output['domain'][f'k{k}']
    output['orbit_counts'] = [ {'k':k,'representative':rep,'count':count}
        for (k,rep),count in sorted(Counter((r['k'],tuple(r['orbit']))
                                  for r in output['survivors']).items()) ]
    assert len(output['survivors']) == 30
    print(json.dumps(output, indent=2))

if __name__ == '__main__':
    main()
