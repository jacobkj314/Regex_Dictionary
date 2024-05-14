from sys import argv

language = argv[1] if len(argv) > 1 else "Spanish"

import re

dictionary = open(f"dictionaries/{language}.dic").readlines()
dictionary = [word.lower().strip(' ').strip('\n') for word in dictionary]
dictionary = [re.sub(r"/.*", "", word) for word in dictionary]

while True:
	pattern = input()
	for word in dictionary:
		if re.fullmatch(pattern, word):
			print(word, end="\t")
	print('\n')
