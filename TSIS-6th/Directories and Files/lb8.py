import os

path = input("Enter the path of the file to be deleted: ")

if not os.path.exists(path):
    print("The specified file does not exist.")
elif not os.access(path, os.W_OK):
    print("You do not have write access to the specified file.")
else:
    os.remove(path)
    print("The file has been deleted successfully.")
