#!/usr/bin/env python3
"""Nondestructively replay retained certificates and independent verifiers.

Run with the arisearch Conda environment. Outputs are captured in memory and
compared as parsed JSON; retained certificates are never overwritten.
This verifies the recorded finite computations, not global mathematical proofs.
"""
import argparse
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]
SEARCHES = ROOT / "research/searches"
CERTIFICATE_DIR = ROOT / "research/certificates"
CERTIFICATES = (
    ("walton_vertex_rank.py", "walton_vertex_rank_certificate.json"),
    ("walton_relative_relabeling_rank.py", "walton_relative_relabeling_rank_certificate.json"),
    ("walton_state_assignment_rank.py", "walton_state_assignment_rank_certificate.json"),
    ("nonresonant_5_6_scaffold.py", "nonresonant_5_6_scaffold_certificate.json"),
    ("joint_5_6_local_verify.py", "joint_5_6_local_certificate.json"),
    ("new-angle-equilateral-rational-verify.py", "new-angle-equilateral-rational-certificate.json"),
    ("two_obtuse_angle_pentagon.py", "two_obtuse_angle_pentagon.json"),
    ("hexagon-holonomy-classify.py", "hexagon-holonomy-classification.json"),
    ("hexagon-five-length-classify.py", "hexagon-five-length-classification.json"),
    ("distinct_pentagon_higher_length_graph.py", "distinct_pentagon_higher_length_graph.json"),
    ("two_angle_5_7_periodic_witness.py", "two_angle_5_7_periodic.json"),
    ("new-angle-two-equilateral-hexagons-verify.py", "new-angle-two-equilateral-hexagons-certificate.json"),
    ("new-angle-three-pentagon-counterexample-verify.py", "new-angle-three-pentagon-counterexample.json"),
    ("new-angle-three-pentagon-irrational-angle-verify.py", "new-angle-three-pentagon-irrational-angle.json"),
    ("new-angle-three-pentagon-mixed-word-verify.py", "new-angle-three-pentagon-mixed-word-rank.json"),
    ("pentagrid_pentagon_angles.py", "pentagrid_pentagon_angles.json"),
    ("pentagrid-golden-metric.py", "pentagrid-golden-metric-closure.json"),
    ("pentagrid-golden-metric-torus.py", "pentagrid-golden-metric-four-face-tori.json"),
    ("pentagrid-golden-metric-periodic.py", "pentagrid-golden-metric-periodic.json"),
    ("pentagrid_monohedral_family_filter.py", "pentagrid-monohedral-family-filter.json"),
    ("pentagrid-golden-metric-two-length-stars.py", "pentagrid-golden-metric-two-length-stars.json"),
    ("pentagrid-golden-metric-area-compatible.py", "pentagrid-golden-metric-area-compatible.json"),
    ("regular_pentagon_private_octagon_geometry.py", "regular-pentagon-private-octagon-geometry.json"),
    ("all_obtuse_pentagon_regular_heptagon_witness.py", "all-obtuse-pentagon-regular-heptagon-witness.json"),
    ("pentagrid-area-family-edge-stars.py", "pentagrid-area-family-edge-stars.json"),
    ("pentagrid-u-w-periodic-continuum.py", "pentagrid-u-w-periodic-continuum.json"),
    ("pentagrid-golden-metric-robinson-partitions.py", "pentagrid-golden-metric-robinson-partitions.json"),
    ("pentagrid-golden-metric-robinson-boundary.py", "pentagrid-golden-metric-robinson-boundary.json"),
    ("obtuse_pentagon_regular_dodecagon_witness.py", "obtuse-pentagon-regular-dodecagon-witness.json"),
    ("pentagrid-robinson-height-boundary.py", "pentagrid-robinson-height-boundary.json"),
    ("pentagrid-robinson-diagonal-boundary.py", "pentagrid-robinson-diagonal-boundary.json"),
    ("pentagrid-robinson-boundary-completion.py", "pentagrid-robinson-boundary-completion.json"),
    ("pentagrid-v-w-periodic-continuum.py", "pentagrid-v-w-periodic-continuum.json"),
    ("pentagrid-v-v-double-y-periodic.py", "pentagrid-v-v-double-y-periodic.json"),
    ("pentagrid-v-v-general-double-y.py", "pentagrid-v-v-general-double-y.json"),
    ("two-angle-5-7-metric-continuum.py", "two-angle-5-7-metric-continuum.json"),
    ("two-angle-5-7-equal-private-scaffold.py", "two-angle-5-7-equal-private-scaffold.json"),
    ("new-octagon-q3-metric-deformation.py", "new-octagon-q3-metric-deformation.json"),
    ("private-octagon-equal-private-unit-closure.py", "private-octagon-equal-private-unit-closure.json"),
    ("hexagon-adjacent-repeat-periodic-cone.py", "hexagon-adjacent-repeat-periodic-cone.json"),
    ("pentagrid-v-v-reciprocal-partial-periodic.py", "pentagrid-v-v-reciprocal-partial-periodic.json"),
    ("branching-hexagon-rational-deformation.py", "branching-hexagon-rational-deformation.json"),
    ("branching-hexagon-new-chirality-collapse.py", "branching-hexagon-new-chirality-collapse.json"),
)
VERIFIERS = (
    ROOT / "research/reviews/verify_ammann_forcing_repair_rereview.py",
    ROOT / "research/reviews/verify_two_hexagon_low_rank_registry.py",
    ROOT / "research/searches/two-hexagon-global-check.py",
    ROOT / "research/reviews/verify_penrose_kite_dart_recomposition.py",
    ROOT / "research/reviews/verify_penrose_kite_dart_edge_stars.py",
    ROOT / "research/reviews/verify_partial_contact_cairo_first_corona_independent.py",
    ROOT / "research/reviews/verify_partial_contact_cairo_first_corona_geometry_extra.py",
    ROOT / "research/reviews/verify_two_homogeneous_center_pure_independent.py",
    ROOT / "research/reviews/verify_partial_contact_cairo_ray459_independent.py",
    ROOT / "research/reviews/verify_two_homogeneous_opposite_phase_independent.py",
    ROOT / "research/reviews/verify_two_homogeneous_opposite_full_independent.py",
    ROOT / "research/reviews/verify_partial_contact_cairo_lower_carriers_independent.py",
    ROOT / "research/reviews/verify_two_homogeneous_forward_obstruction_independent.py",
    ROOT / "research/reviews/verify_partial_contact_cairo_orbit6_flat239_independent.py",
    ROOT / "research/reviews/verify_partial_contact_cairo_orbit6_flat142_independent.py",
    ROOT / "research/reviews/verify_partial_contact_cairo_carrier_containment_independent.py",
    ROOT / "research/reviews/verify_branching_hexagon_pp_center_necessity_independent.py",
    ROOT / "research/reviews/verify_branching_hexagon_pp_center_cross_family_independent.py",
    ROOT / "research/reviews/verify_partial_contact_cairo_orbit0_flat23_complementary_independent.py",
    ROOT / "research/reviews/verify_partial_contact_cairo_orbit0_flat23_independent.py",
    ROOT / "research/reviews/verify_partial_contact_cairo_orbit0_flat11_complementary_independent.py",
    ROOT / "research/reviews/verify_partial_contact_cairo_orbit0_flat11_independent.py",
    ROOT / "research/reviews/verify_partial_contact_cairo_orbit7_flat12_independent.py",
    ROOT / "research/reviews/verify_partial_contact_cairo_orbit7_flat12_complementary_independent.py",
    ROOT / "research/reviews/verify_partial_contact_cairo_mixed_quotient_complementary_independent.py",
    ROOT / "research/reviews/verify_branching_hexagon_pp_center_family_independent.py",
    ROOT / "research/reviews/verify_partial_contact_cairo_mixed_quotient_independent.py",
    ROOT / "research/reviews/verify_branching_hexagon_one_noncentral_homogeneous_arc_independent.py",
    ROOT / "research/reviews/verify_walton_vertex_rank.py",
    ROOT / "research/reviews/verify_walton_relative_relabeling.py",
    ROOT / "research/reviews/verify_joint_5_6_two_ended.py",
    ROOT / "research/reviews/verify_two_obtuse_angle_pentagon.py",
    ROOT / "research/reviews/hexagon-holonomy-verify.py",
    ROOT / "research/reviews/hexagon-five-length-verify.py",
    ROOT / "research/reviews/verify_distinct_pentagon_higher.py",
    ROOT / "research/reviews/verify_two_angle_5_7_periodic.py",
    ROOT / "research/reviews/verify_two_equilateral_hexagons.py",
    ROOT / "research/reviews/hexagon-five-length-private-repeat-verify.py",
    ROOT / "research/reviews/verify_private_repeat_independent.py",
    ROOT / "research/reviews/verify_cairo_two_scalene.py",
    ROOT / "research/reviews/verify_cairo_two_scalene_independent.py",
    ROOT / "research/reviews/verify_cairo_distinct_side_ete.py",
    ROOT / "research/reviews/verify_cairo_distinct_side_independent.py",
    ROOT / "research/reviews/verify_three_angle_pentagon_periodic_independent.py",
    ROOT / "research/reviews/verify_three_pentagon_mixed_word_independent.py",
    ROOT / "research/reviews/verify_hexagon_affine_mirror_escape.py",
    ROOT / "research/reviews/verify_hexagon_affine_mirror_independent.py",
    ROOT / "research/reviews/verify_pentagrid_pentagon_angles.py",
    ROOT / "research/reviews/verify_pentagrid_golden_periodic_independent.py",
    ROOT / "research/reviews/verify_pentagrid_monohedral_filter.py",
    ROOT / "research/reviews/verify_pentagrid_two_length_edge_obstruction.py",
    ROOT / "research/reviews/verify_pentagrid_area_family_independent.py",
    ROOT / "research/reviews/verify_regular_pentagon_private_octagon_geometry.py",
    ROOT / "research/reviews/verify_all_obtuse_regular_heptagon_independent.py",
    ROOT / "research/reviews/verify_pentagrid_area_family_edge_obstruction.py",
    ROOT / "research/reviews/verify_pentagrid_u_w_periodic_continuum.py",
    ROOT / "research/reviews/verify_pentagrid_robinson_partitions_independent.py",
    ROOT / "research/reviews/verify_regular_dodecagon_independent.py",
    ROOT / "research/reviews/verify_pentagrid_robinson_height_boundary_independent.py",
    ROOT / "research/reviews/verify_pentagrid_robinson_boundary_geometry_independent.py",
    ROOT / "research/reviews/verify_pentagrid_robinson_residual_independent.py",
    ROOT / "research/reviews/verify_pentagrid_v_w_periodic_continuum.py",
    ROOT / "research/reviews/verify_pentagrid_robinson_penrose_window_independent.py",
    ROOT / "research/reviews/verify_pentagrid_robinson_generalized_window_independent.py",
    ROOT / "research/reviews/verify_pentagrid_v_v_double_y_independent.py",
    ROOT / "research/reviews/verify_pentagrid_v_v_general_partner_independent.py",
    ROOT / "research/reviews/verify_general_y_partner_formal_independent.py",
    ROOT / "research/searches/general-y-pentagon-partner-verify.py",
    ROOT / "research/reviews/verify_two_angle_5_7_metric_continuum.py",
    ROOT / "research/reviews/verify_private_octagon_pentagon_rigidity.py",
    ROOT / "research/reviews/verify_two_angle_5_7_corner_holonomy_fresh.py",
    ROOT / "research/searches/pentagrid-v-w-general-metric.py",
    ROOT / "research/reviews/verify_pentagrid_v_w_general_metric_independent.py",
    ROOT / "research/searches/verify_two_angle_5_7_equal_private_certificate.py",
    ROOT / "research/reviews/verify_octagon_q3_equal_private_independent.py",
    ROOT / "research/reviews/verify_private_octagon_equal_private_unit_independent.py",
    ROOT / "research/reviews/verify_reciprocal_v_partial_periodic_independent.py",
    ROOT / "research/reviews/verify_hexagon_adjacent_repeat_cone_independent.py",
    ROOT / "research/searches/partial-contact-cairo-private-arms.py",
    ROOT / "research/reviews/verify_partial_contact_cairo_private_arms_independent.py",
    ROOT / "research/searches/partial-contact-cairo-two-t-switch.py",
    ROOT / "research/reviews/verify_partial_contact_cairo_two_t_independent.py",
    ROOT / "research/searches/angle-frequency-cover-counterexample.py",
    ROOT / "research/reviews/verify_angle_frequency_cover_independent.py",
    ROOT / "research/reviews/verify_branching_hexagon_rational_deformation_independent.py",
    ROOT / "research/reviews/verify_branching_hexagon_new_chirality_collapse_independent.py",
    ROOT / "research/searches/partial-contact-cairo-swapped-arms-periodic.py",
    ROOT / "research/reviews/verify_partial_contact_cairo_swapped_arms_independent.py",
    ROOT / "research/searches/partial-contact-cairo-generic-arm-patterns.py",
    ROOT / "research/reviews/verify_cairo_generic_arm_patterns_independent.py",
    ROOT / "research/searches/partial-contact-cairo-alternate-resonances.py",
    ROOT / "research/searches/partial-contact-cairo-alternate-endpoint-marginals.py",
    ROOT / "research/reviews/verify_cairo_alternate_endpoint_marginals_independent.py",
    ROOT / "research/reviews/verify_cairo_alternate_f2a_slot_edge_independent.py",
    ROOT / "research/searches/partial-contact-cairo-repeated-arm-not-monotile.py",
    ROOT / "research/reviews/verify_cairo_repeated_arm_counterexample_independent.py",
    ROOT / "research/searches/partial-contact-cairo-adjacent-repeat-obstruction.py",
    ROOT / "research/reviews/verify_cairo_alternate_eac_periodic_independent.py",
    ROOT / "research/reviews/verify_two_run_four_face_periodic_independent.py",
    ROOT / "research/reviews/verify_two_run_second_curve_periodic_independent.py",
    ROOT / "research/reviews/verify_two_run_catalog_slot_independent.py",
    ROOT / "research/reviews/verify_two_run_catalog_periodic_independent.py",
    ROOT / "research/reviews/verify_branching_hexagon_new_two_run_third_curve_independent.py",
    ROOT / "research/reviews/verify_branching_hexagon_new_two_run_two_parameter_cone_independent.py",
    ROOT / "research/searches/partial-contact-cairo-single-shared-exception.py",
    ROOT / "research/reviews/verify_partial_contact_cairo_single_shared_notch_independent.py",
    ROOT / "research/reviews/verify_partial_contact_cairo_single_shared_family_independent.py",
    ROOT / "research/reviews/verify_cairo_single_shared_roots_independent.py",
    ROOT / "research/reviews/verify_partial_contact_cairo_single_shared_r1_periodic_independent.py",
    ROOT / "research/searches/partial-contact-cairo-adjacent-repeat-periodic.py",
    ROOT / "research/reviews/verify_partial_contact_cairo_symmetric_monohedral_independent.py",
    ROOT / "research/reviews/verify_partial_contact_cairo_generic_repeated_patterns_independent.py",
    ROOT / "research/reviews/verify_partial_contact_cairo_single_shared_core_independent.py",
    ROOT / "research/searches/partial-contact-cairo-paired-repeat-periodic.py",
    ROOT / "research/reviews/verify_partial_contact_cairo_one_shared_event_flats_independent.py",
    ROOT / "research/reviews/verify_cairo_one_shared_single_core_notch_independent.py",
    ROOT / "research/reviews/verify_branching_hexagon_new_complementary_pp_independent.py",
    ROOT / "research/reviews/verify_cairo_other_one_shared_flats_independent.py",
    ROOT / "research/reviews/verify_partial_contact_cairo_optional_seams_independent.py",
    ROOT / "research/reviews/verify_branching_hexagon_double_end_independent.py",
    ROOT / "research/reviews/verify_two_run_resonance_inventory_independent.py",
    ROOT / "research/reviews/verify_branching_hexagon_reverseqq_positive_reflection_independent.py",
    ROOT / "research/reviews/verify_branching_hexagon_mixed_pp_reverseqq_strata_independent.py",
    ROOT / "research/reviews/verify_branching_hexagon_mixed_pp_reverseqq_inventory_independent.py",
    ROOT / "research/reviews/verify_branching_hexagon_single_120_reverseqq_strata_independent.py",
    ROOT / "research/reviews/verify_branching_hexagon_single_120_reverseqq_inventory_independent.py",
    ROOT / "research/reviews/verify_branching_hexagon_mixed_pp_strata_independent.py",
    ROOT / "research/reviews/verify_branching_hexagon_mixed_pp_exceptional_inventory_independent.py",
    ROOT / "research/reviews/verify_partial_contact_cairo_two_cross_order_chambers_independent.py",
    ROOT / "research/reviews/verify_reverse_qq_actual_phases_independent.py",
    ROOT / "research/reviews/verify_mixed_pp_actual_phase_independent.py",
    ROOT / "research/reviews/verify_branching_hexagon_single_120_strata_independent.py",
    ROOT / "research/reviews/verify_branching_hexagon_single_120_exceptional_inventory_independent.py",
    ROOT / "research/reviews/verify_partial_contact_cairo_reversed_right_pair_cone_independent.py",
    ROOT / "research/reviews/verify_single_120_actual_phase_independent.py",
    ROOT / "research/reviews/verify_partial_contact_cairo_two_cross_orbits_independent.py",
    ROOT / "research/reviews/verify_branching_hexagon_single_120_obstruction_independent.py",
    ROOT / "research/reviews/verify_partial_contact_cairo_remaining_two_cross_seams_independent.py",
    ROOT / "research/reviews/verify_partial_contact_cairo_two_cross_seams_independent.py",
    ROOT / "research/reviews/verify_cairo_two_cross_flats_independent.py",
    ROOT / "research/reviews/verify_branching_hexagon_mixed_cover_independent.py",
    ROOT / "research/reviews/verify_branching_hexagon_no_homogeneous_swap_independent.py",
)

