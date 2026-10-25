"""Move the existing angular endpoint-cycle rejection before support geometry.

This is an optimization comparison on the unchanged finite mixed-obtuse
support domain. The reduced catalogue is explicitly a filtered subset;
nominal coverage includes the two whole angle-word scopes rejected early.
Old sources, catalogues and certificates are read-only dependencies.
"""
from __future__ import annotations

import argparse
from functools import lru_cache
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import subprocess
import sys
import tempfile
from time import perf_counter,process_time

REPO=Path(__file__).resolve().parents[2]
BASELINE=REPO/"research/discovery/runs/mixed-obtuse-2026-10-24"
DEFAULT_OUTPUT=REPO/"research/discovery/runs/mixed-angular-first-2026-10-24"
EXPECTED_BASELINE={
    "source_sha256":"40126e82f44e19805ba7f129abf2235efb8394438e9cef449ce5eb6fcecba907",
    "catalogue_content_sha256":"9000d3cabc7c7b1e3483780b8416903f2d5ce9263afcd85b4139aed56b799932",
    "preflight_content_sha256":"12371eb9470c8eee718cefeca1d31b79adfa3d5658b786dc132d64fdc04afdbf",
    "scale_audit_sha256":"f6193e5a0a8dbf6277a1a887454a83f8b4644149d432cf37c6e7e20d32d3c6fa",
}


@lru_cache(None)
def base():
    if str(REPO) not in sys.path:
        sys.path.insert(0,str(REPO))
    from research.discovery import mixed_angles
    return mixed_angles


def stable_hash(value):
    def scrub(obj):
        if isinstance(obj,dict):
            return {k:scrub(v) for k,v in obj.items()
                    if k not in ("elapsed_seconds","cpu_seconds","wall_seconds","content_sha256","measurements")}
        if isinstance(obj,(tuple,list)):
            return [scrub(v) for v in obj]
        return obj
    return sha256(json.dumps(scrub(value),sort_keys=True,separators=(",",":")).encode()).hexdigest()


def angle_prefilter():
    m=base()
    proofs=[]
    accepted=[]; rejected=[]
    for angles in m.Q_ANGLES:
        p=m.angle_endpoint_cycle(m.P_ANGLES,m.P_ANGLES,angles)
        q=m.angle_endpoint_cycle(angles,m.P_ANGLES,angles)
        keep=p["feasible"] and q["feasible"]
        (accepted if keep else rejected).append(list(angles))
        proofs.append({"Q_angle_word":list(angles),"accepted":keep,"P":p,"Q":q})
    data={"schema":"mixed-angular-first-prefilter-v1",
          "same_nominal_domain_as_baseline":True,"support_domain":[1,2],
          "nominal_Q_angle_word_count":16,"accepted_Q_angle_words":accepted,
          "rejected_Q_angle_words":rejected,"nominal_support_assignments":2080,
          "enumerated_support_assignments":32+128*len(accepted),
          "early_rejected_support_assignments":128*len(rejected),
          "proofs":proofs,"necessary_only":True,"geometry_called_for_rejected_words":False}
    data["content_sha256"]=stable_hash(data)
    return data


