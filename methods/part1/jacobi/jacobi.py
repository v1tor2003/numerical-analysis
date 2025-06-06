import math
from methods.utils.file_utils import save_iter, create_out_header, read_matrix_with_tol, save_results

INPUT_PATH = "methods/part1/jacobi/input.txt"
OUTPUT_PATH = "methods/part1/jacobi/result.txt"

def jacobi_method(matrix, tol=1e-5, max_iter=100, out_path=OUTPUT_PATH):
    """
        Jacobi method for solving a system of linear equations.
        Args:
            matrix (list of list of floats): Coefficient matrix augmented with the constants.
            tol (float): Tolerance for convergence.
            max_iter (int): Maximum number of iterations.
            out_path (str): Path to save the output results.
    """
   
    n = len(matrix)
    A = [row[:-1] for row in matrix]
    b = [row[-1] for row in matrix]
    x_old = [0.0 for _ in range(n)]  # inital guess
    x_new = x_old[:]

    create_out_header("Jacobi Method Results\n" + "\t".join([f"x{i}\t\t" for i in range(n)]) + "\n", out_path)

    for it in range(1, max_iter + 1):
        for i in range(n):
            sum_ = sum(A[i][j] * x_old[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum_) / A[i][i]

        save_iter("\t".join([f"{xi:.6f}" for xi in x_new]) + "\n", out_path)

        # Check convergence
        if all(abs(x_new[i] - x_old[i]) < tol for i in range(n)):
            return x_new, it

        x_old = x_new[:]

    raise RuntimeError("Max iterations reached but it did not converge.")

if __name__ == "__main__":
    tol, matrix = read_matrix_with_tol(INPUT_PATH)
    max_iter = 100

    print("Jacobi Method")
    print("Tolerance:", tol)

    try:
        solution, iters = jacobi_method(matrix, tol, max_iter, OUTPUT_PATH)
        solution = [f"x{i} = {solution[i]:.6f}" for i in range(len(solution))]
        save_results(OUTPUT_PATH, solution)
    except Exception as e:
        save_results(OUTPUT_PATH, f"\nErro: {e}")
        print(f"Erro: {e}")