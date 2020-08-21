#Test cases for calculator app
from main import add, subtract, multiply, division, exponent
import pytest

@pytest.mark.parametrize('test_input_1,test_input_2, expected', [
    (10,10, '10+10 = 20'),
    (10,-10, '10+-10 = 0'),
    (-10,-10, '-10+-10 = -20'),
    ])
def test_add(test_input_1, test_input_2, expected):
    assert add(test_input_1, test_input_2) == expected

def test_subtract():
    result = subtract(20,30)
    expected = '20-30 = -10'
    assert result == expected

def test_multiply():
    result = multiply(-1.1, 4)
    expected = '-1.1*4 = -4.4'
    assert result == expected

@pytest.mark.parametrize('input_1, input_2, expected', 
[(10, 15, '10/15 = 0.6667'),
 #pytest.param(10,0, marks=pytest.raises(Exception, match='Error: DIV ERROR'))   
])
def test_division(input_1,input_2,expected):
    assert division(input_1,input_2) == expected

def test_exponent():
    assert exponent(3,2) == '3 ** 2 = 9'
