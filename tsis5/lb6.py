import re

# input string
string = input("Enter a string: ")

# pattern to match space, comma, or dot
pattern = r'[ ,.]'

# replace all matches with a colon
result = re.sub(pattern, ':', string)

# print the result
print(result)
