import unittest
from prime_check import is_prime

class TestIsPrime(unittest.TestCase):

    def test_prime_numbers(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(13))
        self.assertNotEqual(is_prime(4), True)

    def test_non_prime_numbers(self):
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(-7))
        self.assertFalse(is_prime(9))

    def test_type_error(self):
        with self.assertRaises(TypeError):
            is_prime(5.5)
        with self.assertRaises(TypeError):
            is_prime("seven")

if __name__ == '__main__':
    unittest.main()
