#!/usr/bin/env bash
source "$(dirname "$0")/common.sh"
require_deploy
for host in "$MASTER_HOST" $WORKER_HOSTS; do sync_dir "$host" spark; done
