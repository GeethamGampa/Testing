# test_reverse_string.py

import pytest
from reverse_string import rev_str

def test_reverse_normal():
    assert rev_str("hello") == "olleh"

def test_reverse_empty():
    assert rev_str("") == ""

def test_reverse_palindrome():
    assert rev_str("madam") == "madam"

def test_reverse_single_char():
    assert rev_str("a") == "a"

def test_type_error():
    with pytest.raises(TypeError):
        rev_str(123)
