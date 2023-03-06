# ask the user to enter a string
string = input("Enter a string: ")

# initialize counters for uppercase and lowercase letters
upper_count = 0
lower_count = 0

# loop through each character in the string
for char in string:
    # check if the character is uppercase or lowercase
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1

# print the results
print("Number of uppercase letters: ", upper_count)
print("Number of lowercase letters: ", lower_count)