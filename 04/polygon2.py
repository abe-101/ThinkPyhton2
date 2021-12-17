#!/usr/bin/python3

import turtle

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

bob = turtle.Turtle()
print(bob)
polygon(bob, 7, 70)
turtle.mainloop()
