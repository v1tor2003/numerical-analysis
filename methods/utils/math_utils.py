def intervals(inicio, fim, h):
	xi = [inicio]
	aux = inicio + h
 
	while(aux < fim):
		xi.append(aux)
		aux += h
	xi.append(aux)
	
	return xi

def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

def matmul(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            s = sum(A[i][k] * B[k][j] for k in range(len(B)))
            row.append(s)
        result.append(row)
    return result