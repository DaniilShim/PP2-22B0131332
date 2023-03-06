import os

# get the path from the user
path = input("Enter the path: ")

# check if the path exists
if os.path.exists(path):
    print(f"Contents of path: {path}\n")
    print("Directories:")
    for dir_name in os.listdir(path):
        if os.path.isdir(os.path.join(path, dir_name)):
            print(dir_name)
    print("\nFiles:")
    for file_name in os.listdir(path):
        if os.path.isfile(os.path.join(path, file_name)):
            print(file_name)
    print("\nAll Directories and Files:")
    for dirpath, dirnames, filenames in os.walk(path):
        for dirname in dirnames:
            print(os.path.join(dirpath, dirname))
        for filename in filenames:
            print(os.path.join(dirpath, filename))
else:
    print("Invalid path!")
