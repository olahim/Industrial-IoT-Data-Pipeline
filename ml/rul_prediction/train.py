import argparse
from pathlib import Path
import joblib
from sklearn.ensemble import RandomForestRegressor
from ml.common import load_csv

def main():
 p=argparse.ArgumentParser();p.add_argument('--data',default='data/sample/telemetry.csv');p.add_argument('--output',default='artifacts/rul_model.joblib');args=p.parse_args()
 x,y=load_csv(args.data,'Remaining_Useful_Life_days')
 model=RandomForestRegressor(n_estimators=50,random_state=42).fit(x,y)
 Path(args.output).parent.mkdir(parents=True,exist_ok=True);joblib.dump(model,args.output)
 print('Saved',args.output,'(training demo; not independently evaluated)')
if __name__=='__main__':main()
