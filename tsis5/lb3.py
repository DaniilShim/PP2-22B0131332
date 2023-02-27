import re

# input string
string = input("Enter a string: ")

# pattern to match lowercase letters joined with an underscore
pattern = r'[a-z]+_[a-z]+'

# find all matches in the input string
matches = re.findall(pattern, string)

# print the matches
print(matches)
