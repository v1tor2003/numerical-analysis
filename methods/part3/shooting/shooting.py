import math
from methods.part3.runge_kutta_4order.runge_kutta_4order import runge_kutta_4order
from methods.utils.file_utils import read_function, save_results

INPUT_PATH = "methods/part3/shooting/input.txt"
OUTPUT_PATH = "methods/part3/shooting/output.txt"

def shooting_method(f, a, b, alpha, beta, s0, s1, h, tol=1e-6, max_iter=50):
    """
    Solves a boundary value problem using the shooting method with RK4.
    
    Parameters:
        f      : function f(x, y, z) where z = dy/dx
        a, b   : endpoints of the interval
        alpha  : y(a)
        beta   : y(b)
        s0, s1 : initial guesses for y'(a)
        h      : step size
        tol    : tolerance for convergence at y(b)
        max_iter: maximum number of iterations for shooting

    Returns:
        x_list, y_list: lists of x and y values for the final integrated solution
    """
    def system(x, Y):
        y, z = Y
        return [z, f(x, y, z)]

    def rk4_vector(f_vec, x0, Y0, h, n):
        x_list = [x0]
        y_list = [Y0[0]]
        xk = x0
        Yk = Y0

        for _ in range(n):
            k1 = [h * val for val in f_vec(xk, Yk)]
            k2_input = [Yk[i] + 0.5 * k1[i] for i in range(2)]
            k2 = [h * val for val in f_vec(xk + 0.5 * h, k2_input)]
            k3_input = [Yk[i] + 0.5 * k2[i] for i in range(2)]
            k3 = [h * val for val in f_vec(xk + 0.5 * h, k3_input)]
            k4_input = [Yk[i] + k3[i] for i in range(2)]
            k4 = [h * val for val in f_vec(xk + h, k4_input)]

            Yk = [Yk[i] + (1/6)*(k1[i] + 2*k2[i] + 2*k3[i] + k4[i]) for i in range(2)]
            xk = xk + h

            x_list.append(xk)
            y_list.append(Yk[0])

        return x_list, y_list, Yk  # final Yk contains [y, y']

    n = int((b - a) / h)

    for _ in range(max_iter):
        # First guess
        _, _, Y_end0 = rk4_vector(system, a, [alpha, s0], h, n)
        F0 = Y_end0[0] - beta

        # Second guess
        _, _, Y_end1 = rk4_vector(system, a, [alpha, s1], h, n)
        F1 = Y_end1[0] - beta

        if abs(F1) < tol:
            x_vals, y_vals, _ = rk4_vector(system, a, [alpha, s1], h, n)
            return x_vals, y_vals

        # Secant update
        s = s1 - F1 * (s1 - s0) / (F1 - F0)

        # Prepare for next iteration
        s0, s1 = s1, s

    raise RuntimeError("Shooting method did not converge.")

def main():
    equation, a, b, h = read_function(INPUT_PATH)
    alpha = 0.0
    beta = 2.0

    s0 = 0.0  # Initial guess for y'(a)
    s1 = 1.0  # Second guess for y'(a)

    def f(x, y, y_prime):
        return eval(equation)

    xs, ys = shooting_method(f, a, b, alpha, beta, s0, s1, h)

    results = [f"x = {xs[i]:.6f},  y = {ys[i]:.6f}" for i in range(len(xs))]
    save_results(OUTPUT_PATH, results)


if __name__ == "__main__":
    main()