#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
[[ -f "$ROOT/.env" ]] && set -a && source "$ROOT/.env" && set +a
: "${KAFKA_BIN:=/home/hadoop-user/kafka/kafka/bin}"
: "${KAFKA_BOOTSTRAP_SERVERS:=WorkerC1:9092,WorkerC2:9092,WorkerC3:9092}"
: "${KAFKA_TOPIC:=industrial-iot-telemetry}"
"$KAFKA_BIN/kafka-topics.sh" --bootstrap-server "$KAFKA_BOOTSTRAP_SERVERS" --create --if-not-exists --topic "$KAFKA_TOPIC" --partitions "${KAFKA_PARTITIONS:-3}" --replication-factor "${KAFKA_REPLICATION_FACTOR:-3}"
