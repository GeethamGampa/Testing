import unittest
from age_check import is_adult

class TestAgeCheck(unittest.TestCase):
    def test_adult_true(self):
        self.assertTrue(is_adult(20))

    def test_adult_false(self):
        self.assertFalse(is_adult(16))

    def test_not_equal(self):
        self.assertNotEqual(is_adult(16), True)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            is_adult("twenty")

if __name__ == '__main__':
    unittest.main()
