import math
from methods.utils.file_utils import save_iter, create_out_header, read_matrix, save_results, compute_max_iterations

INPUT_PATH = "methods/part1/gauss_elimination/input.txt"
OUTPUT_PATH = "methods/part1/gauss_elimination/result.txt"

def formatted_solution(solution):
    """
    Format the solution for output.
    """
    formatted = []
    for i, value in enumerate(solution):
        formatted.append(f"x{i} = {value:.6f}")
    return formatted

def find_substitutions(matrix):
    """
    Find the substitutions in the matrix.
    The matrix should be in augmented form.
    """
    n = len(matrix)

    solution = [0] * n
    for i in range(n - 1, -1, -1):
        solution[i] = matrix[i][-1] / matrix[i][i]
        for j in range(i + 1, n):
            solution[i] -= (matrix[i][j] / matrix[i][i]) * solution[j]

    return solution

def gauss_elimination(matrix):
    """
    Perform Gauss elimination on the given matrix.
    The matrix should be in augmented form.
    """
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        pivot = matrix[i][i]

        # If the pivot is zero, try to swap with a non-zero row
        if pivot == 0:
            for k in range(i + 1, n):
                if matrix[k][i] != 0:
                    matrix[i], matrix[k] = matrix[k], matrix[i]
                    pivot = matrix[i][i]  # update pivot!
                    break
            else:
                raise ZeroDivisionError(f"Cannot eliminate: zero pivot at row {i}")

        # Eliminate below
        for j in range(i + 1, n):
            factor = matrix[j][i] / pivot
            for k in range(i, m):
                matrix[j][k] -= factor * matrix[i][k]

    return matrix


if __name__ == "__main__":
    matrix = read_matrix(INPUT_PATH)
    if not matrix:
        raise ValueError("Matrix is empty or not properly formatted.")
    
    print("Gauss Elimination Method")

    matrix_two = gauss_elimination(matrix)
    solution = formatted_solution(find_substitutions(matrix_two))
    create_out_header("Gauss Elimination Results\n", OUTPUT_PATH)
    save_results(OUTPUT_PATH, matrix_two)
    save_results(OUTPUT_PATH, solution)