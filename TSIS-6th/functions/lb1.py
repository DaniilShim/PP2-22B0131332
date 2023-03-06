from functools import reduce

# ask the user to input a list of numbers
num_list = input("Enter a list of numbers, separated by commas: ")

# split the input string into a list of strings and convert each to a float
num_list = list(map(float, num_list.split(",")))

# use reduce() to multiply all the numbers in the list
result = reduce(lambda x, y: x * y, num_list)

# print the result
print(result)