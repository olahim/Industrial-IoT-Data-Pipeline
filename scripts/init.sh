#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
[[ -f "$ROOT/.env" ]] || cp "$ROOT/.env.example" "$ROOT/.env"
mkdir -p "$ROOT/data/raw" "$ROOT/artifacts"
echo 'Initialized local project. Edit .env for your cluster.'
