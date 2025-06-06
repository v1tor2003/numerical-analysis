from sympy import symbols, sympify
from methods.utils.file_utils import read_function, save_results

INPUT_PATH = "methods/part2/multiple_trapezoids/input.txt"
OUTPUT_PATH = "methods/part2/multiple_trapezoids/output.txt"

x = symbols("x")

def interval(x0, xn, h):
    xi = [x0]
    aux = x0 + h

    while (aux < xn):
        xi.append(aux)
        aux = aux + h
    
    xi.append(aux)
    return xi

def multiple_trapezoids_method(func, a, b, n):
    h = (b - a) / n
    xi = interval(a, b, h)
    l = len(xi)
    result = func.subs(x, a) + func.subs(x, b)

    for i in range(1, l - 1):
        result = result + 2 * func.subs(x, xi[i])
    
    result = result * h / 2
    return result

def main():
    func, a, b, n = read_function(INPUT_PATH)
    ab = list(map(float, [a, b]))
    result = multiple_trapezoids_method(sympify(func), ab[0], ab[1], n)
    save_results(OUTPUT_PATH, [f"I(f(x)) = {result}"])

if __name__ == "__main__":
    main()