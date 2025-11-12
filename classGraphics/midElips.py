import matplotlib.pyplot as plt

def draw_ellipse(rx, ry, xc, yc):
    x = 0
    y = ry

    d1 = (ry * ry) - (rx * rx * ry) + (0.25 * rx * rx)
    dx = 2 * ry * ry * x
    dy = 2 * rx * rx * y

    points = []

    # Region 1
    while dx < dy:
        points.extend([
            (x + xc, y + yc),
            (-x + xc, y + yc),
            (x + xc, -y + yc),
            (-x + xc, -y + yc)
        ])
        if d1 < 0:
            x += 1
            dx += 2 * ry * ry
            d1 += dx + (ry * ry)
        else:
            x += 1
            y -= 1
            dx += 2 * ry * ry
            dy -= 2 * rx * rx
            d1 += dx - dy + (ry * ry)

    # Region 2
    d2 = ((ry * ry) * ((x + 0.5) ** 2)) + ((rx * rx) * ((y - 1) ** 2)) - (rx * rx * ry * ry)
    while y >= 0:
        points.extend([
            (x + xc, y + yc),
            (-x + xc, y + yc),
            (x + xc, -y + yc),
            (-x + xc, -y + yc)
        ])
        if d2 > 0:
            y -= 1
            dy -= 2 * rx * rx
            d2 += (rx * rx) - dy
        else:
            y -= 1
            x += 1
            dx += 2 * ry * ry
            dy -= 2 * rx * rx
            d2 += dx - dy + (rx * rx)

    # Sort points for smooth connection
    points = list(set(points))  
    points.sort()

    # Plot smooth curve
    xs, ys = zip(*points)
    plt.plot(xs, ys, 'b-', linewidth=1.5)  # blue smooth line

    plt.title("Midpoint Ellipse Algorithm (Smooth)")
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()


# Example usage
draw_ellipse(120, 70, 0, 0)
