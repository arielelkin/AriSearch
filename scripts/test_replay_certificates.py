"""Check that Python patch upgrades preserve strict certificate replay."""

from unittest.mock import patch

import pytest

from research.discovery.verify import digest
from research.replay_provenance import matches_retained_digest
from research.searches.verify import certificate_matches


@pytest.mark.parametrize("section", ["software", "environment"])
@patch("research.replay_provenance.sys.version_info", (3, 12, 16))
def test_certificate_accepts_only_running_patch_provenance(section):
    expected = {section: {"python": "3.12.13", "sage": "10.9"}, "witness": [1, 2]}
    actual = {section: {"python": "3.12.16", "sage": "10.9"}, "witness": [1, 2]}

    assert certificate_matches(actual, expected)
    assert expected[section]["python"] == "3.12.13"
    assert actual[section]["python"] == "3.12.16"
    assert not certificate_matches(dict(actual, witness=[2, 1]), expected)
    for changed in (
        {"python": "3.12.16", "sage": "11.0"},
        {"python": "3.12.15", "sage": "10.9"},
        {"python": "3.13.16", "sage": "10.9"},
        {"sage": "10.9"},
    ):
        assert not certificate_matches(dict(actual, **{section: changed}), expected)


@patch("research.replay_provenance.sys.version_info", (3, 12, 16))
def test_discovery_digest_accepts_only_python_patch_provenance():
    retained = {"versions": {"python": "3.12.13", "solver": "1"}, "result": [1, 2]}
    retained["result_sha256"] = digest(retained)
    fresh = {"versions": {"python": "3.12.16", "solver": "1"}, "result": [1, 2]}

    assert matches_retained_digest(fresh, retained, digest)
    assert not matches_retained_digest(dict(fresh, result=[1.0, 2]), retained, digest)
    assert not matches_retained_digest(
        dict(fresh, versions={"python": "3.12.16", "solver": "2"}), retained, digest
    )
