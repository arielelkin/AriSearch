"""Adversarial controls for exact angular-first scope and comparison binding."""
import copy
import json
from pathlib import Path
import tempfile
import unittest

from research.discovery.angular_first_verify import (
    comparison_hash,expected_subset,load_audited_baseline,verify,verify_angle_filter,
    verify_metric_rows,verify_reduced_catalogue,
)
from research.discovery.verify import VerificationError
from research.discovery.mixed_verify import stable_content_hash

ROOT = Path(__file__).parent/'runs'


class AngularFilterControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalogue,cls.preflight = load_audited_baseline(ROOT/'mixed-obtuse-2026-10-24')
        cls.accepted,cls.rejected = verify_angle_filter(cls.preflight['angle_endpoint_cycle_audit'])

    def reduced(self):
        data = copy.deepcopy(self.catalogue)
        data['tiles'] = expected_subset(data,self.accepted)
        rows = [r for r in data['stats']['by_angle_word'] if r['species'] == 'P' or tuple(r['angles']) in self.accepted]
        data['stats'].update(Q_angle_words=14,attempted=sum(r['attempted'] for r in rows),
                             inactive_or_zero=sum(r['attempted']-r['valid_definitions'] for r in rows),
                             by_angle_word=rows,Q_tiles=371)
        data['content_sha256'] = stable_content_hash(data)
        return data

    def test_all_nominal_words_are_partitioned_by_exact_proofs(self):
        self.assertEqual((len(self.accepted),len(self.rejected)),(14,2))
        self.assertEqual(32+128*len(self.accepted)+128*len(self.rejected),2080)
        bad = copy.deepcopy(self.preflight['angle_endpoint_cycle_audit'])
        record = next(r for r in bad if tuple(r['Q_angle_word']) in self.rejected)
        record['P']['feasible'] = True
        with self.assertRaises(VerificationError):
            verify_angle_filter(bad)

    def test_reduced_catalogue_preserves_every_exact_definition(self):
        data = self.reduced()
        result = verify_reduced_catalogue(data,self.catalogue,self.accepted)
        self.assertEqual((result['attempted'],result['P_tiles'],result['Q_tiles']),(1824,20,371))
        data['tiles'][0]['defining_data'].pop()
        with self.assertRaisesRegex(VerificationError,'exactly'):
            verify_reduced_catalogue(data,self.catalogue,self.accepted)

    def test_rejected_q_inclusion_and_allowed_q_omission_fail(self):
        data = self.reduced()
        rejected = next(t for t in self.catalogue['tiles'] if tuple(t['angles']) in self.rejected)
        data['tiles'].append(rejected)
        with self.assertRaisesRegex(VerificationError,'exactly'):
            verify_reduced_catalogue(data,self.catalogue,self.accepted)
        data = self.reduced()
        data['tiles'].pop()
        with self.assertRaisesRegex(VerificationError,'exactly'):
            verify_reduced_catalogue(data,self.catalogue,self.accepted)

    def test_exact_metric_stream_filter_and_row_tampering(self):
        unique = {'id':'first','Q':'accepted','status':'missing-native-corner-support','missing_corners':[0]}
        rejected = {'id':'excluded','Q':'rejected','status':'missing-native-corner-support'}
        duplicate = {'Q':'accepted','status':'common-scaling-duplicate','representative':'first'}
        old = [unique,rejected,duplicate]
        new = [copy.deepcopy(unique),copy.deepcopy(duplicate)]
        counts = verify_metric_rows(iter(new),iter(old),{'accepted'})
        self.assertEqual((counts['native_pair_scales'],counts['unique_pair_scales'],counts['common_scale_duplicates']),(2,1,1))
        new[0]['missing_corners'] = [1]
        with self.assertRaisesRegex(VerificationError,'row differs'):
            verify_metric_rows(iter(new),iter(old),{'accepted'})
        with self.assertRaisesRegex(VerificationError,'missing or extra'):
            verify_metric_rows(iter([unique]),iter(old),{'accepted'})


class RetainedComparisonControls(unittest.TestCase):
    def test_retained_comparison_and_rehashed_funnel_mutation(self):
        directory = ROOT/'mixed-angular-first-2026-10-24'
        result = verify(directory)
        self.assertEqual(result['final_leads'],0)
        self.assertEqual(result['work_avoided']['geometry_checked_stars'],357)
        self.assertEqual(result['filtered_metric_funnel']['native_pair_scales'],150102)
        with tempfile.TemporaryDirectory(prefix='arisearch-angular-test-') as temporary:
            target = Path(temporary)
            for source in directory.iterdir():
                if source.name != 'manifest.json':
                    (target/source.name).symlink_to(source.resolve())
            data = json.loads((directory/'manifest.json').read_text())
            data['work_avoided']['geometry_checked_stars'] += 1
            data['content_sha256'] = comparison_hash(data)
            (target/'manifest.json').write_text(json.dumps(data))
            with self.assertRaisesRegex(VerificationError,'work-avoidance'):
                verify(target)
            data['content_sha256'] = '0'*64
            (target/'manifest.json').write_text(json.dumps(data))
            with self.assertRaisesRegex(VerificationError,'manifest hash'):
                verify(target)


if __name__ == '__main__':
    unittest.main()
