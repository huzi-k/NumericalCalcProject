import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

def cubic_spline(x, y):
    cs = CubicSpline(x, y, bc_type='natural')

    x_new = np.linspace(x[0], x[-1], 100)
    y_new = cs(x_new)

    print("Interpolated Values:")

    for i in range(len(x_new)):
        print("x =", round(x_new[i], 2),
              "y =", round(y_new[i], 4))

    plt.scatter(x, y, label="Original Data Points")
    plt.plot(x_new, y_new, label="Cubic Spline")

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Cubic Spline Interpolation")
    plt.legend()
    plt.grid()
    plt.show()

    return cs


# Given data points
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 4, 9, 16, 25])

# Run cubic spline
cs = cubic_spline(x, y)