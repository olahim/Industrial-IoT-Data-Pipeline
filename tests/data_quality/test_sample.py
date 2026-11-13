import csv

def test_sample_ranges():
    with open('data/sample/telemetry.csv',newline='') as f: rows=list(csv.DictReader(f))
    assert rows
    assert len({r['Machine_ID'] for r in rows})==len(rows)
    for r in rows:
        assert -40<=float(r['Temperature_C'])<=200
        assert 0<=float(r['Vibration_mms'])<=100
        assert int(r['Failure_Within_7_Days']) in (0,1)
