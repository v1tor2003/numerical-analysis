import math
import numpy as np
from methods.utils.file_utils import read_fds_params, save_results

INPUT_PATH = "methods/part3/shooting/input.txt"
OUTPUT_PATH = "methods/part3/shooting/output.txt"

def resolve_edo(y0, z0, intervals):
    results = []
    for t in intervals:
        results.append([y0, z0])
        y0, z0 = y0 + z0 * (intervals[1] - intervals[0]), z0 + (-2 * z0 - y0 + np.sin(t)) * (intervals[1] - intervals[0])
    return np.array(results)

def shooting(a, b, intervals, n):  
    def func_obj(z0):
        ys = resolve_edo(a, z0, intervals)
        return ys[-1, 0] - b

    z0_values = np.linspace(a, b, n)
    for z0 in z0_values:
        if np.sign(func_obj(z0)) != np.sign(func_obj(a)):
            break

    ys = resolve_edo(a, z0, intervals)

    return ys[:, 0]

def main():
    a, b, x, h, n, _ = read_fds_params(INPUT_PATH)

    interval = [x, x + n * h]

    y = shooting(a, b, interval, n)

    save_results(OUTPUT_PATH, [f"a = {a:.6f}"])
    save_results(OUTPUT_PATH, y)
    save_results(OUTPUT_PATH, [f"b = {b:.6f}"])


if __name__ == "__main__":
    main()