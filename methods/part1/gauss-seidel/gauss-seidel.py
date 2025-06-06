import math, sys
from methods.utils.file_utils import save_iter, create_out_header, read_matrix_with_tol, save_results

INPUT_PATH = "methods/part1/gauss-seidel/input.txt"
OUTPUT_PATH = "methods/part1/gauss-seidel/result.txt"

def gauss_seidel_method(matrix, tol=1e-5, max_iter=100, out_path=OUTPUT_PATH):
    """
        Gauss-Seidel method for solving a system of linear equations.
        Args:
            matrix (list of list of floats): Coefficient matrix augmented with the constants.
            tol (float): Tolerance for convergence.
            max_iter (int): Maximum number of iterations.
            out_path (str): Path to save the output results.
    """
   
    n = len(matrix)
    A = [row[:-1] for row in matrix]
    b = [row[-1] for row in matrix]
    x = [0.0 for _ in range(n)]  # initial guess

    create_out_header("Gauss-Seidel Method Results\n" 
                      + "\t".join([f"x{i}\t\t" for i in range(n)]) + "\n", out_path)

    for it in range(1, max_iter + 1):
        x_old = x[:]
        for i in range(n):
            s1 = sum(A[i][j] * x[j] for j in range(i))              # using updated values
            s2 = sum(A[i][j] * x_old[j] for j in range(i + 1, n))   # using last iteration values
            x[i] = (b[i] - s1 - s2) / A[i][i]

        save_iter("\t".join([f"{xi:.6f}" for xi in x]) + "\n", out_path)

        if all(abs(x[i] - x_old[i]) < tol for i in range(n)):
            return x, it

    raise RuntimeError("Max iterations reached but it did not converge.") 


if __name__ == "__main__":
    tol, matrix = read_matrix_with_tol(INPUT_PATH)
    max_iter = 100

    print("Gauss-Seidel Method")
    print("Tolerance:", tol)

    try:
        solution, iters = gauss_seidel_method(matrix, tol, max_iter, OUTPUT_PATH)
        solution = [f"x{i} = {solution[i]:.6f}" for i in range(len(solution))]
        save_results(OUTPUT_PATH, solution)
    except Exception as e:
        save_results(OUTPUT_PATH, f"\nErro: {e}")
        print(f"Erro: {e}")