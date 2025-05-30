import unittest
from string_repeater import repeat_string

class TestRepeatString(unittest.TestCase):
    def test_repeat(self):
        self.assertEqual(repeat_string("abc", 3), "abcabcabc")
        self.assertNotEqual(repeat_string("abc", 2), "abcabcabc")

    def test_empty_repeat(self):
        self.assertEqual(repeat_string("test", 0), "")

    def test_type_error(self):
        with self.assertRaises(TypeError):
            repeat_string(123, 3)
        with self.assertRaises(TypeError):
            repeat_string("abc", "3")

    def test_value_error(self):
        with self.assertRaises(ValueError):
            repeat_string("abc", -1)

if __name__ == '__main__':
    unittest.main()
