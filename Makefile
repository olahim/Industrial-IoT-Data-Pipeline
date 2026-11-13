.DEFAULT_GOAL := help
.PHONY: help init check-env lint test test-unit test-integration test-dq simulate kafka-topic deploy deploy-spark deploy-airflow deploy-ml verify rollback monitoring-check clean
PYTHON ?= python3
help:
	@grep -E '^[a-zA-Z_-]+:' Makefile | cut -d: -f1
init:
	bash scripts/init.sh
check-env:
	bash scripts/check-env.sh
lint:
	$(PYTHON) -m compileall -q simulator spark ml airflow monitoring tests experiments
	@for s in scripts/*.sh kafka/scripts/*.sh jenkins/scripts/*.sh; do bash -n "$$s" || exit 1; done
test-unit:
	$(PYTHON) -m pytest -q tests/unit
test-integration:
	$(PYTHON) -m pytest -q tests/integration
test-dq:
	$(PYTHON) -m pytest -q tests/data_quality
test: lint
	$(PYTHON) -m pytest -q tests
simulate:
	$(PYTHON) simulator/iot_simulator.py --input data/sample/telemetry.csv --count 10 --output /tmp/iot-events.jsonl
kafka-topic:
	bash kafka/scripts/create_topic.sh
deploy: check-env test
	bash scripts/deploy.sh
deploy-spark:
	bash scripts/deploy-spark.sh
deploy-airflow:
	bash scripts/deploy-airflow.sh
deploy-ml:
	bash scripts/deploy-ml.sh
verify:
	bash scripts/verify-deployment.sh
rollback:
	bash scripts/rollback.sh
monitoring-check:
	@command -v promtool >/dev/null && promtool check config monitoring/prometheus/prometheus.yml || echo 'promtool not installed; skipped'
clean:
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
