import numpy as np
import matplotlib.pyplot as plt
import math

def newton_forward(x, y, value):
    n = len(x)
    h = x[1] - x[0]
    p = (value - x[0]) / h

    diff = np.zeros((n, n))
    diff[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            diff[i][j] = diff[i+1][j-1] - diff[i][j-1]

    result = y[0]
    term = 1

    for i in range(1, n):
        term = term * (p - i + 1) / i
        result += term * diff[0][i]

    return result


# Given data points
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 4, 9, 16, 25])

# Generate interpolation points
x_new = np.linspace(x[0], x[-1], 100)
y_new = np.array([newton_forward(x, y, value) for value in x_new])

# Display interpolated values
print("Newton Forward Interpolated Values:")

for i in range(len(x_new)):
    print("x =", round(x_new[i], 2),
          "y =", round(y_new[i], 4))

# Plot
plt.scatter(x, y, label="Original Data Points")
plt.plot(x_new, y_new, label="Newton Forward")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Newton Forward Interpolation")
plt.legend()
plt.grid()
plt.show()