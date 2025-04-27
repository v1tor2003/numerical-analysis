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

    tol = float(lines[2].strip())

    return func, a, b, tol

def save_results(out_path, results):
    """Saves the results to a file."""
    if(out_path == None):
        raise ValueError("Output path must be specified.")

    with open(out_path, 'a') as file:
        for result in results:
            file.write(f"{result}\n")