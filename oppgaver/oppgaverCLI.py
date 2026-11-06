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

def help() -> None:
    print("Commands:\n" + "╔" + "═" * 96 + "╗")
    print(f"║ {'Kommando':<30} │ {'Beskrivelse':<40} │ {'Funksjonsnavn':<18} ║")
    for navn, (funksjon, beskrivelse) in commands.items():
        funksjonsnavn = funksjon.__name__ if funksjon else "-"
        print(f"║ {navn:<30} │ {beskrivelse:<40} │ {funksjonsnavn:<18} ║")
    print("╚" + "═" * 96 + "╝")

def oppgave_b():
    print("Oppgave B")

    xmin = -10
    xmax = 10
    antall_punkter = 100
    x_verdier = np.linspace(xmin, xmax, antall_punkter)

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

def oppgave_c():
    print("Oppgave C")

    x = 2
    dx = 1E-4   

    print(f"Analytisk:  {df(x):.10f}")
    print(f"Fremover:   {newton_fwd(x, dx):.10f}")
    print(f"Symmetrisk: {newton_sym(x, dx):.10f}")

def oppgave_d():
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

commands = {
    "help": (help, "Vis kommandoer"),
    "q": (None, "Avslutt programmet"),
    "b": (oppgave_b, "Kjører oppgave b"),
    "c": (oppgave_c, "Kjører oppgave c"),
    "d": (oppgave_d, "Kjører oppgave d"),
}

help()

while True:
    navn = input(" > ").strip().lower()
    if navn == "q":
        break
    if navn in commands:
        funksjon, beskrivelse = commands[navn]
        funksjon()
    else:
        print("Ukjent kommando.")
