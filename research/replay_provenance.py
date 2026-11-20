"""Compare current replay output with evidence produced by an older Python patch."""

import re
import sys


def with_retained_python(actual, retained, sections):
    """Use the recorded version only for a verified forward patch difference."""
    if not isinstance(actual, dict) or not isinstance(retained, dict):
        return actual

    normalized = dict(actual)
    for section in sections:
        recorded = retained.get(section)
        replayed = actual.get(section)
        if not isinstance(recorded, dict) or not isinstance(replayed, dict):
            continue
        original_version = recorded.get("python")
        runtime_version = replayed.get("python")
        if not isinstance(original_version, str) or not isinstance(runtime_version, str):
            continue
        original = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", original_version)
        runtime = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", runtime_version)
        if not original or not runtime:
            continue
        if (tuple(map(int, runtime.groups())) == sys.version_info[:3]
                and original.groups()[:2] == runtime.groups()[:2]
                and int(original[3]) < int(runtime[3])):
            normalized[section] = dict(replayed, python=original_version)
    return normalized


def matches_retained_digest(actual, retained, digest):
    """Compare fresh discovery data against an independently verified retained hash."""
    normalized = with_retained_python(actual, retained, ("versions",))
    stable = {key: value for key, value in normalized.items()
              if key not in ("result_sha256", "execution")}
    return digest(stable) == retained["result_sha256"]
