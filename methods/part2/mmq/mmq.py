from methods.utils.file_utils import read_vectors, save_results
from methods.utils.math_utils import transpose, matmul
from methods.part1.gauss_elimination.gauss_elimination import gauss_elimination, find_substitutions

from sympy import symbols, Eq

INPUT_PATH = "methods/part2/mmq/input.txt"
OUTPUT_PATH = "methods/part2/mmq/output.txt"

x = symbols('x')

def mmq(X, Y):
    n = len(X)
    sum_X = sum(X)
    sum_Y = sum(Y)
    sum_X2 = sum(x ** 2 for x in X)
    sum_XY = sum(x*y for x, y in zip(X, Y))

    matrix = [
        [sum_X2, sum_X,  sum_XY],
        [sum_X,  n,      sum_Y]
    ]

    upper = gauss_elimination(matrix)
    solution = find_substitutions(upper)

    return solution

def main():
    X, Y = read_vectors(INPUT_PATH)
    a, b = mmq(X, Y)
    save_results(OUTPUT_PATH, [f"y = {a} * x + {b}"])

if __name__ == "__main__":
    main()
