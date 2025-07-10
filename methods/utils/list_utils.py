import math

def format_xy_to_list(x, y):
    """
    Formats two lists of x and y values into a list of strings.
    """
    return [f"x{i} = {x[i]:.6f}, y{i} = {y[i]:.6f}" for i in range(len(x))]