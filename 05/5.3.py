#!/usr/bin/python3

"""
Exercise 5.3. If you are given three sticks, you may or may not be able to arrange them in a triangle. For example, if one of the sticks is 12 inches long and the other two are one inch long, you will not be able to get the short sticks to meet in the middle. For any three lengths, there is a simple test to see if it is possible to form a triangle:
    If any of the three lengths is greater than the sum of the other two, then you cannot form a triangle. Otherwise, you can. (If the sum of two lengths equals the third, they form what is called a “degenerate” triangle.)

    1. Write a function named is_triangle that takes three integers as arguments, and that prints either “Yes” or “No”, depending on whether you can or cannot form a triangle from sticks with the given lengths.
    2. Write a function that prompts the user to input three stick lengths, converts them to integers, and uses is_triangle to check whether sticks with the given lengths can form a triangle.
"""

def is_triangle(side1, side2, side3):
    if side1 > side2 + side3:
        print('No')
    elif side2 > side1 + side3:
        print('No')
    elif side3 > side1 + side2:
        print('No')
    else:
        print('Yes')

def get_length():
    side1 = int(input('Side 1: '))
    side2 = int(input('Side 2: '))
    side3 = int(input('Side 3: '))
    is_triangle(side1, side2, side3)

get_length()

