import re

dictionary = open("dictionaries/Spanish.dic").readlines()
dictionary = [word.lower().strip(' ').strip('\n') for word in dictionary]
dictionary = [re.sub(r"/.*", "", word) for word in dictionary]

while True:
	pattern = input()
	for word in dictionary:
		if re.fullmatch(pattern, word):
			print(word, end="\t")
	print('\n')
