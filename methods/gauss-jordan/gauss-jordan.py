import math, sys
from utils.file_utils import save_iter, create_out_header, read_matrix_with_tol, save_results

OUTPUT_PATH = "gauss-jordan/result.txt"
INPUT_PATH = "gauss-jordan/input.txt"

def gauss_jordan(matrix, tol=1e-5, out_path=OUTPUT_PATH):
    n = len(matrix)
    m = len(matrix[0]) 

    create_out_header("Gauss-Jordan Method Results\n" 
                      + "\t".join([f"x{i}\t\t" for i in range(n)]) + "\n", out_path)

    for i in range(n):
        pivot = matrix[i][i] # main pivot element

        if abs(pivot) < tol:
            # line to swap
            for k in range(i + 1, n):
                if abs(matrix[k][i]) > tol:
                    matrix[i], matrix[k] = matrix[k], matrix[i]
                    pivot = matrix[i][i]
                    break
            else:
                raise ZeroDivisionError(f"Valid pivot not found for {i}")

        # Normalize pivot row
        for j in range(m):
            matrix[i][j] /= pivot

        # delete row 1
        for k in range(n):
            if k != i:
                factor = matrix[k][i]
                for j in range(m):
                    matrix[k][j] -= factor * matrix[i][j]
        save_iter("\n".join("\t".join(f"{elem:.6f}" for elem in row) for row in matrix) + "\n\n", out_path)

    solution = [row[-1] for row in matrix]

    return solution


if __name__ == "__main__":
    tol, matrix = read_matrix_with_tol(INPUT_PATH)

    print("Gauss-Jordan Method")
    print(f"Tolerance: {tol}")

    try:
        solution = gauss_jordan(matrix, tol, OUTPUT_PATH)
        solution = [f"x{i} = {solution[i]:.6f}" for i in range(len(solution))]
        save_results(OUTPUT_PATH, solution)
    except Exception as e:
        save_results(OUTPUT_PATH, f"Erro: {e}")
        print(f"Erro: {e}")