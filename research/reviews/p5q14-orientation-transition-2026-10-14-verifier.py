"""Small independent verifier of all64 pointed forced-neighbor T witnesses.

Imports neither transition producer nor earlier adversary modules. It uses
a NumberField presentation, reconstructs native polygons and reflected
alpha mates from frozen raw placements, audits all28 normalization maps,
and generates all Q-v attachments by both endpoint orders and both hands.
The earlier complete ring/palette classifications are explicit dependencies.
"""
import argparse
import json
from collections import Counter
from functools import cache
from pathlib import Path

from sage.all import AA, QQ, QQbar, NumberField, PolynomialRing

ROOT = Path(__file__).resolve().parents[1]
R = PolynomialRing(QQ, 't')
t = R.gen()
K = NumberField(t**12-t**10+t**8-t**6+t**4-t**2+1, 'z')
z = K.gen()
conj = K.hom([z**-1], K)
embedding = K.hom([QQbar.zeta(28)], QQbar)
i = z**7


def decode(a):
    return sum((QQ(c)*z**j for j, c in enumerate(a)), K(0))


def cross(a, b):
    return (conj(a)*b-a*conj(b))/(2*i)


@cache
def sign(a):
    assert a == conj(a)
    r = AA(embedding(a))
    return 1 if r > 0 else -1 if r < 0 else 0


def area(F):
    return sum(cross(a, F[(j+1) % len(F)]) for j, a in enumerate(F))/2


def moved(F, hand, rotation, shift):
    return tuple(shift+rotation*(p if hand == 1 else conj(p)) for p in F)


def alpha_mate(F):
    # Reflection in native y edge fixes unique alpha and beta endpoints.
    a, b = F[4], F[0]
    return tuple(a+(b-a)/conj(b-a)*conj(p-a) for p in F)


def key(F):
    return frozenset(F)


