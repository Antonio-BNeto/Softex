def tamanho_lista(lista):
	if len(lista) == 0:
		return 0
	else:
		return 1 + tamanho_lista(lista[1:])

lista = [2, 3, 4 ,18, 0, -1, -2]

print(tamanho_lista(lista))
