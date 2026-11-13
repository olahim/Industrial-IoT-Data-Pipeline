#!/usr/bin/env bash
source "$(dirname "$0")/common.sh"
for host in "$MASTER_HOST" $WORKER_HOSTS; do
  echo "Checking $host"
  remote "$host" "test -f '$PROJECT_DIR/spark/common.py' && test -f '$PROJECT_DIR/ml/common.py'" || exit 1
 done
 echo 'Remote file presence verified (not an end-to-end service health check).'
