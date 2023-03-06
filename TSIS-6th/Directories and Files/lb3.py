import os

path = input("Enter a path: ")

if os.path.exists(path):
    print("The path exists.")
    dirname, filename = os.path.split(path)
    print("Directory:", dirname)
    print("Filename:", filename)
else:
    print("The path does not exist.")
