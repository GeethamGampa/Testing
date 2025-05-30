import unittest
from count_vowels import count_vowels_in_string

class TestCountVowels(unittest.TestCase):

    def test_count_vowels(self):
        self.assertEqual(count_vowels_in_string("hello"), 2)
        self.assertEqual(count_vowels_in_string("HELLO"), 2)
        self.assertEqual(count_vowels_in_string("xyz"), 0)
        self.assertNotEqual(count_vowels_in_string("world"), 3)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            count_vowels_in_string(123)
        with self.assertRaises(TypeError):
            count_vowels_in_string(['a', 'e'])

if __name__ == '__main__':
    unittest.main()
