import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(5, 3) == 8

def test_subtract():
    assert subtract(10, 4) == 6

def test_multiply():
    assert multiply(3, 7) == 21

def test_divide():
    assert divide(20, 4) == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

def test_not_equal():
    assert add(2, 2) != 5
