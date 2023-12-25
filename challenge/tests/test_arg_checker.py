from challenge.arg_checker import arg_checker
import pytest

arg_checker(int, int, int)
def adder(a, b, c):
    '''Returns the sum of the arguments'''
    return a + b + c

def test_correct_args():
    assert adder(1, 2, 3) == 6

def test_incorrect_number_of_args():
    with pytest.raises(TypeError):
        adder(1, 2)
        adder(1, 2, 3, 4)

def test_type_of_args():
    with pytest.raises(TypeError): 
        adder('1', 2, 3)
        adder(1, 2.0, 3)
        adder(1, 2, '3')

def test_decorated_function():
    assert adder.__name__ == 'adder'
    assert adder.__doc__ == 'Returns the sum of the arguments'
