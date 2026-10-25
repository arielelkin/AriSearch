"""Early-rejection ordering and exact subset regression tests."""
from collections import Counter
import json

from research.discovery.angular_first import (
    BASELINE, EXPECTED_BASELINE, angle_prefilter, base,
    enumerate_filtered_catalogue, stable_hash,
)


def test_all16_angle_words_accounted_before_geometry():
    proof=angle_prefilter()
    assert len(proof["proofs"])==16
    assert len(proof["accepted_Q_angle_words"])==14
    assert proof["rejected_Q_angle_words"]==[
        [120,120,120,120,150,120,150],
        [120,120,120,150,120,120,150],
    ]
    assert proof["nominal_support_assignments"]==2080
    assert proof["enumerated_support_assignments"]==1824
    assert proof["early_rejected_support_assignments"]==256
    assert all(not p["P"]["feasible"] for p in proof["proofs"] if not p["accepted"])
    assert proof["content_sha256"]==stable_hash(proof)


def test_rejected_angles_never_reach_support_geometry():
    proof=angle_prefilter()
    seen=Counter()
    rejected={tuple(w) for w in proof["rejected_Q_angle_words"]}
    def geometry(angles,offsets):
        assert angles not in rejected
        assert set(offsets)<={1,2}
        seen[angles]+=1
        return None
    tiles,stats=enumerate_filtered_catalogue(proof,geometry=geometry)
    assert tiles==()
    assert sum(seen.values())==1824
    assert seen[base().P_ANGLES]==32
    assert set(seen)=={base().P_ANGLES}|{tuple(w) for w in proof["accepted_Q_angle_words"]}
    assert all(count==128 for word,count in seen.items() if len(word)==7)
    assert stats["attempted"]+stats["early_rejected_supports"]==stats["nominal_attempted"]


def test_reduced_catalogue_is_exact_old_subset_with_identical_ids_and_definitions():
    proof=angle_prefilter()
    tiles,stats=enumerate_filtered_catalogue(proof)
    rejected={tuple(w) for w in proof["rejected_Q_angle_words"]}
    old=json.loads((BASELINE/"catalogue.json").read_text())
    expected=[t for t in old["tiles"] if t["species"]=="P" or tuple(t["angles"]) not in rejected]
    actual=json.loads(json.dumps([t.to_dict() for t in tiles]))
    assert actual==expected
    assert stats["P_tiles"]==20 and stats["Q_tiles"]==371
    assert stats["attempted"]==1824 and stats["inactive_or_zero"]==1322
    assert sum(len(t.defining_data) for t in tiles)==502
    assert len({t.id for t in tiles})==391


def test_baseline_bindings_and_timing_independent_manifest_hash():
    old_catalogue=json.loads((BASELINE/"catalogue.json").read_text())
    old_preflight=json.loads((BASELINE/"preflight.json").read_text())
    assert old_catalogue["content_sha256"]==EXPECTED_BASELINE["catalogue_content_sha256"]
    assert old_preflight["content_sha256"]==EXPECTED_BASELINE["preflight_content_sha256"]
    a={"counts":[1824,256],"measurements":{"total":{"cpu_seconds":4}},"stats":{"elapsed_seconds":3}}
    b={"counts":[1824,256],"measurements":{"total":{"cpu_seconds":400}},"stats":{"elapsed_seconds":300}}
    assert stable_hash(a)==stable_hash(b)
    b["counts"][0]+=1
    assert stable_hash(a)!=stable_hash(b)


def test_existing_comparison_output_fails_before_any_worker(tmp_path,monkeypatch):
    import pytest
    from research.discovery import angular_first
    (tmp_path/"manifest.json").write_text("{}")
    def forbidden(*args,**kwargs):
        raise AssertionError("worker must not run for existing output")
    monkeypatch.setattr(angular_first,"_subprocess_worker",forbidden)
    with pytest.raises(ValueError,match="fresh"):
        angular_first.run_comparison(tmp_path)
