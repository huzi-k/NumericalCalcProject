import numpy as np

def trapezoidal(f, a, b, N):
    # Composite trapezoidal rule with N subintervals

    x = np.linspace(a, b, N + 1)
    y = f(x)

    h = (b - a) / N

    # First add the internal nodes
    sum = 0.0

    for i in range(1, N):
        sum += 2.0 * y[i]

    # Add the two boundary nodes
    sum = 0.5 * h * (f(a) + sum + f(b))

    return sum