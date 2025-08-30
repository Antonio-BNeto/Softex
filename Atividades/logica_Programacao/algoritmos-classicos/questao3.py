def bubble_sort(lista):
	for i in range(len(lista)):
		for j in range(len(lista)-i-1):
			if lista[j] < lista[j+1]:
				lista[j], lista[j+1] = lista[j+1], lista[j]

	return lista

lista = [2, 3, 4 ,18, 0, -1, -2]

lista = bubble_sort(lista)

print(lista)