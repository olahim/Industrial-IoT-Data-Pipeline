"""Publish replayed telemetry to Kafka. Requires reachable brokers."""
import argparse,json,os
from simulator.iot_simulator import replay

def main():
    p=argparse.ArgumentParser();p.add_argument('--input',default='data/sample/telemetry.csv');p.add_argument('--count',type=int,default=100);p.add_argument('--rate',type=float,default=10);args=p.parse_args()
    from kafka import KafkaProducer
    brokers=os.getenv('KAFKA_BOOTSTRAP_SERVERS','WorkerC1:9092,WorkerC2:9092,WorkerC3:9092').split(',')
    topic=os.getenv('KAFKA_TOPIC','industrial-iot-telemetry')
    producer=KafkaProducer(bootstrap_servers=brokers,value_serializer=lambda v:json.dumps(v).encode(),acks='all',retries=5)
    try: replay(args.input,args.count,args.rate,lambda e:producer.send(topic,key=e['machine_id'].encode(),value=e))
    finally: producer.flush(timeout=30);producer.close()
if __name__=='__main__':main()
