from sympy import symbols, sympify
from methods.utils.file_utils import read_function, save_results
from methods.utils.math_utils import intervals

INPUT_PATH = "methods/part2/simpson1by3/input.txt"
OUTPUT_PATH = "methods/part2/simpson1by3/output.txt"

x = symbols("x")

def simpson1by3(func, a, b, n):
	h = (b - a) / (2 * n)
	xi = intervals(a, b, h)
	I = func.subs(x, a) + func.subs(x, b)

	for i in range(1, len(xi) - 1):
		aux = func.subs(x, xi[i])
		if(i % 2 == 0):
			I += 2 * aux
		elif i % 2 != 0:
			I += 4 * aux
	I *= h / 3
	
	return I

def main():
    func, a, b, n = read_function(INPUT_PATH)
    result = simpson1by3(sympify(func), a, b, n)
    save_results(OUTPUT_PATH, [f"I(f(x)) = {result}"])

if __name__ == "__main__":
    main()