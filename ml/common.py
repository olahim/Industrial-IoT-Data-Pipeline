"""Shared offline training helpers. Sample dataset is illustrative, not model validation."""
import csv
FEATURES=['Temperature_C','Vibration_mms','Oil_Level_pct','Coolant_Level_pct','Power_Consumption_kW','Operational_Hours']
def load_csv(path,target):
    with open(path,newline='',encoding='utf-8') as f: rows=list(csv.DictReader(f))
    return [[float(r[k]) for k in FEATURES] for r in rows],[float(r[target]) for r in rows]
