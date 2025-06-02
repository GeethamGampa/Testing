# test_safe_divide.py

import pytest
from safe_divide import safe_division

def test_divide_normal():
    assert safe_division(10, 2) == 5

def test_divide_negative():
    assert safe_division(-10, 2) == -5

def test_divide_float():
    assert safe_division(5.5, 2) == 2.75

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
       safe_division(5, 0)

def test_type_error():
    with pytest.raises(TypeError):
      safe_division("ten", 2)
