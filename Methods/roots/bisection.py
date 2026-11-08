import numpy as np

def bisection_rates(f, a, b, tol=1.e-6):
    iteration = 0

    if f(a) == 0:
        return a

    if f(b) == 0:
        return b

    if f(a) * f(b) < 0.0:
        e1 = abs(b - a)
        e2 = e1 * 2
        e3 = e1

        while ((b - a) > tol):
            e1 = e2
            e2 = e3

            iteration = iteration + 1
            x = (a + b) / 2

            if (f(a) * f(x) < 0.0):
                b = x

            elif (f(x) * f(b) < 0.0):
                a = x

            else:
                break

            e3 = np.abs(b - a)
            rate = np.log(e2 / e3) / np.log(e1 / e2)

            print('iteration = ', iteration, 'rate =', rate)

    else:
        print('failure')
        return None

    return (a + b) / 2