import pytest
from factorial import factorial_calc

def test_factorial_zero():
    assert factorial_calc(0) == 1

def test_factorial_positive():
    assert factorial_calc(5) == 120

def test_factorial_one():
    assert factorial_calc(1) == 1

def test_type_error():
    with pytest.raises(TypeError):
        factorial_calc("five")

def test_value_error():
    with pytest.raises(ValueError):
        factorial_calc(-3)

def test_not_equal():
    assert factorial_calc(4) != 23
