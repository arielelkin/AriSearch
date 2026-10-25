"""Adversarial controls for the independent certificate verifier."""
import copy
import json
from pathlib import Path
import unittest

from research.discovery.verify import (
    VerificationError, area2, cell_polygon, congruent, convex_polygon,
    hull, interiors_overlap, verify_cells_polygon, verify_patch, verify_periodic,
    verify_screen, digest,
)


def monokite_domain(a=1,b=0,c=1):
    base = (0,0,0,0)
    placements = []
    for i in range(a):
        for j in range(c):
            for o in range(2):
                for k in range(3):
                    cell = (i,j,o,k)
                    placements.append({'tile':'kite','cells':[cell], 'polygon':cell_polygon(cell)})
    return {'domain_hnf':[a,b,c], 'period_vectors':[[12*a,0],[12*b+6*c,6*c]],
            'prototiles':[{'id':'kite','cells':[base],'polygon':cell_polygon(base)}],
            'placements':placements}


class GeometryControls(unittest.TestCase):
    def test_mesh_area_and_nonoverlap(self):
        mesh = [cell_polygon((0,0,o,k)) for o in range(2) for k in range(3)]
        self.assertEqual(sum(map(area2,mesh)),144)
        for i,poly in enumerate(mesh):
            for q in mesh[:i]:
                self.assertFalse(interiors_overlap(poly,q))

    def test_union_rejects_missing_and_duplicated_cells(self):
        cells = [(0,0,0,k) for k in range(3)]
        triangle = ((0,0),(12,0),(6,6))
        self.assertEqual(area2(verify_cells_polygon(cells,triangle)),72)
        for bad in (cells[:-1],cells+[cells[0]]):
            with self.assertRaises(VerificationError):
                verify_cells_polygon(bad,triangle)

    def test_invalid_boundary_order(self):
        with self.assertRaises(VerificationError):
            convex_polygon(((0,0),(4,4),(0,4),(4,0)))
        with self.assertRaises(VerificationError):
            convex_polygon(((0,0),(4,0),(2,1),(4,4),(0,4)))

    def test_congruence_is_metric_and_allows_translation_reflection(self):
        poly = cell_polygon((0,0,0,0))
        moved = tuple((31-x,y-17) for x,y in poly)
        self.assertTrue(congruent(poly,moved))
        # Euclidean squared distance uses x*x + 3*y*y, not the stored-coordinate norm.
        self.assertFalse(congruent(((0,0),(4,0),(0,2)),((0,0),(2,0),(0,4))))

    def test_boundary_contact_is_not_overlap(self):
        a = ((0,0),(4,0),(4,4),(0,4))
        b = ((4,0),(8,0),(8,4),(4,4))
        self.assertFalse(interiors_overlap(a,b))
        self.assertTrue(interiors_overlap(a,((3,0),(7,0),(7,4),(3,4))))


