#special punctuation marks (period, question mark, exclamation point, comma, semicolon, colon, dash, hyphen,
#parentheses, brackets, braces, apostrophe, quotation marks, and ellipsis) and of course the space (or spaces)
#and the end of a line (new paragraph)

import re

delimeters = " ","\t","\n",".","?","!",",",":",";""-","~","[","]","{","}","(",")","'","\""
file_name = "Book.txt"

#split string by delimiters
def split(delimiters, string):
    regexPattern = '|'.join(map(re.escape, delimiters))
    return re.split(regexPattern, string)

#lowercase words and clean special symbols
def clean(delimeters,strings):
    result_list = []
    for string in strings:
        for delimiter in delimeters:
            clear_str = string.lower().replace(delimiter,"")
        if clear_str != "":
            result_list.append(clear_str)
    return result_list

#let's roll
word_map = {}

file = open(file_name, "r")
for line in file:
    res1 = split(delimeters, line)
    res2 = clean(delimeters, res1)
    for word in res2:
        word_map[word] = word_map.get(word, 0) + 1

#check result in std out
print(word_map)