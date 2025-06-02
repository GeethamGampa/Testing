# test_palindrome.py

import pytest
from palindrome import check_palindrome

def test_palindrome_true():
    assert check_palindrome("Madam") is True

def test_palindrome_with_space():
    assert check_palindrome("nurses run") is True

def test_palindrome_false():
    assert check_palindrome("hello") is False

def test_not_equal():
    assert check_palindrome("world") != True

def test_type_error():
    with pytest.raises(TypeError):
        check_palindrome(12321)
