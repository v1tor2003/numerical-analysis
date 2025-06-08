from sympy import symbols, sympify
import math
from methods.utils.file_utils import read_function, save_results

INPUT_PATH = "methods/part2/simple_trapeze/input.txt"
OUTPUT_PATH = "methods/part2/simple_trapeze/output.txt"

x = symbols("x")

def simple_trapeze_method(a, b, func):
    result = abs(a - b) * ((func.subs(x, a) + func.subs(x, b)) / 2) # (a - b) was fixed to (b - a)
    return result

def main():
    func, a ,b = read_function(INPUT_PATH)
    result = simple_trapeze_method(a, b, sympify(func))
    save_results(OUTPUT_PATH, [f"I(f(x)) = {result}"])

if __name__ == "__main__":
    main()