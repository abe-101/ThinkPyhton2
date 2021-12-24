#!/usr/bin/python3

def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True

count = 0
no_e = 0 
fin = open('words.txt')
for line in fin:
    count = count + 1
    if has_no_e(line):
        #print(line)
        no_e = no_e + 1
percentage = no_e / count * 100
print(percentage)
