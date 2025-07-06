import math
from methods.utils.file_utils import read_equation, save_results

INPUT_PATH = "methods/part3/ralston/input.txt"
OUTPUT_PATH = "methods/part3/ralston/output.txt"

def ralston(f, x0, y0, h, n):
    x_list = [x0]
    y_list = [y0]

    for i in range(n):
        k0 = f(x0, y0)
        k1 = f(x0 + 0.75 * h, y0 + 0.75 * h * k0)

        y0 = y0 + h * ((1 / 3 * k0) + (2 / 3 * k1))
        x0 = x0 + h

        x_list.append(x0)
        y_list.append(y0)

    return x_list, y_list

def main():
    equation, x0, y0, h, k = read_equation(INPUT_PATH)
    func = lambda x = 0, y = 0: eval(equation)
    xr, yr = ralston(func, x0, y0, h, n=k)

    results = [f"x{i} = {xr[i]}  ||  y{i} = {yr[i]}" for i in range(len(xr))]
    save_results(OUTPUT_PATH, results)

if __name__ == "__main__":
    main()