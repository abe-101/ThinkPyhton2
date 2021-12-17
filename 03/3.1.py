#!/usr/bin/python3

def right_justify(s):
    width = 70
    spaces = width - len(s)
    print(f"{' '*spaces}{s}")

right_justify('hello')
