"""Independent metric, full M6 word census, and adversarial controls."""
import copy
import json
from pathlib import Path
from itertools import product
import unittest

from research.discovery.boundary_verify import (
    DIRECTIONS, STEPS, VerificationError, canonical_word, disk_faces,
    face_distance, polygons_touch, segments_meet, verify_patch,
    verify_periodic, verify_batch, word_polygon,
)
from research.discovery.verify import area2, digest, shift


def central_certificate(word=(1,1,1,1,1,1),radius=None):
    # Independently specified exact central hexagon fixtures and translations.
    fixtures = {
        (1,1,1,1,1,1):(((0,0),(2,0),(3,1),(2,2),(0,2),(-1,1)),(0,-2),(3,-1)),
        (1,2,3,1,2,3):(((0,0),(2,0),(4,2),(1,5),(-1,5),(-3,3)),(1,-5),(5,-3)),
    }
    poly,u,v = fixtures[word]
    cert = {'kind':'boundary_periodic' if radius is None else 'boundary_patch',
            'prototiles':[{'id':'A','word':word,'polygon':poly}], 'placements':[]}
    faces = {(0,0)} if radius is None else disk_faces(radius)
    for i,j in sorted(faces):
        origin = (i*u[0]+j*v[0],i*u[1]+j*v[1])
        cert['placements'].append({'tile':'A','word':word,'face':(i,j),'origin':origin,'polygon':shift(poly,origin)})
    if radius is None:
        cert.update(domain_hnf=[1,0,1],period_vectors=[u,v])
    else:
        cert.update(seed_face=[0,0],symbolic_radius=radius)
    return cert


class BoundaryMetricControls(unittest.TestCase):
    def test_central_periodic_geometry_and_anisotropic_scale(self):
        for word in ((1,1,1,1,1,1),(1,2,3,1,2,3)):
            result = verify_periodic(central_certificate(word))
            self.assertTrue(result['valid'])
            self.assertEqual(result['seam_checks'],6)

    def test_native_disk_layers(self):
        for radius in (0,1,2,4):
            result = verify_patch(central_certificate(radius=radius))
            self.assertEqual(result['placements'],1+3*radius*(radius+1))
            self.assertEqual(result['layer_counts'],[1]+[6*r for r in range(1,radius+1)])
            self.assertIn('no infinite extension',result['scope'])

    def test_bad_period_origin_domain_and_word(self):
        cert = central_certificate()
        cert['period_vectors'][0] = (0,-4)
        with self.assertRaisesRegex(VerificationError,'holonomy'):
            verify_periodic(cert)
        cert = central_certificate()
        cert['period_vectors'][1] = cert['period_vectors'][0]
        with self.assertRaisesRegex(VerificationError,'dependent'):
            verify_periodic(cert)
        cert = central_certificate(radius=1)
        item = cert['placements'][-1]
        item['origin'] = (item['origin'][0]+1,item['origin'][1])
        item['polygon'] = shift(item['polygon'],(1,0))
        with self.assertRaisesRegex(VerificationError,'origins'):
            verify_patch(cert)
        cert = central_certificate(radius=1)
        cert['placements'].pop()
        with self.assertRaisesRegex(VerificationError,'native disk'):
            verify_patch(cert)
        with self.assertRaisesRegex(VerificationError,'does not close'):
            word_polygon((1,1,1,1,1,2))

    def test_reflections_allowed_and_different_species_rejected(self):
        word = (1,3,3,2,2,4)
        reversed_word = word[::-1]
        self.assertNotIn(reversed_word,{word[k:]+word[:k] for k in range(6)})
        cert = {'kind':'boundary_patch','seed_face':[0,0],'symbolic_radius':0,
                'prototiles':[{'id':'A','word':word,'polygon':word_polygon(word)}],
                'placements':[{'tile':'A','word':reversed_word,'face':[0,0],'origin':[0,0],
                               'polygon':word_polygon(reversed_word)}]}
        self.assertTrue(verify_patch(cert)['valid'])
        other = (1,2,3,1,2,3)
        cert['placements'][0]['word'] = other
        cert['placements'][0]['polygon'] = word_polygon(other)
        with self.assertRaisesRegex(VerificationError,'not congruent'):
            verify_patch(cert)

    def test_close_corner_contacts_count_as_contacts(self):
        a = ((0,0),(2,0),(2,2),(0,2))
        # A corner touching a side is important even with disjoint interiors.
        b = ((2,1),(4,0),(4,2))
        self.assertTrue(polygons_touch(a,b))
        self.assertTrue(segments_meet((0,0),(2,0),(1,0),(1,3)))
        self.assertFalse(polygons_touch(a,shift(b,(1,0))))


