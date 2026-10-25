"""Independent exact-field, contact, incidence, cycle and calibration controls."""
import copy
from fractions import Fraction
import json
from pathlib import Path
import random
import unittest

from research.discovery.mixed_verify import (
    F,ZERO,ONE,SQRT2,SQRT3,SQRT6,VerificationError,angular_ring_possible,
    decode,direction,edge_lengths,encode_points,independent_angle_words,
    interiors_overlap,normal_indices,point,polygon_signature,support_polygon,
    verify_angle_cycle,verify_catalogue,verify_incidence,verify_star,
)

BASE = Path(__file__).parent/'runs/mixed-obtuse-2026-10-24'


class IndependentFieldControls(unittest.TestCase):
    def test_basis_products_inverse_and_real_order(self):
        self.assertEqual(SQRT2*SQRT2,F(2))
        self.assertEqual(SQRT3*SQRT3,F(3))
        self.assertEqual(SQRT2*SQRT3,SQRT6)
        self.assertEqual((ONE+SQRT2+SQRT3+SQRT6)*(ONE+SQRT2+SQRT3+SQRT6).inverse(),ONE)
        self.assertEqual(((ONE-SQRT2)**40).sign(),1)
        self.assertEqual(((ONE-SQRT2)**41).sign(),-1)
        self.assertEqual(ZERO.sign(),0)
        self.assertEqual((SQRT3-SQRT2).sign(),1)
        with self.assertRaises(VerificationError):
            ZERO.inverse()

    def test_independent_coefficients_match_sage_field(self):
        from research.discovery import mixed_angles as producer
        rng = random.Random(2315)
        for _ in range(30):
            a,b = (F(tuple(Fraction(rng.randrange(-5,6),rng.randrange(1,6)) for _ in range(4))) for _ in range(2))
            sa,sb = producer.decode(a.wire()),producer.decode(b.wire())
            self.assertEqual(producer.encode(sa+sb),(a+b).wire())
            self.assertEqual(producer.encode(sa*sb),(a*b).wire())
            if b:
                self.assertEqual(producer.encode(sa/sb),(a/b).wire())
            self.assertEqual(producer.sign(sa),a.sign())
            self.assertEqual(decode(a.wire()),a)

    def test_all_native_directions_and_normal_index(self):
        from research.discovery import mixed_angles as producer
        for i in range(24):
            x,y = direction(i)
            self.assertEqual(x*x+y*y,ONE)
            self.assertEqual([x.wire(),y.wire()],[producer.encode(v) for v in producer.NORMALS[i]])
        self.assertEqual(direction(6),(ZERO,ONE))
        self.assertEqual(direction(12),(-ONE,ZERO))
        self.assertEqual(normal_indices((105,105,105,105,120)),(0,5,10,15,19))
        self.assertEqual(len(independent_angle_words()),16)

    def test_support_geometry_and_congruence_preserve_size(self):
        from research.discovery import mixed_angles as producer
        angles = (105,105,105,105,120)
        for mask in range(32):
            offsets = tuple(1+((mask>>i)&1) for i in range(5))
            poly = support_polygon(angles,offsets)
            self.assertEqual(encode_points(poly),producer.encode_points(producer.support_polygon(angles,offsets)))
            self.assertEqual([v.wire() for v in edge_lengths(poly,angles)],[producer.encode(v) for v in producer.edge_lengths(producer.support_polygon(angles,offsets),angles)])
        small,big = support_polygon(angles,(1,)*5),support_polygon(angles,(2,)*5)
        self.assertNotEqual(polygon_signature(small),polygon_signature(big))
        self.assertEqual(polygon_signature(small),polygon_signature(big,Fraction(1,2)))


class ExactRetainedContactControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalogue = json.loads((BASE/'catalogue.json').read_text())
        cls.preflight = json.loads((BASE/'preflight.json').read_text())
        cls.tiles = {t['id']:t for t in cls.catalogue['tiles']}

    def test_positive_star_transform_and_full_sides(self):
        row = self.preflight['corner_supported_pairs'][0]
        p,q = self.tiles[row['P']],self.tiles[row['Q']]
        scale = decode(row['Q_scale'])
        for star in row['stars'][:3]:
            verify_star(star,p,q,scale)
        bad = copy.deepcopy(row['stars'][0])
        bad['corners'][0]['rotation_index_15deg'] = (bad['corners'][0]['rotation_index_15deg']+1)%24
        with self.assertRaisesRegex(VerificationError,'isometries'):
            verify_star(bad,p,q,scale)
        bad = copy.deepcopy(row['stars'][0])
        bad['polygons'][0][1][0][0][0] += 1
        with self.assertRaises(VerificationError):
            verify_star(bad,p,q,scale)

    def test_all_exact_primal_and_farkas_certificates(self):
        counts = [0,0]
        for row in self.preflight['corner_supported_pairs']:
            stars = {tuple(star['native_corner_multiset']) for star in row['stars']}
            feasible = verify_incidence(row['incidence_relaxation'],stars)
            counts[feasible] += 1
            bad = copy.deepcopy(row['incidence_relaxation'])
            if feasible:
                bad['weights'][0]['weight'] = [0,1]
            else:
                bad['farkas']['native_corner_weights'] = [[0,1]]*12
            with self.assertRaises(VerificationError):
                verify_incidence(bad,stars)
        self.assertEqual(counts,[7,7])

    def test_all_angular_dp_proof_traces_both_reflections(self):
        p = (105,105,105,105,120)
        impossible = []
        for row in self.preflight['angle_endpoint_cycle_audit']:
            q = tuple(row['Q_angle_word'])
            possible = verify_angle_cycle(row['P'],p,q)
            self.assertEqual(possible,angular_ring_possible(p,p,q))
            verify_angle_cycle(row['Q'],p,q)
            if not possible:
                impossible.append(q)
        self.assertEqual(len(impossible),2)
        self.assertIn((120,120,120,120,150,120,150),impossible)
        self.assertTrue(all(tuple(r['Q_angle_word']) in impossible for r in self.preflight['incidence_survivors']))
        self.assertEqual(self.preflight['strong_survivors'],[])
        self.assertFalse(self.preflight['allocation_gate']['passed'])

    def test_close_contacts_and_tiny_exact_overlap(self):
        square = tuple((F(x),F(y)) for x,y in ((0,0),(1,0),(1,1),(0,1)))
        touching = tuple((x+1,y) for x,y in square)
        self.assertFalse(interiors_overlap(square,touching))
        epsilon = (ONE-SQRT2)**40
        overlap = tuple((x+1-epsilon,y) for x,y in square)
        self.assertTrue(interiors_overlap(square,overlap))


class CatalogueEnvelopeControls(unittest.TestCase):
    def catalogue(self):
        return json.loads((BASE/'catalogue.json').read_text())

    def test_pentagon_cannot_be_relabelled_as_q(self):
        data = self.catalogue()
        tile = data['tiles'][0]
        self.assertEqual(tile['species'],'P')
        tile['species'] = 'Q'
        tile['id'] = 'q'+tile['id'][1:]
        with self.assertRaisesRegex(VerificationError,'species'):
            verify_catalogue(data)

    def test_aggregate_catalogue_counts_are_checked(self):
        data = self.catalogue()
        data['stats']['P_tiles'] += 1
        with self.assertRaisesRegex(VerificationError,'counters'):
            verify_catalogue(data)

    def test_duplicate_support_definitions_are_rejected(self):
        data = self.catalogue()
        definitions = data['tiles'][0]['defining_data']
        definitions.append(copy.deepcopy(definitions[0]))
        with self.assertRaisesRegex(VerificationError,'support definitions'):
            verify_catalogue(data)


class CalibrationEnvelopeControls(unittest.TestCase):
    def test_m8_full_integer_word_census(self):
        from research.discovery.calibration_verify import independent_library
        words = independent_library(8)
        self.assertEqual(len(words),330)
        self.assertEqual(sum(w[:3] == w[3:] for w in words),120)
        self.assertIn((8,8,8,8,8,8),words)
        with self.assertRaises(VerificationError):
            independent_library(9)


if __name__ == '__main__':
    unittest.main()
