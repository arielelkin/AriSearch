"""Exact contact-derived Q-neighbor completion domain, no patch-size grid.

Normalize Q to vvuvvuu twice. Its four audited palette-positive rings are
reconstructed from frozen raw placements. For each of its six unit guests,
the exposed native P-v side forces a Q. Try all eight Q-v native indices,
both Q hands, and all four audited mandatory states. Both isometry hands
are included even though this Q has reflection symmetry. Actual face
identities are deduplicated only after their indexed obligations are kept.
"""
import argparse
import json
from collections import Counter
from functools import cache
from itertools import combinations
from pathlib import Path
from platform import python_version
import runpy

from sage.all import QQ
from sage.env import SAGE_VERSION

ROOT = Path(__file__).resolve().parents[1]
D = runpy.run_path(str(ROOT/'reviews'/'construction-adversary-2026-10-14-p5q14-independent.py'))
K, z, P = D['K'], D['z'], tuple(D['P'])
conj, cross, real, sign = D['conj'], D['cross'], D['real'], D['sign']


def encode(q):
    return [str(a) for a in q.list()]+['0']*(12-len(q.list()))


def decode(a):
    return sum((QQ(t)*z**i for i, t in enumerate(a)), K(0))


def alpha_mate(F):
    a, b = F[4], F[0]
    return tuple(a+(b-a)/conj(b-a)*conj(p-a) for p in F)


def face_key(F):
    return frozenset(F)


def transform(F, hand, rotation, shift):
    return tuple(rotation*(p if hand == 1 else conj(p))+shift for p in F)


@cache
def ccw(F):
    return F if sign(D['area'](list(F))) > 0 else tuple(reversed(F))


@cache
def disjoint(F, G):
    # Exact separating support test for closed convex polygons, with
    # interiors disjoint iff at least one native support separates them.
    for H, Other in ((ccw(F), G), (ccw(G), F)):
        for i, a in enumerate(H):
            edge = H[(i+1) % len(H)]-a
            if all(sign(cross(edge, p-a)) <= 0 for p in Other):
                return True
    return False


@cache
def strict_segment(p, a, b):
    return cross(b-a, p-a) == 0 and sign(real((p-a)*conj(p-b))) < 0


def pair_defect(F, G):
    if face_key(F) == face_key(G):
        return None
    if not disjoint(F, G):
        return {'kind': 'positive_area_overlap'}
    for subject, host, reverse in ((F, G, False), (G, F, True)):
        for c, p in enumerate(subject):
            for e, a in enumerate(host):
                if strict_segment(p, a, host[(e+1) % len(host)]):
                    return {'kind': 'forbidden_T_contact', 'subject_is_second': reverse,
                            'subject_corner': c, 'host_side': e}
    return None


def combined_defect(faces, newfaces):
    oldkeys = {face_key(F) for F in faces}
    for b, G in enumerate(newfaces):
        if face_key(G) in oldkeys:
            continue
        for a, F in enumerate(faces):
            witness = pair_defect(F, G)
            if witness:
                return {'old_face': a, 'new_face': b, **witness}
    actual = list(faces)
    actual.extend(G for G in newfaces if face_key(G) not in oldkeys)
    groups = {}
    for f, F in enumerate(actual):
        for c, p in enumerate(F):
            counts = groups.setdefault(p, [0, 0, 0])
            counts[2 if len(F) == 14 else 0 if c == 0 else 1] += 1
    for p, counts in groups.items():
        if not any(all(a <= b for a, b in zip(counts, star))
                   for star in ((2, 1, 0), (0, 2, 1))):
            return {'kind': 'forbidden_native_star', 'point': encode(p), 'counts': counts}
    return None


def reconstruct(row, cycle):
    faces = [tuple(map(decode, row['Q_vertices']))]
    for slot, choice in enumerate(cycle):
        placement = [a for a in row['raw_native_guests'][slot]
                     if a['rejection'] is None][choice]
        faces.append(transform(P, placement['hand'], decode(placement['rotation']),
                               decode(placement['shift'])))
    keys = {face_key(F) for F in faces}
    for F in faces[1:].copy():
        M = alpha_mate(F)
        if face_key(M) not in keys:
            keys.add(face_key(M))
            faces.append(M)
    assert len(faces) == len(keys) == 21
    return tuple(faces)


def source_data():
    producer = json.loads((ROOT/'certificates'/'contact-pentagon-5pi7-q14-exact.json').read_text())
    palette = json.loads((ROOT/'certificates'/'construction-adversary-2026-10-14-p5q14-palette.json').read_text())
    assert P == tuple(map(decode, producer['source']['P_vertices']))
    return producer, palette


