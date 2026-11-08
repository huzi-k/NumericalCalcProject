import numpy as np

def Simpson_13(f, a, b, N):
    # Composite Simpson 1/3 rule

    if N % 2 != 0:
        print("Error: N must be even for Simpson's 1/3 Rule")
        return None

    h = (b - a) / float(N)

    x = np.linspace(a, b, N + 1)

    s = f(x)

    s[1:N:2] = 4 * s[1:N:2]
    s[2:N-1:2] = 2 * s[2:N-1:2]

    return h / 3.0 * np.sum(s)