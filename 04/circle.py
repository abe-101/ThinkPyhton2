#!/usr/bin/python3

import turtle
import math

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)

bob = turtle.Turtle()
print(bob)
circle(bob, 100)
turtle.mainloop()