class CertificateControls(unittest.TestCase):
    def test_monokite_periodic_controls(self):
        for domain in ((1,0,1),(2,1,2),(1,0,3)):
            self.assertTrue(verify_periodic(monokite_domain(*domain))['valid'])

    def test_wrapped_placements_may_be_arbitrarily_far_from_origin(self):
        cert = monokite_domain()
        # Rechoose a representative of ONE tile by 7 periods, beyond a 3x3 check.
        item = cert['placements'][0]
        item['cells'] = [(7,0,0,0)]
        item['polygon'] = cell_polygon(item['cells'][0])
        self.assertTrue(verify_periodic(cert)['valid'])
        # Duplicate another residue seven periods away: total area still agrees.
        item['cells'] = [(7,0,0,1)]
        item['polygon'] = cell_polygon(item['cells'][0])
        with self.assertRaisesRegex(VerificationError,'periodic overlap'):
            verify_periodic(cert)

    def test_periodic_rejects_gap_overlap_wrong_type_and_period(self):
        cert = monokite_domain()
        cert['placements'].pop()
        with self.assertRaisesRegex(VerificationError,'area'):
            verify_periodic(cert)
        cert = monokite_domain()
        cert['placements'][0] = copy.deepcopy(cert['placements'][1])
        with self.assertRaisesRegex(VerificationError,'overlap'):
            verify_periodic(cert)
        cert = monokite_domain()
        cert['placements'][0]['wrapped_cells'] = [(9,9,0,0)]
        with self.assertRaisesRegex(VerificationError,'stored wrapped'):
            verify_periodic(cert)
        cert = monokite_domain()
        cert['period_vectors'][1] = [0,0]
        with self.assertRaisesRegex(VerificationError,'dependent'):
            verify_periodic(cert)
        cert = monokite_domain()
        item = cert['placements'][0]
        item['cells'] = [(0,0,0,k) for k in range(3)]
        item['polygon'] = ((0,0),(12,0),(6,6))
        with self.assertRaisesRegex(VerificationError,'congruent'):
            verify_periodic(cert)

    def test_patch_target_coverage_and_overlap(self):
        cert = monokite_domain()
        del cert['period_vectors']
        cert['target_cells'] = [(0,0,0,0)]
        cert['seed_index'] = 0
        self.assertTrue(verify_patch(cert)['valid'])
        cert['target_cells'].append((100,0,0,0))
        with self.assertRaisesRegex(VerificationError,'coverage'):
            verify_patch(cert)
        cert['target_cells'].pop()
        cert['placements'].append(copy.deepcopy(cert['placements'][0]))
        with self.assertRaisesRegex(VerificationError,'repeats'):
            verify_patch(cert)


def reference_connected_masks(limit):
    """Tiny unpruned animal census: no closure, hull pruning, or D6 reduction."""
    from collections import defaultdict
    edge_owners = defaultdict(list)
    for i in range(-limit-1,limit+2):
        for j in range(-limit-1,limit+2):
            for o in range(2):
                for k in range(3):
                    cell = (i,j,o,k)
                    poly = cell_polygon(cell)
                    for a,b in zip(poly,poly[1:]+poly[:1]):
                        edge_owners[tuple(sorted((a,b)))].append(cell)
    adjacent = defaultdict(set)
    for owners in edge_owners.values():
        if len(owners) == 2:
            a,b = owners
            adjacent[a].add(b)
            adjacent[b].add(a)
    def normalize(cells):
        mi,mj = min(c[0] for c in cells),min(c[1] for c in cells)
        return frozenset((i-mi,j-mj,o,k) for i,j,o,k in cells)
    states = {frozenset({(0,0,o,k)}) for o in range(2) for k in range(3)}
    all_states = set(states)
    for size in range(1,limit):
        following = set()
        for state in states:
            for cell in set.union(*(adjacent[c] for c in state))-state:
                following.add(normalize(state|{cell}))
        states = following
        all_states.update(states)
    return all_states


def reference_grid_key(cells):
    """Canonicalize cell polygons geometrically under D6 and mesh translations."""
    def transform(p,r,f):
        x,y = p
        if f:
            y = -y
        for _ in range(r):
            x,y = (x-3*y)//2,(x+y)//2
        return x,y
    words = []
    for r in range(6):
        for f in (False,True):
            polygons = [tuple(transform(p,r,f) for p in cell_polygon(c)) for c in cells]
            # A mesh translation is determined by the difference of lex-min vertices.
            origin = min(p for poly in polygons for p in poly)
            words.append(tuple(sorted(tuple(sorted((x-origin[0],y-origin[1]) for x,y in poly)) for poly in polygons)))
    return min(words)


