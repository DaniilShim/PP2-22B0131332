# ask the user to enter a string
s = input("Enter a string: ")

# reverse the string
reverse_s = s[::-1]

# check if the original string and the reversed string are the same
if s == reverse_s:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
