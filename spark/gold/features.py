"""Build Gold machine-level features from validated Silver telemetry."""
import os
from pyspark.sql import functions as F
from spark.common import session

def main():
 s=session('iot-gold');c=os.getenv('ICEBERG_CATALOG','iot');s.sql(f'CREATE NAMESPACE IF NOT EXISTS {c}.gold')
 df=s.table(f'{c}.silver.telemetry')
 out=df.groupBy('machine_id').agg(F.avg('temperature_c').alias('avg_temperature_c'),F.avg('vibration_mms').alias('avg_vibration_mms'),F.count('*').alias('event_count'))
 out.writeTo(f'{c}.gold.machine_features').using('iceberg').createOrReplace()
if __name__=='__main__':main()
