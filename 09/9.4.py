#!/usr/bin/python3

"""
Exercise 9.4. Write a function named uses_only that takes a word and a string of letters, and
that returns True if the word contains only letters in the list. Can you make a sentence using only
the letters acefhlo? Other than “Hoe alfalfa”?
"""
def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True

available = input('Enter available letters: ')
fin = open('words.txt')
for line in fin:
    if uses_only(line, available):
        print(line)
