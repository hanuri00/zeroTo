# -*- coding: utf-8 -*-
"""
@author: hanuri
"""

lines = ["we'll find a way we always have - Interstellar\n", 
         "I'll find you and I'll kill you - Taken\n",
         "I'll be back - Terminator 2\n"]

with open('d:/src/movie_quotes.txt', 'w') as file:
    for line in lines:
        file.write(line)
