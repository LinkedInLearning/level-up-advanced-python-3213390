# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians
# Assume a year has 365.25 days

def get_data():
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.read()
    return content

def get_event_time(line):
    """Given a line with Jennifer Rhines' race times from 10k_racetimes.txt, 
       parse it and return a tuple of (age at event, race time).
       Assume a year has 365.25 days"""
    pass
    
def get_age_slowest_times():
    '''Return a tuple (age, race_time) where:
       age: AyBd is in this format where A and B are integers'''
    races = get_data()
