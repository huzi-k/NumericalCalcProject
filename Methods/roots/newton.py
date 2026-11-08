import numpy as np

def newton(f, df, x0, tol=1.e-6, maxit=100):
    # f = the function f(x)
    # df = the derivative of f(x)
    # x0 = the initial guess of the solution
    # tol = tolerance for the absolute error
    # maxit = maximum number of iterations

    err = 1.0
    iteration = 0
    xk = x0

    while (err > tol and iteration < maxit):
        iteration = iteration + 1

        err = xk  # store previous approximation
        xk = xk - f(xk) / df(xk)  # Newton's iteration

        err = np.abs(err - xk)  # compute the new error

        print(iteration, xk)

    return xk