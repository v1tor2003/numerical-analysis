from sympy import symbols, expand
from methods.utils.file_utils import read_vectors, save_results

INPUT_PATH = "methods/part2/lagrange/input.txt"
OUTPUT_PATH = "methods/part2/lagrange/output.txt"

def lagrange_interpolation(xi, fk):
    x = symbols('x')
    lk = []
    result = 0

    for i in range(len(xi)):
        termo = 1
        for j in range(len(xi)):
            if i != j:
                termo *= (x - xi[j]) / (xi[i] - xi[j])
        lk.append(termo)

    for i in range(len(xi)):
        result += lk[i] * fk[i]

    return expand(result)

def main():
    X, Y = read_vectors(INPUT_PATH)

    result = lagrange_interpolation(X, Y)
    save_results(OUTPUT_PATH, [f"y = {result}"])

if __name__ == "__main__":
    main()
