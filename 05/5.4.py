#!/usr/bin/python3

"""
Exercise 5-4
What is the output of the following program? Draw a stack diagram that shows the state of the program when it prints the result.
"""
def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

recurse(3, 0)

# ANSWER
# it will print sum of series 3, 2, 1
# result = n + (n-1) + (n-2) + ... + 2 + 1

"""
1. What would happen if you called this function like this: recurse(-1, 0)?
"""
# ANSWER
# as this function's base case checks only for 0 value and call itself
# recursively with decreasing its value so when we start this function
# with a value that already less than 0 but not equal to 0 this recursive
# function call itself infinitely.

"""
2. Write a docstring that explains everything someone would need to know in order to use this function (and nothing else).
"""

def recurse_with_docs(n, s):
    """
    sum of Natural number series from 1 to n (inclusive) and a starting
    number 's'
    n : any positive integer
    s : any number
    """
    if n == 0:
        print(s)
    else:
        recurse_with_docs(n-1, n+s)
