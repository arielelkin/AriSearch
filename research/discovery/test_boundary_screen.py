import itertools
import time
import unittest

from research.discovery.boundary_words import enumerate_words, canonical_word
from research.discovery.boundary_screen import (STEPS, StateBank, develop_certificate, disk,
                              graph_for_faces, search_periodic, solve_csp,
                              solve_disk, wrap_face)


class BoundaryScreenTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tiles = [tile.to_dict() for tile in enumerate_words(3)]
        cls.bank = StateBank(cls.tiles)

    def test_exact_disk_and_skew_wrap(self):
        self.assertEqual([len(disk(r)) for r in (1, 2, 4)], [7, 19, 61])
        self.assertTrue(all(step in disk(1) for step in STEPS))
        self.assertEqual(wrap_face((-1, -1), (3, 2, 2)), ((1, 1), (0, -1)))
        for face in [(-4, 7), (8, -5), (3, 3)]:
            (i, j), (m, n) = wrap_face(face, (3, 2, 2))
            self.assertEqual((i+3*m+2*n, j+2*n), face)

    def test_one_face_period_matches_opposite_lengths(self):
        for tile in self.tiles:
            result = search_periodic(self.bank, [tile["id"]], max_index=1)
            self.assertEqual(result["status"] == "PERIODIC_WITNESS",
                             tile["centrally_symmetric"])

    def test_csp_matches_bruteforce_on_skew_two_face_torus(self):
        noncentral = [tile["id"] for tile in self.tiles if not tile["centrally_symmetric"]][:2]
        graph = graph_for_faces(((0, 0), (1, 0)), (2, 1, 1))
        allowed = [i for i, state in enumerate(self.bank.states) if state["tile_id"] in noncentral]
        brute = any(all(self.bank.states[assignment[u]]["word"][k] ==
                        self.bank.states[assignment[v]]["word"][(k+3)%6]
                        for u, v, k in graph[1])
                    for assignment in itertools.product(allowed, repeat=2))
        result = solve_csp(self.bank, graph, noncentral)
        self.assertEqual(result["status"], "SAT" if brute else "UNSAT")

    def test_mixed_states_are_species_aware(self):
        ids = [tile["id"] for tile in self.tiles if not tile["centrally_symmetric"]][:2]
        for k in range(6):
            mask = self.bank.mask(ids)
            support = self.bank.support(mask, k)
            for index, state in enumerate(self.bank.states):
                expected = any(other["tile_id"] in ids and
                               state["word"][k] == other["word"][(k+3)%6]
                               for other in self.bank.states)
                self.assertEqual(bool(support & (1 << index)), expected)

    def test_unknown_is_not_exhausted(self):
        tile = self.tiles[0]["id"]
        graph = graph_for_faces(disk(1))
        node_stop = solve_csp(self.bank, graph, [tile], node_budget=0)
        propagation_stop = solve_csp(self.bank, graph, [tile], propagation_budget=0)
        self.assertEqual(node_stop["status"], "UNKNOWN")
        self.assertEqual(node_stop["budget_reason"], "node_budget")
        self.assertEqual(propagation_stop["status"], "UNKNOWN")
        self.assertEqual(propagation_stop["budget_reason"], "propagation_budget")

    def test_outer_cpu_cap_interrupts_solver_as_unknown(self):
        bank = StateBank(self.tiles)
        bank.cpu_deadline = time.process_time()-1
        tile = self.tiles[0]["id"]
        result = solve_csp(bank, graph_for_faces(disk(4)), [tile])
        self.assertEqual(result["status"], "UNKNOWN")
        self.assertEqual(result["budget_reason"], "outer_cpu_budget")
        self.assertEqual(result["nodes"], 0)

    def test_seeded_disk_is_exactly_developed(self):
        tile = next(tile for tile in self.tiles if tile["word"] == [1]*6)
        result = solve_disk(self.bank, [tile["id"]], 2, tile["id"])
        self.assertEqual(result["status"], "SAT")
        witness = result["witness"]
        self.assertEqual(len(witness["placements"]), 19)
        self.assertEqual(witness["symbolic_radius"], 2)
        by_face = {tuple(p["face"]): p for p in witness["placements"]}
        for face, placement in by_face.items():
            for k, step in enumerate(STEPS):
                other = by_face.get((face[0]+step[0], face[1]+step[1]))
                if other:
                    self.assertEqual(placement["polygon"][k], other["polygon"][(k+4)%6])
                    self.assertEqual(placement["polygon"][(k+1)%6], other["polygon"][(k+3)%6])

    def test_bad_periodic_development_rejected(self):
        tile = next(tile for tile in self.tiles if not tile["centrally_symmetric"])
        index = next(i for i, state in enumerate(self.bank.states) if state["tile_id"] == tile["id"])
        with self.assertRaisesRegex(ValueError, "holonomy"):
            develop_certificate(self.bank, ((0, 0),), [index], [tile["id"]], hnf=(1, 0, 1))

    def test_legacy_mixed_period_four_positive_control(self):
        tiles = [tile.to_dict() for tile in enumerate_words(5)]
        words = {canonical_word((1, 3, 2, 3, 1, 4)), canonical_word((2, 5, 3, 4, 3, 5))}
        pair = [tile["id"] for tile in tiles if tuple(tile["word"]) in words]
        bank = StateBank(tiles)
        self.assertEqual(len(pair), 2)
        self.assertTrue(all(search_periodic(bank, [tile], max_index=4)["status"] ==
                            "NO_PERIODIC_WITNESS_IN_TESTED_DOMAINS" for tile in pair))
        result = search_periodic(bank, pair, max_index=4)
        self.assertEqual(result["status"], "PERIODIC_WITNESS")
        self.assertEqual(set(result["witness"]["species_present"]), set(pair))
        self.assertEqual(len(result["witness"]["placements"]), 4)


if __name__ == "__main__":
    unittest.main()
