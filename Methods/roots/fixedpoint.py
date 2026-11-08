import numpy as np



def fixedpoint(g, x0, tol=1.e-6, maxit=100):
    # g = the function g(x)
    # x0 = initial guess of the fixed point x = g(x)
    # tol = tolerance for absolute error
    # maxit = maximum number of iterations allowed

    error = 1.0
    iteration = 0
    xk = x0

    while (error > tol and iteration < maxit):
        iteration = iteration + 1

        previous = xk
        xk = g(xk)

        error = np.abs(previous - xk)

        print('iteration =', iteration, ', x =', xk)

    return xk