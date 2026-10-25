"""Independent M8 envelope/manifest audit; prior M6 sources stay unchanged.

Positive geometry uses the preserved solver-free verifier. The optional
--replay runs fresh finite CSP searches in memory and compares the full stable
result hash. Actual M8 has no survivors; unused cache branches are not claimed.
"""
from __future__ import annotations
import argparse
from collections import Counter
from functools import reduce
import hashlib
from itertools import combinations, product
import json
from math import gcd
from pathlib import Path

from .boundary_verify import (DIRECTIONS, STEPS, _bound_witness, canonical_word,
                              word_polygon)
from .verify import area2, digest, points, require


def independent_library(max_length):
    require(max_length == 8, 'calibration must use M8 exactly')
    words = set()
    for w in product(range(1,9),repeat=6):
        if 2*w[0]+w[1]-w[2]-2*w[3]-w[4]+w[5] == 0 and w[1]+w[2]-w[4]-w[5] == 0:
            words.add(canonical_word(w))
    require(len(words) == 330 and sum(w[:3] == w[3:] for w in words) == 120,
            'independent M8 census disagrees with claimed 330/120')
    return words


def verify_m8_batch(data,*,check_sources=True):
    """Verify full library/pair coverage and all retained positive certificates.

    UNSAT/UNKNOWN and SAT summaries without retained coordinates remain solver
    reports. This checker neither calls nor trusts the CSP solver for positives.
    """
    require(data['schema'] == 'arisearch.discovery.boundary.v1', 'unknown boundary batch schema')
    require(digest({k:v for k,v in data.items() if k not in ('result_sha256','execution')}) == data['result_sha256'],
            'boundary result hash mismatch')
    require(digest(data['catalogue']) == data['catalogue_sha256'], 'boundary catalogue hash mismatch')
    provenance = data['provenance']
    if check_sources:
        expected_files = {'boundary_words.py','boundary_screen.py','boundary_render.py'}
        require(set(provenance['source_sha256']) == expected_files, 'incomplete boundary source hashes')
        for name,expected in provenance['source_sha256'].items():
            require(hashlib.sha256((Path(__file__).parent/name).read_bytes()).hexdigest() == expected,
                    f'boundary source hash mismatch: {name}')
    expected_words = independent_library(provenance['max_length'])
    catalogue,actual_words = {},set()
    for tile in data['catalogue']:
        word = tuple(tile['word'])
        require(canonical_word(word) == word, 'noncanonical library word')
        require(word not in actual_words and tile['id'] not in catalogue, 'duplicate library shape or ID')
        require(tile['id'] == 'bw120-'+'-'.join(map(str,word)), 'library ID disagrees with word')
        poly = word_polygon(word)
        require(points(tile['polygon']) == poly, 'library polygon disagrees with word')
        require(tile['centrally_symmetric'] is (word[:3] == word[3:]), 'incorrect central symmetry flag')
        require(tile['closure_parameter'] == word[0]-word[3], 'closure metadata mismatch')
        require(tile['side_count'] == 6 and tile['angles_degrees'] == [120]*6, 'angle metadata mismatch')
        require(tile['edge_squared_lengths'] == [4*x*x for x in word], 'edge metric metadata mismatch')
        require(tile['double_area_coefficient_sqrt3'] == area2(poly), 'area metadata mismatch')
        require(tile['corner_length_pairs'] == [[word[i-1],word[i]] for i in range(6)], 'corner metadata mismatch')
        require(tile['angle_cos_data'] == [{'dot':-2*word[i-1]*word[i], 'norm_product_squared':16*word[i-1]**2*word[i]**2} for i in range(6)], 'angle metric metadata mismatch')
        orbit = sorted({seq[k:]+seq[:k] for seq in (word,word[::-1]) for k in range(6)})
        require([tuple(w) for w in tile['orientation_words']] == orbit, 'reflection/rotation state catalogue mismatch')
        actual_words.add(word)
        catalogue[tile['id']] = tile
    require(actual_words == expected_words, 'full bounded library coverage mismatch')
    metadata = data['metadata']
    central_count = sum(t['centrally_symmetric'] for t in catalogue.values())
    require((metadata['tile_count'],metadata['central_count'],metadata['noncentral_count']) ==
            (len(catalogue),central_count,len(catalogue)-central_count), 'library count metadata mismatch')
    histogram = Counter(len(set(w)) for w in actual_words)
    require({int(k):v for k,v in metadata['distinct_length_count_histogram'].items()} == dict(histogram), 'length histogram mismatch')
    similarity = {canonical_word(tuple(x//reduce(gcd,w) for x in w)) for w in actual_words}
    require(metadata['integer_similarity_family_count'] == len(similarity) and metadata['common_physical_length_scale'] == 2,
            'similarity/scale metadata mismatch')
    conventions = data['conventions']
    require(tuple(map(tuple,conventions['face_steps'])) == STEPS
            and tuple(map(tuple,conventions['edge_vectors_per_native_length'])) == DIRECTIONS, 'native coordinate conventions mismatch')
    central = {identifier for identifier,t in catalogue.items() if t['centrally_symmetric']}
    noncentral = set(catalogue)-central
    omissions = data['central_omissions']
    require(len(omissions) == len(central) and {r['tile'] for r in omissions} == central
            and all(r['status'] == 'MONOHEDRAL_THEOREM' for r in omissions), 'central omission coverage mismatch')
    budgets = data['budgets']
    require(budgets['workers'] == 1 and budgets['periodic_requires_both_species'] is False, 'unsupported species/worker policy')
    require(type(budgets['max_index']) is int and budgets['max_index'] > 0, 'invalid HNF bound')
    require(all(type(budgets[k]) is int and budgets[k] > 0 for k in ('node_budget','propagation_budget')), 'invalid deterministic budget')
    radii = budgets['radii']
    require(radii and len(set(radii)) == len(radii) and all(type(r) is int and r > 0 for r in radii), 'invalid disk radii')
    domains = [(a,b,index//a) for index in range(1,budgets['max_index']+1)
               for a in range(1,index+1) if index%a == 0 for b in range(a)]
    checked = Counter()
    def finite_summary(record):
        require(record['status'] in ('SAT','UNSAT','UNKNOWN'), 'invalid finite solver status')
        for field,budget in (('nodes','node_budget'),('propagations','propagation_budget')):
            require(type(record[field]) is int and 0 <= record[field] <= budgets[budget], 'solver counter exceeds deterministic budget')
        if record['status'] == 'UNKNOWN':
            require(record.get('budget_reason') in ('node_budget','propagation_budget','outer_cpu_budget'), 'unexplained UNKNOWN')
    def periodic(summary,identifiers):
        attempts = summary['attempts']
        require(0 < len(attempts) <= len(domains), 'invalid periodic attempt count')
        require([tuple(a['domain_hnf']) for a in attempts] == domains[:len(attempts)], 'periodic attempts differ from HNF prefix')
        for attempt in attempts:
            finite_summary(attempt)
        if summary['status'] == 'PERIODIC_WITNESS':
            require(attempts[-1]['status'] == 'SAT' and all(a['status'] != 'SAT' for a in attempts[:-1]), 'periodic positive status mismatch')
            require(tuple(summary['witness']['domain_hnf']) == domains[len(attempts)-1], 'witness uses a different tested HNF')
            require(summary['witness']['kind'] == 'boundary_periodic', 'wrong periodic witness kind')
            _bound_witness(summary,identifiers,catalogue)
            checked['periodic'] += 1
        else:
            outer_stop = summary.get('budget_reason') == 'outer_cpu_budget'
            require((len(attempts) == len(domains) or outer_stop) and all(a['status'] != 'SAT' for a in attempts), 'negative periodic summary stopped early')
            if outer_stop:
                require(attempts[-1].get('budget_reason') == 'outer_cpu_budget', 'unexplained truncated period search')
            expected = 'UNKNOWN' if any(a['status'] == 'UNKNOWN' for a in attempts) else 'NO_PERIODIC_WITNESS_IN_TESTED_DOMAINS'
            require(summary['status'] == expected and 'witness' not in summary, 'periodic nonpositive summary mismatch')
    mono,seen_singletons = set(),set()
    for row in data['singletons']:
        identifier = row['tile']
        require(identifier in noncentral and identifier not in seen_singletons, 'duplicate/invalid singleton reference')
        seen_singletons.add(identifier)
        if row['status'] == 'NOT_RUN_OUTER_BUDGET':
            continue
        periodic(row,[identifier])
        if row['status'] == 'PERIODIC_WITNESS':
            mono.add(identifier)
    require(seen_singletons == noncentral, 'singleton coverage mismatch')
    selection = data.get('selection',{'pair_filter':None,'expected_pair_count':len(noncentral)*(len(noncentral)-1)//2})
    pair_filter = selection['pair_filter']
    if pair_filter is None:
        expected_pairs = {frozenset(pair) for pair in combinations(noncentral,2)}
    else:
        require(len(pair_filter) == len(set(pair_filter)) == 2 and set(pair_filter) <= noncentral, 'invalid focused pair selection')
        expected_pairs = {frozenset(pair_filter)}
    require(selection['expected_pair_count'] == len(expected_pairs), 'declared pair selection count mismatch')
    seen_pairs = set()
    statuses = Counter()
    for row in data['pairs']:
        identifiers = row['tiles']
        pair = frozenset(identifiers)
        require(len(identifiers) == len(pair) == 2 and pair in expected_pairs and pair not in seen_pairs, 'duplicate/invalid pair reference')
        seen_pairs.add(pair)
        status = row['status']
        statuses[status] += 1
        if status == 'OMITTED_MONOHEDRAL_MEMBER':
            require(set(row['positive_members']) == pair & mono and pair & mono, 'unsupported singleton omission')
            continue
        require(not pair & mono, 'positive singleton pair was unnecessarily screened')
        if status == 'NOT_RUN_OUTER_BUDGET':
            continue
        require(status in ('LOCAL_OBSTRUCTION','FINITE_EXTENSION_FAILURE','PERIODIC_WITNESS','UNKNOWN','SURVIVES_BOUNDED_SCREENS'), 'unknown pair status')
        local,growth = row['local'],row['growth']
        require(0 < len(local) <= 2 and [r['seed_tile'] for r in local] == identifiers[:len(local)], 'local seed coverage mismatch')
        for record in local+growth:
            if 'nodes' in record and 'propagations' in record:
                finite_summary(record)
            else:
                require(record in growth and any(all(record[k] == r[k] for k in ('seed_tile','symbolic_radius','status')) for r in local),
                        'counterless growth record has no corresponding local summary')
            require(record['seed_tile'] in pair and record['symbolic_radius'] in radii, 'disk summary has wrong seed/radius')
            if record in local:
                require(record['symbolic_radius'] == min(radii), 'local summary uses wrong radius')
            if 'witness' in record:
                require(record['status'] == 'SAT' and record['witness']['kind'] == 'boundary_patch', 'invalid disk positive status')
                witness = record['witness']
                require(witness['seed_tile'] == record['seed_tile'] and witness['symbolic_radius'] == record['symbolic_radius'], 'disk witness summary mismatch')
                _bound_witness(record,identifiers,catalogue)
                checked['patch'] += 1
        # Retain one strongest SAT disk for each attempted seed, even when
        # later growth is impossible; old SAT summaries may omit coordinates.
        if status != 'PERIODIC_WITNESS':
            last_sat = {r['seed_tile']:i for i,r in enumerate(growth) if r['status'] == 'SAT'}
            require(all(('witness' in r) == (r['status'] == 'SAT' and last_sat[r['seed_tile']] == i)
                        for i,r in enumerate(growth)), 'strongest SAT disk witness missing or duplicated')
        outer_stop = row.get('budget_reason') == 'outer_cpu_budget'
        if outer_stop:
            require(status == 'UNKNOWN', 'outer budget stop must remain UNKNOWN')
            if 'attempts' in row.get('periodic',{}):
                periodic(row['periodic'],identifiers)
            continue
        initial = [(r['seed_tile'],min(radii)) for r in local if r['status'] == 'SAT']
        schedule = initial+[(seed,radius) for radius in sorted(set(radii)-{min(radii)}) for seed in identifiers]
        actual = [(r['seed_tile'],r['symbolic_radius']) for r in growth]
        if status == 'LOCAL_OBSTRUCTION':
            require(actual == initial, 'local obstruction retained unexpected growth stages')
            require(any(r['status'] == 'UNSAT' for r in local) and row.get('periodic',{}).get('status','DEFERRED_LOCAL_OBSTRUCTION') == 'DEFERRED_LOCAL_OBSTRUCTION', 'local obstruction summary mismatch')
            continue
        require(len(local) == 2 and all(r['status'] != 'UNSAT' for r in local), 'periodic stage lacks local seed screens')
        periodic(row['periodic'],identifiers)
        if status == 'PERIODIC_WITNESS':
            require(row['periodic']['status'] == status and growth == [], 'pair periodic funnel mismatch')
        elif status == 'FINITE_EXTENSION_FAILURE':
            require(actual == schedule[:len(actual)] and len(actual) > len(initial) and all(r['status'] != 'UNSAT' for r in growth[:-1]), 'finite growth schedule mismatch')
            require(row['periodic']['status'] != 'PERIODIC_WITNESS' and growth[-1]['status'] == 'UNSAT', 'finite-extension summary mismatch')
        else:
            require(actual == schedule, 'survivor omitted an asserted growth radius or seed')
            require(row['periodic']['status'] != 'PERIODIC_WITNESS' and all(r['status'] != 'UNSAT' for r in local+growth), 'survivor funnel mismatch')
            expected = 'UNKNOWN' if row['periodic']['status'] == 'UNKNOWN' or any(r['status'] == 'UNKNOWN' for r in local+growth) else 'SURVIVES_BOUNDED_SCREENS'
            require(status == expected, 'survivor status mismatch')
    require(seen_pairs == expected_pairs, 'full unordered pair coverage mismatch')
    def budget_stopped(value):
        if isinstance(value,dict):
            return value.get('budget_reason') == 'outer_cpu_budget' or value.get('status') == 'NOT_RUN_OUTER_BUDGET' or any(budget_stopped(v) for v in value.values())
        if isinstance(value,(list,tuple)):
            return any(budget_stopped(v) for v in value)
        return False
    require(data['batch_complete'] is (not budget_stopped([data['singletons'],data['pairs']])), 'batch completion flag mismatch')
    expected_funnel = {'library':len(catalogue),'central_theorem_omissions':len(central),
                       'noncentral_singletons':len(noncentral),'positive_singleton_periodic':len(mono),
                       'unordered_pairs':len(expected_pairs),'pair_status_counts':dict(sorted((k,v) for k,v in statuses.items() if v))}
    require(data['funnel'] == expected_funnel, 'boundary funnel mismatch')
    return {'valid':True,'kind':'boundary_batch','library':len(catalogue),'central':len(central),
            'noncentral':len(noncentral),'pairs':len(expected_pairs),'verified_witnesses':dict(checked),
            'funnel':expected_funnel,'scope':'all retained positive geometry verified; negative solver labels require fresh replay; finite library only'}


def _effort(value):
    result = dict.fromkeys(('solves','nodes','propagations','initial_domains','initial_arcs','max_nodes','max_propagations'),0)
    def visit(item):
        if isinstance(item,dict):
            if 'nodes' in item and 'propagations' in item:
                result['solves'] += 1
                for key in ('nodes','propagations','initial_domains','initial_arcs'):
                    result[key] += item.get(key,0)
                result['max_nodes'] = max(result['max_nodes'],item['nodes'])
                result['max_propagations'] = max(result['max_propagations'],item['propagations'])
            for key,child in item.items():
                if key != 'effort_summary':
                    visit(child)
        elif isinstance(item,(list,tuple)):
            for child in item:
                visit(child)
    visit(value)
    return result


def verify_manifest(manifest_path,replay=False):
    manifest_path = Path(manifest_path)
    manifest = json.loads(manifest_path.read_text())
    require(manifest['schema'] == 'arisearch.discovery.length8-calibration.v1','unknown calibration manifest')
    require(digest({k:v for k,v in manifest.items() if k not in ('manifest_sha256','execution')}) == manifest['manifest_sha256'],
            'calibration manifest hash mismatch')
    source = Path(__file__).parent
    for name,expected in manifest['preserved_source_sha256'].items():
        require(hashlib.sha256((source/name).read_bytes()).hexdigest() == expected,'preserved M6 source changed')
    require(set(manifest['preserved_source_sha256']) == {'boundary_words.py','boundary_screen.py','boundary_render.py'},'incomplete preserved source set')
    orchestrator = hashlib.sha256((source/'length8_experiment.py').read_bytes()).hexdigest()
    require(orchestrator == manifest['orchestrator_source_sha256'],'calibration orchestrator source mismatch')
    baseline_budget = {'max_length':8,'max_index':8,'radii':[1,2,4],'node_budget':1000,'propagation_budget':50000,'cpu_seconds':600}
    followup_budget = {'max_index':16,'radii':[1,2,4,8],'node_budget':10000,'propagation_budget':500000,'cpu_seconds_shared_total':600}
    require(manifest['baseline_budget'] == baseline_budget and manifest['followup_budget'] == followup_budget,'calibration exceeds authorized bounds')
    summary = manifest['baseline']
    require(summary['path'] == 'boundary-screen.json','unexpected calibration baseline path')
    baseline = json.loads((manifest_path.parent/summary['path']).read_text())
    for field in ('result_sha256','batch_complete','selection','funnel','effort_summary'):
        require(summary[field] == baseline[field],f'manifest baseline {field} mismatch')
    require(baseline['experiment_provenance'] == {'orchestrator_source_sha256':orchestrator,'stage':'M8_BASELINE'},'baseline experiment provenance mismatch')
    require(baseline['provenance']['source_sha256'] == manifest['preserved_source_sha256'],'baseline used different preserved sources')
    for field in ('max_index','radii','node_budget','propagation_budget'):
        require(baseline['budgets'][field] == baseline_budget[field],'baseline search budget mismatch')
    require(baseline['budgets']['cpu_seconds_outer_cap'] == 600,'baseline outer cap mismatch')
    result = verify_m8_batch(baseline)
    require(_effort(baseline) == baseline['effort_summary'],'actual baseline effort counters mismatch')
    eligible = [r['tiles'] for r in baseline['pairs'] if r['status'] in ('SURVIVES_BOUNDED_SCREENS','UNKNOWN')]
    require(manifest['followup_eligible_pairs'] == eligible,'calibration final lead binding mismatch')
    require(not eligible and baseline['batch_complete'] and manifest['status'] == 'COMPLETE',
            'this audit only covers the completed no-followup calibration')
    require(manifest['followups'] == manifest['unfinished'] == [],'spurious followup or unfinished record')
    require(manifest['actual_followup_effort'] == _effort({}),'uncached followup work was charged')
    result.update(manifest_sha256=manifest['manifest_sha256'],result_sha256=baseline['result_sha256'],followup_eligible_pairs=0)
    if replay:
        from .boundary_screen import run_batch
        replayed = run_batch(max_length=8,max_index=8,radii=(1,2,4),node_budget=1000,
                             propagation_budget=50000,cpu_seconds=600,output_dir=None)
        replayed['experiment_provenance'] = {'orchestrator_source_sha256':orchestrator,'stage':'M8_BASELINE'}
        replayed['effort_summary'] = _effort(replayed)
        replay_hash = digest({k:v for k,v in replayed.items() if k not in ('result_sha256','execution')})
        require(replay_hash == baseline['result_sha256'],'fresh M8 computation differs from retained result')
        result['fresh_replay'] = True
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manifest',nargs='?',type=Path,default=Path(__file__).parent/'runs/boundary-m8-2026-10-24/manifest.json')
    parser.add_argument('--replay',action='store_true')
    args = parser.parse_args()
    print(json.dumps(verify_manifest(args.manifest,replay=args.replay),sort_keys=True))


if __name__ == '__main__':
    main()
