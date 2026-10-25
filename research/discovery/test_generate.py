"""Protect retained data and reject invalid caps before launching a search."""
from pathlib import Path
from types import SimpleNamespace

import pytest

from research.discovery import generate


def test_existing_output_is_untouched_and_never_launches(tmp_path, monkeypatch):
    destination = tmp_path / "retained"
    destination.mkdir()
    witness = destination / "scale-audit.jsonl.gz"
    witness.write_bytes(b"retained exact evidence")
    monkeypatch.setattr(generate.subprocess, "run", lambda *a, **k: pytest.fail("must not launch"))
    with pytest.raises(FileExistsError):
        generate.run_generation(destination)
    assert witness.read_bytes() == b"retained exact evidence"


@pytest.mark.parametrize("cap", [0, -1, float("nan"), float("inf")])
def test_invalid_cpu_cap_has_no_side_effects(tmp_path, monkeypatch, cap):
    destination = tmp_path / "new"
    monkeypatch.setattr(generate.subprocess, "run", lambda *a, **k: pytest.fail("must not launch"))
    with pytest.raises(ValueError):
        generate.run_generation(destination, cpu_cap=cap)
    assert not destination.exists()


@pytest.mark.parametrize("family", ["mixed", "angular-first"])
def test_fresh_output_launches_only_selected_fixed_family(tmp_path, monkeypatch, family):
    destination = tmp_path / "new"
    calls = []
    def launch(command, **kwargs):
        assert destination.is_dir() and not list(destination.iterdir())
        calls.append((command, kwargs))
        return SimpleNamespace(returncode=0)
    monkeypatch.setattr(generate.subprocess, "run", launch)
    code, actual = generate.run_generation(destination, family=family, cpu_cap=12)
    assert code == 0 and actual == destination
    command, options = calls[0]
    assert command[-4:] == ["--output", str(destination), "--cpu-cap", "12"]
    assert options["cwd"] == generate.ROOT
    assert ("--worker" in command) is (family == "angular-first")


def test_dangling_output_symlink_is_not_followed(tmp_path, monkeypatch):
    destination = tmp_path / "existing-link"
    destination.symlink_to(tmp_path / "absent-target")
    monkeypatch.setattr(generate.subprocess, "run", lambda *a, **k: pytest.fail("must not launch"))
    with pytest.raises(FileExistsError):
        generate.run_generation(destination)
    assert destination.is_symlink()
    assert not (tmp_path / "absent-target").exists()