def run(certificate):
    producer = json.loads((ROOT/'certificates'/'contact-pentagon-5pi7-q14-exact.json').read_text())
    palette = json.loads((ROOT/'certificates'/'construction-adversary-2026-10-14-p5q14-palette.json').read_text())
    data = json.loads(certificate.read_text())
    s = (z-z**-1)/(2*i)
    y = 2*s+4*s*s
    v = 1+2*s*(1-y)
    P = [K(0)]
    edges = [L*z**e for L, e in zip([1, 1, 1, v, y], [-5, 1, 7, 13, 19])]
    for edge in edges[:-1]:
        P.append(P[-1]+edge)
    assert P[-1]+edges[-1] == 0
    P = tuple(P)
    assert P == tuple(map(decode, producer['source']['P_vertices']))
    assert sign(area(P)) == 1 and sign(y) > 0 and sign(1-y) > 0 and sign(v-1) > 0
    rows = {r['period']: r for r in producer['rows']}

    def patch(period, cycle):
        row = rows[period]
        Q = tuple(map(decode, row['Q_vertices']))
        assert tuple(Q[(j+1) % 14]-Q[j] for j in range(14)) == tuple(
            (v if tag == 'v' else 1)*z**(2*j) for j, tag in enumerate(period*2))
        faces = [Q]
        for j, bit in enumerate(cycle):
            guest = [g for g in row['raw_native_guests'][j] if g['rejection'] is None][bit]
            faces.append(moved(P, guest['hand'], decode(guest['rotation']), decode(guest['shift'])))
        identities = {key(F) for F in faces}
        for F in faces[1:].copy():
            mate = alpha_mate(F)
            if key(mate) not in identities:
                faces.append(mate)
                identities.add(key(mate))
        assert len(faces) == len(identities) == 21
        return tuple(faces)

    positives = {}
    for r in palette['patches']:
        if r['status'] == 'no_obstruction_in_this_patch':
            assert r['word'][:7] == r['word'][7:]
            period = ''.join('v' if bit else 'u' for bit in r['word'][:7])
            cycle = tuple(1-bit for bit in r['cycle'])
            positives[(period, cycle)] = patch(period, cycle)
    assert len(positives) == 28
    cycles = sorted(cycle for period, cycle in positives if period == 'vvuvvuu')
    assert len(cycles) == 4 and data['central_cycles'] == [list(c) for c in cycles]
    states = [positives['vvuvvuu', c] for c in cycles]
    Q = states[0][0]
    # Verify the entire normalization certificate, not just its stated count.
    normalized = set()
    for record in data['normalization_of_all_28_indexed_states']:
        source = record['period'], tuple(record['author_cycle'])
        assert source in positives and source not in normalized
        normalized.add(source)
        m = record['normalization']
        rotation, shift = z**m['rotation_exponent'], decode(m['shift'])
        transformed = [moved(F, 1, rotation, shift) for F in positives[source]]
        target = states[m['state']]
        assert set(map(key, transformed)) == set(map(key, target))
        indices = m['target_face_indices']
        assert len(indices) == 21 and set(indices) == set(range(21))
        assert all(key(F) == key(target[j]) for F, j in zip(transformed, indices))
        assert all(F == target[j] for F, j in zip(transformed[1:], indices[1:]))
    assert normalized == set(positives)

    indexed = {(r['central_state'], r['Q_hand'], r['Q_native_side']): r for r in data['records']}
    sides = [j for j, tag in enumerate('vvuvvuu'*2) if tag == 'v']
    expected = {(state, hand, side) for state in range(4) for hand in [1, -1] for side in sides}
    assert set(indexed) == expected and len(indexed) == len(data['records']) == 64
    physical_counts = []
    parameters = Counter()
    for state, faces in enumerate(states):
        F = faces[6]
        assert F == states[0][6] and faces[7] == states[0][7] and faces[16] == states[0][16]
        assert alpha_mate(F) == faces[16]
        a, b = F[3], F[4]
        assert not any({a, b} == {Q[j], Q[(j+1) % 14]} for j in range(14))
        fcentre = sum(F)/5
        seen_physical = set()
        for hand in [1, -1]:
            base = Q if hand == 1 else tuple(map(conj, Q))
            for side in sides:
                choices = []
                # Generate both edge endpoint maps, then independently
                # select the one with polygons on opposite halfplanes.
                for start, end in [(a, b), (b, a)]:
                    rotation = (end-start)/(base[(side+1) % 14]-base[side])
                    shift = start-rotation*base[side]
                    qface = moved(Q, hand, rotation, shift)
                    qcentre = sum(qface)/14
                    if sign(cross(b-a, qcentre-a))*sign(cross(b-a, fcentre-a)) < 0:
                        choices.append((rotation, shift, qface))
                assert len(choices) == 1
                rotation, shift, qface = choices[0]
                assert rotation*conj(rotation) == 1
                rec = indexed[state, hand, side]
                assert rotation == z**rec['rotation_exponent'] and shift == decode(rec['shift'])
                w = rec['witness']
                assert w['kind'] == 'forbidden_T_contact' and w['subject_is_second']
                assert w['new_face'] == 0 and w['old_face'] in [7, 16] and w['host_side'] == 3
                host = faces[w['old_face']]
                p = qface[w['subject_corner']]
                hstart, hend = host[3], host[4]
                assert p == decode(rec['point']) and hstart == decode(rec['host_start'])
                assert hend == decode(rec['host_end'])
                assert cross(hend-hstart, p-hstart) == 0
                dot = ((p-hstart)*conj(p-hend)+(p-hend)*conj(p-hstart))/2
                assert sign(dot) < 0
                parameter = (p-hstart)/(hend-hstart)
                assert parameter == decode(rec['segment_parameter'])
                assert parameter in (1/v, 1-1/v)
                assert sign(parameter) > 0 and sign(1-parameter) > 0
                parameters[str(parameter)] += 1
                seen_physical.add(key(qface))
        assert len(seen_physical) == 4
        physical_counts.append(len(seen_physical))
    assert data['summary'] == {'central_states': 4, 'indexed_Q_attachments': 64,
                               'forbidden_T_contacts': 64, 'compatible_Q_attachments': 0}
    print('PASS independent NumberField reconstruction: all28 indexed states normalize to4;')
    print('all64 outside Q-v attachments (both hands, all8 native sides) have pointed strict T contacts;')
    print('four physical Q placements per central state; parameter multiplicities:', dict(parameters))


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('certificate', nargs='?', type=Path,
                   default=ROOT/'certificates'/'p5q14-orientation-transition-2026-10-14-compact.json')
    run(p.parse_args().certificate)
