"""Audit the angular-first reordering of the unchanged finite mixed domain.

The old run is bound by its previously independently audited fingerprints.
All angle proofs are rechecked independently. Exact catalogue subset and
ordered metric-audit filtering preserve the full nominal domain certificate;
no repeated150k Fraction scan or claim about another tile family is needed.
"""
from __future__ import annotations
import argparse
from collections import Counter
import gzip
import hashlib
from itertools import zip_longest
import json
from pathlib import Path
import tempfile

from .mixed_verify import independent_angle_words, stable_content_hash, verify_angle_cycle
from .verify import digest, require

OLD_SOURCE = '40126e82f44e19805ba7f129abf2235efb8394438e9cef449ce5eb6fcecba907'
OLD_CATALOGUE = '9000d3cabc7c7b1e3483780b8416903f2d5ce9263afcd85b4139aed56b799932'
OLD_PREFLIGHT = '12371eb9470c8eee718cefeca1d31b79adfa3d5658b786dc132d64fdc04afdbf'
OLD_AUDIT = 'f6193e5a0a8dbf6277a1a887454a83f8b4644149d432cf37c6e7e20d32d3c6fa'
P_ANGLES = (105,105,105,105,120)


def load_audited_baseline(directory):
    directory = Path(directory)
    catalogue = json.loads((directory/'catalogue.json').read_text())
    preflight = json.loads((directory/'preflight.json').read_text())
    require(stable_content_hash(catalogue) == catalogue['content_sha256'] == OLD_CATALOGUE,'previous catalogue fingerprint changed')
    require(stable_content_hash(preflight) == preflight['content_sha256'] == OLD_PREFLIGHT,'previous preflight fingerprint changed')
    require(hashlib.sha256((directory/'scale-audit.jsonl.gz').read_bytes()).hexdigest() == OLD_AUDIT,'previous audit fingerprint changed')
    require(hashlib.sha256((Path(__file__).parent/'mixed_angles.py').read_bytes()).hexdigest() == OLD_SOURCE,'preserved mixed source changed')
    return catalogue,preflight


def verify_angle_filter(proofs):
    require([tuple(r['Q_angle_word']) for r in proofs] == independent_angle_words(),'early angle filter omits a nominal Q word')
    accepted,rejected = [],[]
    for record in proofs:
        q = tuple(record['Q_angle_word'])
        require(tuple(record['P']['root_angles']) == P_ANGLES and tuple(record['Q']['root_angles']) == q,'early angle proof root mismatch')
        p_ok = verify_angle_cycle(record['P'],P_ANGLES,q)
        q_ok = verify_angle_cycle(record['Q'],P_ANGLES,q)
        (accepted if p_ok and q_ok else rejected).append(q)
    return accepted,rejected


def expected_subset(old_catalogue,accepted):
    accepted = set(accepted)
    return [t for t in old_catalogue['tiles'] if t['species'] == 'P' or tuple(t['angles']) in accepted]


def verify_reduced_catalogue(new_catalogue,old_catalogue,accepted):
    expected = expected_subset(old_catalogue,accepted)
    require(digest(new_catalogue['tiles']) == digest(expected),'reduced catalogue is not exactly the accepted-angle old subset')
    require(new_catalogue['schema'] == old_catalogue['schema'] and new_catalogue['field_basis'] == old_catalogue['field_basis']
            and new_catalogue['support_domain'] == [1,2],'filtered catalogue changed the finite geometric family')
    by_word = [r for r in old_catalogue['stats']['by_angle_word'] if r['species'] == 'P' or tuple(r['angles']) in set(accepted)]
    expected_stats = {'P_angle_words':1,'Q_angle_words':len(accepted),'attempted':sum(r['attempted'] for r in by_word),
                      'inactive_or_zero':sum(r['attempted']-r['valid_definitions'] for r in by_word),
                      'by_angle_word':by_word,'P_tiles':sum(t['species'] == 'P' for t in expected),
                      'Q_tiles':sum(t['species'] == 'Q' for t in expected)}
    require(all(new_catalogue['stats'][key] == value for key,value in expected_stats.items()),'reduced support-domain phase counters mismatch')
    require(new_catalogue['content_sha256'] == stable_content_hash(new_catalogue),'filtered catalogue hash mismatch')
    return expected_stats


