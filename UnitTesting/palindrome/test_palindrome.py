import unittest
from palindrome import is_palindrome

class TestIsPalindrome(unittest.TestCase):

    def test_true_palindromes(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("Racecar"))
        self.assertTrue(is_palindrome("nurses run"))

    def test_false_palindromes(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("python"))

    def test_assert_not_equal(self):
        self.assertNotEqual(is_palindrome("world"), True)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            is_palindrome(12321)

if __name__ == '__main__':
    unittest.main()