class IndependentFullLibraryAudit(unittest.TestCase):
    def test_all_six_power_six_words_preserve_scale_and_match_catalogue(self):
        from research.discovery.boundary_words import enumerate_words, states
        expected = set()
        directed = set()
        # Independent six-loop closure test; does not use the four-free formula.
        for word in product(range(1,7),repeat=6):
            x = 2*word[0]+word[1]-word[2]-2*word[3]-word[4]+word[5]
            y = word[1]+word[2]-word[4]-word[5]
            if x == y == 0:
                directed.add(word)
                expected.add(min(seq[k:]+seq[:k] for seq in (word,word[::-1]) for k in range(6)))
        catalogue = enumerate_words(6)
        self.assertEqual(expected,{tile.word for tile in catalogue})
        self.assertEqual((len(expected),sum(w[:3] == w[3:] for w in expected)),(126,56))
        self.assertEqual(directed,{tuple(s['word']) for s in states(catalogue)})
        self.assertIn((1,1,1,1,1,1),expected)
        self.assertIn((6,6,6,6,6,6),expected)
        for tile in catalogue:
            poly = word_polygon(tile.word)
            self.assertEqual(tuple(tile.polygon),poly)
            # Every boundary side supports the whole hexagon strictly off that side.
            for k,(x,y) in enumerate(poly):
                q = poly[(k+1)%6]
                for j,p in enumerate(poly):
                    cross = (q[0]-x)*(p[1]-y)-(q[1]-y)*(p[0]-x)
                    self.assertGreaterEqual(cross,0)
                    if j not in (k,(k+1)%6):
                        self.assertGreater(cross,0)
            self.assertEqual(tile.centrally_symmetric,tile.word[:3] == tile.word[3:])


class IndependentCspControls(unittest.TestCase):
    def test_all_assignments_on_tiny_tori_match_bounded_solver(self):
        from research.discovery.boundary_screen import StateBank, graph_for_faces, solve_csp
        cases = [((1,1,1,1,1,1),), ((1,2,1,2,1,2),),
                 ((1,3,2,3,1,4),(2,5,3,4,3,5))]
        for words in cases:
            tiles = [{'id':str(i),'word':w,'polygon':word_polygon(w)} for i,w in enumerate(words)]
            bank = StateBank(tiles)
            for a,b,c in ((1,0,1),(2,0,1),(2,1,1),(1,0,2)):
                faces = [(i,j) for i in range(a) for j in range(c)]
                index = {f:i for i,f in enumerate(faces)}
                arcs = []
                for i,face in enumerate(faces):
                    for k,step in enumerate(STEPS):
                        x,y = face[0]+step[0],face[1]+step[1]
                        n,j = divmod(y,c)
                        neighbor = ((x-n*b)%a,j)
                        arcs.append((i,index[neighbor],k))
                expected = any(all(bank.states[assignment[i]]['word'][k] == bank.states[assignment[j]]['word'][(k+3)%6]
                                   for i,j,k in arcs)
                               for assignment in product(range(len(bank.states)),repeat=len(faces)))
                graph = graph_for_faces(faces,(a,b,c))
                self.assertEqual(set(graph[1]),set(arcs))
                actual = solve_csp(bank,graph,[t['id'] for t in tiles],node_budget=100000,propagation_budget=1000000)
                self.assertEqual(actual['status'],'SAT' if expected else 'UNSAT')

    def test_legacy_noncentral_pair_has_exact_mixed_four_face_tiling(self):
        a,b = (1,3,2,3,1,4),(2,5,3,4,3,5)
        specifications = [('A',(2,3,1,4,1,3),(0,0),(0,0)),
                          ('B',b,(0,1),(9,-5)),
                          ('B',(4,3,5,2,5,3),(1,0),(-2,-8)),
                          ('A',(4,1,3,2,3,1),(1,1),(7,-9))]
        cert = {'kind':'boundary_periodic','domain_hnf':[2,1,2],'period_vectors':[(0,-12),(18,-12)],
                'prototiles':[{'id':identifier,'word':w,'polygon':word_polygon(w)} for identifier,w in (('A',a),('B',b))],
                'placements':[{'tile':identifier,'word':w,'face':face,'origin':origin,'polygon':shift(word_polygon(w),origin)}
                              for identifier,w,face,origin in specifications]}
        result = verify_periodic(cert)
        self.assertEqual((result['placements'],result['area2']),(4,432))
        self.assertEqual({p['tile'] for p in cert['placements']},{'A','B'})
        cert['period_vectors'][0] = (0,-24)
        with self.assertRaisesRegex(VerificationError,'holonomy'):
            verify_periodic(cert)

    def test_corner_support_is_species_specific(self):
        a,b = (1,2,2,2,1,3),(3,2,2,2,3,1)
        pairs = lambda w: {tuple(sorted((w[i-1],w[i]))) for i in range(6)}
        self.assertNotIn((2,3),pairs(a))
        self.assertNotIn((1,2),pairs(b))
        self.assertTrue({(1,2),(2,3),(1,3)} <= pairs(a)|pairs(b))


class RetainedBoundaryEnvelopeControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = json.loads((Path(__file__).parent/'runs/boundary-m6-2026-10-24/boundary-screen.json').read_text())

    def resign(self,data):
        data['catalogue_sha256'] = digest(data['catalogue'])
        def visit(item):
            if isinstance(item,dict):
                if 'witness' in item:
                    item['witness_sha256'] = digest(item['witness'])
                for value in list(item.values()):
                    visit(value)
            elif isinstance(item,list):
                for value in item:
                    visit(value)
        visit(data)
        data['result_sha256'] = digest({k:v for k,v in data.items() if k not in ('result_sha256','execution')})
        return data

    def test_full_retained_batch(self):
        result = verify_batch(self.source)
        self.assertEqual((result['library'],result['central'],result['noncentral'],result['pairs']),(126,56,70,2415))
        self.assertEqual(result['verified_witnesses'],{'patch':103,'periodic':62})

    def test_rehashed_missing_pairs_or_growth_fail(self):
        data = copy.deepcopy(self.source)
        data['pairs'].pop()
        with self.assertRaisesRegex(VerificationError,'pair coverage'):
            verify_batch(self.resign(data))
        data = copy.deepcopy(self.source)
        row = next(r for r in data['pairs'] if r['status'] == 'SURVIVES_BOUNDED_SCREENS')
        row['growth'] = []
        with self.assertRaisesRegex(VerificationError,'growth radius'):
            verify_batch(self.resign(data))

    def test_rehashed_wrong_seed_species_fails(self):
        data = copy.deepcopy(self.source)
        for row in data['pairs']:
            retained = [r for r in row.get('growth',[]) if 'witness' in r]
            if retained:
                record = retained[0]
                wrong = next(t for t in row['tiles'] if t != record['seed_tile'])
                record['seed_tile'] = wrong
                record['witness']['seed_tile'] = wrong
                break
        with self.assertRaises(VerificationError):
            verify_batch(self.resign(data))

    def test_periodic_unknown_cannot_be_reported_surviving(self):
        data = copy.deepcopy(self.source)
        row = next(r for r in data['pairs'] if r['status'] == 'SURVIVES_BOUNDED_SCREENS')
        row['periodic']['attempts'][0]['status'] = 'UNKNOWN'
        row['periodic']['attempts'][0]['budget_reason'] = 'node_budget'
        row['periodic']['status'] = 'UNKNOWN'
        with self.assertRaisesRegex(VerificationError,'survivor status'):
            verify_batch(self.resign(data))

    def test_explicit_focused_selection_is_checked(self):
        data = copy.deepcopy(self.source)
        row = next(r for r in data['pairs'] if r['status'] == 'PERIODIC_WITNESS')
        data['pairs'] = [row]
        data['selection'] = {'pair_filter':row['tiles'],'expected_pair_count':1}
        data['funnel']['unordered_pairs'] = 1
        data['funnel']['pair_status_counts'] = {'PERIODIC_WITNESS':1}
        self.assertEqual(verify_batch(self.resign(data))['pairs'],1)


if __name__ == '__main__':
    unittest.main()
