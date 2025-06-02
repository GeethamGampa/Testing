# test_max_of_two.py

import pytest
from max_of_two import max_num

def test_max_normal():
    assert max_num(10, 5) == 10

def test_max_reversed():
    assert max_num(3, 9) == 9

def test_max_equal():
    assert max_num(7, 7) == 7

def test_type_error():
    with pytest.raises(TypeError):
        max_num(10, "twenty")

def test_not_equal():
    assert max_num(4, 8) != 4
