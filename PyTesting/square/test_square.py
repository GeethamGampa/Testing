# test_square.py

import pytest
from square import square_num

def test_square_positive():
    assert square_num(4) == 16

def test_square_negative():
    assert square_num(-3) == 9

def test_square_zero():
    assert square_num(0) == 0

def test_square_float():
    assert square_num(2.5) == 6.25

def test_type_error():
    with pytest.raises(TypeError):
        square_num("four")
