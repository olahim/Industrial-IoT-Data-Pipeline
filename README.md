# Scalable Industrial IoT Data Engineering Pipeline for Predictive Maintenance

Overview
This project designs and develops an end-to-end, scalable Industrial Internet of Things (IIoT) data engineering pipeline for predictive maintenance.

The dataset for this system comes from Kaggle and is a realistic machine telemetry dataset for an Industrial IoT application. The machine's sensor values are streamed to Apache Kafka via a Python-based IoT message-stream simulator, and Apache Spark Structured Streaming processes the incoming data.

Data is stored in a Bronze–Silver–Gold lakehouse architecture on HDFS. The Gold layer offers features designed for predictive-maintenance machine-learning models.

There are two main predictive-maintenance issues solved:

Failure Prediction — predict if a machine will fail in the next 7 days.
Remaining Useful Life (RUL) Prediction — predict the number of running days until maintenance or failure.

The project also tests distributed pipeline scalability under increasing IoT workloads by measuring throughput, latency, Kafka consumer lag, Spark processing performance, CPU and memory usage, and other system metrics.
