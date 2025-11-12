# post="Hey Rajan is good Rajan is great and Rajan Rajan"
post=input("Enter the post")

if("Rajan".lower() in post.lower()):     # this lower () work for the capital to small and when it compare showing the result is valid
    print("This post is talking about Rajan")

else:
    print("This post is not taking about Rajan")
