import argparse,json
import joblib
from ml.common import FEATURES

def main():
 p=argparse.ArgumentParser();p.add_argument('--model',required=True);p.add_argument('--features',required=True,help='JSON object with feature names');a=p.parse_args()
 values=json.loads(a.features);model=joblib.load(a.model)
 print(json.dumps({'prediction':float(model.predict([[float(values[k]) for k in FEATURES]])[0])}))
if __name__=='__main__':main()
