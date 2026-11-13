from simulator.iot_simulator import normalize,events

def test_normalize():
    e=normalize({'Machine_ID':'M1','Temperature_C':'77.2','Vibration_mms':'4.1'},'2026-01-01T00:00:00+00:00')
    assert e['machine_id']=='M1' and e['temperature_c']==77.2 and e['event_time'].startswith('2026')

def test_replay_count():
    assert len(list(events('data/sample/telemetry.csv',7)))==7
