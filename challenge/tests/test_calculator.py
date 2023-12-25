import pytest
from challenge.calculator import Calculator

def test_no_error():
    with Calculator(TypeError, ValueError, NameError, ZeroDivisionError) as c:
        print(1 * 2)    
        print(2 / 3)
        print(3 + 4)
    assert c.error == None

def test_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        with Calculator(TypeError, ValueError, NameError, ZeroDivisionError) as c:
            print(1 * 2)    
            print(2 / 0)
            print(3 + 4)
        raise c.error

def test_type_error():
    with pytest.raises(TypeError):
        with Calculator(TypeError, ValueError, NameError, ZeroDivisionError) as c:
            print(1 * 2)    
            print(2 + '2')
            print(3 + 4)
        raise c.error

def test_value_error():
    with pytest.raises(ValueError):
        with Calculator(TypeError, ValueError, NameError, ZeroDivisionError) as c:
            print(1 * 2)    
            print(2 + int('a'))
            print(3 + 4)
        raise c.error

def test_name_error():
    with pytest.raises(NameError):
        with Calculator(TypeError, ValueError, NameError, ZeroDivisionError) as c:
            print(1 * 2)    
            print(2 / num)
            print(3 + 4)
        raise c.error