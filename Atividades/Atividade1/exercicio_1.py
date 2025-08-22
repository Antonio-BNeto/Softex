# ======== Questão 1 ==========

# Conversão de Tipos

# Converta a string "123" para int e depois para float.

numero_str = "123"  # String

numero_int = int(numero_str)  # Converte a string para inteiro
numero_float = float(numero_str) #Converte a string para ponto flutuante

print("Questão 1:")

print(numero_int)
print(numero_float)

print("\n")

# ======== Questão 2 ==========

# Operação com Strings

# Dada a string "Python é incrível!", faça o seguinte:

# • Conte quantos caracteres ela possui (incluindo espaços)
# • Converta toda a string para maiúsculas
# • Substitua a palavra ”incrível”por ”poderoso”

frase = "Python é incrível!"

print("Questão 2:")

print(len(frase)) # Conta quantos caracteres a string possui
print(frase.upper()) #Converte toda a string para maiúsculas
print(frase.replace("incrível", "poderoso")) # Substitui a palavra "incrível" por "poderoso"

print("\n")

# ======== Questão 3 ==========

# Listas e Indexação

# Dada a lista de numeros = [10, 20, 30, 40, 50], faça:

# • Acesse e imprima o terceiro elemento
# • Adicione o número 60 no final da lista
# • Remova o número 20 da lista

numeros = [10, 20, 30, 40, 50]

print("Questão 3:")

print(numeros[2]) #imprime o terceiro elemento da lista, afinal a lista começa do 0.
numeros.append(60) #Adiciona o 60 ao final da lista de números.
numeros.remove(20) #Remove o número 20 da lista de números.

print(numeros) #Imprimindo a lista Final

print("\n")

# Lista Final Esperada: [10, 30, 40, 50, 60] 

# ======== Questão 4 ==========

# Dicionários

# Crie um dicionário chamado aluno com:
# • "nome": ”Maria”
# • "idade": 22
# • "curso": ”Engenharia”

# Depois:
# • Adicione uma nova chave "notas" com a lista [8.5, 7.0, 9.2]
# • Imprima apenas o valor da chave "curso"

aluno = {
    "nome": "Maria",
    "idade": 22,
    "curso": "Engenharia"
}

print("Questão 4:")

aluno["notas"] = [8.5, 7.0, 9.2] # Adiciona uma nova chave chamada "notas"
print(aluno["curso"]) # Imprime apenas o valor da chave "curso"
print(aluno) # Imprime o dicionário completo para ver a nova chave adicionada

print("\n")

# ======== Questão 5 ==========

# Tuplas e Conjuntos

# Dada a tupla cores = ("vermelho", "verde", "azul", "verde"):
# • Converta-a em um conjunto para remover duplicatas
# • Adicione a cor "amarelo" ao conjunto

# Observação do uso do set:
#  -> O set é uma coleção que não permite elementos duplicados. Ao adicionar um elemento que já existe, nada acontece.
#  -> No entanto, ele é uma estrutura que não mantém a ordem dos elementos.

cores = ("vermelho", "verde", "azul", "verde")
cores = set(cores) # Converte a tupla em um conjunto
cores.add("amarelo") # Adiciona a cor "amarelo" ao conjunto

print("Questão 5:")

print(cores) # Imprime o conjunto de cores final

print("\n")

# ======== Questão 6 ==========

# Operações Matemáticas

# Declare duas variáveis:
# • a = 15 (int)
# • b = 4 (int)
# Calcule e imprima:
# • A divisão inteira de a por b
# • O resto da divisão de a por b

a = 15
b = 4

print("Questão 6:")

print(a//b) #Imprime o resultado da divisão inteira
print(a%b) #Imprime o resultado do resto da divisão

print("\n")

# ======== Questão 7 ==========

# Verificação de Tipos

# Dada a lista dados = [42, 3.14, "Python", True, [1, 2]], percorra
# cada elemento e imprima seu tipo

dados = [42, 3.14, "Python", True, [1, 2]]

print("Questão 7:")

for elemento in dados:
    print(type(elemento))

print("\n")

# ======== Questão 8 ==========

# Manipulação de Strings

# Dada a string "programação"

# • Inverta a string
# • Verifique se a string original é igual à string invertida

string = "programação"
string_invertida = string[::-1] # Inverte a string

print("Questão 8:")

print(string_invertida) # Imprime a string invertida
print(string == string_invertida) # Verifica se a string original é igual à string invertida

print("\n")

# ======== Questão 9 ==========

# Lista Aninhadas

# Dada a lista matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]]:
# • Acesse e imprima o número 5
# • Substitua o número 8 por 10

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("Questão 9:")

print(matriz[1][1]) # Acessa e imprime o número 5
matriz[2][2] = 10 # Acessa o número 8 e substitui por 10

print(matriz) # Imprime a matriz após a substituição do número 8 por 10

print("\n")

# ======== Questão 10 ==========

# Desafio Final

# Crie um dicionário estoque com:
# • "maçã": 10
# • "banana": 5
# • "laranja": 8
# Faça o seguinte:
# • Adicione "pera" com quantidade 12
# • Remova "banana"
# • Imprima apenas os nomes dos itens (chaves)


estoque = {
    "maçã": 10,
    "banana": 5,
    "laranja": 8
}

estoque["pera"] = 12 # Adicionando "pera" com quantidade 12
del estoque["banana"] # Removendo "banana"

print("Questão 10:")

print(estoque.keys()) # Imprime apenas os nomes dos itens (chaves)