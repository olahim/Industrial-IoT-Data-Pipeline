-- Run in Spark SQL after tables exist; schedule outside ingestion windows.
CALL iot.system.rewrite_data_files(table => 'silver.telemetry');
CALL iot.system.expire_snapshots(table => 'silver.telemetry', retain_last => 5);
