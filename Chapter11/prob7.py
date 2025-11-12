class Vector:
    def __init__(self, l):
        self.l = l  # store the list

    def __len__(self):
        return len(self.l)  # return length of the list

v1 = Vector([1, 2, 3])
print(len(v1))  # Output: 3
