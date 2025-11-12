f=open("twinkle.txt")
content=f.read()
if("twinkle" in content ):
   print("the word twinkle is present in the content")
else:
   print("The word twinkle is not present in the content")
   f.close()