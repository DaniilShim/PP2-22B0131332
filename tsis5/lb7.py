import re

# input string in snake case
string = input("Enter a string in snake case: ")

# pattern to match words separated by underscores
pattern = r'_\w'

# replace matches with the capitalized version of the word
result = re.sub(pattern, lambda x: x.group()[1:].upper(), string)

# print the result
print(result)
