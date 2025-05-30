import unittest
from largest_number import find_largest

class TestFindLargest(unittest.TestCase):
    def test_largest_number(self):
        self.assertEqual(find_largest([1, 5, 3, 9, 2]), 9)
        self.assertEqual(find_largest([-10, -3, -1]), -1)
        self.assertNotEqual(find_largest([4, 7, 2]), 4)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            find_largest("12345")
        with self.assertRaises(TypeError):
            find_largest([1, "two", 3])

    def test_value_error(self):
        with self.assertRaises(ValueError):
            find_largest([])

if __name__ == '__main__':
    unittest.main()
