#!/usr/bin/env bash
source "$(dirname "$0")/common.sh"
require_deploy
sync_dir "$MASTER_HOST" airflow
# Airflow scheduler reads DAGs from configured AIRFLOW_DAGS_DIR.
remote "$MASTER_HOST" "mkdir -p '${AIRFLOW_DAGS_DIR:-/home/hadoop-user/airflow/dags}' && cp '$PROJECT_DIR/airflow/dags/'*.py '${AIRFLOW_DAGS_DIR:-/home/hadoop-user/airflow/dags}/'"
