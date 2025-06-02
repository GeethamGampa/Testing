# test_power_calculator.py

import pytest
from power_calculator import power as calc_power

def test_power_positive():
    assert calc_power(2, 3) == 8

def test_power_zero_exponent():
    assert calc_power(5, 0) == 1

def test_power_zero_base():
    assert calc_power(0, 4) == 0

def test_power_float():
    assert calc_power(2.5, 2) == 6.25

def test_type_error():
    with pytest.raises(TypeError):
        calc_power("two", 3)
