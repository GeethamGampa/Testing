import unittest
from square import square_num

class TestSquare(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square_num(4), 16)
        self.assertNotEqual(square_num(5), 30)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            square_num("abc")

if __name__ == '__main__':
    unittest.main()
