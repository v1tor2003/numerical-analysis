import math

def compute_max_iterations(a, b, tol=1e-5):
    return math.ceil(math.log2(abs(b - a) / tol))

def create_out_header(header_str, out_path):
    """Creates the output file and writes the header."""
    if(out_path == None):
        raise ValueError("Output path must be specified.")
    
    with open(out_path, "w") as file:
        file.write(header_str)

def save_iter(iter_str, out_path):
    """Saves the current iteration data to the result file."""
    if(out_path == None):
        raise ValueError("Output path must be specified.")

    with open(out_path, "a") as file:
        file.write(iter_str)

def save_results(out_path, results):
    """Saves the results to a file."""
    if(out_path == None):
        raise ValueError("Output path must be specified.")

    with open(out_path, 'a') as file:
        for result in results:
            file.write(f"{result}\n")

def read_function(in_path):
    """Reads a function from a file and returns it as a callable."""
    if(in_path == None):
        raise ValueError("Input path must be specified.")
    
    with open(in_path, 'r') as file:
        lines = file.readlines()
    
    func = lines[0].rstrip()
    
    a_str, b_str = lines[1].split()
    a = float(a_str.strip())
    b = float(b_str.strip())

    tol = float(lines[2].strip()) if len(lines) > 2 else None
    if tol is None:
        return func, a, b
    return func, a, b, tol

def read_matrix(in_path):
    """Reads a matrix from a file."""
    if(in_path == None):
        raise ValueError("Input path must be specified.")
    
    with open(in_path, 'r') as file:
        lines = file.readlines()
    
    matrix = []
    for line in lines:
        row = list(map(float, line.split()))
        matrix.append(row)
    
    return matrix

def read_matrix_with_tol(in_path):
    """Reads a matrix from a file with tolerance as its first line."""
    if(in_path == None):
        raise ValueError("Input path must be specified.")
    
    with open(in_path, 'r') as file:
        lines = file.readlines()

    if not lines:
        raise ValueError("File is empty.")
    
    try:
        tol = float(lines[0].strip())
        lines = lines[1:]
    except ValueError:
        raise ValueError("First line must be a float representing the tolerance.")

    matrix = []
    for line in lines:
        row = list(map(float, line.split()))
        matrix.append(row)
    
    return tol, matrix

def read_edo_equation(in_path):
    """Reads an equation and its parameters from a file."""
    if(in_path == None):
        raise ValueError("Input path must be specified.")
    
    with open(in_path, 'r') as file:
        lines = file.readlines()
    
    if len(lines) < 4:
        raise ValueError("Input file must contain at least 4 lines.")

    equation = lines[0].strip()
    x0_str, y0_str = lines[1].split()
    x0 = float(x0_str.strip())
    y0 = float(y0_str.strip())
    h = float(lines[2].strip())
    k = int(lines[3].strip())

    return equation, x0, y0, h, k

def read_fds_params(in_path):
    """ Reads params for the finite diff and shooting methods from a file."""
    if(in_path == None):
        raise ValueError("Input path must be specified.")
    
    with open(in_path, 'r') as file:
        lines = file.readlines()

    a_str, b_str = lines[0].split()
    a = float(a_str.strip())
    b = float(b_str.strip())
    x = float(lines[1].strip())
    h = float(lines[2].strip()) 
    points = int(lines[3].strip())
    Ta = float(lines[4].strip())

    return a, b, x, h, points, Ta

def read_vectors(in_path):
    """Reads vectors from a file."""
    if(in_path == None):
        raise ValueError("Input path must be specified.")
    
    with open(in_path, 'r') as file:
        lines = file.readlines()
    
    vectors = []
    for line in lines:
        vector = list(map(float, line.split()))
        vectors.append(vector)
    
    return vectors

