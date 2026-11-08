import numpy as np
import matplotlib.pyplot as plt


def lagrange_basis(z, x):
    # Compute the Lagrange basis l_i(z)
    # given the nodes x_i stored in vector x

    n = len(x)
    m = len(z)

    basis = np.ones((n, m))

    for i in range(n):
        for j in range(n):
            if i != j:
                basis[i, :] *= (z - x[j]) / (x[i] - x[j])

    return basis


def lagrange_interpolant(z, x, y):
    # Compute the interpolant using Lagrange polynomials

    n = len(x)
    m = len(z)

    P = np.zeros(m)

    basis = lagrange_basis(z, x)

    for i in range(n):
        P += basis[i, :] * y[i]

    return P
