import data
import hw1
import unittest
import math
from data import Book, Point, Rectangle

# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_1(self):
        x= "Hi, How are you."
        result = hw1.vowel_count(x)
        expected = 6
        self.assertEqual(result,expected)

    def test_vowel_2(self):
        x = "I am doing well. What are your plans today"
        result = hw1.vowel_count(x)
        expected = 13
        self.assertEqual(result, expected)

    # Part 2
    def test_short_lists1(self):
        x = [[1, 2], [3, 4, 5], [6], [7, 8], [9, 10, 11]]
        result = hw1.short_lists(x)
        expected = [[1, 2], [7, 8]]
        self.assertEqual(result, expected)

    def test_short_lists2(self):
        x = [[1, 2, 6], [3, 4, 5,7], [6], [7, 8], [9, 10]]
        result = hw1.short_lists(x)
        expected = [[7, 8],[9,10]]
        self.assertEqual(result, expected)


    # Part 3
    def test_ascending_pairs_case_1(self):
        x = [[3, 1], [5, 2], [4], [7, 8]]
        result = hw1.ascending_pairs(x)
        expected = [[1, 3], [2, 5], [4], [7, 8]]
        self.assertEqual(result, expected)

    def test_ascending_pairs_case_2(self):
        x = [[9, 7], [6], [4, 5], [10, 10]]
        result = hw1.ascending_pairs(x)
        expected = [[7, 9], [6], [4, 5], [10, 10]]
        self.assertEqual(result, expected)

    # Part 4
    def test_add_prices1(self):
        price1 = data.Price(1, 50)
        price2 = data.Price(2, 75)
        result = hw1.add_prices(price1, price2)
        expected = data.Price(4, 25)
        self.assertEqual(result.dollars, expected.dollars)
        self.assertEqual(result.cents, expected.cents)

    def test_add_prices2(self):
        price1 = data.Price(0, 99)
        price2 = data.Price(1, 1)
        result = hw1.add_prices(price1, price2)
        expected = data.Price(2, 0)
        self.assertEqual(result.dollars, expected.dollars)
        self.assertEqual(result.cents, expected.cents)

    # Part 5
    def test_rectangle_area1(self):
        rectangle = data.Rectangle(top_left=(1, 2), bottom_right=(4, 5))
        expected_area = 9
        self.assertEqual(hw1.rectangle_area(rectangle), expected_area)

    def test_rectangle_area2(self):
        rectangle = data.Rectangle(top_left=(0,0), bottom_right=(5,-9))
        expected_area = 45
        self.assertEqual(hw1.rectangle_area(rectangle), expected_area)

    # Part 6

    from data import Book
    def test_books_by_author1(self):
        books = [
            Book(["JK Rowling"], 'Harry Potter 1'),
            Book(['JK Rowling'], 'Harry Potter 2'),
            Book(['Stephen King'], 'It'),
            Book(['Jesus'], 'The Bible')
            ]

        result = hw1.books_by_author('JK Rowling', books)
        expected = [
            Book(['JK Rowling'], 'Harry Potter 1'),
            Book(['JK Rowling'], 'Harry Potter 2')
            ]

        self.assertEqual(result, expected)

    def test_books_by_author2(self):
        books = [
            Book(["JK Rowling"], 'Harry Potter 1'),
            Book(['JK Rowling'], 'Harry Potter 2'),
            Book(['Stephen King'], 'It'),
            Book(['Jesus'], 'The Bible')
        ]

        result = hw1.books_by_author('Stephen King', books)
        expected = [
            Book(['Stephen King'], 'It'),
        ]

        self.assertEqual(result, expected)


    # Part 7
    def test_circle_bound_square(self):
        rectangle = Rectangle(Point(0, 0), Point(3, 8))
        circle = hw1.circle_bound(rectangle)

        expected_center = Point(1.5, 4)
        expected_radius = math.sqrt(18.25)

        self.assertEqual(circle.center, expected_center)
        self.assertAlmostEqual(circle.radius, expected_radius)

    def test_circle_bound_square(self):
        rectangle = Rectangle(Point(0, 0), Point(2, 2))
        circle = hw1.circle_bound(rectangle)
        expected_center = Point(1, 1)
        expected_radius = math.sqrt(2)
        self.assertEqual(circle.center, expected_center)
        self.assertAlmostEqual(circle.radius, expected_radius)

    # Part 8
    def test_below_pay_average_no_employees(self):
        employees = []
        result = hw1.below_pay_average(employees)
        expected = []
        self.assertEqual(result, expected)

    def test_below_pay_average_some_employees(self):
        employees = [
            data.Employee('Alice', 50),
            data.Employee('Bob', 40),
            data.Employee('Charlie', 30)
        ]
        result = hw1.below_pay_average(employees)
        expected = ['Charlie']
        self.assertEqual(result, expected)




if __name__ == '__main__':
    unittest.main()
