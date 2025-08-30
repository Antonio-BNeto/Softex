tabuleiro = {
	(0,0): "-", (0,1): "-", (0, 2): "-",
	(1, 0): "-", (1, 1): "-", (1, 2): "-",
	(2, 0): "-", (2, 1): "-", (2, 2): "-",
}

def mostrar_tabuleiro(tabuleiro):
    for linha in range(3):
        for coluna in range(3):
            print(tabuleiro[(linha, coluna)], end="")
        print()


mostrar_tabuleiro(tabuleiro)