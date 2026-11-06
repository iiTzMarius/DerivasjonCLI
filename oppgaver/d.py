import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 2 * x**3 + x**2 - 13 * x + 6

def df(x):
    return 6 * x**2 + 2 * x - 13

def newton_fwd(x, dx):
    return (f(x + dx) - f(x)) / dx

def newton_sym(x, dx):
    return (f(x + dx) - f(x - dx)) / (2 * dx)

print("Oppgave D")

x = np.linspace(-3, 3, 1000)

fig, akser = plt.subplots(
    2, 2, figsize=(12, 8), sharex=True, sharey=True
)

def tegn_graf(akse, dx):
    akse.plot(x, f(x), color="gray", linestyle=":", label="f(x)")
    akse.plot(x, df(x), color="black", linewidth=2, label="Analytisk f'(x)")
    akse.plot(x, newton_fwd(x, dx), color="red", linestyle="--", label="Fremoverkvotient")
    akse.plot(x, newton_sym(x, dx), color="blue", linestyle="-.", label="Symmetrisk kvotient")
    akse.axhline(color="black", linewidth=0.5)
    akse.axvline(color="black", linewidth=0.5)
    akse.set(title=f"dx = {dx}", xlabel="x", ylabel="y")
    akse.grid()
    akse.legend()

tegn_graf(akser[0, 0], 1e-4)
tegn_graf(akser[0, 1], 0.1)
tegn_graf(akser[1, 0], 1.0)
tegn_graf(akser[1, 1], 2.0)

fig.suptitle("Oppgave D")
fig.tight_layout()
plt.show()
