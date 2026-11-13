from pathlib import Path

def test_required_assets():
    for path in ('Makefile','Jenkinsfile','monitoring/prometheus/prometheus.yml','airflow/dags/industrial_iot_pipeline.py','spark/streaming/kafka_to_bronze.py'):
        assert Path(path).is_file()
