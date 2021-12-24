#!/usr/bin/python3

def rotate_word(secret, num):
    for c in secret:
        new_n=ord(c)+num
        if (new_n-ord('z')>0):
            new_n=new_n-26
        new_c=chr(new_n)
        print(new_c,end='')

word = str(input('Enter a word: '))
key = int(input('Enter shift key: '))
rotate_word(word, key)
print()
