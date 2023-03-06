file_name = input("Enter the file name: ")

with open(file_name, 'r') as file:
    lines = file.readlines()
    num_lines = len(lines)
    print("The file has", num_lines, "lines.")
