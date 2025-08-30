def busca_ocorrencia(lista, valor):
	conta_occorrencia = 0

	for i in range(len(lista)):
		if lista[i] == valor:
			conta_occorrencia += 1

	return conta_occorrencia

lista = [29, 10, 14, 37, 13, 29]

print(busca_ocorrencia(lista, 29))