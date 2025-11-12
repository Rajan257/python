import os
#  Select the directory whose content you want to list 
directory_path = "."
#  Use the os module to list the directory 
try:
    contents = os.listdir(directory_path)
    print(f"Contents of directory '{directory_path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"You do not have permission to access '{directory_path}'.")
