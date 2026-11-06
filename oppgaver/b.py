import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 2 * x**3 + x**2 - 13 * x + 6

def df(x):
    return 6 * x**2 + 2 * x - 13

xmin = -10
xmax = 10
antall_punkter = 100
x_verdier = np.linspace(xmin, xmax, antall_punkter)

print("Oppgave B")

plt.figure(figsize=(10, 6))
plt.plot(x_verdier, f(x_verdier), label="f(x)")
plt.plot(x_verdier, df(x_verdier), "--", label="f'(x)")
plt.axhline(color="black", linewidth=0.5)
plt.axvline(color="black", linewidth=0.5)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Oppgave B")
plt.grid(alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()
