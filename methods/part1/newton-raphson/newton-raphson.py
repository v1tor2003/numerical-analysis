import math
from methods.utils.file_utils import save_iter, create_out_header, save_results, compute_max_iterations

INPUT_PATH = "methods/part1/newton-raphson/input.txt"
OUTPUT_PATH = "methods/part1/newton-raphson/result.txt"


def read_function(in_path):
    """Reads a function from a file and returns it as a callable."""
    if(in_path == None):
        raise ValueError("Input path must be specified.")
    
    with open(in_path, 'r') as file:
        lines = file.readlines()
    
    func = lines[0].rstrip()
    dfx = lines[1].rstrip()

    a_str, b_str = lines[2].split()
    a = float(a_str.strip())
    b = float(b_str.strip())

    tol = float(lines[3].strip())

    return func, dfx, a, b, tol

def newton_raphson(func, df, x0, tol=1e-5, max_iter=50, out_path=OUTPUT_PATH):
    """Finds the root of a function using the Newton-Raphson method.

    Args:
        func (callable): The function for which to find the root.
        df (callable): The derivative of the function.
        x0 (float): The initial guess for the root.
        tol (float): The tolerance for convergence.
        max_iter (int): The maximum number of iterations.
        out_path (str): Path to save iteration results.

    Returns:
        float: The approximate root of the function.
    """
    create_out_header("x\t\t\tf(x)\t\tdf(x)\t\tx_new\t\tf(x_new)\n", out_path)

    x = x0
    x_new = None
    fx_new = None
    for i in range(max_iter):
        fx = func(x)
        dfx = df(x)

        if dfx == 0:
            raise ValueError("Derivative is zero. No solution found.")
        
        x_new_str = f"{x_new:.6f}" if x_new is not None else " "
        fx_new_str = f"{fx_new:.6f}" if fx_new is not None else " "

        save_iter(f"{x:.6f}\t{fx:.6f}\t{dfx:.6f}\t{x_new_str}\t{fx_new_str}\n", out_path)

        if abs(fx) <= tol:
            return x, i + 1  # Root found

        x_new = x - fx / dfx
        fx_new = func(x_new)

        if abs(x_new - x) < tol:
            return x_new, i + 1  # Converged

        x = x_new

    raise RuntimeError(f"Max iterations reached without convergence.")


if __name__ == "__main__":
    func, dfx, a, b, tol = read_function(INPUT_PATH)
    max_iter = 100 # compute_max_iterations(a, b, tol)
    x0 = (a + b) / 2  # Initial guess

    print("Newton-Raphson Method")
    print(f"Function: {func}")
    print(f"Interval: [{a}, {b}]")
    print(f"Tolerance: {tol}")
    print(f"Starting guess: {x0:.6f}")
    print(f"Maximum iterations: {max_iter}")

    try:
        root, iters = newton_raphson(lambda x: eval(func), lambda x: eval(dfx), x0, tol, max_iter)
        print(f"Root found: {root:.6f} in {iters} iterations")
        save_results(OUTPUT_PATH, [f"Root: {root:.6f}"])
    except Exception as e:
        print(f"Error: {e}")
        save_results(f"Error: {e}\n", OUTPUT_PATH)

    