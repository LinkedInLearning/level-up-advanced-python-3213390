# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians

import re
import math


def get_data():
    """Return content from the 10k_racetimes.txt file"""
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.readlines()
    return content


def get_rhines_times():
    """Return a list of Jennifer Rhines' race times"""
    rhines_times = []
    races = get_data()
    for line in races:
        if 'Jennifer Rhines' in line:
            rhines_times.append(re.findall(r'\d{2}:\S+', line)[0])
    return rhines_times


def get_average():
    """Return Jennifer Rhines' average race time in the format:
       mm:ss:M where :
       m corresponds to a minutes digit
       s corresponds to a seconds digit
       M corresponds to a milliseconds digit (no rounding, just the single digit)"""
    def total_seconds(x, y): return (x * 60) + y

    race_times = get_rhines_times()
    total_time = 0.0

    for time in race_times:
        minutes, seconds = time.split(':')
        total_time += total_seconds(int(minutes), float(seconds))

    average_seconds = total_time / len(race_times)
    return_minutes = math.floor(average_seconds / 60)
    return_seconds = (average_seconds % 60)
    return f"{return_minutes}:{return_seconds:.1f}"
