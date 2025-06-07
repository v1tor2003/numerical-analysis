import math
from methods.utils.file_utils import create_out_header, read_matrix, save_results

INPUT_PATH = "methods/part1/lu_factorization/input.txt"
OUTPUT_PATH = "methods/part1/lu_factorization/result.txt"

def forward_substitution(L, b):
    """Solve Ly = b using forward substitution."""
    n = len(L)
    y = [0.0 for _ in range(n)]
    for i in range(n):
        sum_ = sum(L[i][j] * y[j] for j in range(i))
        y[i] = (b[i] - sum_) / L[i][i]
    return y

def backward_substitution(U, y):
    """Solve Ux = y using backward substitution."""
    n = len(U)
    x = [0.0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        sum_ = sum(U[i][j] * x[j] for j in range(i + 1, n))
        if abs(U[i][i]) < 1e-12:
            raise ZeroDivisionError(f"Null pivot found at U[{i}][{i}]")
        x[i] = (y[i] - sum_) / U[i][i]
    return x

def lu_factorization(matrix):
    """Performs LU factorization using Doolittle's method."""
    n = len(matrix)
    A = [row[:] for row in matrix]  
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]

    for i in range(n):
        # Upper triangular
        for j in range(i, n):
            U[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(i))

        # Lower triangular
        for j in range(i, n):
            if i == j:
                L[i][i] = 1.0
            else:
                if abs(U[i][i]) < 1e-12:
                    raise ZeroDivisionError(f"Null pivot found at U[{i}][{i}]")
                L[j][i] = (A[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]

    return L, U

if __name__ == "__main__":
    matrix = read_matrix(INPUT_PATH)
    if not matrix:
        raise ValueError("Matrix is empty or not properly formatted.")

    A = [row[:-1] for row in matrix]
    b = [row[-1] for row in matrix]

    print("LU Factorization Method")

    try:
        L, U = lu_factorization(A)
        y = forward_substitution(L, b)
        x = backward_substitution(U, y)
        solution = [f"x{i} = {x[i]:.6f}" for i in range(len(x))]

        create_out_header("LU Factorization Results\n", OUTPUT_PATH)
        save_results(OUTPUT_PATH, "L")
        save_results(OUTPUT_PATH, L)
        save_results(OUTPUT_PATH, "U")
        save_results(OUTPUT_PATH, U)
        save_results(OUTPUT_PATH, solution)

    except Exception as e:
        save_results(OUTPUT_PATH, f"Erro: {e}")
        print(f"Erro: {e}")
