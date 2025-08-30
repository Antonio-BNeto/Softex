def potencia_recursiva(valor, expoente):
	if expoente == 0:
		return 1
	else:
		return valor * potencia_recursiva(valor, expoente-1)

print(potencia_recursiva(2, 3))