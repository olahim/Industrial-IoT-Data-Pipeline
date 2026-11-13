#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
if [[ -f "$ROOT/.env" ]]; then
  set -a
  source "$ROOT/.env"
  set +a
fi
: "${DEPLOY_USER:=hadoop-user}"
: "${MASTER_HOST:=MasterDB}"
: "${WORKER_HOSTS:=WorkerC1 WorkerC2 WorkerC3}"
: "${PROJECT_DIR:=/home/hadoop-user/industrial-iot-pipeline}"
require_deploy() { [[ "${CONFIRM_DEPLOY:-no}" == yes ]] || { echo 'Remote deployment blocked: set CONFIRM_DEPLOY=yes' >&2; exit 2; }; }
remote() { ssh -o BatchMode=yes -o ConnectTimeout=8 "${DEPLOY_USER}@$1" "${@:2}"; }
sync_dir() { local host="$1" dir="$2"; remote "$host" "mkdir -p '$PROJECT_DIR/$dir'"; rsync -az --exclude __pycache__ --exclude '*.pyc' "$ROOT/$dir/" "${DEPLOY_USER}@${host}:$PROJECT_DIR/$dir/"; }
