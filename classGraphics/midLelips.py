import matplotlib.pyplot as plt

def draw_ellipse(rx, ry, xc, yc):
    x = 0
    y = ry

    # Initial decision parameter of region 1
    d1 = (ry * ry) - (rx * rx * ry) + (0.25 * rx * rx)
    dx = 2 * ry * ry * x
    dy = 2 * rx * rx * y

    points = []

    # Region 1
    while dx < dy:
        points.append((x + xc, y + yc))
        points.append((-x + xc, y + yc))
        points.append((x + xc, -y + yc))
        points.append((-x + xc, -y + yc))

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

    # Decision parameter for region 2
    d2 = ((ry * ry) * ((x + 0.5) ** 2)) + ((rx * rx) * ((y - 1) ** 2)) - (rx * rx * ry * ry)

    # Region 2
    while y >= 0:
        points.append((x + xc, y + yc))
        points.append((-x + xc, y + yc))
        points.append((x + xc, -y + yc))
        points.append((-x + xc, -y + yc))

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

    # Plot ellipse
    for p in points:
        plt.plot(p[0], p[1], 'ro')

    plt.title("Midpoint Ellipse Algorithm")
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()


# Example usage
rx = 80   # radius along x-axis
ry = 40   # radius along y-axis
xc = 0    # center x
yc = 0    # center y

draw_ellipse(rx, ry, xc, yc)
