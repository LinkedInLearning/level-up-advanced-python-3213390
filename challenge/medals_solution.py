from collections import namedtuple

with open('olympics.txt', 'rt', encoding='utf-8') as file:    
    olympics = file.read()

medal = namedtuple('medal', ['City', 'Edition', 'Sport', 'Discipline', 'Athlete', 'NOC', 'Gender',
       'Event', 'Event_gender', 'Medal'])

medals = [medal(*line.split(';')) for line in olympics.splitlines()[1:]]

def get_medals(**kwargs):
    '''Return a list of medal namedtuples '''
    return [medal 
            for medal in medals 
            if all(getattr(medal, key) == value 
            for key,value in kwargs.items())]