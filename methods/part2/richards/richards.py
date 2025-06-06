from sympy import symbols, sympify
from methods.utils.file_utils import read_function, save_results
from methods.part2.multiple_trapezoids.multiple_trapezoids import multiple_trapezoids_method

INPUT_PATH = "methods/part2/richards/input.txt"
OUTPUT_PATH = "methods/part2/richards/output.txt"

x = symbols("x")

def richards(func, a, b):
    Ih1 = multiple_trapezoids_method(func, a, b, 4)
    Ih2 = multiple_trapezoids_method(func, a, b, 2)

    return (4 / 3 * Ih1) - (1 / 3 * Ih2)


def main():
    func, a, b = read_function(INPUT_PATH)
    result = richards(sympify(func), a, b)
    save_results(OUTPUT_PATH, [f"I(f(x)) = {result}"])

if __name__ == "__main__":
    main()