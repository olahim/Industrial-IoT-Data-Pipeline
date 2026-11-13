import argparse
from pathlib import Path
import joblib
from sklearn.ensemble import RandomForestClassifier
from ml.common import load_csv

def main():
 p=argparse.ArgumentParser();p.add_argument('--data',default='data/sample/telemetry.csv');p.add_argument('--output',default='artifacts/failure_model.joblib');args=p.parse_args()
 x,y=load_csv(args.data,'Failure_Within_7_Days')
 if len(set(y))<2: raise ValueError('Training requires both target classes')
 model=RandomForestClassifier(n_estimators=50,random_state=42).fit(x,y)
 Path(args.output).parent.mkdir(parents=True,exist_ok=True);joblib.dump(model,args.output)
 print('Saved',args.output,'(training demo; not independently evaluated)')
if __name__=='__main__':main()
