from methods.utils.file_utils import read_vectors, save_results
from methods.utils.math_utils import transpose, matmul, vandermonde
from methods.part1.gauss_elimination.gauss_elimination import gauss_elimination, find_substitutions

from sympy import symbols, Eq

INPUT_PATH = "methods/part2/mmq/input.txt"
OUTPUT_PATH = "methods/part2/mmq/output.txt"

x = symbols('x')

def generate_polynomial(coefficients):
    terms = []
    for i, a in enumerate(coefficients):
        term = f"{a:.6f}"
        if i == 1:
            term += "*x"
        elif i > 1:
            term += f"*x**{i}"
        terms.append(term)
    return "y = " + " + ".join(terms)

def mmq(X, Y, order=1):
    if(len(X) != len(Y)):
        raise ValueError("X and Y must have the same length.")
    
    X_matrix = vandermonde(X, order)

    XT = transpose(X_matrix)
    XT_X = matmul(XT, X_matrix)

    Y_col = [[yi] for yi in Y]
    XT_Y = matmul(XT, Y_col)

    system = []
    for i in range(len(XT_X)):
        row = XT_X[i] + [XT_Y[i][0]]
        system.append(row)

    upper = gauss_elimination(system)
    solution = find_substitutions(upper)

    return solution  

def main():
    X, Y = read_vectors(INPUT_PATH)
    order = 2
    coefficients = mmq(X, Y, order=order)
    result = generate_polynomial(coefficients)
    save_results(OUTPUT_PATH, [result])

if __name__ == "__main__":
    main()
