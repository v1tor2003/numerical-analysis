import math
from utils.file_utils import save_iter, create_out_header, read_matrix, save_results

INPUT_PATH = "lu-factorization/input.txt"
OUTPUT_PATH = "lu-factorization/result.txt"

def lu_factorization(matrix):
    n = len(matrix)
    L = [[0] * n for _ in range(n)]
    U = [[0] * n for _ in range(n)]

    for i in range(n):
        # Upper Triangular
        for j in range(i, n):
            U[i][j] = matrix[i][j]
            for k in range(i):
                U[i][j] -= L[i][k] * U[k][j]

        # Lower Triangular
        for j in range(i, n):
            if i == j:
                L[i][i] = 1  # Diagonal elements of L are 1
            else:
                L[j][i] = matrix[j][i]
                for k in range(i):
                    L[j][i] -= L[j][k] * U[k][i]
                L[j][i] /= U[i][i]

    return L, U

if __name__ == "__main__":
    matrix = read_matrix(INPUT_PATH)
    n = len(matrix)
    L, U = lu_factorization(matrix)
    create_out_header("LU Factorization Results\n", OUTPUT_PATH)
    save_results(OUTPUT_PATH, "L:")
    save_results(OUTPUT_PATH, L)
    save_results(OUTPUT_PATH, "U:")
    save_results(OUTPUT_PATH, U)