def load_states():
    producer, palette = source_data()
    row = next(r for r in producer['rows'] if r['period'] == 'vvuvvuu')
    Q = tuple(map(decode, row['Q_vertices']))
    cycles = sorted(tuple(1-c for c in r['cycle']) for r in palette['patches']
                    if r['status'] == 'no_obstruction_in_this_patch'
                    and r['word'][:7] == [1, 1, 0, 1, 1, 0, 0])
    assert len(cycles) == 4
    states = [reconstruct(row, cycle) for cycle in cycles]
    return Q, cycles, states


def normalization(Q, states):
    producer, palette = source_data()
    rows = {r['period']: r for r in producer['rows']}
    results = []
    for record in palette['patches']:
        if record['status'] != 'no_obstruction_in_this_patch':
            continue
        period = ''.join('v' if bit else 'u' for bit in record['word'][:7])
        cycle = tuple(1-c for c in record['cycle'])
        faces = reconstruct(rows[period], cycle)
        oldQ = faces[0]
        matches = []
        for side in range(14):
            rotation = (Q[(side+1) % 14]-Q[side])/(oldQ[1]-oldQ[0])
            if rotation*conj(rotation) != 1:
                continue
            shift = Q[side]-rotation*oldQ[0]
            moved = tuple(transform(F, 1, rotation, shift) for F in faces)
            if face_key(moved[0]) != face_key(Q):
                continue
            for state, target in enumerate(states):
                targetkeys = {face_key(F): j for j, F in enumerate(target)}
                if set(map(face_key, moved)) != set(targetkeys):
                    continue
                indices = [targetkeys[face_key(F)] for F in moved]
                # Whole-P congruence preserves the unique alpha and unique
                # v/y sides, hence all five native labels. Verify that fact
                # here, beyond merely identifying unordered polygons.
                assert all(moved[j] == target[indices[j]] for j in range(1, 21))
                exponents = [k for k in range(28) if rotation == z**k]
                assert len(exponents) == 1
                matches.append({'state': state, 'rotation_exponent': exponents[0],
                                'shift': encode(shift), 'target_face_indices': indices})
        assert matches
        results.append({'period': period, 'author_cycle': list(cycle),
                        'normalization': matches[0]})
    assert len(results) == 28
    return results


def run_compact():
    Q, cycles, states = load_states()
    qv = [j for j, tag in enumerate('vvuvvuu'*2) if tag == 'v']
    records = []
    for state, faces in enumerate(states):
        # Only this one obligation is required in the theorem: unit-slot5
        # P guest, its obligatory Q-v side. All four central states agree
        # on this guest, the unit-slot6 guest and the first guest's mate.
        F = faces[6]
        assert face_key(F) == face_key(states[0][6])
        a, b = F[3], F[4]
        phand = sign(D['area'](list(F)))
        actual = {}
        for hand in (1, -1):
            base = Q if hand == 1 else tuple(map(conj, Q))
            for side in qv:
                start, end = (b, a) if phand == hand else (a, b)
                rotation = (end-start)/(base[(side+1) % 14]-base[side])
                shift = start-rotation*base[side]
                qface = transform(Q, hand, rotation, shift)
                assert rotation*conj(rotation) == 1 and disjoint(F, qface)
                witness = combined_defect(faces, (qface,))
                assert witness['kind'] == 'forbidden_T_contact'
                assert witness['subject_is_second'] and witness['new_face'] == 0
                host = faces[witness['old_face']]
                p = qface[witness['subject_corner']]
                hstart = host[witness['host_side']]
                hend = host[(witness['host_side']+1) % 5]
                parameter = (p-hstart)/(hend-hstart)
                assert parameter == conj(parameter) and sign(parameter) > 0 and sign(1-parameter) > 0
                key = face_key(qface)
                if key not in actual:
                    actual[key] = len(actual)
                exponent = next(k for k in range(28) if rotation == z**k)
                records.append({'central_state': state, 'Q_hand': hand, 'Q_native_side': side,
                                'rotation_exponent': exponent, 'shift': encode(shift),
                                'physical_Q': actual[key], 'witness': witness,
                                'point': encode(p), 'host_start': encode(hstart),
                                'host_end': encode(hend), 'segment_parameter': encode(parameter)})
        assert len(actual) == 4
    assert len(records) == 64
    return {'schema': 'arisearch-p5q14-orientation-transition-2026-10-14-compact-v1',
            'software': {'sage': SAGE_VERSION, 'python': python_version()},
            'domain': {'central_states': 4, 'normalized_period': 'vvuvvuu',
                       'central_obligation_unit_slot': 5, 'required_P_face': 6,
                       'required_P_native_side': 3, 'Q_v_native_sides': qv,
                       'Q_hands': [1, -1], 'indexed_Q_attachments_per_state': 16,
                       'physical_Q_attachments_per_state': 4,
                       'total_indexed_cases': 64},
            'central_cycles': [list(c) for c in cycles],
            'normalization_of_all_28_indexed_states': normalization(Q, states),
            'summary': {'central_states': 4, 'indexed_Q_attachments': 64,
                        'forbidden_T_contacts': 64, 'compatible_Q_attachments': 0},
            'records': records}


