import matplotlib.pyplot as plt
import numpy as np

def draw_black_ellipse(rx, ry, xc, yc):
    # Generate 2000 points for sharpness
    t = np.linspace(0, 2*np.pi, 2000)  
    x = xc + rx * np.cos(t)
    y = yc + ry * np.sin(t)

    # Plot with sharp black line
    plt.plot(x, y, 'k-', linewidth=2)   # 'k-' means black solid line
    plt.title("Sharp Black Ellipse")
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# Example usage
draw_black_ellipse(120, 70, 0, 0)

