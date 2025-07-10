import math
from methods.utils.file_utils import read_edo_equation, save_results
from methods.utils.list_utils import format_xy_to_list

INPUT_PATH = "methods/part3/runge_kutta_3order/input.txt"
OUTPUT_PATH = "methods/part3/runge_kutta_3order/output.txt"

def runge_kutta_3order(f, xk, yk, h, n):
    x_list = [xk]
    y_list = [yk]

    for i in range(n):
        k1 = h * f(xk, yk)
        k2 = h * f(xk + (0.5 * h), yk + (0.5 * k1))
        k3 = h * f(xk + (0.75 * h), yk + (0.75 * k2))

        yk = yk + (1 / 9) * ((2 * k1) + (3 * k2) + (4 * k3))
        xk = xk + h

        x_list.append(xk)
        y_list.append(yk)

    return x_list, y_list

def main():
    equation, x0, y0, h, k = read_edo_equation(INPUT_PATH)
    func = lambda x = 0, y = 0: eval(equation)
    xr, yr = runge_kutta_3order(func, x0, y0, h, n=k)

    results = format_xy_to_list(xr, yr)
    save_results(OUTPUT_PATH, results)

if __name__ == "__main__":
    main()