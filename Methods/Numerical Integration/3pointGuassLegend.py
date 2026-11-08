import numpy as np

def GaussLegendre3(f, a, b):
    # Implementation of Gauss-Legendre quadrature with
    # 3 nodes in general interval [a, b]

    N = 2

    # Define quadrature weights and nodes
    w = np.array([5.0/9.0, 8.0/9.0, 5.0/9.0])

    z = np.array([
        -np.sqrt(3.0/5.0),
        0.0,
        np.sqrt(3.0/5.0)
    ])

    # Implement Gauss-Legendre formula
    c1 = (b - a) / 2.0
    c2 = (a + b) / 2.0

    s = c1 * np.inner(w, f(c1 * z + c2))

    return s