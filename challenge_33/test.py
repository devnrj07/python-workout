from main import make_deposit, make_withdrawl
import pytest



def test_make_deposit():
    temp_dict = {
        "savings" : 12.90,
        "checking" : 90.278
    }

    make_deposit(temp_dict,'savings', 10.90)
    make_deposit(temp_dict, 'checking', 10.000)

    assert temp_dict == {
        "savings" : 23.80,
        "checking" : 100.278
    }

def test_make_withdrawl():
    temp_dict = {
        "savings" : 12.90,
        "checking" : 90.278
    }

    make_withdrawl(temp_dict,'savings', 10.90)
    make_withdrawl(temp_dict, 'checking', 10.000)

    assert temp_dict == {
        "savings" : 02.00,
        "checking" : 80.278
    }