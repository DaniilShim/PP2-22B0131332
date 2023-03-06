# take input from user
my_list = input("Enter elements of list separated by comma: ").split(",")

# open file in write mode
with open("my_list.txt", "w") as file:
    # write each element of list as a line in file
    for element in my_list:
        file.write(element.strip() + "\n")

print("List written to file successfully!")
