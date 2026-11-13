#!/usr/bin/env bash
source "$(dirname "$0")/common.sh"
require_deploy
sync_dir "$MASTER_HOST" ml
for host in $WORKER_HOSTS; do sync_dir "$host" ml; done
