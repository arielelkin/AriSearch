"""Meaningful bounds, wrapping, reflection, and exterior-conflict regressions."""
import unittest

from research.discovery.kite_grid import cell_polygon, normalize_cells, transform_cell
from research.discovery.screen import (_orientations, digest, hnf_domains, periodic_placements,
                     run_screen, search_periodic, solve_exact_cover, wrap_cell)


class ScreenTests(unittest.TestCase):
    def test_skew_wrapping_positive_and_negative(self):
        hnf = (3, 2, 2)
        cell = (1, 1, 0, 2)
        self.assertEqual(wrap_cell((4, 1, 0, 2), hnf), cell)
        self.assertEqual(wrap_cell((3, 3, 0, 2), hnf), cell)
        self.assertEqual(wrap_cell((-1, -1, 0, 2), hnf), cell)
        self.assertIn((3, 2, 2), list(hnf_domains(6)))

    def test_torus_self_overlap_rejected(self):
        tile = {"id": "long", "cells": [(0, 0, 0, 0), (1, 0, 0, 0)]}
        self.assertEqual(periodic_placements([tile], (1, 0, 1)), [])

    def test_kite_all_orientations_tile_fundamental_domain(self):
        tile = {"id": "kite", "cells": [(0, 0, 0, 0)],
                "polygon": cell_polygon((0, 0, 0, 0))}
        placements = periodic_placements([tile], (1, 0, 1))
        self.assertEqual({p["wrapped_cells"][0] for p in placements},
                         {(0, 0, o, k) for o in range(2) for k in range(3)})
        result = search_periodic([tile], max_index=1, solve_seconds=1)
        self.assertEqual(result["status"], "PERIODIC_WITNESS")
        self.assertEqual(len(result["witness"]["placements"]), 6)
        self.assertEqual(result["witness_sha256"], digest(result["witness"]))

    def test_reflected_masks_are_not_lost(self):
        mask = [(0, 0, 0, 0), (0, 0, 0, 1), (0, 0, 1, 0)]
        rotations = {normalize_cells(transform_cell(c, r, False) for c in mask)
                     for r in range(6)}
        orientations = {frozenset(mask) for mask in _orientations({"cells": mask})}
        reflected = normalize_cells(transform_cell(c, 0, True) for c in mask)
        self.assertNotIn(reflected, rotations)
        self.assertIn(reflected, orientations)

    def test_repeated_congruence_classes_are_rejected(self):
        tile = {"cells": [(0, 0, 0, 0)], "polygon": cell_polygon((0, 0, 0, 0))}
        with self.assertRaisesRegex(ValueError, "distinct congruence"):
            run_screen([tile, tile])

    def test_patch_exterior_conflicts_are_enforced(self):
        a, b, exterior = (0, 0, 0, 0), (0, 0, 0, 1), (5, 5, 0, 0)
        placements = [{"tile": "A", "cells": [a, exterior]},
                      {"tile": "B", "cells": [b, exterior]}]
        result = solve_exact_cover(placements, [a, b], seconds=1)
        self.assertEqual(result["status"], "INFEASIBLE")

    def test_required_both_types_and_unknown_status(self):
        a = (0, 0, 0, 0)
        placements = [{"tile": "A", "cells": [a]}]
        result = solve_exact_cover(placements, [a], required_tiles=["A", "B"], seconds=1)
        self.assertEqual(result["status"], "INFEASIBLE")
        # Zero effort terminates before a feasible answer and must remain UNKNOWN.
        result = solve_exact_cover(placements, [a], seconds=0, deterministic_time=0)
        self.assertEqual(result["status"], "UNKNOWN")


if __name__ == "__main__":
    unittest.main()
