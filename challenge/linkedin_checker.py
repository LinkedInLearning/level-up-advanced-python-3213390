from collections import namedtuple
import re

with open('specifications.txt', 'rt') as file:
    specifications = file.read()

specs = namedtuple('specs', 'range regex')
#specs range builtin module
#specs regex from re.compile

def get_linkedin_dict():
    '''Convert specifications into a dict where:
       keys: feature
       values: specs namedtuple'''
    pass

def check_linkedin_feature(feature_text, url_or_login):
    '''Raise a ValueError if the url_or_login isn't login or custom_url
       If feature_text is valid, return True otherwise return False'''
    pass