def enumerate_filtered_catalogue(prefilter=None,geometry=None):
    """Enumerate P and only accepted Q words, with injectable geometry audit.

    Primitive construction and congruence signatures come from the immutable
    baseline module. No globals are patched. IDs and defining data therefore
    coincide exactly with the corresponding full-catalogue subset.
    """
    m=base()
    prefilter=angle_prefilter() if prefilter is None else prefilter
    accepted=tuple(tuple(w) for w in prefilter["accepted_Q_angle_words"])
    geometry=m.support_polygon if geometry is None else geometry
    grouped={}
    stats={"P_angle_words":1,"Q_angle_words":len(accepted),"attempted":0,
           "inactive_or_zero":0,"by_angle_word":[],"nominal_Q_angle_words":16,
           "nominal_attempted":2080,"early_rejected_supports":prefilter["early_rejected_support_assignments"]}
    started=perf_counter()
    for species,angle_list in (("P",(m.P_ANGLES,)),("Q",accepted)):
        for angles in angle_list:
            attempted=valid=0; signatures=set()
            for offsets in product((1,2),repeat=len(angles)):
                attempted+=1
                poly=geometry(angles,offsets)
                if poly is None:
                    continue
                valid+=1
                lengths=m.edge_lengths(poly,angles)
                assert all(m.sign(x)>0 for x in lengths)
                signature=m.polygon_signature(poly)
                signatures.add(signature)
                if signature not in grouped:
                    grouped[signature]=[species,angles,offsets,poly,lengths,[]]
                grouped[signature][-1].append((angles,offsets))
            stats["attempted"]+=attempted
            stats["inactive_or_zero"]+=attempted-valid
            stats["by_angle_word"].append({"species":species,"angles":list(angles),
                 "attempted":attempted,"valid_definitions":valid,"congruence_classes":len(signatures)})
    tiles=[]
    for signature,(species,angles,offsets,poly,lengths,defs) in grouped.items():
        digest=sha256(json.dumps(signature,separators=(",",":")).encode()).hexdigest()[:16]
        tiles.append(m.MixedTile(species.lower()+str(len(angles))+"-"+digest,species,angles,offsets,
                                 poly,lengths,signature,tuple(defs)))
    tiles=tuple(sorted(tiles,key=lambda tile:(tile.species,tile.angles,tile.id)))
    stats.update({"P_tiles":sum(t.species=="P" for t in tiles),
                  "Q_tiles":sum(t.species=="Q" for t in tiles),"elapsed_seconds":perf_counter()-started})
    return tiles,stats


def write_filtered_catalogue(destination,prefilter=None,geometry=None):
    prefilter=angle_prefilter() if prefilter is None else prefilter
    tiles,stats=enumerate_filtered_catalogue(prefilter,geometry)
    destination=Path(destination); destination.mkdir(parents=True,exist_ok=True)
    data={"schema":"mixed-obtuse-support-v1","catalogue_scope":"angular-first-filtered-subset",
          "not_a_full_domain_support_catalogue":True,
          "field_basis":["1","sqrt(2)","sqrt(3)","sqrt(6)"],"support_domain":[1,2],
          "early_filter":prefilter,"tiles":[t.to_dict() for t in tiles],"stats":stats}
    data["content_sha256"]=stable_hash(data)
    (destination/"catalogue.json").write_text(json.dumps(data,indent=2)+"\n")
    (destination/"angle-prefilter.json").write_text(json.dumps(prefilter,indent=2)+"\n")
    return tiles,stats


def _phase(action):
    cpu=process_time(); wall=perf_counter()
    result=action()
    return result,{"cpu_seconds":process_time()-cpu,"wall_seconds":perf_counter()-wall}


def run_worker(destination,filtered=True,cpu_cap=540):
    """One cold-process worker; optimized replay does not rerun the baseline.

    Call in a new Python process for timing comparison. The original engine's
    cooperative cap remains540, and an outer process CPU limit is300 seconds.
    """
    import resource
    resource.setrlimit(resource.RLIMIT_CPU,(300,301))
    destination=Path(destination)
    if (destination/"catalogue.json").exists():
        raise ValueError("worker output must be fresh; refusing cached catalogue")
    destination.mkdir(parents=True,exist_ok=True)
    total_cpu=process_time(); total_wall=perf_counter()
    m,imports=_phase(base)
    measurements={"import_exact_engine":imports}
    if filtered:
        prefilter,measurements["early_angular_filter"]=_phase(angle_prefilter)
        _,measurements["support_catalogue"]=_phase(lambda:write_filtered_catalogue(destination,prefilter))
    else:
        _,measurements["support_catalogue"]=_phase(lambda:m.write_catalogue(destination))
    preflight,measurements["metric_preflight"]=_phase(lambda:m.run_preflight(destination,cpu_cap))
    measurements["total"]={"cpu_seconds":process_time()-total_cpu,"wall_seconds":perf_counter()-total_wall}
    catalogue=json.loads((destination/"catalogue.json").read_text())
    result={"schema":"mixed-angular-first-worker-v1","filtered":filtered,
            "cooperative_cpu_cap_seconds":cpu_cap,"outer_process_cpu_limit_seconds":300,
            "source_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),
            "engine_source_sha256":sha256(Path(m.__file__).read_bytes()).hexdigest(),
            "catalogue_content_sha256":catalogue["content_sha256"],
            "preflight_content_sha256":preflight["content_sha256"],
            "scale_audit_sha256":preflight["scale_audit_sha256"],
            "catalogue_stats":catalogue["stats"],"funnel":preflight["funnel"],
            "allocation_gate":preflight["allocation_gate"],"complete":preflight["complete"],
            "measurements":measurements}
    if filtered:
        result["prefilter_content_sha256"]=prefilter["content_sha256"]
    result["content_sha256"]=stable_hash(result)
    (destination/"worker-result.json").write_text(json.dumps(result,indent=2)+"\n")
    return result


