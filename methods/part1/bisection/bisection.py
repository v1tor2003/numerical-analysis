import math
from methods.utils.file_utils import save_iter, create_out_header, read_function, save_results, compute_max_iterations

INPUT_PATH = "methods/part1/bisection/input.txt"
OUTPUT_PATH = "methods/part1/bisection/result.txt"

def bisection_method(func, a, b, tol=1e-5, max_iter=1000, out_path=OUTPUT_PATH):
    """Finds the root of a function using the bisection method.

    Args:
        func (callable): The function for which to find the root.
        a (float): The lower bound of the interval.
        b (float): The upper bound of the interval.
        tol (float): The tolerance for convergence. aka epsilon
        max_iter (int): The maximum number of iterations.

    Returns:
        float: The approximate root of the function.
    """
    if func(a) * func(b) >= 0:
        raise ValueError("The function must have different signs at a and b.")

    create_out_header("a\t\t\tb\t\t\tf(a)\t\tf(b)\t\t(b-a)\t\t(b-a)/a\t\tx\t\t\tf(x)\n", out_path)

    for i in range(max_iter):
        c = (a + b) / 2
        fa = func(a)
        fb = func(b)
        fc = func(c)

        save_iter(
            f"{a:.6f}\t{b:.6f}\t{fa:.6f}\t{fb:.6f}\t{(b - a):.6f}\t"
            f"{((b - a) / a):.6f}\t{c:.6f}\t{fc:.6f}\n" if a != 0 
            else f"{a:.6f}\t{b:.6f}\t{fa:.6f}\t{fb:.6f}\t{(b - a):.6f}\tinf\t{c:.6f}\t{fc:.6f}\n", out_path)

        if abs(fc) < tol or (b - a) / 2 < tol:
            return c, i + 1  # Root found

        if fc * fa < 0:
            b = c  # Root is in left half
        else:
            a = c  # Root is in right half

    raise RuntimeError("Maximum iterations reached without convergence.")

if __name__ == "__main__":
    func, a, b, tol = read_function(INPUT_PATH)
    max_iter = compute_max_iterations(a, b, tol)
    
    print("Bisection Method")
    print(f"Function: {func}")
    print(f"Interval: [{a}, {b}]")
    print(f"Tolerance: {tol}")
    print(f"Maximum iterations: {max_iter}")
    
    try:
        res, iterations = bisection_method(lambda x: eval(func), a, b, tol, max_iter)
        save_results(OUTPUT_PATH, [f"Root: {res}"])
        print(f"Root found: {res}, took {iterations} iterations")
    except Exception as e:
        print(f"Error: {e}")
        save_results(OUTPUT_PATH, [f"Error: {e}"])