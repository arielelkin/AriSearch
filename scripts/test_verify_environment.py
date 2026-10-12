"""Regression checks for environment contamination and setup failure handling."""

import hashlib
import io
from contextlib import redirect_stdout
import importlib.metadata
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import tomllib
import unittest
from unittest.mock import patch

from verify_environment import verify_distributions
import replay_research


ROOT = Path(__file__).resolve().parents[1]


class DistributionChecks(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.prefix = Path(self.tmp.name)
        self.site = self.prefix / "lib/python3.12/site-packages"
        self.site.mkdir(parents=True)
        self.metadata = self.write_distribution("numpy", "2.5.2")
        filename = str(self.metadata.relative_to(self.prefix))
        self.records = {"numpy": {
            "files": [filename],
            "paths_data": {"paths": [{
                "_path": "site-packages/" + filename.split("/site-packages/")[1],
                "sha256": hashlib.sha256(self.metadata.read_bytes()).hexdigest(),
            }]},
        }}
        self.write_distribution("ortools", "9.15.6755")
        self.packages = [{"manager": "pip", "name": "ortools", "version": "9.15.6755"}]

    def write_distribution(self, name, version):
        directory = self.site / f"{name}-{version}.dist-info"
        directory.mkdir()
        metadata = directory / "METADATA"
        metadata.write_text(f"Name: {name}\nVersion: {version}\n")
        return metadata

    def check(self):
        distributions = list(importlib.metadata.distributions(path=[str(self.site)]))
        with patch("importlib.metadata.distributions", return_value=distributions):
            return verify_distributions(self.prefix, self.records, self.packages)

    def test_clean_environment_and_noarch_paths(self):
        self.assertEqual(self.check(), [])

    def test_extra_pip_package(self):
        self.write_distribution("extra_package", "1.0")
        self.assertIn("Unexpected Python distribution: extra-package", self.check())

    def test_pip_shadow_of_conda_package(self):
        self.write_distribution("numpy", "3.0")
        errors = self.check()
        self.assertIn("Duplicate Python distribution: numpy", errors)
        self.assertTrue(any("expected 2.5.2, got 3.0" in error for error in errors))

    def test_overwritten_metadata(self):
        self.metadata.write_text("Name: numpy\nVersion: 3.0\n")
        self.assertTrue(any("metadata overwritten" in error for error in self.check()))

    def test_missing_conda_metadata(self):
        self.metadata.unlink()
        self.assertTrue(any("Missing Conda distribution metadata" in error for error in self.check()))

    def test_missing_pip_package(self):
        (self.site / "ortools-9.15.6755.dist-info/METADATA").unlink()
        self.assertIn("Missing Python distribution: ortools", self.check())

    def test_wrong_pip_version(self):
        (self.site / "ortools-9.15.6755.dist-info/METADATA").write_text("Name: ortools\nVersion: 0.1\n")
        self.assertIn("Python distribution ortools: expected 9.15.6755, got 0.1", self.check())

    def test_vendor_metadata_is_not_a_distribution(self):
        vendor = self.site / "numpy/_vendor/extra-1.dist-info/METADATA"
        vendor.parent.mkdir(parents=True)
        vendor.write_text("Name: extra\nVersion: 1\n")
        self.records["numpy"]["files"].append(str(vendor.relative_to(self.prefix)))
        self.assertEqual(self.check(), [])


class SetupChecks(unittest.TestCase):
    def run_setup(self, exists, install_status, verify_status):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "environment").mkdir()
            lock = root / "environment/conda-lock.yml"
            lock.write_text("url: cddlib-1%210.94n\n")
            envs = root / "envs"
            if exists:
                (envs / "arisearch").mkdir(parents=True)
            binaries = root / "bin"
            binaries.mkdir()
            for name, script in {
                "uv": f"exit {install_status}\n",
                "conda": f"echo verifying\nexit {verify_status}\n",
            }.items():
                executable = binaries / name
                executable.write_text("#!/bin/sh\n" + script)
                executable.chmod(0o755)
            task = tomllib.loads((ROOT / "mise.toml").read_text())["tasks"]["setup"]["run"]
            result = subprocess.run(["bash", "-c", task], cwd=root, env={
                **os.environ, "PATH": str(binaries) + os.pathsep + os.environ["PATH"],
                "CONDA_ENVS_PATH": str(envs),
            }, capture_output=True, text=True)
            self.assertEqual(lock.read_text(), "url: cddlib-1%210.94n\n")
            return result

    def test_existing_broken_environment_fails(self):
        result = self.run_setup(True, 0, 7)
        self.assertEqual(result.returncode, 7)
        self.assertIn("skipping installation", result.stdout)
        self.assertIn("interrupted install", result.stdout)
        self.assertIn("remove", result.stdout)
        self.assertIn("rerun mise run setup", result.stdout)

    def test_install_failure_is_not_hidden(self):
        result = self.run_setup(False, 9, 0)
        self.assertEqual(result.returncode, 9)
        self.assertNotIn("verifying", result.stdout)

    def test_new_environment_is_verified(self):
        result = self.run_setup(False, 0, 7)
        self.assertEqual(result.returncode, 7)
        self.assertIn("verifying", result.stdout)


