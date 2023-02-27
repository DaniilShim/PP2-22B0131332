import re

# input string in camel case
camel_case_string = input("Enter a camel case string: ")

# pattern to match capital letters in the input string
pattern = r'([A-Z])'

# convert the camel case string to snake case
snake_case_string = re.sub(pattern, r'_\1', camel_case_string).lower().lstrip('_')

# print the snake case string
print(snake_case_string)
