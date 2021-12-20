#!/usr/bin/python3

# Chapter 7 Exercise 2 from the book:
#     
# Think Python, 2nd Edition
# by Allen Downey
# http://thinkpython2.com
#
# Write a function called eval_loop that iteratively
# prompts the user, takes the resulting input and evaluates
# it using eval, and prints the result. It should continue until the user enters 'done'.

def eval_loop():
    while True:
        response = input('Enter a equation, enter "done" to exit: ')
        if response == 'done':
            break
        print(eval(response))

eval_loop()
