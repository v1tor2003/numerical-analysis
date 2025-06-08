## Project: Numerical Methods — Solving Equations, Linear Systems and Interpolation

### Description

This project gathers the implementation of several classical numerical methods, organized into two main parts:

* **Part 1**: Solving nonlinear equations and linear systems.
* **Part 2**: Interpolation, numerical derivatives, and integration.

The algorithms are implemented in Python with a focus on modularity, component reuse, and automatic report generation. Each method is executed using input files (`input.txt`), and the results are saved to output files (`result.txt`).

> ⚠️ **Note**: To run any method, the script must be executed from the **root folder** of the project. Additionally, the `sympy` library must be installed.

---

### Implemented Methods

#### Part 1 — Equations and Linear Systems

##### Nonlinear Equations (single variable)

* **Bisection**
* **False Position (Regula Falsi)**
* **Newton-Raphson**
* **Secant**

##### Linear Systems

**Direct Methods:**

* **Gauss Elimination**
* **LU Factorization (Doolittle)**
* **Gauss-Jordan**

**Iterative Methods:**

* **Jacobi**
* **Gauss-Seidel**

#### Part 2 — Interpolation, Derivatives, and Integrals

##### Interpolation and Curve Fitting

* **Lagrange Interpolation**
* **Newton Interpolation**
* **Simple Linear Regression**
* **Least Squares (LSQ)**

##### Numerical Derivatives

* **First-Order Derivative**
* **Second-Order Derivative**
* **Richardson Extrapolation**

##### Numerical Integration

* **Simple Trapezoidal Rule**
* **Multiple Trapezoids**
* **Simpson’s 1/3 Rule**
* **Simpson’s 3/8 Rule**
* **Gaussian Quadrature**

---

### Project Structure

```
/methods
│
├── part1/
│   ├── bisection/
│   ├── falseposition/
│   ├── newton_raphson/
│   ├── secant/
│   ├── gauss_elimination/
│   ├── lu_factorization/
│   ├── gauss_jordan/
│   ├── jacobi/
│   └── gauss_seidel/
│
├── part2/
│   ├── lagrange/
│   ├── newton/
│   ├── linear-regression/
│   ├── mmq/
│   ├── derivative_1order/
│   ├── derivative_2order/
│   ├── richards/
│   ├── simple_trapeze/
│   ├── multiple_trapezoids/
│   ├── simpson1by3/
│   ├── simpson3by8/
│   └── gauss/
│
├── utils/
│   └── file_utils.py
```

---

### Input File Format

#### Nonlinear Equations (e.g., Bisection, Newton-Raphson)

```
# input.txt
1 - (1 + x + x**2 / 2) * math.exp(-x) - 0.1     # f(x)
(x**2 / 2) * math.exp(-x)                       # f'(x), if needed
0.1 1.0                                         # Interval [a, b]
0.0001                                          # Tolerance
```

#### Linear Systems (e.g., Gauss, LU, Jacobi)

```
# input.txt
0.0001
10 -1 2 6
-1 11 -1 25
2 -1 10 -11
```

The last column represents vector \$b\$ in the system \$Ax = b\$.

---

### Output Report

Each `result.txt` file includes:

* Detailed iterations
* Tabular formatting (for iterative methods)
* Final root or solution
* Error messages, if any

---

### Requirements

* **Python 3.10+**
* **External library:** `sympy`
  Install it with:

  ```bash
  pip install sympy
  ```

---

### Execution

Run the scripts from the **root folder** of the project:

```bash
python -m methods.part<number>.<method_name>.<methodname>
```

---

### Author

Project developed by **Vitor Pires** as part of the course **DEX000086 - Numerical Analysis**.

