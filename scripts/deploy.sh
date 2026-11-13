#!/usr/bin/env bash
source "$(dirname "$0")/common.sh"
require_deploy
bash "$ROOT/scripts/deploy-spark.sh"
bash "$ROOT/scripts/deploy-airflow.sh"
bash "$ROOT/scripts/deploy-ml.sh"
for host in "$MASTER_HOST" $WORKER_HOSTS; do
  sync_dir "$host" simulator
  sync_dir "$host" data/schema
 done
 echo 'Deployment copy completed. Restart/reload services as required by your installation.'
