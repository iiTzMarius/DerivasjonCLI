from collections.abc import Callable
from math import e
from matplotlib import pyplot as plt
import numpy as np
from simpleeval import simple_eval
import sympy as sp
from typing import Any

class Command:
    def __init__(self,
                name: str,
                function: Callable,
                description: str | None = None,
                alternative: str | None = None
            ):
        
        self.name = [name, alternative]
        self.description = description
        self.function = function
    
    def run(self, *args) -> Any:
        return self.function(*args)

def main() -> int:    
    command: str = ""
    
    while (command != "exit"):
        command = input(" > ")
        
        found = False
        for cmd in commands:
            if (command in cmd.name):
                cmd.run()
                found = True
                break
        
        if not found:
            print("Command not found.")

def help() -> None:
    print(f"Commands:\n{"╔" + "═"*96 + "╗"}")
    print(f"║\033[4m {"Name / Alias":<30} │ {"Description":<40} │ {"Function name":<18} \033[0m║")
    for command in commands:
        name = str(command.name).replace("[", "").replace("]", "").replace(", ", " / ").replace(" / None", "").replace("'", "")
        print(f"║ {str(name):<30} │ {command.description:<40} │ {command.function.__name__:<18} ║")
    print("╚" + "═"*96 + "╝")
    return

def expressionChange() -> None:
    """
    Changes the expression

    Args:
        nytt_uttrykk (str): new formula which must be written for it to be solven in normal python syntax.
    """
    global uttrykk, derivert_uttrykk
    uttrykk = format_equation(input("New formula: "))
    
    try:
        derivert_uttrykk = getDerivativeFunction(uttrykk)
    except Exception as error:
        print("Couldnt calculate the derivated function: {error}")
        derivert_uttrykk = "0"
    
    print(f"Set f(x) = {uttrykk} !")

def getEq() -> None:
    print(uttrykk)

def evaluateExpression() -> None:
    x: float = float(input("x = "))
    print(f"f({x}) = {f(x)}")
    return

def evaluateDerivativeExpression() -> None:
    x: float = float(input("x = "))
    print(f"f'({x}) = {f_derived(x)}")
    return

def printUttrykk() -> None:
    print(f"f(x) = {uttrykk}")
    return

def plotExpression() -> None:
    x_0 = float(input("Graph start: "))
    x_final = float(input("Graph end: "))
    step_size_inp = input("Step size (0.1% of dx as default): ")
    try:
        step_size = float(step_size_inp)
    except ValueError:
        step_size = abs(x_final - x_0) / 1000
    except:
        print("Unknown error, input not accepted")
        return    
    x = np.arange(x_0, x_final, step_size)
    
    derive = input("Do you want to plot the derived function? (y/n) ")[0].lower() == "y"
    if (derive):        
        use_symmetric_quotient: bool = input("Do you want to use symmetric quotient? (y/n) ")[0].lower() == "y"
        delta_x: float = float(input("Choose value for h (1E-8 as default): "))
        delta_x = delta_x if delta_x else None
        
        if use_symmetric_quotient:
            y = [f_derived_symmetrical_quotient(xi, delta_x) for xi in x]
        else:
            y = [f_derived(xi, delta_x) for xi in x]
    else:
        y = [f(xi) for xi in x]
    
    plt.plot(x, y)
    plt.grid(True)
    plt.show()
    

