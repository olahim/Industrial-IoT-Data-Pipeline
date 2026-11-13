"""Structured Streaming Kafka JSON -> Iceberg Bronze (microbatch append)."""
import os
from pyspark.sql import functions as F
from spark.common import session

def main():
    spark=session('iot-kafka-bronze');catalog=os.getenv('ICEBERG_CATALOG','iot')
    spark.sql(f'CREATE NAMESPACE IF NOT EXISTS {catalog}.bronze')
    spark.sql(f"""CREATE TABLE IF NOT EXISTS {catalog}.bronze.telemetry (
        event_id string, machine_id string, event_time string, temperature_c double,
        vibration_mms double, payload string, ingestion_time timestamp)
        USING iceberg""")
    raw=(spark.readStream.format('kafka').option('kafka.bootstrap.servers',os.getenv('KAFKA_BOOTSTRAP_SERVERS','WorkerC1:9092,WorkerC2:9092,WorkerC3:9092')).option('subscribe',os.getenv('KAFKA_TOPIC','industrial-iot-telemetry')).option('startingOffsets','latest').load())
    from pyspark.sql.types import StructType,StructField,StringType,DoubleType
    schema=StructType([StructField('event_id',StringType()),StructField('machine_id',StringType()),StructField('event_time',StringType()),StructField('temperature_c',DoubleType()),StructField('vibration_mms',DoubleType())])
    df=raw.select(F.col('value').cast('string').alias('payload')).withColumn('parsed',F.from_json('payload',schema)).select('parsed.*','payload').withColumn('ingestion_time',F.current_timestamp())
    def write_batch(batch,batch_id):
        batch.writeTo(f'{catalog}.bronze.telemetry').append()
    query=(df.writeStream.foreachBatch(write_batch).option('checkpointLocation',os.getenv('HDFS_BASE','hdfs://MasterDB:9000/user/hadoop-user/industrial-iot')+'/checkpoints/bronze').start())
    query.awaitTermination()
if __name__=='__main__':main()
