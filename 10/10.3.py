#!/usr/bin/python3

"""
Exercise 10.3. Write a function called middle that takes a list and returns a new list that contains
all but the first and last elements. For example:
>>> t = [1, 2, 3, 4]
>>> middle(t)
[2, 3]
"""

def middle(t):
    """Returns alll but first and last elements of t.

    t: list

    returns: new list
    """
    return t[1:-1]
