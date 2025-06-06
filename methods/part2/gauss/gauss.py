from sympy import symbols, sympify
from methods.utils.file_utils import read_function, save_results

INPUT_PATH = "methods/part2/gauss/input.txt"
OUTPUT_PATH = "methods/part2/gauss/output.txt"

def gauss_quadrature(func, a, b):
    """
    Calculate the integral of func from a to b using Gauss quadrature.
    """
    x = symbols("x")
    I = ((b - a) / 2) * (func.subs(x, a) + func.subs(x, b))
    return I

def main():
    func, a, b = read_function(INPUT_PATH)
    result = gauss_quadrature(sympify(func), a, b)
    save_results(OUTPUT_PATH, [f"I(f(x)) = {result}"])

if __name__ == "__main__":
    main()