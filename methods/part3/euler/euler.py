import math
from methods.utils.file_utils import read_equation, save_results

INPUT_PATH = "methods/part3/euler/input.txt"
OUTPUT_PATH = "methods/part3/euler/output.txt"

def euler(f, x0, y0, h, k):
    x_list = [x0]
    y_list = [y0]
    x = x0
    y = y0

    for _ in range(k):
        y = y + h * f(x, y)
        x = x + h

        x_list.append(x)
        y_list.append(y)

    return x_list, y_list

def main():
    equation, x0, y0, h, k = read_equation(INPUT_PATH)
    func = lambda x = 0, y = 0: eval(equation)
    xr, yr = euler(func, x0, y0, h, k)

    results = [f"x{i} = {xr[i]}  ||  y{i} = {yr[i]}" for i in range(len(xr))]
    save_results(OUTPUT_PATH, results)

if __name__ == "__main__":
    main()