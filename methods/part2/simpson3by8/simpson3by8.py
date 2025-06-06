from sympy import symbols, sympify
from methods.utils.file_utils import read_function, save_results
from methods.utils.math_utils import intervals

INPUT_PATH = "methods/part2/simpson3by8/input.txt"
OUTPUT_PATH = "methods/part2/simpson3by8/output.txt"

x = symbols("x")

def simpson3by8(func, a, b, n):
	h = (b - a) / (2 * n)
	xi = intervals(a, b, h)
	I = func.subs(x, a) + func.subs(x, b)
	count = 0

	for i in range(1, len(xi) - 1):
		aux = func.subs(x, xi[i])

		if(count >= 2):
			I += 2 * aux
			count = 0
		elif count < 2:
			I += 3 * aux
			count += 1
			
	I *= (3 * h) / 8

	return I

def main():
    func, a, b, n = read_function(INPUT_PATH)
    ab = list(map(float, [a, b]))
    result = simpson3by8(sympify(func), ab[0], ab[1], n)
    save_results(OUTPUT_PATH, [f"I(f(x)) = {result}"])

if __name__ == "__main__":
    main()