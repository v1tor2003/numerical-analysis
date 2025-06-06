def intervals(inicio, fim, h):
	xi = [inicio]
	aux = inicio + h
 
	while(aux < fim):
		xi.append(aux)
		aux += h
	xi.append(aux)
	
	return xi