class LockChecks(unittest.TestCase):
    def run_lock(self, status):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "environment").mkdir()
            lock = root / "environment/conda-lock.yml"
            original = "  url: cddlib-1%210.94n\n  note: preserve-%21\n"
            lock.write_text(original)
            binaries = root / "bin"
            binaries.mkdir()
            uv = binaries / "uv"
            uv.write_text(f"#!/bin/sh\nexit {status}\n")
            uv.chmod(0o755)
            task = tomllib.loads((ROOT / "mise.toml").read_text())["tasks"]["lock"]["run"]
            result = subprocess.run(["bash", "-c", task], cwd=root, env={
                **os.environ, "PATH": str(binaries) + os.pathsep + os.environ["PATH"],
            }, capture_output=True, text=True)
            return result, lock.read_text(), original

    def test_only_url_lines_are_normalized(self):
        result, content, _ = self.run_lock(0)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(content, "  url: cddlib-1!0.94n\n  note: preserve-%21\n")

    def test_failed_lock_is_not_normalized(self):
        result, content, original = self.run_lock(9)
        self.assertEqual(result.returncode, 9)
        self.assertEqual(content, original)


class ReplayChecks(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "research/searches").mkdir(parents=True)
        for name in ("discovery-log.md", "research-problem.md", "research-protocol.md", "main_prompt.md"):
            (self.root / name).write_text("retained evidence\n")

    def run_replay(self, status):
        verifier = self.root / "research/searches/verify.py"
        verifier.write_text(f"raise SystemExit({status})\n")
        output = io.StringIO()
        with patch.object(replay_research, "ROOT", self.root), patch.object(sys, "argv", ["replay"]), redirect_stdout(output):
            result = replay_research.main()
        return result, output.getvalue()

    def test_failed_replay_reports_failure_and_preserves_exit_code(self):
        result, output = self.run_replay(7)
        self.assertEqual(result, 7)
        self.assertIn("Research replay failed (exit 7).", output)
        self.assertIn("Original research files are unchanged.", output)
        self.assertNotIn("passed", output)

    def test_successful_replay_reports_success(self):
        result, output = self.run_replay(0)
        self.assertEqual(result, 0)
        self.assertIn("Research replay passed.", output)

    def test_original_evidence_changes_are_rejected(self):
        def mutate(*args, **kwargs):
            (self.root / "discovery-log.md").write_text("changed\n")
            return subprocess.CompletedProcess(args[0], 0)

        with patch.object(replay_research.subprocess, "run", side_effect=mutate):
            with self.assertRaisesRegex(SystemExit, "Research files changed"):
                self.run_replay(0)


if __name__ == "__main__":
    unittest.main()
