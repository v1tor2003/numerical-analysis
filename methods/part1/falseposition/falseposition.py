import math
from methods.utils.file_utils import create_out_header, read_function, save_results, save_iter, compute_max_iterations

INPUT_PATH = "methods/part1/falseposition/input.txt"
OUTPUT_PATH = "methods/part1/falseposition/result.txt"

def falseposition_method(func, a, b, tol=1e-5, max_iter=100, out_path=OUTPUT_PATH):
    """
    False Position Method for finding roots of a function.

    Args:
        func (callable): The function for which to find the root.
        a (float): The lower bound of the interval.
        b (float): The upper bound of the interval.
        tol (float): The tolerance for convergence. aka epsilon

    Returns:
        float: The approximate root of the function.
    """
    if func(a) * func(b) >= 0:
        raise ValueError("The function must have different signs at a and b.")

    create_out_header("a\t\t\tb\t\t\tf(a)\t\tf(b)\t\t(bk-ak)\t\tck\t\t\tf(ck)\n", out_path)

    for i in range(max_iter):
        fa = func(a)
        fb = func(b)
        c = (a * fb - b * fa) / (fb - fa)
        fc = func(c)

        save_iter(
            f"{a:6f}\t"
            f"{b:6f}\t"
            f"{fa:6f}\t"
            f"{fb:6f}\t"
            f"{(b - a):6f}\t"
            f"{c:6f}\t"
            f"{fc:6f}\n", out_path)

        if abs(fc) < tol:
            return c, i + 1  # Root found

        if fc * fa < 0:
            b = c
        else:
            a = c

    raise RuntimeError("Max iterations exceeded without convergence")

if __name__ == "__main__":
    func, a, b, tol = read_function(INPUT_PATH)
    max_iter = compute_max_iterations(a, b, tol)

    print("False Position Method")
    print(f"Function: {func}")
    print(f"Interval: [{a}, {b}]")
    print(f"Tolerance: {tol}")
    print(f"Maximum iterations: {max_iter}")

    try:
        res, iterations = falseposition_method(lambda x: eval(func), a, b, tol, max_iter)
        save_results(OUTPUT_PATH, [f"Root: {res}"])
        print(f"Root found: {res}, took {iterations} iterations")
    except Exception as e:
        print(f"Error: {e}")
        save_results(OUTPUT_PATH, [f"Error: {e}"])