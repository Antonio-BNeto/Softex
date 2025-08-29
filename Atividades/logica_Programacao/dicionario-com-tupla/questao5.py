precos = {
	("Camiseta","M") : 35,
	("Camiseta", "G") : 40
}

produto = input("Qual produto você deseja?: ")
tamanho = input("Qual o tamanho do produto?: ")

print(f"O preço do produto é {precos[(produto, tamanho)]}")