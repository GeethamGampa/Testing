# test_string_repeater.py

import pytest
from string_repeater import repeater

def test_repeat_once():
    assert repeater("hi", 1) == "hi"

def test_repeat_multiple():
    assert repeater("abc", 3) == "abcabcabc"

def test_repeat_zero():
    assert repeater("test", 0) == ""

def test_type_error_string():
    with pytest.raises(TypeError):
        repeater(123, 2)

def test_type_error_times():
    with pytest.raises(TypeError):
        repeater("hello", "2")

def test_value_error_negative():
    with pytest.raises(ValueError):
        repeater("fail", -1)
