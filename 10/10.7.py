#!/usr/bin/python3

"""
Exercise 10.7. Write a function called has_duplicates that takes a list and returns True if there
is any element that appears more than once. It should not modify the original list.
"""
def has_duplicates(s):
    """Returns True if any element appears more than once in a sequence.
    s: string or list
    returns: bool
    """
    # make a copy of t to avoid modifying the parameter
    t = list(s)
    t.sort()

    # check for adjacent elements that are equal
    for i in range(len(t)-1):
        if t[i] == t[i+1]:
            return True
    return False
