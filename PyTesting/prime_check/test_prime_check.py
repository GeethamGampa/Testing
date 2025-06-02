# test_prime_check.py

import pytest
from prime_check import check_prime

def test_prime_true():
    assert check_prime(7) is True

def test_prime_false():
    assert check_prime(8) is False

def test_prime_edge_case():
    assert check_prime(1) is False

def test_prime_zero():
    assert check_prime(0) is False

def test_type_error():
    with pytest.raises(TypeError):
        check_prime("seven")
