tabuleiro = {
	(0,0): "-", (0,1): "-", (0, 2): "-",
	(1, 0): "-", (1, 1): "-", (1, 2): "-",
	(2, 0): "-", (2, 1): "-", (2, 2): "-",
}

instrucao = "Formato das jogadas (linha coluna)"

tabela = [(linha, coluna) for linha, coluna in tabuleiro]

jogada = input("Digite uma posição aonde quer realizar sua jogada: ")

while True:

	if all(tabuleiro.values()) != "-":
	 	break

	for i in range(0, len(tabela), 3):
		print(tabuleiro[tabela[i]], tabuleiro[tabela[i+1]], tabuleiro[tabela[i+2]])

	jogador2 = input("Digite uma posição aonde quer realizar sua jogada: ")
