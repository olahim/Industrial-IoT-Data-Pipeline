"""Validate Bronze records and merge a deduplicated snapshot into Silver."""
import os
from pyspark.sql import functions as F
from spark.common import session

def main():
 s=session('iot-silver');c=os.getenv('ICEBERG_CATALOG','iot');s.sql(f'CREATE NAMESPACE IF NOT EXISTS {c}.silver')
 source=s.table(f'{c}.bronze.telemetry')
 valid=source.filter('machine_id IS NOT NULL AND event_id IS NOT NULL AND temperature_c BETWEEN -40 AND 200 AND vibration_mms BETWEEN 0 AND 100').dropDuplicates(['event_id'])
 valid.writeTo(f'{c}.silver.telemetry').using('iceberg').createOrReplace()
if __name__=='__main__':main()
