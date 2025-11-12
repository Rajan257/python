import os

# Specify the path of the directory (or leave empty to use current directory)
directory_path = "/Rajan"

# List all files and directories
try:
    contents = os.listdir(directory_path)
    print(f"Contents of directory '{directory_path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"You do not have permission to access '{directory_path}'.")
