# -*- coding: utf-8 -*-
"""
Created on Sun Sep 06 23:38:16 2015

@author: Jongbin
"""

# 1. 
words = {}
with open('two_cities.txt', 'r') as text:
    for line in text:
        for word in line.lower().split():
            try:
                words[word] += 1
            except KeyError:
                words[word] = 1
                

# 2.
def filter_counts(min, max, d):
    for k,v in d.iteritems():
        if v >= min and v <= max:
            print k, ':', v

filter_counts(500, 700, words)

for word in sorted(words, key=words.get):
    print word, words[word]