import re

# input string
string = input("Enter a string: ")

# pattern to match words starting with capital letters
pattern = r'(?<!^)(?=[A-Z])'

# insert space before words starting with capital letters
result = re.sub(pattern, ' ', string)

# print the result
print(result)
