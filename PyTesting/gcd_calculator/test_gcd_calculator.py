# test_gcd_calculator.py

import pytest
from gcd_calculator import gcd

def test_gcd_basic():
    assert gcd(48, 18) == 6

def test_gcd_negative():
    assert gcd(-48, 18) == 6

def test_gcd_zero():
    assert gcd(0, 5) == 5
    assert gcd(5, 0) == 5

def test_type_error():
    with pytest.raises(TypeError):
        gcd(10, "20")

def test_not_equal():
    assert gcd(12, 8) != 3
