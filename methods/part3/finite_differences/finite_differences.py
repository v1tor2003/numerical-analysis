import math
from methods.utils.file_utils import save_results, read_fds_params

INPUT_PATH = "methods/part3/finite_differences/input.txt"
OUTPUT_PATH = "methods/part3/finite_differences/output.txt"

def format_result(results):
    strs = [f"{item:.6f}\n" if i < len(results) - 1 else f"{item:.6f}" for i, item in enumerate(results)]
    return "".join(strs)

def finite_differences(a, b, x, h, points, Ta):
    matrix = []
    b_vec = []
    aux = 0
    Dx = x/points
    
    for _ in range(points - 1):
        aux_vec = []

        for _ in range(points - 1):
            aux_vec.append(0)
        
        if aux == 0:
            aux_vec[aux] = (2 + h * Dx**2)
            aux_vec[aux+1] = -1
        elif aux == points - 2:
            aux_vec[aux] = (2 + h * Dx**2)
            aux_vec[aux-1] = -1
        else:
            aux_vec[aux] = (2 + h * Dx**2)
            aux_vec[aux+1] = -1
            aux_vec[aux-1] = -1

        matrix.append(aux_vec)
        aux+=1
        
    b_vec.append(h * (Dx**2) * Ta + a)

    for _ in range(points-3):
        b_vec.append(h * (Dx**2) * Ta)

    b_vec.append(h * (Dx**2) * Ta + b)
            
    A = lu_factorization(matrix)
    y = lower_triangular(A, b_vec)
    result = upper_triangular(A, y)
    
    return result

def lu_factorization(matriz):
    n = len(matriz)

    for k in list(range(1,n,1)):
        for i in list(range(k+1,n+1,1)):
            m = matriz[i-1][k-1]/matriz[k-1][k-1]
            matriz[i-1][k-1] = m
            for j in list(range(k+1,n+1,1)):
                matriz[i-1][j-1] = matriz[i-1][j-1] - m*matriz[k-1][j-1]
    
    return matriz

def lower_triangular(L,b):
    n = len(b)
    y = [0]*n
    
    for i in list(range(1,n+1,1)):
        s = 0
        for j in list(range(1, i,1)):
            s = s + L[i-1][j-1]*y[j-1]

        y[i-1] = b[i-1] - s

    return y

def upper_triangular(U,b):
    n =  len(b)
    x = [0]*n
    x[n-1] = b[n-1]/U[n-1][n-1]

    for i in list(range(n-1,0,-1)):
        s = 0
        for j in list(range(i+1,n+1,1)):
            s = s + U[i-1][j-1]*x[j-1]

        x[i-1] = (b[i-1]-s)/(U[i-1][i-1])

    return x

def main():
    a, b, x, h, points, Ta = read_fds_params(INPUT_PATH)

    result = finite_differences(a, b, x, h, points, Ta)

    save_results(OUTPUT_PATH, [f"a = {a:.6f}"])
    save_results(OUTPUT_PATH, [format_result(result)])
    save_results(OUTPUT_PATH, [f"b = {b:.6f}"])

if __name__ == "__main__":
    main()
