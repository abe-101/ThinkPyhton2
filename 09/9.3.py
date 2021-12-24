#!/usr/bin/python3

"""
Exercise 9.3. Write a function named avoids that takes a word and a string of forbidden letters,
and that returns True if the word doesn’t use any of the forbidden letters.
Write a program that prompts the user to enter a string of forbidden letters and then prints the
number of words that don’t contain any of them. Can you find a combination of 5 forbidden letters
that excludes the smallest number of words?
"""
def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True

forbidden = input('Enter forbidden letters: ')
clean = 0
fin = open('words.txt')
for line in fin:
    if avoids(line, forbidden):
        clean = clean + 1
print(clean)
