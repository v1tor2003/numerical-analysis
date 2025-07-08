import math
import numpy as np
from methods.utils.file_utils import read_fds_params, save_results

INPUT_PATH = "methods/part3/shooting/input.txt"
OUTPUT_PATH = "methods/part3/shooting/output.txt"

def resolve_edo(y0, z0, intervalo):
    resultados = []
    for t in intervalo:
        resultados.append([y0, z0])
        y0, z0 = y0 + z0 * (intervalo[1] - intervalo[0]), z0 + (-2 * z0 - y0 + np.sin(t)) * (intervalo[1] - intervalo[0])
    return np.array(resultados)

def shooting(a, b, intervalo, n):  
    def func_obj(z0):
        valores_y = resolve_edo(a, z0, intervalo)
        return valores_y[-1, 0] - b

    valores_z0 = np.linspace(a, b, n)
    for z0 in valores_z0:
        if np.sign(func_obj(z0)) != np.sign(func_obj(a)):
            break

    valores_y = resolve_edo(a, z0, intervalo)

    return valores_y[:, 0]

def main():
    a, b, x, h, n, _ = read_fds_params(INPUT_PATH)

    interval = [x, x + n * h]

    y = shooting(a, b, interval, n)

    save_results(OUTPUT_PATH, [f"a = {a:.6f}"])
    save_results(OUTPUT_PATH, y)
    save_results(OUTPUT_PATH, [f"b = {b:.6f}"])


if __name__ == "__main__":
    main()