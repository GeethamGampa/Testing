import pytest
from count_vowels import count_vowels_in_string

def test_count_vowels_basic():
    assert count_vowels_in_string("hello") == 2

def test_count_vowels_empty():
    assert count_vowels_in_string("") == 0

def test_count_vowels_mixed_case():
    assert count_vowels_in_string("AEiou") == 5

def test_type_error():
    with pytest.raises(TypeError):
       count_vowels_in_string(123)

def test_not_equal():
    assert count_vowels_in_string("hello") != 3
