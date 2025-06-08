from methods.utils.file_utils import read_function, save_results
from methods.utils.math_utils import f

INPUT_PATH = "methods/part2/derivative_1order/input.txt"
OUTPUT_PATH = "methods/part2/derivative_1order/output.txt"

def derivative_1order(fx, h):
    derivatives = []
    n = len(fx)
    for i in range(n - 1):
        derivada = (fx[i + 1] - fx[i]) / h
        derivatives.append(derivada)

    return derivatives

def main():
    func, x, h = read_function(INPUT_PATH) 
    fx = [f(x, func), f(x + h, func)]
    result = derivative_1order(fx, h)[0]
    save_results(OUTPUT_PATH, [f"Dfx(x) = {result}"])

if __name__ == "__main__":
    main()