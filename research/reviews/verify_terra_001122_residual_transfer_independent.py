#!/usr/bin/env python3
"""Supplemental hostile-review checks: exact residual coverage and metric fibres."""
from pathlib import Path
import json
root=Path(__file__).resolve().parents[2]
D=json.loads((root/"research/certificates/terra-001122-all-metric-native-rings.json").read_text())
F=json.loads((root/"research/certificates/terra-001122-residual-functional-actions.json").read_text())
residual=[r for r in D["records"] if r["full_ring_ids"]
          and not r["A_monohedral_matches"] and not r["B_monohedral_matches"]]
indices={r["B_word_index"] for r in residual}
assert indices=={5,9,10}
assert len(F["records"])==3 and {r["B_word_index"] for r in F["records"]}==indices
for row in F["records"]:
    wi=row["B_word_index"]
    assert row["B_word"]==D["B_words"][wi]["word"]
    ids=[i for i,r in enumerate(D["raw_rings"]) if r["B_word_index"]==wi]
    assert len(ids)==12
    raw=[D["raw_rings"][i] for i in ids]
    assert all(all(a==b for a,b in r["AA_equalities"]) for r in raw)
    assert all(o["species"]=="B" and o["colours"][0]==o["colours"][1]
               and any(o["arms"]==f["arms"] for f in o["offers"])
               for r in raw for o in r["outer"])
    selected=[r for r in residual if r["B_word_index"]==wi]
    assert len(selected)==123
    assert all(r["AA_ring_ids"]==ids and r["full_ring_ids"]==ids for r in selected)
print("PASS: all3 residual indexed words covered; all native offers hold before merging; every123 metric record retains all12 B aliases")
