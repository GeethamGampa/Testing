import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertNotEqual(add(2, 3), 6)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertNotEqual(subtract(5, 2), 1)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertNotEqual(multiply(3, 4), 10)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertNotEqual(divide(10, 2), 4)
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

if __name__ == '__main__':
    unittest.main()
