import numpy as np

def midpoint(f, a, b, N):
    h = (b - a) / N

    x = np.linspace(a, b, N + 1)

    z = (x[1:] + x[:-1]) / 2.0

    w = h * np.ones_like(z)

    quad = np.inner(w, f(z))

    return quad