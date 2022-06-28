from collections import namedtuple

with open('olympics.txt', 'rt', encoding='utf-8') as file:    
    olympics = file.read()

medal = namedtuple('medal', ['City', 'Edition', 'Sport', 'Discipline', 'Athlete', 'NOC', 'Gender',
       'Event', 'Event_gender', 'Medal'])

medals = [] #Complete this - medals is a list of medal namedtuples

def get_medals(**kwargs):
    '''Return a list of medal namedtuples '''
    pass
