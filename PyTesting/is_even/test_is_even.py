# test_is_even.py

import pytest
from is_even import is_even_num

def test_even_true():
    assert is_even_num(4) is True

def test_even_false():
    assert is_even_num(5) is False

def test_zero():
    assert is_even_num(0) is True

def test_type_error():
    with pytest.raises(TypeError):
        is_even_num("ten")

def test_not_equal():
    assert is_even_num(3) != True
