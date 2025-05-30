import unittest
from max_of_two import max_of_two_num

class TestMaxOfTwo(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max_of_two_num(10, 20), 20)
        self.assertEqual(max_of_two_num(5, 5), 5)
        self.assertNotEqual(max_of_two_num(10, 20), 10)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            max_of_two_num(10, "twenty")

if __name__ == '__main__':
    unittest.main()
