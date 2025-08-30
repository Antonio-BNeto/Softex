def bubble_sort(lista):
	for i in range(len(lista)):
		for j in range(len(lista)-i-1):
			if lista[j] > lista[j+1]:
				lista[j], lista[j+1] = lista[j+1], lista[j]

	return lista

def busca_linear(lista, valor):
	inicio = 0
	fim = len(lista)-1

	while inicio <= fim:
		meio = (inicio+fim) // 2
		if lista[meio] == valor:
			return True

		if valor > lista[meio]:
			inicio = meio + 1
		else:
			fim = meio - 1
	return False

lista = [2, 3, 4 ,18, 0, -1, -2]

lista = bubble_sort(lista)

print(busca_linear(lista, 18))