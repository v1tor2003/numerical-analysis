from methods.utils.file_utils import read_function, save_results
from methods.utils.math_utils import f

INPUT_PATH = "methods/part2/derivative_2order/input.txt"
OUTPUT_PATH = "methods/part2/derivative_2order/output.txt"

def derivative_2order(fx, h):
    derivatives = []
    n = len(fx)
    
    for i in range(1, n - 1):
        derivada = (fx[i + 1] - 2 * fx[i] + fx[i - 1]) / (h ** 2)
        derivatives.append(derivada)
    
    return derivatives

def main():
    func, x, h = read_function(INPUT_PATH) 
    fx = [f(x - h, func), f(x, func), f(x + h, func)]
    result = derivative_2order(fx, h)[0]
    save_results(OUTPUT_PATH, [f"D2fx(x) = {result}"])

if __name__ == "__main__":
    main()