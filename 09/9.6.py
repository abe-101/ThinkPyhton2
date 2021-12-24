#!/usr/bin/python3

"""
Exercise 9.6. Write a function called is_abecedarian that returns True if the letters in a word
appear in alphabetical order (double letters are ok). How many abecedarian words are there?
"""
def is_abecedarian(word):
    i = 0
    while i < len(word)-1:
        if word[i+1] < word[i]:
            return False
        i = i+1
    return True

fin = open('words.txt')
count = 0
for line in fin:
    if is_abecedarian(line):
        print(line)
        count = count + 1
print('Total: ' + str(count))
