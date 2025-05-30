import unittest
from anagram_checker import are_anagrams

class TestAnagramChecker(unittest.TestCase):
    
    def test_anagrams_true(self):
        self.assertTrue(are_anagrams("Listen", "Silent"))
        self.assertTrue(are_anagrams("Astronomer", "Moon starer"))
    
    def test_anagrams_false(self):
        self.assertFalse(are_anagrams("Hello", "World"))
        self.assertNotEqual(are_anagrams("Test", "Best"), True)
    
    def test_type_error(self):
        with self.assertRaises(TypeError):
            are_anagrams(123, "abc")
        with self.assertRaises(TypeError):
            are_anagrams("abc", None)

if __name__ == '__main__':
    unittest.main()
