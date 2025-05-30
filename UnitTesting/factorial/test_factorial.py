import unittest
from factorial import factorial_calc

class TestFactorialCalc(unittest.TestCase):
    def test_factorial_values(self):
        self.assertEqual(factorial_calc(0), 1)
        self.assertEqual(factorial_calc(1), 1)
        self.assertEqual(factorial_calc(5), 120)
        self.assertNotEqual(factorial_calc(4), 20)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            factorial_calc(5.5)

    def test_value_error(self):
        with self.assertRaises(ValueError):
            factorial_calc(-1)

if __name__ == '__main__':
    unittest.main()
