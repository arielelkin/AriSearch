#!/usr/bin/env python3
"""Independent exhaustive four-face X/Y gluing and radical-kernel audit."""
import ast
from itertools import permutations
from pathlib import Path
import json
import time
from sage.all import AA, QQ, NumberField, PolynomialRing, matrix, vector

ROOT = Path(__file__).resolve().parents[2]
ANGLE_CERT = ROOT / "research/certificates/new-angle-three-pentagon-mixed-word-angle-models.json"
CLOSURE_CERT = ROOT / "research/certificates/new-angle-three-pentagon-mixed-word-closure.json"
WORDS = ((90,150,90,105,105),)*2 + ((90,105,90,105,150),)*2
PREDECESSOR = tuple(5*(i//5)+(i-1) % 5 for i in range(20))


def canonical_partition(labels):
    seen = {}
    return tuple(seen.setdefault(z,len(seen)) for z in labels)


def seam_key(flags, pairs):
    return tuple(flags), tuple(sorted(tuple(sorted((5*f+i,5*g+j)))
                                     for (f,i),(g,j) in pairs))


def partition_from_pairs(native, twin):
    graph = [set() for _ in range(10)]
    for i,j in enumerate(twin):
        a,b = native[i],native[j]
        graph[a].add(b)
        graph[b].add(a)
    labels = [None]*10
    for start in range(10):
        if labels[start] is not None:
            continue
        labels[start] = start
        queue = [start]
        while queue:
            a = queue.pop()
            for b in graph[a]:
                if labels[b] is None:
                    labels[b] = start
                    queue.append(b)
    return canonical_partition(labels)


def enumerate_models():
    attempted = 0
    models = {}
    for mask in range(8):
        flags = (False,bool(mask & 1),bool(mask & 2),bool(mask & 4))
        angles = tuple(WORDS[f][(-i) % 5 if flags[f] else i]
                       for f in range(4) for i in range(5))
        native = tuple(5*(f//2)+((-i-1) % 5 if flags[f] else i)
                       for f in range(4) for i in range(5))
        rn = tuple(i for i in range(20) if angles[i] == 90)
        nr = tuple(i for i in range(20)
                   if angles[i] != 90 and angles[5*(i//5)+(i+1) % 5] == 90)
        nn = tuple(i for i in range(20) if i not in rn and i not in nr)
        assert (len(rn),len(nr),len(nn)) == (8,8,4)
        for partner in (1,2,3):
            other = [i for i in (1,2,3) if i != partner]
            base = [-1]*20
            for a,b in ((nn[0],nn[partner]),(nn[other[0]],nn[other[1]])):
                base[a],base[b] = b,a
            for target in permutations(nr):
                attempted += 1
                twin = base.copy()
                for a,b in zip(rn,target):
                    twin[a],twin[b] = b,a
                # Vertex links are cycles of twin after the incoming-side
                # permutation.  This is independent of author's union-find.
                todo = (1 << 20)-1
                cycles = []
                valid = True
                while todo:
                    start = (todo & -todo).bit_length()-1
                    cur = start
                    cycle = []
                    total = 0
                    while True:
                        cycle.append(cur)
                        total += angles[cur]
                        todo &= ~(1 << cur)
                        cur = twin[PREDECESSOR[cur]]
                        if cur == start:
                            break
                        if total >= 360:
                            valid = False
                            break
                    if not valid or total != 360:
                        valid = False
                        break
                    cycles.append(tuple(sorted(cycle)))
                if not valid:
                    continue
                assert len(cycles) == 6
                pairs = [(divmod(i,5),divmod(j,5)) for i,j in enumerate(twin) if i < j]
                key = seam_key(flags,pairs)
                assert key not in models
                # All surviving links are actual circles and face graph is
                # connected.  These are checked rather than assumed.
                seen = {0}
                changed = True
                while changed:
                    new = seen | {j//5 for i,j in enumerate(twin) if i//5 in seen}
                    changed = new != seen
                    seen = new
                assert len(seen) == 4
                models[key] = (tuple(sorted(cycles)),partition_from_pairs(native,twin))
        print("mask",mask,"attempts",attempted,"surviving models",len(models),flush=True)
    assert attempted == 967680 and len(models) == 8
    return models


def exact_closure_check(models):
    R = PolynomialRing(QQ,"t")
    t = R.gen()
    K = NumberField(t**4-10*t**2+1,"z",embedding=AA(2).sqrt()+AA(3).sqrt())
    z = K.gen()
    sqrt2, sqrt3 = (z**3-9*z)/2,(11*z-z**3)/2
    assert sqrt2**2 == 2 and sqrt3**2 == 3 and sqrt2 > 0 and sqrt3 > 0
    sqrt6 = sqrt2*sqrt3
    radicals = {2:sqrt2,3:sqrt3,6:sqrt6}
    def parse(text):
        def visit(n):
            if isinstance(n,ast.Constant) and type(n.value) is int:
                return K(n.value)
            if isinstance(n,ast.UnaryOp) and isinstance(n.op,ast.USub):
                return -visit(n.operand)
            if isinstance(n,ast.BinOp):
                a,b = visit(n.left),visit(n.right)
                if isinstance(n.op,ast.Add): return a+b
                if isinstance(n.op,ast.Sub): return a-b
                if isinstance(n.op,ast.Mult): return a*b
                if isinstance(n.op,ast.Div): return a/b
            if isinstance(n,ast.Call) and isinstance(n.func,ast.Name) and n.func.id == "sqrt":
                assert len(n.args) == 1 and not n.keywords
                assert isinstance(n.args[0],ast.Constant)
                return radicals[n.args[0].value]
            raise AssertionError("Unexpected expression in exact certificate: "+text)
        return visit(ast.parse(text,mode="eval").body)
    directions = [((1,0),(sqrt3/2,K(1)/2),(-K(1)/2,sqrt3/2),
                   (-(sqrt6+sqrt2)/4,-(sqrt6-sqrt2)/4),(0,-1)),
                  ((1,0),((sqrt6-sqrt2)/4,(sqrt6+sqrt2)/4),
                   (-(sqrt6+sqrt2)/4,(sqrt6-sqrt2)/4),(-K(1)/2,-sqrt3/2),(0,-1))]
    actual_partitions = {v[1] for v in models.values()}
    assert len(actual_partitions) == 3
    closure_certificate = json.loads(CLOSURE_CERT.read_text())
    records = closure_certificate["partitions"]
    assert closure_certificate["raw_partition_labelings"] == len(records) == 4
    assert closure_certificate["distinct_equality_relations"] == len(actual_partitions) == 3
    assert {tuple(r["partition"]) for r in records} == {
        tuple(r["native_side_partition"]) for r in json.loads(ANGLE_CERT.read_text())["models"]}
    covered = set()
    nullities = {}
    for record in records:
        labels = record["partition"]
        assert len(labels) == 10 and set(labels) == set(range(len(set(labels))))
        canonical = canonical_partition(labels)
        assert canonical in actual_partitions
        assert tuple(record["canonical_equality_relation"]) == canonical
        covered.add(canonical)
        n = len(set(labels))
        exact = matrix(K,4,n)
        for native_side in range(10):
            f,i = divmod(native_side,5)
            for d in (0,1):
                exact[2*f+d,labels[native_side]] += directions[f][i][d]
        retained = matrix(K,[[parse(x) for x in row] for row in record["matrix"]])
        assert retained == exact
        basis = [vector(K,[parse(x) for x in row]) for row in record["nullspace"]]
        kernel = exact.right_kernel()
        assert len(basis) == kernel.dimension()
        assert all(exact*v == 0 for v in basis)
        assert not basis or matrix(K,basis).rank() == len(basis)
        if kernel.dimension():
            assert kernel.dimension() == 1 and labels[3] == labels[8]
            assert all(v[labels[3]] == 0 for v in kernel.basis())
        else:
            assert n == 3 and exact.rank() == 3
        nullities[canonical] = kernel.dimension()
    assert covered == actual_partitions
    assert sorted(nullities.values()) == [0,1,1]
    return len(records),len(actual_partitions)


if __name__ == "__main__":
    started = time.monotonic()
    models = enumerate_models()
    retained = json.loads(ANGLE_CERT.read_text())
    assert retained["attempts"] == 967680 and retained["flat_models"] == 8
    raw_partitions = {tuple(r["native_side_partition"]) for r in retained["models"]}
    assert retained["raw_partition_labelings"] == len(raw_partitions) == 4
    assert retained["distinct_equality_relations"] == 3
    assert [tuple(p) for p in retained["canonical_equality_relations"]] == sorted({v[1] for v in models.values()})
    keys = []
    for record in retained["models"]:
        key = seam_key(record["reflected"],record["pairs"])
        keys.append(key)
        assert key in models
        classes = tuple(sorted(tuple(sorted(5*f+i for f,i in c)) for c in record["vertex_classes"]))
        assert classes == models[key][0]
        assert canonical_partition(record["native_side_partition"]) == models[key][1]
    assert len(keys) == 8 and len(set(keys)) == 8 and set(keys) == set(models)
    stored, distinct = exact_closure_check(models)
    print("PASS independent mixed-word audit: 967680 candidates, 8 exact angle-flat linked models;",
          stored,"stored closure records,",distinct,"distinct equality relations;",
          "exact complete nullspaces exclude all positive lengths.")
    print("runtime seconds:",round(time.monotonic()-started,3))
