f=open("testfile.txt")
print(f.read())
f.close()

# the same can be written using with statement like this
with open("testfile.txt")as f:
    print(f.read())

    # you do not explicitly close the file
    