import math, sys
from utils.file_utils import save_iter, create_out_header, read_function, save_results

OUTPUT_PATH = "secant/result.txt"
INPUT_PATH = "secant/input.txt"

def secant_method(func, a, b, tol=1e-5, out_path=OUTPUT_PATH):
    create_out_header(
        "xn\t\t\t\t\tf(xn)\n"
        f"{a:6f}\t\t\t{func(a):6f}\n",
        out_path
    )

    while True:
        f1 = func(a)
        f2 = func(b)

        save_iter(f"{b:6f}\t\t\t{f2:6f}\n", out_path)

        if abs(f2) <= tol:
            return b

        if a == b:
            print("Zero division ahead\n")
            sys.exit()

        b_temp = b
        b = (f2 * a - f1 * b) / (f2 - f1)
        a = b_temp

if __name__ == "__main__":
    func, a, b, tol = read_function(INPUT_PATH)

    print("Secant Method")
    print(f"Function: {func}")
    print(f"Interval: [{a}, {b}]")
    print(f"Tolerance: {tol}")

    res = secant_method(lambda x: eval(func), a, b, tol)
    save_results(OUTPUT_PATH, [f"Root: {res}"])
    print(f"Root found: {res}")