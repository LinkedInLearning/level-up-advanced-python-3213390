from challenge.age_slowest_race import get_data, get_event_time, get_age_slowest_times

def test_age():
    expected = '40y67d'
    result = get_age_slowest_times()[0]
    assert expected == result

def test_slowest_time():
    expected = '33:31'
    result = get_age_slowest_times()[1]
    assert expected == result