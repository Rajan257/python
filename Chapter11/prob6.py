class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __add__(self, other):
        # Vector addition
        return Vector(self.i + other.i, self.j + other.j, self.k + other.k)

    def __mul__(self, other):
        # Dot product
        return self.i * other.i + self.j * other.j + self.k * other.k

    def __str__(self):
        # Return vector in i, j, k format
        parts = []
        if self.i != 0:
            parts.append(f"{self.i}i")
        if self.j != 0:
            parts.append(f"{self.j}j")
        if self.k != 0:
            parts.append(f"{self.k}k")
        return " + ".join(parts) if parts else "0"


# Example usage:
v1 = Vector(2, 3, 4)
v2 = Vector(1, 0, -1)

print("v1 =", v1)
print("v2 =", v2)

# Vector addition
print("v1 + v2 =", v1 + v2)

# Dot product
print("v1 • v2 =", v1 * v2)
