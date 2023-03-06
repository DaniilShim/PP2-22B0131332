import os

path = '/path/to/directory'

# Check if path exists
if os.path.exists(path):
    print(f"{path} exists")

    # Check if path is a directory
    if os.path.isdir(path):
        print(f"{path} is a directory")

        # Check if path is readable
        if os.access(path, os.R_OK):
            print(f"{path} is readable")
        else:
            print(f"{path} is not readable")

        # Check if path is writable
        if os.access(path, os.W_OK):
            print(f"{path} is writable")
        else:
            print(f"{path} is not writable")

        # Check if path is executable
        if os.access(path, os.X_OK):
            print(f"{path} is executable")
        else:
            print(f"{path} is not executable")
    else:
        print(f"{path} is not a directory")
else:
    print(f"{path} does not exist")
