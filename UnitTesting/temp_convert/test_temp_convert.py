import unittest
from temp_convert import celsius_to_fahrenheit

class TestTempConvert(unittest.TestCase):
    def test_conversion(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32)
        self.assertEqual(celsius_to_fahrenheit(100), 212)
        self.assertNotEqual(celsius_to_fahrenheit(20), 50)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            celsius_to_fahrenheit("thirty")

if __name__ == '__main__':
    unittest.main()
