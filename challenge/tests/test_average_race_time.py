from challenge.average_race_time import get_data, get_average, get_rhines_times

def test_rhine_times():
    result = get_rhines_times()
    expected = ['32:32.006', '33:04', '33:21', '33:25', '33:30', '33:31']
    assert result == expected

def test_average_race_time():
    result = get_average()
    expected = '33:13.8'
    assert result == expected
