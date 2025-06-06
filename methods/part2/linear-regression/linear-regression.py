from methods.utils.file_utils import read_vectors, save_results

INPUT_PATH = "methods/part2/linear-regression/input.txt"
OUTPUT_PATH = "methods/part2/linear-regression/output.txt"

def linear_regression(X, y):
    n = len(X)
    sum_x = sum(X)
    sum_y = sum(y)
    sum_xy = sum(x * y for x, y in zip(X, y))
    sum_x2 = sum(x ** 2 for x in X)

    a1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
    a0 = (sum_y / n) - (a1 * (sum_x / n))

    return f'{a0} + {a1} * x'

def main():
    X, Y = read_vectors(INPUT_PATH)
    result = linear_regression(X, Y)
    save_results(OUTPUT_PATH, [f"y = {result}"])

if __name__ == "__main__":
    main()

