SELECT machine_id, avg_temperature_c, avg_vibration_mms, event_count
FROM iceberg.gold.machine_features
ORDER BY avg_vibration_mms DESC;
