def f(x):
    return 2 * x**3 + x**2 - 13 * x + 6

def df(x):
    return 6 * x**2 + 2 * x - 13

def newton_fwd(x, dx):
    return (f(x + dx) - f(x)) / dx

def newton_sym(x, dx):
    return (f(x + dx) - f(x - dx)) / (2 * dx)

x = 2
dx = 1E-4   

print("Oppgave C")
print(f"Analytisk:  {df(x):.10f}")
print(f"Fremover:   {newton_fwd(x, dx):.10f}")
print(f"Symmetrisk: {newton_sym(x, dx):.10f}")
