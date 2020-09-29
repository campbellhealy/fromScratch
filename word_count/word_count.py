# word_count.py
'''
Started with a simple count the letters, then count the words
Counting the words in a piece of text
Counting the words in a set of text files, to reuse the code (No matter how many files)
Added most_common to limit the results
'''
from re import findall
from os import system
from collections import Counter

da_files = ('text.txt', 'text2.txt', 'text3.txt', 'text4.txt')

def wordcounter(text_file):
    system('cls') # Clear the console for a clean look
    for item in text_file:
        words = findall(r'\w+', open(item).read().lower())
        output = dict(Counter(words).most_common(10))
        print(output,'\n')

wordcounter(da_files)