# Producer-style controls write only to a disposable output selected by run().
VERIFIER_ARGS = {
    "verify_two_hexagon_low_rank_registry.py": ["--check"],
    "two-hexagon-global-check.py": [
        "research/certificates/two-hexagon-global-covering-rank3-strata.json"],
    "verify_penrose_kite_dart_recomposition.py": ["--output", "{output}"],
    "verify_penrose_kite_dart_edge_stars.py": [
        "--checkpoint", "research/certificates/penrose-kite-dart-edge-stars-patch4.jsonl",
        "--output", "{output}"],
}
VERIFIER_CERTIFICATES = {
    "verify_penrose_kite_dart_recomposition.py": "penrose-kite-dart-encoding-controls.json",
    "verify_penrose_kite_dart_edge_stars.py": "penrose-kite-dart-edge-stars-controls.json",
    "verify_distinct_pentagon_higher.py": "distinct_pentagon_higher_verification.json",
    "verify_two_angle_5_7_periodic.py": "two_angle_5_7_periodic_verification.json",
    "verify_pentagrid_area_family_edge_obstruction.py": "pentagrid-area-family-edge-review.json",
    "verify_pentagrid_u_w_periodic_continuum.py": "pentagrid-u-w-periodic-continuum-review.json",
    "verify_pentagrid_v_w_periodic_continuum.py": "pentagrid-v-w-periodic-continuum-review.json",
    "verify_pentagrid_v_v_double_y_independent.py": "pentagrid-v-v-double-y-review.json",
}