def verify_metric_rows(new_rows,old_rows,accepted_q_ids):
    """Exact ordered equality, including each common-scaling reference."""
    filtered = (row for row in old_rows if row['Q'] in accepted_q_ids)
    counts,representatives = Counter(),set()
    sentinel = object()
    for new,old in zip_longest(new_rows,filtered,fillvalue=sentinel):
        require(new is not sentinel and old is not sentinel,'filtered metric audit has missing or extra rows')
        require(new['Q'] in accepted_q_ids,'metric audit evaluated an angularly rejected Q')
        require(digest(new) == digest(old),'filtered metric row differs from audited baseline')
        counts['native_pair_scales'] += 1
        if new['status'] == 'common-scaling-duplicate':
            require(new['representative'] in representatives,'filtered common-scale reference crosses an excluded angle word')
            counts['common_scale_duplicates'] += 1
        else:
            representatives.add(new['id'])
            counts['unique_pair_scales'] += 1
            require(new['status'] == 'missing-native-corner-support','accepted-angle metric audit contains an unexpected surviving/geometry record')
            counts['missing_native_corner_support'] += 1
    return counts


def audit_rows(path):
    with gzip.open(path,'rt') as stream:
        for line in stream:
            yield json.loads(line)


def verify_binary_filter(new_path,old_path,accepted_q_ids):
    counts,representatives = Counter(),set()
    expected_hash,actual_hash = hashlib.sha256(),hashlib.sha256()
    omitted = 0
    with gzip.open(old_path,'rb') as old,gzip.open(new_path,'rb') as new:
        for line in old:
            row = json.loads(line)
            if row['Q'] not in accepted_q_ids:
                omitted += 1
                continue
            actual = new.readline()
            require(actual == line,'filtered metric byte stream differs from audited baseline')
            expected_hash.update(line)
            actual_hash.update(actual)
            counts['native_pair_scales'] += 1
            if row['status'] == 'common-scaling-duplicate':
                require(row['representative'] in representatives,'common-scale reference crosses excluded angle scope')
                counts['common_scale_duplicates'] += 1
            else:
                require(row['status'] == 'missing-native-corner-support','filtered metric phase unexpectedly invokes heavy geometry')
                representatives.add(row['id'])
                counts['unique_pair_scales'] += 1
                counts['missing_native_corner_support'] += 1
        require(not new.readline(),'filtered metric byte stream has extra rows')
    equivalence = {'exact_row_equality':True,'retained_rows':counts['native_pair_scales'],'early_omitted_rows':omitted,
                   'baseline_filtered_stream_sha256':expected_hash.hexdigest(),'optimized_stream_sha256':actual_hash.hexdigest(),
                   'all_common_scale_references_retained':True}
    return counts,equivalence


def comparison_hash(value):
    def scrub(item):
        if isinstance(item,dict):
            return {k:scrub(v) for k,v in item.items() if k not in ('elapsed_seconds','cpu_seconds','wall_seconds','content_sha256','measurements')}
        if isinstance(item,(tuple,list)):
            return [scrub(v) for v in item]
        return item
    return digest(scrub(value))


