freinds=["Apple","Orange",5,5.75,False,"Ambani","Rajan"]

print(freinds)

freinds.append("Rajan")

print(freinds)

l1=[1,3,4,5,6,5,7,8]

l1.sort() #increasing
print(l1)

l1.reverse()  #decreasing
print(l1)

l1.insert(3,3333) #inserting 333 such that its index in the list is 3

print(l1)

l1.pop(3)
print(l1)
print(l1.pop(3))


value=l1.pop(3)
print(value)

freinds.remove("Rajan")
print(freinds)