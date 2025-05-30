import unittest
from reverse_string import reverse_str

class TestReverseString(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(reverse_str("hello"), "olleh")
        self.assertNotEqual(reverse_str("world"), "world")

    def test_type_error(self):
        with self.assertRaises(TypeError):
            reverse_str(123)

if __name__ == '__main__':
    unittest.main()