def run():
    Q, cycles, states = load_states()
    word = 'vvuvvuu'*2
    obligations = [slot for slot, tag in enumerate(word) if tag == 'u']
    qv = [j for j, tag in enumerate(word) if tag == 'v']
    rows = []
    totals = Counter()
    for state, faces in enumerate(states):
        central = {'state': state, 'cycle': list(cycles[state]), 'obligations': []}
        for slot in obligations:
            F = faces[slot+1]
            a, b = F[3], F[4]
            phand = sign(D['area'](list(F)))
            assert not any({a, b} == {Q[j], Q[(j+1) % 14]} for j in range(14))
            records = []
            physical = {}
            for hand in (1, -1):
                base = Q if hand == 1 else tuple(map(conj, Q))
                for side in qv:
                    start, end = (b, a) if phand == hand else (a, b)
                    rotation = (end-start)/(base[(side+1) % 14]-base[side])
                    shift = start-rotation*base[side]
                    assert rotation*conj(rotation) == 1
                    qface = transform(Q, hand, rotation, shift)
                    assert disjoint(F, qface)
                    powers = [k for k in range(28) if z**k == rotation]
                    assert len(powers) == 1
                    qkey = face_key(qface)
                    if qkey not in physical:
                        physical[qkey] = len(physical)
                    for neighbor, newbase in enumerate(states):
                        newfaces = tuple(transform(G, hand, rotation, shift) for G in newbase)
                        matches = [j for j, G in enumerate(newfaces[1:], 1)
                                   if face_key(G) == face_key(F)]
                        rec = {'Q_hand': hand, 'Q_native_side': side,
                               'rotation_exponent': powers[0], 'shift': encode(shift),
                               'neighbor_state': neighbor, 'physical_Q': physical[qkey]}
                        if not matches:
                            rec['status'] = 'missing_required_guest'
                        else:
                            assert len(matches) == 1
                            rec['required_guest_index'] = matches[0]
                            rec['defect'] = combined_defect(faces, newfaces)
                            rec['status'] = rec['defect']['kind'] if rec['defect'] else 'compatible_completion'
                        totals[rec['status']] += 1
                        records.append(rec)
            assert len(records) == 64
            viable = [r for r in records if r['status'] == 'compatible_completion']
            central['obligations'].append({'unit_slot': slot, 'required_P_face': slot+1,
                                           'indexed_cases': records,
                                           'distinct_physical_Q_candidates': len(physical),
                                           'compatible_indexed_cases': len(viable)})
            print('central', state, 'u-slot', slot, 'completed64 cases',
                  Counter(r['status'] for r in records), flush=True)
        rows.append(central)
    summary = dict(totals)
    summary['central_states'] = len(states)
    summary['required_unit_guest_obligations'] = len(states)*len(obligations)
    summary['indexed_domain_cases'] = sum(totals.values())
    return {'schema': 'arisearch-p5q14-orientation-transition-2026-10-14-v1',
            'software': {'sage': SAGE_VERSION, 'python': python_version()},
            'domain': {'central_period': 'vvuvvuu', 'central_states': 4,
                       'central_unit_slots': obligations, 'Q_v_native_sides': qv,
                       'Q_hands': [1, -1], 'neighbor_states': 4,
                       'indexed_cases_per_obligation': 64,
                       'total_indexed_cases': 1536,
                       'arithmetic': 'CyclotomicField(28), exact AA signs'},
            'summary': summary, 'rows': rows}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    parser.add_argument('--check', type=Path)
    parser.add_argument('--compact-output', type=Path)
    parser.add_argument('--compact-check', type=Path)
    args = parser.parse_args()
    compact = args.compact_output or args.compact_check
    data = run_compact() if compact else run()
    check = args.compact_check if compact else args.check
    output = args.compact_output if compact else args.output
    if check:
        assert json.loads(check.read_text()) == data
    if output:
        with output.open('x') as out:
            json.dump(data, out, indent=2, sort_keys=True)
            out.write('\n')
    print(json.dumps(data['summary'], indent=2, sort_keys=True), flush=True)


if __name__ == '__main__':
    main()
