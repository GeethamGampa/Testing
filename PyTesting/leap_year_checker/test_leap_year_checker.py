# test_leap_year_checker.py

import pytest
from leap_year_checker import leap_check

def test_leap_true():
    assert leap_check(2020) is True

def test_leap_false():
    assert leap_check(2019) is False

def test_century_non_leap():
    assert leap_check(1900) is False

def test_century_leap():
    assert leap_check(2000) is True

def test_type_error():
    with pytest.raises(TypeError):
        leap_check("two thousand")

def test_value_error():
    with pytest.raises(ValueError):
        leap_check(-400)
