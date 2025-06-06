from sympy import symbols, Poly
from methods.utils.file_utils import read_vectors, save_results

INPUT_PATH = "methods/part2/newton/input.txt"
OUTPUT_PATH = "methods/part2/newton/output.txt"

x = symbols('x')

def divided_difference_table(values, points):
    n = len(points)
    if n == 1:
        return values[points[0]]
    elif n == 2:
        return (values[points[0]] - values[points[1]]) / (points[0] - points[1])
    else:
        return (
            divided_difference_table(values, points[:-1]) -
            divided_difference_table(values, points[1:])
        ) / (points[0] - points[-1])

def newton_interpolation(values, points):
    term = 1
    result = 0
    used_points = []

    for i, point in enumerate(points):
        used_points.append(point)
        result += term * divided_difference_table(values, used_points)
        term *= Poly(x - point)

    return str(result.args[0])  


def main():
    points, values_list = read_vectors(INPUT_PATH)
    values = dict(zip(points, values_list))

    polynomial = newton_interpolation(values, points)
    save_results(OUTPUT_PATH, [f"P(x) = {polynomial}"])

if __name__ == "__main__":
    main()