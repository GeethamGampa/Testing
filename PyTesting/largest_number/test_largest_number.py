# test_largest_number.py

import pytest
from largest_number import find_largest

def test_largest_normal():
    assert find_largest(3, 5, 2) == 5

def test_largest_negative():
    assert find_largest(-3, -5, -2) == -2

def test_largest_equal():
    assert find_largest(4, 4, 4) == 4

def test_type_error():
    with pytest.raises(TypeError):
        find_largest(4, "five", 6)

def test_not_equal():
    assert find_largest(1, 7, 3) != 3
