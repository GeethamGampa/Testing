import unittest
from safe_divide import safe_division

class TestSafeDivide(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(safe_division(10, 2), 5)
        self.assertNotEqual(safe_division(10, 2), 4)

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            safe_division(5, 0)

if __name__ == '__main__':
    unittest.main()
