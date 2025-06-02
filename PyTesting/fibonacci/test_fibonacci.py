# test_fibonacci.py

import pytest
from fibonacci import fibonacci_calc

def test_fibonacci_zero():
    assert fibonacci_calc(0) == 0

def test_fibonacci_one():
    assert fibonacci_calc(1) == 1

def test_fibonacci_positive():
    assert fibonacci_calc(7) == 13

def test_type_error():
    with pytest.raises(TypeError):
        fibonacci_calc("seven")

def test_value_error():
    with pytest.raises(ValueError):
        fibonacci_calc(-2)

def test_not_equal():
    assert fibonacci_calc(5) != 10
