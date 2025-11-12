with open("this.txt") as f:
    content = f.read()
with open("this_copy.txt","w") as f:
    f.write(content)









#matches the content one file to another file

# with open("this.txt") as f:
#     content1 = f.read()
# with open("this_copy.txt") as f:
#    content2=f.read()

# if(content1==content2):
#     print("yes these files are identical")

# else:
#     print("No thse files are not identical")