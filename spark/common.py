"""Shared Spark session configuration for Hive-backed Iceberg catalog."""
import os

def session(app):
    from pyspark.sql import SparkSession
    catalog=os.getenv('ICEBERG_CATALOG','iot')
    return (SparkSession.builder.appName(app)
      .config(f'spark.sql.catalog.{catalog}','org.apache.iceberg.spark.SparkCatalog')
      .config(f'spark.sql.catalog.{catalog}.type','hive')
      .config(f'spark.sql.catalog.{catalog}.uri',os.getenv('HIVE_METASTORE_URI','thrift://MasterDB:9083'))
      .config(f'spark.sql.catalog.{catalog}.warehouse',os.getenv('ICEBERG_WAREHOUSE','hdfs://MasterDB:9000/user/hadoop-user/industrial-iot/warehouse'))
      .getOrCreate())