def run(script):
    with tempfile.TemporaryDirectory(prefix="arisearch-verify-") as scratch:
        output = str(Path(scratch) / "control.json")
        args = [output if arg == "{output}" else arg
                for arg in VERIFIER_ARGS.get(script.name, [])]
        result = subprocess.run([sys.executable, str(script), *args], cwd=ROOT,
                                capture_output=True, text=True, check=False)
    if result.returncode:
        detail = result.stderr.strip() or result.stdout.strip()
        raise RuntimeError(f"{script.name} exited {result.returncode}: {detail}")
    return result.stdout


def main():
    if sys.flags.optimize:
        print("FAIL: assertions must be enabled; do not use python -O or PYTHONOPTIMIZE.",
              file=sys.stderr)
        return 1
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--only", action="append", default=[], metavar="SCRIPT",
                        help="Run a named completed check; repeat for dependency-affected checks.")
    args = parser.parse_args()
    known = {script for script, _ in CERTIFICATES} | {p.name for p in VERIFIERS}
    selected = set(args.only)
    unknown = selected - known
    if unknown:
        parser.error("unknown checks: " + ", ".join(sorted(unknown)))
    certificates = tuple(item for item in CERTIFICATES if not selected or item[0] in selected)
    verifiers = tuple(p for p in VERIFIERS if not selected or p.name in selected)
    failures = []
    for script, certificate in certificates:
        try:
            expected = json.loads((CERTIFICATE_DIR / certificate).read_text())
            actual = json.loads(run(SEARCHES / script))
            if actual != expected:
                raise ValueError(f"generated JSON differs from {certificate}")
            print(f"PASS certificate replay: {script}", flush=True)
        except (OSError, ValueError, RuntimeError) as error:
            failures.append(str(error))
            print(f"FAIL: {error}", file=sys.stderr, flush=True)
    for script in verifiers:
        # The endpoint obstruction relies on the distinct-length closure check.
        if script.name == "verify_joint_5_6_two_ended.py" and failures:
            print("SKIP endpoint verifier: resolve certificate failures first.", flush=True)
            continue
        try:
            output = run(script)
            if script.name == "verify_joint_5_6_two_ended.py":
                data = json.loads(output)
                if data["verdict"] != "no plane tiling":
                    raise ValueError("endpoint verifier did not certify no plane tiling")
            if script.name in VERIFIER_CERTIFICATES:
                expected = json.loads((CERTIFICATE_DIR / VERIFIER_CERTIFICATES[script.name]).read_text())
                if json.loads(output) != expected:
                    raise ValueError(f"independent verification JSON differs for {script.name}")
            print(f"PASS verifier: {script.name}", flush=True)
        except (OSError, ValueError, KeyError, RuntimeError) as error:
            failures.append(str(error))
            print(f"FAIL: {error}", file=sys.stderr, flush=True)
    if failures:
        print(f"Verification failed ({len(failures)} failures).", file=sys.stderr)
        return 1
    print(f"All {len(certificates)} certificate replays and {len(verifiers)} verifiers passed; no certificates written.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
