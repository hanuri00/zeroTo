# -*- coding: utf-8 -*-
"""
@author: hanuri
"""

with open('d:/src/movie_quotes.txt', 'r', encoding='utf-8') as f:    
    lines = f.readlines()
    line = ''
    for line in lines:
        print(line, end='')
