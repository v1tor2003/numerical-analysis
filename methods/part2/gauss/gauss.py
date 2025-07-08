from sympy import symbols, sympify
from methods.utils.file_utils import read_function, save_results
from math import sqrt

INPUT_PATH = "methods/part2/gauss/input.txt"
OUTPUT_PATH = "methods/part2/gauss/output.txt"

def gauss_quadrature(func, a, b):
    """
    Calculates the definite integral of func from a to b using Gauss quadrature with 2 points.
    """
    x = symbols("x")

    t1 = -1 / sqrt(3)
    t2 =  1 / sqrt(3)

    x1 = ((b - a) / 2) * t1 + (a + b) / 2
    x2 = ((b - a) / 2) * t2 + (a + b) / 2

    fx1 = func.subs(x, x1)
    fx2 = func.subs(x, x2)

    I = ((b - a) / 2) * (fx1 + fx2)

    return I

def main():
    func, a, b = read_function(INPUT_PATH)
    result = gauss_quadrature(sympify(func), a, b)
    save_results(OUTPUT_PATH, [f"I(f(x)) = {result}"])

if __name__ == "__main__":
    main()