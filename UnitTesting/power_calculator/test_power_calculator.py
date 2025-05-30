import unittest
from power_calculator import power

class TestPowerCalculator(unittest.TestCase):
    def test_power_values(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertNotEqual(power(3, 2), 8)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            power("2", 3)
        with self.assertRaises(TypeError):
            power(2, 2.5)

if __name__ == '__main__':
    unittest.main()
