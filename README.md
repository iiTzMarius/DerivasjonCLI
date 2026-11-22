# DerivasjonCLI

An interactive command-line tool in Python for exploring derivatives. Enter a function f(x), then evaluate it, differentiate it numerically, and plot the function or its derivative.

## Features

- Set and show the current expression f(x)
- Evaluate f(x) and f'(x) at a given point
- Numerical differentiation with the Newton quotient or the symmetric difference quotient, with a configurable step size h
- Compare how accurate the differentiation methods are
- Plot f(x) or f'(x) over an interval with matplotlib
- A `help` command lists every command and its alias

## Getting started

```bash
pip install -r requirements.txt sympy simpleeval
python derivasjonCLI.py
```

Type `help` at the `>` prompt to see the available commands, and `exit` to quit.

## Repository layout

- `derivasjonCLI.py`: the CLI
- `oppgave.pdf`: the assignment
- `oppgaver/`: worked answers to the assignment tasks
