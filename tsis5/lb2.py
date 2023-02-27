import re

# input string
string = input("Enter a string: ")

# pattern to match 'a' followed by two to three 'b's
pattern = r'a(bb|bbb)'

# check if the input string matches the pattern
match = re.search(pattern, string)

if match:
    print("Match found!")
else:
    print("No match found.")
