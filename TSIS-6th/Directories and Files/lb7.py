source_file = input("Enter the source file path: ")
destination_file = input("Enter the destination file path: ")

# Open the source file in read mode
with open(source_file, 'r') as f:
    # Read the contents of the source file
    contents = f.read()

# Open the destination file in write mode
with open(destination_file, 'w') as f:
    # Write the contents of the source file to the destination file
    f.write(contents)

print("File contents copied successfully!")
