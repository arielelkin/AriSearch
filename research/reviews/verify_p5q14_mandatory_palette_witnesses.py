"""Fresh verification of the adversary's same-patch T/star witnesses.

Reconstructs from the author's independently frozen raw placements, not the
adversary's reconstruction functions or stored full patches. No new domain.
"""
import json
from collections import Counter
from functools import cache
from itertools import combinations
from pathlib import Path
from sage.all import AA, QQ, QQbar, NumberField, PolynomialRing

R = PolynomialRing(QQ, "t")
t = R.gen()
K = NumberField(t**12-t**10+t**8-t**6+t**4-t**2+1, "z")
z = K.gen()
conj = K.hom([z**-1], K)
embed = K.hom([QQbar.zeta(28)], QQbar)
ii = z**7


def decode(coefficients):
    return sum((QQ(q)*z**i for i, q in enumerate(coefficients)), K(0))


@cache
def cross(a, b):
    return (conj(a)*b-a*conj(b))/(2*ii)


@cache
def sign(q):
    assert q == conj(q)
    a = AA(embed(q))
    return 1 if a > 0 else -1 if a < 0 else 0


@cache
def strict_in_segment(point, start, end):
    dot = ((point-start)*conj(point-end)+(point-end)*conj(point-start))/2
    return cross(end-start, point-start) == 0 and sign(dot) < 0


@cache
def alpha_mate(face):
    start, end = face[4], face[0]
    edge = end-start
    return tuple(start+edge/conj(edge)*conj(p-start) for p in face)


root = Path("research/certificates")
author = json.loads((root/"contact-pentagon-5pi7-q14-exact.json").read_text())
adversary = json.loads((root/"construction-adversary-2026-10-14-p5q14-palette.json").read_text())
P = tuple(map(decode, author["source"]["P_vertices"]))
rows = {row["period"]: row for row in author["rows"]}
expected = {(row["period"], tuple(record["cycle"])) for row in author["rows"]
            for record in row["forced_dimer_completed_patches"]}
actual, statuses = set(), Counter()
survivors_by_word = Counter()

for record in adversary["patches"]:
    period = "".join("v" if bit else "u" for bit in record["word"][:7])
    assert record["word"][:7] == record["word"][7:]
    row = rows[period]
    # The two producers enumerate native hands in opposite orders.
    cycle = tuple(1-choice for choice in record["cycle"])
    key = period, cycle
    assert key not in actual and key in expected
    actual.add(key)
    Q = tuple(map(decode, row["Q_vertices"]))
    faces = [Q]
    for slot, choice in enumerate(cycle):
        allowed = [placement for placement in row["raw_native_guests"][slot]
                   if placement["rejection"] is None]
        guest = allowed[choice]
        rotation, shift = decode(guest["rotation"]), decode(guest["shift"])
        native = P if guest["hand"] == 1 else tuple(map(conj, P))
        faces.append(tuple(rotation*p+shift for p in native))
    identity = {frozenset(face) for face in faces}
    for face in faces[1:].copy():
        mate = alpha_mate(face)
        if frozenset(mate) not in identity:
            identity.add(frozenset(mate))
            faces.append(mate)
    assert len(faces) == 21
    status = record["status"]
    statuses[status] += 1
    if status == "forbidden_partial_contact":
        witness = record["first_partial"]
        first, second = witness["face_pair"]
        subject, host = (faces[second], faces[first]) if witness["subject_from_second_face"] else (faces[first], faces[second])
        point = subject[witness["native_corner"]]
        start = host[witness["host_edge"]]
        end = host[(witness["host_edge"]+1) % len(host)]
        assert point == decode(witness["point"])
        assert start == decode(witness["host_start"]) and end == decode(witness["host_end"])
        assert strict_in_segment(point, start, end)
    else:
        assert status == "no_obstruction_in_this_patch"
        # Independently exhaust every actual face/edge/corner comparison in
        # each of the 28 positives rather than trusting absence of a witness.
        for first, second in combinations(faces, 2):
            for subject, host in ((first, second), (second, first)):
                assert not any(strict_in_segment(point, start, host[(e+1) % len(host)])
                               for point in subject for e, start in enumerate(host))
        groups = {}
        for f, face in enumerate(faces):
            for native, point in enumerate(face):
                counts = groups.setdefault(point, [0, 0, 0])
                counts[2 if f == 0 else 0 if native == 0 else 1] += 1
        assert all(any(all(n <= m for n, m in zip(counts, full))
                       for full in ((2, 1, 0), (0, 2, 1))) for counts in groups.values())
        survivors_by_word[period] += 1
assert actual == expected and len(actual) == 364
assert statuses == {"forbidden_partial_contact": 336, "no_obstruction_in_this_patch": 28}
assert len(survivors_by_word) == 7 and set(survivors_by_word.values()) == {4}
assert set(survivors_by_word) == {"vvuvvuu", "vvuuvvu", "vuvvuuv", "vuuvvuv",
                                  "uvvuvvu", "uvvuuvv", "uuvvuvv"}
assert adversary["summary"] == {"disjoint_patches": 364, "forbidden_partial_contact": 336,
                               "unextendable_native_star": 0, "no_obstruction_in_this_patch": 28}
print("PASS fresh raw-placement reconstruction: all336 pointed native-corner/host-interior witnesses; complete no-T/native-star check for28 remaining states,4 per7 split-v-run words")
