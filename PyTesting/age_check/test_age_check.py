import pytest
from age_check import is_adult

def test_adult_true():
    assert is_adult(20) is True

def test_adult_false():
    assert is_adult(16) is False

def test_not_equal():
    assert is_adult(16) != True

def test_type_error():
    with pytest.raises(TypeError):
        is_adult("twenty")
