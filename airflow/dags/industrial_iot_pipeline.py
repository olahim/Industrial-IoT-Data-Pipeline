"""Airflow 3 DAG: Spark batch transformations after separate streaming ingestion."""
from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

ROOT='/home/hadoop-user/industrial-iot-pipeline'
SPARK='/home/hadoop-user/spark/bin/spark-submit'
ICEBERG_JAR='/home/hadoop-user/spark/jars/iceberg-spark-runtime.jar'  # replace with matching runtime jar
with DAG('industrial_iot_pipeline',start_date=datetime(2026,1,1),schedule='@daily',catchup=False,tags=['iot','predictive-maintenance']) as dag:
    silver=BashOperator(task_id='silver',bash_command=f'cd {ROOT} && PYTHONPATH={ROOT} {SPARK} --master yarn --deploy-mode client --jars {ICEBERG_JAR} spark/silver/clean_telemetry.py')
    gold=BashOperator(task_id='gold',bash_command=f'cd {ROOT} && PYTHONPATH={ROOT} {SPARK} --master yarn --deploy-mode client --jars {ICEBERG_JAR} spark/gold/features.py')
    silver >> gold
