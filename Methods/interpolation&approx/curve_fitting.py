
import numpy as np
import matplotlib.pyplot as plt

def curve_fitting(x, y, degree=1):
    # Calculate polynomial coefficients
    coefficients = np.polyfit(x, y, degree)

    # Create polynomial equation
    curve = np.poly1d(coefficients)

    # Generate points for plotting
    x_new = np.linspace(x[0], x[-1], 100)
    y_new = curve(x_new)

    # Display equation
    print("Best Fit Equation:")
    print(curve)

    # Display fitted values
    print("\nFitted Values:")

    for i in range(len(x_new)):
        print("x =", round(x_new[i], 2),
              "y =", round(y_new[i], 4))

    # Plot original points and fitted curve
    plt.scatter(x, y, label="Original Data Points")
    plt.plot(x_new, y_new, label="Best Fit Curve")

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Polynomial Curve Fitting")
    plt.legend()
    plt.grid()
    plt.show()

    return curve


# Given data points
x = np.array([1, 2, 3, 4, 5])
y = np.array([2.1, 3.9, 6.2, 7.8, 10.1])

# Perform curve fitting
curve = curve_fitting(x, y, degree=1)
