class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        # Vector addition: (x1+x2, y1+y2, z1+z2)
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, other):
        # Dot product: x1*x2 + y1*y2 + z1*z2
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __str__(self):
        # String representation of the vector
        return f"Vector({self.x}, {self.y}, {self.z})"


# Example usage:
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

# Addition
print("Sum of vectors:", v1 + v2)      # Output: Vector(5, 7, 9)

# Dot Product
print("Dot product:", v1 * v2)         # Output: 32
