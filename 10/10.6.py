#!/usr/bin/python3

"""
Exercise 10.6. Two words are anagrams if you can rearrange the letters from one to spell the other.
Write a function called is_anagram that takes two strings and returns True if they are anagrams.
"""


def is_anagram(word1, word2):
    """Checks whether two words are anagrams
    word1: string or list
    word2: string or list
    returns: boolean
    """
    return sorted(word1) == sorted(word2)



