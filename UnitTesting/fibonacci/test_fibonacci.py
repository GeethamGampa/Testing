import unittest
from fibonacci import fibonacci_calc

class TestFibonacci(unittest.TestCase):

    def test_fibonacci_values(self):
        self.assertEqual(fibonacci_calc(0), 0)
        self.assertEqual(fibonacci_calc(1), 1)
        self.assertEqual(fibonacci_calc(5), 5)
        self.assertNotEqual(fibonacci_calc(6), 10)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            fibonacci_calc(4.5)
        with self.assertRaises(TypeError):
            fibonacci_calc("eight")

    def test_value_error(self):
        with self.assertRaises(ValueError):
            fibonacci_calc(-3)

if __name__ == '__main__':
    unittest.main()
