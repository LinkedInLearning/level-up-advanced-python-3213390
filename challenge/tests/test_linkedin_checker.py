import pytest
from linkedin_checker import (get_linkedin_dict,
                                       check_linkedin_feature,
                                       specifications,
                                       specs)

def test_correct_custom_url():
    assert check_linkedin_feature('jonathanafernandes', 'custom_url')
    assert check_linkedin_feature('jonfernandes2000', 'custom_url')
    assert check_linkedin_feature('JonathanFernandes', 'custom_url')
    assert check_linkedin_feature('JonathanFernandes2000', 'custom_url')
    # atleast 3 characters
    assert check_linkedin_feature('jof', 'custom_url')
    # atmost 100 characters
    assert check_linkedin_feature('jonathanafernandes20' + '0' * 80, 'custom_url')

def test_incorrect_custom_url():
    assert check_linkedin_feature('jonathanafernande$', 'custom_url') == False
    assert check_linkedin_feature('jon-fernandes2000', 'custom_url') == False
    assert check_linkedin_feature('Jonathan_Fernandes', 'custom_url') == False
    assert check_linkedin_feature('JonathanFernandes2000!!', 'custom_url') == False
    # less than 3 characters
    assert check_linkedin_feature('jf', 'custom_url') == False
    # valid regex more than 100 characters
    assert check_linkedin_feature('jonathanafernandes20' + '0' * 81, 'custom_url') == False
    
def test_correct_email():
    assert check_linkedin_feature('jf@gmail.com', 'login')
    assert check_linkedin_feature('jonathanfernandes@gmail.com', 'login')
    assert check_linkedin_feature('jonathan-fernandes@gmail.com', 'login')
    assert check_linkedin_feature('jonathan_fernandes@gmail.com', 'login')
    assert check_linkedin_feature('jonathan.fernandes@gmail.com', 'login')
    # atmost 50 characters
    assert check_linkedin_feature(f'jonathanfernandes{"0" * 23}@gmail.com', 'login')

def test_incorrect_email():
    assert check_linkedin_feature('jonathangmail.com', 'login') == False
    assert check_linkedin_feature('jonathanfernandes@gmail.biz', 'login') == False
    assert check_linkedin_feature('jonathanfernandes@gmail.co.uk', 'login') == False
    # valid email regex but more than 50 characters
    assert check_linkedin_feature(f'jonathanfernandes{"0" * 24}@gmail.com', 'login') == False

def test_incorrect_feature():
    with pytest.raises(ValueError):
        assert check_linkedin_feature('jonathanafernandes', 'www')
        assert check_linkedin_feature('jonathanafernandes', 'webpage')
        assert check_linkedin_feature('jonathanafernandes', 'social')



