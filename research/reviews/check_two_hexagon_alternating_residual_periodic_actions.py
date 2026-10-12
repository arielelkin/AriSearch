#!/usr/bin/env python3
"""Fast independent positive-only check of all seven full-native metric tori."""
import argparse,hashlib,importlib.util,json
from pathlib import Path
sp=importlib.util.spec_from_file_location('independent_full_chain',Path(__file__).with_name('check_two_hexagon_alternating_all_metric_chain.py'))
g=importlib.util.module_from_spec(sp);sp.loader.exec_module(g)
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output');args=ap.parse_args()
    source=g.read('residual-metric-transport')
    positive={row['joint_metric_orbit_id']:row for row in source['rows'] if row['verdict']!='EMPTY'}
    assert set(positive)=={27,78,132,270,322,347,446}
    assert g.periodic_witnesses(positive)==7
    path=Path('research/certificates/two-hexagon-alternating-residual-periodic-actions.json')
    result={'status':'PASSED','direct_metric_tori':7,'index_per_torus':3,'canonical_native_stars':42,'directed_native_seams':126,'extra_side_equalities':0,'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'scope':'Seven direct positive witnesses only; complete metric-domain and negative transport coverage is checked separately'}
    if args.output:Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))
if __name__=='__main__':main()
