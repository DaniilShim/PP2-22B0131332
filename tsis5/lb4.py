import re

# input string
string = input("Enter a string: ")

# pattern to match one uppercase letter followed by lowercase letters
pattern = r'[A-Z][a-z]+'

# find all matches in the input string
matches = re.findall(pattern, string)

# print the matches
print(matches)