def _subprocess_worker(destination,filtered,cpu_cap):
    args=[sys.executable,str(Path(__file__).resolve()),"--worker","filtered" if filtered else "baseline",
          "--output",str(destination),"--cpu-cap",str(cpu_cap)]
    completed=subprocess.run(args,cwd=REPO,text=True,capture_output=True,timeout=360)
    if completed.returncode:
        raise RuntimeError(f"worker failed({completed.returncode}): {completed.stdout} {completed.stderr}")
    return json.loads((Path(destination)/"worker-result.json").read_text())


def audit_subset_equivalence(baseline,destination,accepted_q_ids):
    """Stream-exact old-row filtering, including every common-scale mapping."""
    import gzip
    accepted_q_ids=set(accepted_q_ids)
    expected_hash=sha256(); actual_hash=sha256()
    retained=omitted=0
    seen_representatives=set()
    with gzip.open(Path(baseline)/"scale-audit.jsonl.gz","rb") as old, gzip.open(Path(destination)/"scale-audit.jsonl.gz","rb") as new:
        for line in old:
            row=json.loads(line)
            if row["Q"] not in accepted_q_ids:
                omitted+=1
                continue
            candidate=new.readline()
            if line!=candidate:
                raise AssertionError("filtered scale audit differs from retained baseline rows")
            if row["status"]=="common-scaling-duplicate":
                if row["representative"] not in seen_representatives:
                    raise AssertionError("common-scale representative crossed an omitted angle-word scope")
            else:
                seen_representatives.add(row["id"])
            expected_hash.update(line); actual_hash.update(candidate)
            retained+=1
        if new.readline():
            raise AssertionError("filtered scale audit has unexpected extra rows")
    return {"exact_row_equality":True,"retained_rows":retained,"early_omitted_rows":omitted,
            "baseline_filtered_stream_sha256":expected_hash.hexdigest(),
            "optimized_stream_sha256":actual_hash.hexdigest(),
            "all_common_scale_references_retained":True}


