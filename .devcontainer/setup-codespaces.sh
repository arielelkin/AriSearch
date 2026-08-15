#!/usr/bin/env bash
# Install per-agent Codespaces defaults without weakening sandboxing for
# native local development or locally opened Dev Containers.
#
# Codex and Claude Code each get a tool-permission-bypass config installed
# ONLY when running in GitHub Codespaces, on the reasoning that the dev
# container itself is the isolation boundary there. Native/local checkouts
# never get these files installed, so they keep normal sandboxing and
# permission prompts.

set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" > /dev/null 2>&1 && pwd)"

if [[ "${CODESPACES:-false}" != "true" ]]; then
  exit 0
fi

codex_config_dir="${CODEX_HOME:-${HOME}/.codex}"
install -d -m 0700 "${codex_config_dir}"
install \
  -m 0600 \
  "${script_dir}/codex-codespaces.toml" \
  "${codex_config_dir}/config.toml"

claude_config_dir="${HOME}/.claude"
install -d -m 0700 "${claude_config_dir}"
install \
  -m 0600 \
  "${script_dir}/claude-codespaces.json" \
  "${claude_config_dir}/settings.json"
