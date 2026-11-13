#!/usr/bin/env bash
source "$(dirname "$0")/common.sh"
require_deploy
: "${ROLLBACK_RELEASE:?Set ROLLBACK_RELEASE to an operator-verified backup directory on each node}"
case "$ROLLBACK_RELEASE" in /*) ;; *) echo 'ROLLBACK_RELEASE must be absolute' >&2; exit 1;; esac
for host in "$MASTER_HOST" $WORKER_HOSTS; do
  remote "$host" "test -d '$ROLLBACK_RELEASE' && rsync -a '$ROLLBACK_RELEASE/' '$PROJECT_DIR/'" || exit 1
 done
 echo 'Restored backup files. Validate service state manually.'
