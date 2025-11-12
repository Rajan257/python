# word="Donkey"

# with open("file.txt","r") as f:
#     content=f.read()

# contentNew= content.replace(word,"######")


# with open("file.txt","w") as f:

#     f.write(contentNew)









# words=["Donkey","bad","ganda"]

# with open("file.txt","r") as f:
#     content=f.read()

# for word in words:
#    content= content.replace(word,"#"*len(word))
   
# with open("file.txt","w") as f:

#     f.write(content)









# with open("file.txt") as f:
#     content=f.read()

# if("python" in content):
#     print("yes python is present")
# else:
#     print("pythin is not present")






#fine line number
with open("file.txt") as f:
    lines=f.readlines()

lineno=1
for line in lines: 
  if("python" in line):
    print(f"yes python is present.Line no: {lineno}") #use line instead of loneno if want to print the line too
    break
    lineno+=1
else:
    print("pythin is not present")