def run_comparison(destination=DEFAULT_OUTPUT,baseline=BASELINE,cpu_cap=540):
    """Separate fresh processes, same fixed domain and existing engine cap."""
    baseline=Path(baseline); destination=Path(destination)
    if any((destination/name).exists() for name in ("catalogue.json","manifest.json","worker-result.json")):
        raise ValueError("comparison output must be fresh; refusing existing scientific results")
    old_catalogue=json.loads((baseline/"catalogue.json").read_text())
    old_preflight=json.loads((baseline/"preflight.json").read_text())
    bound={"source_sha256":old_preflight["source_sha256"],
           "catalogue_content_sha256":old_catalogue["content_sha256"],
           "preflight_content_sha256":old_preflight["content_sha256"],
           "scale_audit_sha256":sha256((baseline/"scale-audit.jsonl.gz").read_bytes()).hexdigest()}
    if bound!=EXPECTED_BASELINE:
        raise ValueError("retained baseline binding changed")
    source=REPO/"research/discovery/mixed_angles.py"
    if sha256(source.read_bytes()).hexdigest()!=bound["source_sha256"]:
        raise ValueError("baseline source changed")
    with tempfile.TemporaryDirectory(prefix="arisearch-angular-baseline-") as temporary:
        cold=_subprocess_worker(temporary,False,cpu_cap)
        fresh={"source_sha256":cold["engine_source_sha256"],
               "catalogue_content_sha256":cold["catalogue_content_sha256"],
               "preflight_content_sha256":cold["preflight_content_sha256"],
               "scale_audit_sha256":cold["scale_audit_sha256"]}
        if fresh!=bound:
            raise AssertionError("fresh full baseline failed retained scientific/hash replay")
    optimized=_subprocess_worker(destination,True,cpu_cap)
    prefilter=json.loads((destination/"angle-prefilter.json").read_text())
    accepted_words={tuple(w) for w in prefilter["accepted_Q_angle_words"]}
    accepted_ids={tile["id"] for tile in old_catalogue["tiles"]
                  if tile["species"]=="Q" and tuple(tile["angles"]) in accepted_words}
    omitted_tiles=[{"id":tile["id"],"angles":tile["angles"],"active_definition_count":len(tile["defining_data"])}
                   for tile in old_catalogue["tiles"] if tile["species"]=="Q" and tile["id"] not in accepted_ids]
    audit_equivalence=audit_subset_equivalence(baseline,destination,accepted_ids)
    avoided={"support_geometry_calls":cold["catalogue_stats"]["attempted"]-optimized["catalogue_stats"]["attempted"],
             "valid_support_signature_calls":(cold["catalogue_stats"]["attempted"]-cold["catalogue_stats"]["inactive_or_zero"])
                 -(optimized["catalogue_stats"]["attempted"]-optimized["catalogue_stats"]["inactive_or_zero"]),
             "P_Q_native_pairs":cold["funnel"]["native_tile_pairs"]-optimized["funnel"]["native_tile_pairs"]}
    for key in ("native_pair_scales","unique_pair_scales","geometry_checked_pair_scales","geometry_checked_stars",
                "incidence_infeasible","incidence_feasible"):
        avoided[key]=cold["funnel"][key]-optimized["funnel"][key]
    manifest={"schema":"mixed-angular-first-comparison-v1",
              "source_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),
              "baseline_directory":"research/discovery/runs/mixed-obtuse-2026-10-24",
              "bound_baseline":bound,"fresh_full_baseline_matches_retained":True,
              "same_nominal_domain":True,"support_domain":[1,2],"nominal_support_assignments":2080,
              "accepted_Q_angle_words":prefilter["accepted_Q_angle_words"],
              "rejected_Q_angle_words":prefilter["rejected_Q_angle_words"],
              "early_filter_content_sha256":prefilter["content_sha256"],
              "omitted_Q_tiles":omitted_tiles,"audit_subset_equivalence":audit_equivalence,
              "baseline_and_optimized_final_leads_equal":cold["funnel"]["strong_survivors"]==optimized["funnel"]["strong_survivors"]==0,
              "optimized":{k:v for k,v in optimized.items() if k!="measurements"},
              "cold_full_baseline":{k:v for k,v in cold.items() if k!="measurements"},
              "work_avoided":avoided,
              "measurements":{"baseline":cold["measurements"],"angular_first":optimized["measurements"],
                              "interpretation":"Separate fresh Python processes; timings are measurements, not a controlled benchmark."},
              "scope":"Same finite nominal domain covered by early angular certificates plus reduced metric census; no library expansion and no growth engine."}
    manifest["content_sha256"]=stable_hash(manifest)
    (destination/"manifest.json").write_text(json.dumps(manifest,indent=2)+"\n")
    return manifest


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,default=DEFAULT_OUTPUT)
    parser.add_argument("--baseline",type=Path,default=BASELINE)
    parser.add_argument("--cpu-cap",type=float,default=540)
    parser.add_argument("--worker",choices=("baseline","filtered"))
    parser.add_argument("--replay",action="store_true",help="replay filtered worker only into a fresh output directory")
    args=parser.parse_args()
    if args.worker or args.replay:
        result=run_worker(args.output,filtered=args.worker!="baseline",cpu_cap=args.cpu_cap)
        print(json.dumps({k:result[k] for k in ("filtered","complete","funnel","content_sha256")},indent=2))
    else:
        result=run_comparison(args.output,args.baseline,args.cpu_cap)
        print(json.dumps({"work_avoided":result["work_avoided"],"content_sha256":result["content_sha256"]},indent=2))
