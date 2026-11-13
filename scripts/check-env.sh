#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "$0")/common.sh"
for cmd in python3 bash; do command -v "$cmd" >/dev/null || { echo "Missing $cmd" >&2; exit 1; }; done
for file in "$ROOT/.env" "$ROOT/Makefile" "$ROOT/Jenkinsfile"; do [[ -f "$file" ]] || { echo "Missing $file" >&2; exit 1; }; done
[[ "$PROJECT_DIR" = /* ]] || { echo 'PROJECT_DIR must be absolute' >&2; exit 1; }
echo "Local environment valid: $ROOT; remote target: $PROJECT_DIR"
