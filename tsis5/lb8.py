import re

# input string
string = input("Enter a string: ")

# pattern to match uppercase letters
pattern = r'[A-Z]'

# split the string at uppercase letters
result = re.split(pattern, string)

# print the result
print(result)
