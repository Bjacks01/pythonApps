# Author: Brandon Jacks
# Section: CIS 225 01
# Date: 11/14/22
# File: shakespeare.py
#
# A simple script.

import sys

num_args = len(sys.argv)
if num_args != 1:
    print("Usage: homework_script")
    sys.exit()

from collections import Counter

print('Reading Shakespeare...')
shakespeare = open('shakespeare.txt')
words = shakespeare.read().split()


lower_words = []
for i in words:
    if i.isalpha(): 
        lower_words.append(i.lower())
word_counts = Counter(lower_words).most_common(5)

uniqueWords = []
for i in lower_words:
    if i not in uniqueWords:
        uniqueWords.append(i)


uniqueWords.sort()

print('Shakespeare uses', len(uniqueWords), 'unique words.')
print('Alphabetically, the first five unique words used are:', uniqueWords[0:6])
print('Alphabetically, the last five unique words used are:', uniqueWords[-5:])
print('The 5 most commonly used words are:', word_counts)