class IndependentCatalogueControls(unittest.TestCase):
    def test_closure_census_equals_unpruned_animals_through_four(self):
        from research.discovery import kite_grid
        expected = set()
        expected_geometry = []
        for cells in reference_connected_masks(4):
            poly = hull(p for c in cells for p in cell_polygon(c))
            if area2(poly) == 24*len(cells):
                expected.add(reference_grid_key(cells))
                expected_geometry.append(poly)
        catalogue = kite_grid.enumerate_convex(4)
        actual = {reference_grid_key(embedding) for tile in catalogue for embedding in tile.embeddings}
        self.assertEqual(expected,actual)
        self.assertTrue(all(any(congruent(poly,tile.polygon) for tile in catalogue) for poly in expected_geometry))
        for tile in catalogue:
            verify_cells_polygon(tile.cells,tile.polygon)
            for embedding in tile.embeddings:
                self.assertTrue(congruent(tile.polygon,hull(p for c in embedding for p in cell_polygon(c))))

    def test_grid_transform_and_neighbor_apis_against_independent_geometry(self):
        from research.discovery import kite_grid
        for i in range(-1,2):
            for j in range(-1,2):
                for o in range(2):
                    for k in range(3):
                        cell = (i,j,o,k)
                        self.assertEqual(cell_polygon(cell),kite_grid.cell_polygon(cell))
                        own = set(tuple(sorted(edge)) for edge in zip(cell_polygon(cell),cell_polygon(cell)[1:]+cell_polygon(cell)[:1]))
                        expected = set()
                        for di in range(-1,2):
                            for dj in range(-1,2):
                                for oo in range(2):
                                    for kk in range(3):
                                        other = (i+di,j+dj,oo,kk)
                                        pp = cell_polygon(other)
                                        edges = set(tuple(sorted(edge)) for edge in zip(pp,pp[1:]+pp[:1]))
                                        if cell != other and own & edges:
                                            expected.add(other)
                        self.assertEqual(expected,set(kite_grid.neighbors(cell)))
                        for r in range(6):
                            for f in (False,True):
                                transformed = []
                                for x,y in cell_polygon(cell):
                                    if f:
                                        y = -y
                                    for _ in range(r):
                                        x,y = (x-3*y)//2,(x+y)//2
                                    transformed.append((x,y))
                                image = kite_grid.transform_cell(cell,r,f)
                                self.assertEqual(set(transformed),set(cell_polygon(image)))


class RetainedScreenControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = json.loads((Path(__file__).parent/'runs/kite-n8-2026-10-24/screen.json').read_text())

    def resign(self,data):
        data['catalogue_sha256'] = digest(data['catalogue'])
        for row in data['singletons']:
            if 'witness' in row:
                row['witness_sha256'] = digest(row['witness'])
        data['result_sha256'] = digest({k:v for k,v in data.items() if k not in ('result_sha256','execution')})
        return data

    def test_retained_all_positive_screen(self):
        result = verify_screen(self.source)
        self.assertEqual(result['catalogue_records'],6)
        self.assertTrue(result['valid'])

    def test_funnel_and_tile_binding_cannot_be_fixed_just_by_rehashing(self):
        data = copy.deepcopy(self.source)
        data['funnel']['monohedral_periodic'] = 5
        with self.assertRaisesRegex(VerificationError,'funnel'):
            verify_screen(self.resign(data))
        data = copy.deepcopy(self.source)
        data['singletons'][0]['witness'] = copy.deepcopy(data['singletons'][1]['witness'])
        # Even relabelling a different shape as the desired ID must be rejected.
        data['singletons'][0]['witness']['prototiles'][0]['id'] = data['singletons'][0]['tile']
        with self.assertRaisesRegex(VerificationError,'catalogue definition'):
            verify_screen(self.resign(data))
        data = copy.deepcopy(self.source)
        data['singletons'].pop()
        with self.assertRaisesRegex(VerificationError,'omit'):
            verify_screen(self.resign(data))

    def test_hashes_signatures_and_source_provenance(self):
        data = copy.deepcopy(self.source)
        data['result_sha256'] = '0'*64
        with self.assertRaisesRegex(VerificationError,'result hash'):
            verify_screen(data)
        data = copy.deepcopy(self.source)
        data['catalogue'][0]['signature'][1] += 1
        with self.assertRaisesRegex(VerificationError,'congruence signature'):
            verify_screen(self.resign(data))
        data = copy.deepcopy(self.source)
        data['provenance']['source_sha256']['kite_grid.py'] = '0'*64
        with self.assertRaisesRegex(VerificationError,'source hash'):
            verify_screen(self.resign(data))


if __name__ == '__main__':
    unittest.main()
