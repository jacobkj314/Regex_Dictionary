#!/usr/bin/python3
from sys import argv

language = argv[1] if len(argv) > 1 else "Spanish"

import re

dictionary = open(f"dictionaries/{language}.dic").readlines()
dictionary = [word.lower().strip(' ').strip('\n') for word in dictionary]
dictionary = [re.sub(r"/.*", "", word) for word in dictionary]

print(f"Welcome to my Regex dictionary. Each line you type will be interpreted as a regular expression, and all matching words in the dictionary will be returned, separated by tabs. Your selected language is {language}.\nDictionaries sourced from https://github.com/titoBouzout/Dictionarie.\nVisit https://docs.python.org/3/library/re.html for documentation on using regular expression strings.\n")

while True:
	pattern = input('> ')
	for word in dictionary:
		if re.fullmatch(pattern, word):
			print(word, end="\t")
	print('\n')