def evaluateDerivationMethod() -> None:
    x_0 = float(input("Graph start: "))
    x_final = float(input("Graph end: "))
    step_size_inp = input("Step size (0.1% of dx as default): ")

    try:
        step_size = float(step_size_inp) if step_size_inp else abs(x_final - x_0) / 1000
    except ValueError:
        print("Invalid step size")
        return

    if step_size <= 0 or x_final <= x_0:
        print("Invalid graph range or step size")
        return

    delta_x_inp = input("Choose a value for h (1E-8 as default): ")

    try:
        delta_x = float(delta_x_inp) if delta_x_inp else 1e-8
    except ValueError:
        print("Invalid h value")
        return

    if delta_x == 0:
        print("h cannot be zero")
        return

    x = np.arange(x_0, x_final, step_size)

    y_s = np.array([f_derived_symmetrical_quotient(xi, delta_x) for xi in x])
    y_ns = np.array([f_derived(xi, delta_x) for xi in x])
    y_exact = np.array([f_actual_derived(xi) for xi in x])

    # Calculate average absolute errors
    ae_s_ns = np.mean(np.abs(y_s - y_ns))
    ae_s_exact = np.mean(np.abs(y_s - y_exact))
    ae_ns_exact = np.mean(np.abs(y_ns - y_exact))

    # Create graph
    fig, ax = plt.subplots(figsize=(11, 7))

    ax.plot(x, y_s - y_ns, label="Symmetric vs Forward", linewidth=1.5)
    ax.plot(x, y_s - y_exact, label="Symmetric vs Exact", linewidth=1.5)
    ax.plot(x, y_ns - y_exact, label="Forward vs Exact", linewidth=1.5)

    ax.axhline(0, color="gray", linestyle="--", alpha=0.6)

    ax.set_title(f"Numerical Differentiation Error (h = {delta_x:.2e})")
    ax.set_xlabel("x")
    ax.set_ylabel("Signed difference")
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Display average errors below graph
    error_text = (
        f"Symmetric / forward:  {ae_s_ns:.6e}\n"
        f"Symmetric / exact:    {ae_s_exact:.6e}\n"
        f"Forward / exact:      {ae_ns_exact:.6e}"
    )

    fig.subplots_adjust(bottom=0.28)

    fig.text(
        0.5, 0.06,
        error_text,
        ha="center",
        va="bottom",
        fontsize=10,
        family="monospace",
        linespacing=1.6
    )

    plt.show()

def f(x) -> float:
    alle_ledd: list[str] = uttrykk.replace(" ", "")
    return simple_eval(alle_ledd, names={"x": x})

def f_actual_derived(x) -> float:
    alle_ledd: str = derivert_uttrykk.replace(" ", "")
    return simple_eval(alle_ledd, names={"x": x})

def f_derived_symmetrical_quotient(x, h=1E-8) -> float:
    return round((f(x + h) - f(x - h))/(2*h), 6)

def f_derived(x, h=1E-8) -> float:
    return round((f(x + h) - f(x))/h, 6)


def f_derive_multiple(x, n, h=1e-4):
    if n == 0:
        return f(x)

    return (
        f_derive_multiple(x + h, n - 1, h)
        - f_derive_multiple(x - h, n - 1, h)
    ) / (2 * h)

def format_equation(equation: str) -> str:
    equation = equation.replace("^", "**").replace("e", str(e))
    
    new_equation = equation[:1]
    
    for i in range(1, len(equation)):
        previous = equation[i - 1]
        current = equation[i]
        
        if (
                previous.isdigit() and current.isalpha()
                or
                previous.isalpha() and current.isdigit()
            ):
            new_equation += "*"
        
        new_equation += current
    return new_equation

def getDerivativeFunction(equation: str):
    x = sp.Symbol("x")
    sympy_equation = sp.sympify(equation)
    derived = sp.diff(sympy_equation, x)
    return str(derived)

def findSaddlePoints():
    
    return
    

uttrykk = format_equation("x^3 + 1/2 * x^2 - 13/2 * x + 3")
derivert_uttrykk = getDerivativeFunction(uttrykk)

commands: list[Command] = [
    Command("help", help, "Lists commands and descriptions"),
    Command("expressionChange", expressionChange, "Changes the expression", "eC"),
    Command("evaluateE", evaluateExpression, "Evaluates the expression", "eE"),
    Command("evaluateDE", evaluateDerivativeExpression, "Evaluates d/dx", "eDE"),
    Command("plotE", plotExpression, "Plots expression", "pE"),
    Command("getEq", getEq, "Gets current equation", "gE"),
    Command("evaluateDerivationMethod", evaluateDerivationMethod, "Show difference between with and without symetric quotient derivation.", "eDM"),
    Command("findSaddlePoints", findSaddlePoints, "Finds saddle points on a graph", "fSP")
]

if (__name__ == '__main__'):
    print(f"[INFORMATION] Starting program...\n{'─'*40}")
    try:
        main()
    except Exception as e:
        print(f"[ERROR OCCURED] {e}")
        exit_status = -1
    else:
        exit_status = 0

    print(f"{'─'*40}\n[INFORMATION] Program finished with {exit_status = }\n")