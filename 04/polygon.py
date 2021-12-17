#!/usr/bin/python3

import turtle

def square(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
bob = turtle.Turtle()
print(bob)
square(bob, 100, 10)
turtle.mainloop()
