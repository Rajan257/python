# Writing to a file
with open("testfile.txt", "w") as file:
    file.write("Hello, world!")

# Reading from the file
with open("testfile.txt", "r") as file:
    content = file.read()
    print(content)
