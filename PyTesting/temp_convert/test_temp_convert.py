# test_temp_convert.py

import pytest
from temp_convert import celsius_to_fahrenheit, fahrenheit_to_celsius

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212

def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100

def test_type_error_celsius():
    with pytest.raises(TypeError):
        celsius_to_fahrenheit("thirty")

def test_type_error_fahrenheit():
    with pytest.raises(TypeError):
        fahrenheit_to_celsius(None)
