#!/usr/bin/env python3
"""Complete rooted weighted length-corner walks, exact two metric cases.

Finite domain: all directed graph walks of total integer weight10. Positive
weights bound length by10. Equal native-corner labels are identified; this
is exhaustive for existence/signatures, not a count of physical placements.
"""
import json

LABELS = ("U36", "U108", "U144", "V72", "V144", "V108")
CORNERS = (("A", "A", 1), ("A", "b", 3), ("b", "c", 4),
           ("D", "b", 2), ("b", "E", 4), ("E", "E", 3))


def classify(equal):
    transitions = {}
    for label, (a, b, weight) in zip(LABELS, CORNERS):
        if equal:
            a = "b" if a == "c" else a
            b = "b" if b == "c" else b
        transitions.setdefault(a, []).append((b, weight, label))
        if a != b:
            transitions.setdefault(b, []).append((a, weight, label))
    walks = []
    def visit(start, current, remaining, labels):
        if not remaining:
            if current == start:
                walks.append({"start": start, "corners": labels})
            return
        for endpoint, weight, label in transitions.get(current, []):
            if weight <= remaining:
                visit(start, endpoint, remaining-weight, labels+[label])
    for start in sorted(transitions):
        visit(start, start, 10, [])
    signatures = sorted({tuple(w["corners"].count(label) for label in LABELS)
                         for w in walks})
    assert all(s[4] == s[5] == 0 for s in signatures)
    if not equal:
        assert all(s[2] == 0 for s in signatures)
    else:
        assert all(s[2] == 0 or s == (0, 2, 1, 0, 0, 0) for s in signatures)
    return {"condition": "b=c" if equal else "b!=c",
            "rooted_walk_count": len(walks), "rooted_walks": walks,
            "signatures": [list(s) for s in signatures]}


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run without Python optimization.")
    print(json.dumps({"scope": "complete native full-star length graph; not partial contacts",
                      "label_order": LABELS, "corners": CORNERS,
                      "total_weight": 10, "cases": [classify(False), classify(True)]},
                     indent=2, sort_keys=True))
