#!/usr/bin/python3

"""
Exercise 10.4. Write a function called chop that takes a list, modifies it by removing the first and
last elements, and returns None. For example:
>>> t = [1, 2, 3, 4]
>>> chop(t)
>>> t
[2, 3]
"""
def chop(t):
    """Removes the first and last elements of t.

    t: list
    
    returns: None
    """
    
    del t[0]
    del t[-1]
