import unittest
from count_words import count_words_in_sentence

class TestCountWords(unittest.TestCase):

    def test_word_count(self):
        self.assertEqual(count_words_in_sentence("Hello world"), 2)
        self.assertEqual(count_words_in_sentence("This is a test case"), 5)
        self.assertNotEqual(count_words_in_sentence("One two three"), 5)

    def test_empty_string(self):
        self.assertEqual(count_words_in_sentence(""), 0)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            count_words_in_sentence(123)
        with self.assertRaises(TypeError):
            count_words_in_sentence(["list", "of", "words"])

if __name__ == '__main__':
    unittest.main()
