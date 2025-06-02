import pytest
from count_words import count_words_in_sentence

def test_count_words_basic():
    assert count_words_in_sentence("Hello world") == 2

def test_count_words_empty():
    assert count_words_in_sentence("") == 0

def test_type_error():
    with pytest.raises(TypeError):
        count_words_in_sentence(123)

def test_not_equal():
    assert count_words_in_sentence("Hello world") != 3
