import matplotlib.pyplot as plt

def bresenham(x1, y1, x2, y2):
    points = []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    x, y = x1, y1
    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1

    if dx > dy:
        err = dx / 2.0
        while x != x2:
            points.append((x, y))
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2.0
        while y != y2:
            points.append((x, y))
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy

    points.append((x, y))
    return points

# Example
line = bresenham(2, 2, -20, -10)
x_vals, y_vals = zip(*line)

plt.plot(x_vals, y_vals, marker='o')
plt.title("Bresenham's Line Drawing")
plt.grid(True)
plt.show()
