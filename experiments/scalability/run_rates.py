"""Generate controlled local replay runs; not a Kafka benchmark."""
import argparse,time
from simulator.iot_simulator import replay

def main():
 p=argparse.ArgumentParser();p.add_argument('--rates',default='100,500,1000');p.add_argument('--count',type=int,default=100);a=p.parse_args()
 for rate in map(float,a.rates.split(',')):
  start=time.monotonic();replay('data/sample/telemetry.csv',a.count,rate,lambda event:None)
  elapsed=time.monotonic()-start
  print(f'target={rate:.0f} count={a.count} elapsed={elapsed:.3f}s actual={a.count/elapsed:.1f}/s')
if __name__=='__main__':main()
