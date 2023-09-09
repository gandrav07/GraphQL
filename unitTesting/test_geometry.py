import unittest
from geometry import rectangle_area,square_area

class TestRectangleArea(unittest.TestCase):
    def test_positive_area(self):
        result = rectangle_area(5,10)
        result2 = square_area(2)
        self.assertEqual(result, 50)
        self.assertEqual(result2, 4)

    def test_zero_length(self):
        with self.assertRaises(ValueError):
            rectangle_area(0,10)
            square_area(0)

    def test_negative_width(self):
        with self.assertRaises(ValueError):
            square_area(-2)
            rectangle_area(5, -10)
            square_area(-2)

    # def test_positive_area(self):
    #     result = rectangle_area(5,10)
    #     self.assertEqual(result, 50)



if __name__ == '__main__':
    unittest.main()