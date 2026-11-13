"""Replay CSV rows as normalized industrial telemetry JSON events."""
import argparse,csv,json,time,uuid
from datetime import datetime,timezone
from pathlib import Path

ALIASES={'Machine_ID':'machine_id','Machine_Type':'machine_type','Temperature_C':'temperature_c','Vibration_mms':'vibration_mms','Sound_dB':'sound_db','Oil_Level_pct':'oil_level_pct','Coolant_Level_pct':'coolant_level_pct','Power_Consumption_kW':'power_consumption_kw','Operational_Hours':'operational_hours','Failure_Within_7_Days':'failure_within_7_days','Remaining_Useful_Life_days':'remaining_useful_life_days'}
NUMERIC={'temperature_c','vibration_mms','sound_db','oil_level_pct','coolant_level_pct','power_consumption_kw','operational_hours','failure_within_7_days','remaining_useful_life_days'}
def normalize(row,now=None):
    result={ALIASES.get(k,k): (float(v) if ALIASES.get(k,k) in NUMERIC and v not in ('',None) else v) for k,v in row.items()}
    result['event_id']=str(uuid.uuid4())
    result['event_time']=now or datetime.now(timezone.utc).isoformat()
    return result

def events(path,count=0):
    with open(path,newline='',encoding='utf-8') as f:
        rows=list(csv.DictReader(f))
    if not rows: raise ValueError('CSV contains no records')
    for i in range(count or len(rows)):
        yield normalize(rows[i % len(rows)])

def replay(path,count=0,rate=0,sink=None):
    interval=1/rate if rate>0 else 0
    for event in events(path,count):
        if sink: sink(event)
        else: print(json.dumps(event))
        if interval: time.sleep(interval)

def main():
    p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--count',type=int,default=0);p.add_argument('--rate',type=float,default=0);p.add_argument('--output');args=p.parse_args()
    if args.count<0 or args.rate<0: p.error('count and rate must be nonnegative')
    if args.output:
        with open(args.output,'w',encoding='utf-8') as f: replay(args.input,args.count,args.rate,lambda e:f.write(json.dumps(e)+'\n'))
    else: replay(args.input,args.count,args.rate)
if __name__=='__main__':main()
