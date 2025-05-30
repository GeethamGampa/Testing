import unittest
from leap_year_checker import is_leap_year

class TestLeapYearChecker(unittest.TestCase):
    def test_leap_year_true(self):
        self.assertTrue(is_leap_year(2020))
        self.assertTrue(is_leap_year(2000))
        self.assertNotEqual(is_leap_year(2024), False)

    def test_leap_year_false(self):
        self.assertFalse(is_leap_year(2019))
        self.assertFalse(is_leap_year(1900))
        self.assertNotEqual(is_leap_year(2018), True)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            is_leap_year("two thousand")

    def test_value_error(self):
        with self.assertRaises(ValueError):
            is_leap_year(-400)

if __name__ == '__main__':
    unittest.main()