def verify(directory=None,*,replay=False):
    source = Path(__file__).parent
    directory = Path(directory) if directory is not None else source/'runs/mixed-angular-first-2026-10-24'
    baseline_directory = source/'runs/mixed-obtuse-2026-10-24'
    old_catalogue,old_preflight = load_audited_baseline(baseline_directory)
    manifest = json.loads((directory/'manifest.json').read_text())
    prefilter = json.loads((directory/'angle-prefilter.json').read_text())
    catalogue = json.loads((directory/'catalogue.json').read_text())
    preflight = json.loads((directory/'preflight.json').read_text())
    worker = json.loads((directory/'worker-result.json').read_text())
    require(manifest['schema'] == 'mixed-angular-first-comparison-v1','unknown angular comparison schema')
    require(prefilter['schema'] == 'mixed-angular-first-prefilter-v1','unknown angular prefilter schema')
    runner_hash = hashlib.sha256((source/'angular_first.py').read_bytes()).hexdigest()
    require(manifest['source_sha256'] == worker['source_sha256'] == runner_hash,'angular wrapper source hash mismatch')
    require(manifest['bound_baseline'] == {'source_sha256':OLD_SOURCE,'catalogue_content_sha256':OLD_CATALOGUE,
            'preflight_content_sha256':OLD_PREFLIGHT,'scale_audit_sha256':OLD_AUDIT},'comparison baseline binding mismatch')
    require(manifest['baseline_directory'] == 'research/discovery/runs/mixed-obtuse-2026-10-24'
            and manifest['fresh_full_baseline_matches_retained'] is True,'comparison lacks old baseline replay binding')
    require(comparison_hash(manifest) == manifest['content_sha256'],'comparison manifest hash mismatch')
    require(comparison_hash(prefilter) == prefilter['content_sha256'] == manifest['early_filter_content_sha256'],'angular prefilter hash mismatch')
    accepted,rejected = verify_angle_filter(prefilter['proofs'])
    require(prefilter['accepted_Q_angle_words'] == manifest['accepted_Q_angle_words'] == [list(w) for w in accepted]
            and prefilter['rejected_Q_angle_words'] == manifest['rejected_Q_angle_words'] == [list(w) for w in rejected], 'angle proof decisions differ from selected domain')
    require(all(record['accepted'] is (tuple(record['Q_angle_word']) in accepted) for record in prefilter['proofs']), 'early proof acceptance flag mismatch')
    require(prefilter['same_nominal_domain_as_baseline'] is True and prefilter['necessary_only'] is True
            and prefilter['geometry_called_for_rejected_words'] is False,'early filter scope/order overclaim')
    nominal,enumerated,skipped = 32+16*128,32+len(accepted)*128,len(rejected)*128
    require((prefilter['nominal_Q_angle_word_count'],prefilter['nominal_support_assignments'],
             prefilter['enumerated_support_assignments'],prefilter['early_rejected_support_assignments']) ==
             (16,nominal,enumerated,skipped),'nominal support domain is not partitioned completely')
    require(manifest['same_nominal_domain'] is True and manifest['support_domain'] == prefilter['support_domain'] == [1,2]
            and manifest['nominal_support_assignments'] == nominal,'comparison changed nominal support domain')
    require(catalogue['catalogue_scope'] == 'angular-first-filtered-subset' and catalogue['not_a_full_domain_support_catalogue'] is True
            and digest(catalogue['early_filter']) == digest(prefilter),'filtered catalogue lacks complete excluded-word certificates')
    stats = verify_reduced_catalogue(catalogue,old_catalogue,accepted)
    require((stats['attempted'],stats['P_tiles'],stats['Q_tiles']) == (1824,20,371),'unexpected filtered finite catalogue counts')
    require(catalogue['stats']['nominal_Q_angle_words'] == 16 and catalogue['stats']['nominal_attempted'] == nominal
            and catalogue['stats']['early_rejected_supports'] == skipped,'filtered catalogue nominal counters mismatch')
    require(preflight['schema'] == 'mixed-obtuse-preflight-v1' and preflight['complete'] is True,'filtered metric census incomplete')
    require(preflight['source_sha256'] == OLD_SOURCE and preflight['catalogue_content_sha256'] == catalogue['content_sha256']
            and digest(preflight['catalogue_stats']) == digest(catalogue['stats']),'filtered preflight catalogue/source mismatch')
    require(preflight['content_sha256'] == stable_content_hash(preflight),'filtered preflight content hash mismatch')
    require(hashlib.sha256((directory/'scale-audit.jsonl.gz').read_bytes()).hexdigest() == preflight['scale_audit_sha256'],'filtered metric gzip hash mismatch')
    require(digest(preflight['angle_endpoint_cycle_audit']) == digest(old_preflight['angle_endpoint_cycle_audit']), 'metric engine changed nominal angle audit')
    allowed_ids = {t['id'] for t in catalogue['tiles'] if t['species'] == 'Q'}
    counts,equivalence = verify_binary_filter(directory/'scale-audit.jsonl.gz',baseline_directory/'scale-audit.jsonl.gz',allowed_ids)
    require(manifest['audit_subset_equivalence'] == equivalence,'comparison exact audit subset metadata mismatch')
    omitted = [{'id':t['id'],'angles':t['angles'],'active_definition_count':len(t['defining_data'])} for t in old_catalogue['tiles']
               if t['species'] == 'Q' and t['id'] not in allowed_ids]
    require(digest(manifest['omitted_Q_tiles']) == digest(omitted),'comparison omitted-Q identity/definition metadata mismatch')
    expected_funnel = {key:0 for key in old_preflight['funnel']}
    expected_funnel.update(counts)
    expected_funnel['native_tile_pairs'] = stats['P_tiles']*stats['Q_tiles']
    require(preflight['funnel'] == expected_funnel,'filtered metric funnel disagrees with exact baseline stream selection')
    require(preflight['corner_supported_pairs'] == preflight['incidence_survivors'] == preflight['strong_survivors'] == [], 'filtered metric phase contains unexpected leads or heavy geometry calls')
    require(preflight['strong_survivors'] == old_preflight['strong_survivors'] and manifest['baseline_and_optimized_final_leads_equal'] is True, 'ordering optimization changed final leads')
    require(preflight['allocation_gate'] == old_preflight['allocation_gate'], 'ordering optimization changed allocation gate')
    require(worker['schema'] == 'mixed-angular-first-worker-v1' and worker['filtered'] is True and worker['complete'] is True
            and worker['engine_source_sha256'] == OLD_SOURCE,'filtered worker identity mismatch')
    require(worker['cooperative_cpu_cap_seconds'] == preflight['cpu_cap_seconds'] == 540
            and worker['outer_process_cpu_limit_seconds'] == 300,'worker changed authorized compute bounds')
    require(worker['content_sha256'] == comparison_hash(worker),'worker content hash mismatch')
    for key,value in (('catalogue_content_sha256',catalogue['content_sha256']),('preflight_content_sha256',preflight['content_sha256']),
                      ('scale_audit_sha256',preflight['scale_audit_sha256']),('prefilter_content_sha256',prefilter['content_sha256']),
                      ('catalogue_stats',catalogue['stats']),('funnel',preflight['funnel']),('allocation_gate',preflight['allocation_gate'])):
        require(digest(worker[key]) == digest(value),f'worker {key} binding mismatch')
    require(digest(manifest['optimized']) == digest({k:v for k,v in worker.items() if k != 'measurements'}),'manifest optimized summary mismatch')
    cold = manifest['cold_full_baseline']
    require(cold['content_sha256'] == comparison_hash(cold) and cold['filtered'] is False and cold['complete'] is True
            and cold['source_sha256'] == runner_hash and cold['engine_source_sha256'] == OLD_SOURCE,'fresh cold baseline worker binding mismatch')
    require(cold['cooperative_cpu_cap_seconds'] == worker['cooperative_cpu_cap_seconds'] and cold['outer_process_cpu_limit_seconds'] == worker['outer_process_cpu_limit_seconds'],'comparison uses different worker budgets')
    require((cold['catalogue_content_sha256'],cold['preflight_content_sha256'],cold['scale_audit_sha256']) ==
            (OLD_CATALOGUE,OLD_PREFLIGHT,OLD_AUDIT),'cold full baseline differs from prior audited evidence')
    require(comparison_hash(cold['catalogue_stats']) == comparison_hash(old_catalogue['stats'])
            and cold['funnel'] == old_preflight['funnel'] and cold['allocation_gate'] == old_preflight['allocation_gate'], 'cold full baseline counters differ')
    avoided = {'support_geometry_calls':nominal-enumerated,
               'valid_support_signature_calls':sum(r['valid_definitions'] for r in old_catalogue['stats']['by_angle_word'])-sum(r['valid_definitions'] for r in stats['by_angle_word']),
               'P_Q_native_pairs':old_preflight['funnel']['native_tile_pairs']-expected_funnel['native_tile_pairs']}
    for key in ('native_pair_scales','unique_pair_scales','geometry_checked_pair_scales','geometry_checked_stars','incidence_infeasible','incidence_feasible'):
        avoided[key] = old_preflight['funnel'][key]-expected_funnel[key]
    require(manifest['work_avoided'] == avoided,'comparison work-avoidance counters mismatch')
    measurements = manifest['measurements']
    require(measurements['angular_first'] == worker['measurements'],'manifest optimized timings differ from worker record')
    for name,expected_phases in (('baseline',{'import_exact_engine','support_catalogue','metric_preflight','total'}),
                                 ('angular_first',{'import_exact_engine','early_angular_filter','support_catalogue','metric_preflight','total'})):
        record = measurements[name]
        require(set(record) == expected_phases,'comparison omitted a cold-process timing phase')
        require(all(set(phase) == {'cpu_seconds','wall_seconds'} and all(type(v) in (int,float) and v >= 0 for v in phase.values())
                    for phase in record.values()),'invalid timing measurement')
    result = {'valid':True,'kind':'angular_first_comparison','nominal_support_assignments':nominal,
              'enumerated_support_assignments':enumerated,'early_rejected_support_assignments':skipped,
              'catalogue_tiles':stats['P_tiles']+stats['Q_tiles'],'filtered_metric_funnel':expected_funnel,
              'work_avoided':avoided,'final_leads':0,'content_sha256':manifest['content_sha256'],
              'measured_cpu_seconds':{name:measurements[name]['total']['cpu_seconds'] for name in ('baseline','angular_first')},
              'scope':'same finite nominal domain; early angle proof plus exact filtered old metric audit; timings are single-run measurements'}
    if replay:
        from .angular_first import _subprocess_worker
        with tempfile.TemporaryDirectory(prefix='arisearch-angular-verify-') as temporary:
            replayed = _subprocess_worker(temporary,True,worker['cooperative_cpu_cap_seconds'])
            require(replayed['content_sha256'] == worker['content_sha256'],'fresh angular-first worker differs from retained result')
            for key in ('catalogue_content_sha256','preflight_content_sha256','scale_audit_sha256','prefilter_content_sha256'):
                require(replayed[key] == worker[key],f'fresh angular-first {key} differs')
        result['fresh_replay'] = True
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory',nargs='?',type=Path,default=Path(__file__).parent/'runs/mixed-angular-first-2026-10-24')
    parser.add_argument('--replay',action='store_true')
    args = parser.parse_args()
    print(json.dumps(verify(args.directory,replay=args.replay),sort_keys=True))


if __name__ == '__main__':
    main()
