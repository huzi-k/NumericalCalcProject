import numpy as np

def Simpson_38(f, a, b, N):
    # Composite Simpson 3/8 rule

    if N % 3 != 0:
        print("Error: N must be a multiple of 3 for Simpson's 3/8 Rule")
        return None

    h = (b - a) / float(N)

    x = np.linspace(a, b, N + 1)

    s = f(x)

    for i in range(1, N):
        if i % 3 == 0:
            s[i] = 2 * s[i]
        else:
            s[i] = 3 * s[i]

    return (3 * h / 8.0) * np.sum(s)