import math
from methods.utils.file_utils import save_results, read_function
from methods.part1.gauss_elimination.gauss_elimination import gauss_elimination, find_substitutions

INPUT_PATH = "methods/part3/finite_differences/input.txt"
OUTPUT_PATH = "methods/part3/finite_differences/output.txt"

def finite_differences(a, b, alpha, beta, n, f):
    h = (b - a) / (n + 1)
    xs = [a + (i + 1) * h for i in range(n)]  # Interior points

    # Create matrix A (tridiagonal: 2 on diag, -1 on off-diag)
    A = [[0.0] * n for _ in range(n)]
    for i in range(n):
        A[i][i] = 2.0
        if i > 0:
            A[i][i - 1] = -1.0
        if i < n - 1:
            A[i][i + 1] = -1.0

    # Construct RHS vector b with -h^2 * f(x)
    b_vec = [-f(x) * h**2 for x in xs]
    b_vec[0] += alpha
    b_vec[-1] += beta

    # Augmented matrix for Gauss
    augmented = [A[i] + [b_vec[i]] for i in range(n)]
    solution = gauss_elimination(augmented)
    y_inner = find_substitutions(solution)

    xs_full = [a] + xs + [b]
    ys_full = [alpha] + y_inner + [beta]

    return xs_full, ys_full

def main():
    func, a, b, n = read_function(INPUT_PATH)
    alpha = 0.0
    beta = 1.0
    fxx = lambda x: eval(func)

    xs, ys = finite_differences(a, b, alpha, beta, int(n), fxx)

    results = []
    for x, y in zip(xs, ys):
        line = f"x = {x:.6f}, y = {y:.6f}"
        results.append(line)

    save_results(OUTPUT_PATH, results)

if __name__ == "__main__":
    main()
