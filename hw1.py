import data
import math
# Write your functions for each part in the space below.

# Part 1
"""Design Recipe: 
Purpose: 
Count the number of vowels in a given string.

Input: 
- string: A string in which to count vowels.

Output: 
- Returns the total count of vowels (int).

Representation: 
- A string consisting of characters (both uppercase and lowercase).
"""
def vowel_count(string: str) -> int:
    vowels = 'aeiouAEIOU'
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

# Part 2
"""Design Recipe: 
Purpose: 
Filter out sublists that have exactly two elements from a list of lists.

Input: 
- list: A list of lists of integers.

Output: 
- Returns a list of lists, each containing exactly two integers.

Representation: 
- A list of sublists where each sublist is a list of integers.
"""
def short_lists(list: list[list[int]]) -> list[list[int]]:
    return [sublist for sublist in list if len(sublist) == 2]

# Part 3
"""Design Recipe: 
Purpose: 
Sort pairs of integers within a list of lists, while leaving other sublists unchanged.

Input: 
- input_list: A list of lists of integers.

Output: 
- Returns a list of lists with each pair sorted.

Representation: 
- A list of lists where each sublist may contain two or more integers.
"""
def ascending_pairs(input_list: list[list[int]]) -> list[list[int]]:
    result = []
    for sublist in input_list:
        if len(sublist) == 2:
            result.append(sorted(sublist))
        else:
            result.append(sublist)
    return result

# Part 4
"""Design Recipe: 
Purpose: 
Add two Price objects together and return a new Price object.

Input: 
- price1: A Price object.
- price2: A Price object.

Output: 
- Returns a new Price object representing the total.

Representation: 
- Price: An object with dollars (int) and cents (int).
"""
def add_prices(price1: data.Price, price2: data.Price) -> data.Price:
    total_cents = price1.dollars * 100 + price1.cents + price2.dollars * 100 + price2.cents
    dollars = total_cents // 100
    cents = total_cents % 100
    return data.Price(dollars, cents)


# Part 5
"""Design Recipe: 
Purpose: 
Calculate the area of a rectangle.

Input: 
- rectangle: A Rectangle object defined by top-left and bottom-right points.

Output: 
- Returns the area of the rectangle (float).

Representation: 
- Rectangle: An object with top_left (Point) and bottom_right (Point).
"""
def rectangle_area(rectangle: data.Rectangle) -> float:
    x1, y1 = rectangle.top_left
    x2, y2 = rectangle.bottom_right
    width = x2 - x1
    height = y2 - y1
    area = width * height
    return abs(area)


# Part 6
"""Design Recipe: 
Purpose: 
Find all books by a specified author from a list of books.

Input: 
- author_name: A string representing the author's name.
- books: A list of Book objects.

Output: 
- Returns a list of Book objects written by the specified author.

Representation: 
- Book: An object containing authors (list of strings) and title (string).
"""
from data import Book
def books_by_author(author_name: str, books: list[Book]) -> list[Book]:
    return [book for book in books if author_name in book.authors]



# Part 7
"""Design Recipe: 
Purpose: 
Create a circle that bounds a given rectangle.

Input: 
- rectangle: A Rectangle object.

Output: 
- Returns a Circle object that bounds the rectangle.

Representation: 
- Circle: An object with center (Point) and radius (float).
"""
def circle_bound(rectangle: data.Rectangle) -> data.Circle:
    center = rectangle.center()
    radius = math.sqrt(
        (rectangle.top_left.x - rectangle.bottom_right.x) ** 2 +
        (rectangle.top_left.y - rectangle.bottom_right.y) ** 2
    ) / 2
    return data.Circle(center, radius)

# Part 8
"""Design Recipe: 
Purpose: 
Identify employees whose pay is below the average pay.

Input: 
- employees: A list of Employee objects.

Output: 
- Returns a list of names (strings) of employees with pay below average.

Representation: 
- Employee: An object with name (string) and pay_rate (float).
"""
def below_pay_average(employees: list[data.Employee]) -> list[str]:
    if not employees:
        return []

    total_pay = sum(employee.pay_rate for employee in employees)  
    average_pay = total_pay / len(employees)

    below_average_names = [employee.name for employee in employees if employee.pay_rate < average_pay] 

    return below_average_names
