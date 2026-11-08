from scipy.integrate import solve_ivp

def RK45(f, a, b, y0, rtol=1.e-6):
    tspan = [a, b]

    sol = solve_ivp(
        f,
        tspan,
        y0,
        method='RK45',
        rtol=rtol
    )

    return sol.t, sol.y