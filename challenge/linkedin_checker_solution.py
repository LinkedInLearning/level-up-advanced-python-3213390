from collections import namedtuple
import re

with open('specifications.txt', 'rt') as file:
    specifications = file.read()

specs = namedtuple('specs', 'range regex')
#specs range builtin module
#specs regex from re.compile

def get_linkedin_dict():
    '''Convert specifications into a dict:
       keys:  feature
       values: specs namedtuple'''
    data = {}
    minimum, maximum = 0, 0
    regex = ''
    for line in specifications.splitlines():
        if line:
            if 'requirements' in line:
                minimum, maximum = re.findall(r'\d+', line)
                minimum = int(minimum)
                maximum = int(maximum)
            elif 'permitted characters' in line:
                regex = ''.join(line.split()[2:])
                regex = re.compile(rf'^[{regex}]+$')
            elif 'login characters' in line:
                regex = ''.join(line.split()[2:])
                regex = regex[::-1]
                regex = regex.replace('.', '.\\', 1).replace('-', '-\\', 1)
                regex = regex[::-1]
                regex = re.compile(rf'^[{regex}]+@[{regex}]+.com|net|org$')      
            else:
                feature = line.split()[-1]
            data[feature] = specs(range(minimum, maximum + 1), regex)    
    return data

def check_linkedin_feature(feature_text, url_or_login):
    '''Raise a ValueError if the url_or_login isn't login or custom_url
       If feature_text is valid, return True otherwise return False'''
    data = get_linkedin_dict()
    result = data.get(url_or_login, None)
    if result is None:
        raise ValueError('Feature needs to be either login or custom_url')
    else:
        length = len(feature_text) in data[url_or_login].range
        regex = bool(data[url_or_login].regex.search(feature_text))
        return length & regex

