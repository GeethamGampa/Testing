import unittest
from is_even import is_even_num

class TestIsEven(unittest.TestCase):
    def test_even_true(self):
        self.assertTrue(is_even_num(4))
        self.assertNotEqual(is_even_num(4), False)

    def test_even_false(self):
        self.assertFalse(is_even_num(3))
        self.assertNotEqual(is_even_num(3), True)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            is_even_num(2.5)

if __name__ == '__main__':
    unittest.main()
