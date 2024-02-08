import pytest 

def capital_case(x):  
    if not isinstance(x, str):  
        raise TypeError('Debes de proporcionar un string')         
    return x.capitalize()  

def test_capital_case():  
    assert capital_case('semáforo') == 'Semáforo' 

def test_raise_exception_on_non_string_argument():
    with  pytest.raises(TypeError):  
        capital_case(9)