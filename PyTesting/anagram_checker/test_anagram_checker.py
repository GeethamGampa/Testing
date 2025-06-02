import pytest
from anagram_checker import are_anagrams

def test_anagrams_true():
    assert are_anagrams("Listen", "Silent") is True

def test_anagrams_false():
    assert are_anagrams("Hello", "World") is False

def test_not_equal():
    assert are_anagrams("Hello", "World") != True

def test_type_error():
    with pytest.raises(TypeError):
        are_anagrams(123, "abc")
