import re

# input string
string = input("Enter a string: ")

# pattern to match 'a' followed by anything, ending in 'b'
pattern = r'a.*b$'

# check if the input string matches the pattern
match = re.search(pattern, string)

if match:
    print("Match found!")
else:
    print("No match found.")
