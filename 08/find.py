#!/usr/bin/python3

""" Find.py takes a character and finds the index where that character
appears. If the character is not found, the function returns -1
"""

def find(word, letter, index):
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

print(find('hello', 'e', 0))
