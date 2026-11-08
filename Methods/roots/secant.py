import numpy as np

def secant(f, x1, x2, tol=1.e-6, maxit=100):
    # f = the function f(x)
    # x1 = an initial guess of the solution
    # x2 = another initial guess of the solution
    # tol = tolerance for the absolute error
    # maxit = maximum number of iterations

    err = 1.0
    iteration = 0

    while (err > tol and iteration < maxit):
        xk = x1
        xk1 = x2

        iteration = iteration + 1

        err = xk1

        xk1 = xk - (xk - xk1) / (f(xk) - f(xk1)) * f(xk)

        err = np.abs(err - xk1)

        x1 = x2
        x2 = xk1

        print(iteration, xk1)

    return xk1  