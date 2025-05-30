import unittest
from gcd_calculator import gcd

class TestGCDCalculator(unittest.TestCase):
    def test_gcd_values(self):
        self.assertEqual(gcd(54, 24), 6)
        self.assertEqual(gcd(10, 5), 5)
        self.assertNotEqual(gcd(10, 4), 5)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            gcd(10.5, 5)
        with self.assertRaises(TypeError):
            gcd("10", 5)

if __name__ == '__main__':
    unittest.main()
