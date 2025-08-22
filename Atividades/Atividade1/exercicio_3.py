# Gerenciador de Palavras

# Você deve escrever um programa em Python que:

# Parte 1:
#  -> Solicite para o usuário digitar várias palavras (separadas por espaços)

# Parte 2:
# -> Armazene as palavras em uma lista

# Parte 3 - Para cada palavra da lista, o programa deve:
# -> Mostrar "Começa com A" se a palavra começar com a letra A ou a
# -> Mostrar "É palíndromo" se a palavra for igual quando lida de trás para
#    frente (ex.: "ana", "ovo")
# -> Mostrar "Palavra longa" se tiver 7 ou mais caracteres. Caso contrário,
#    mostrar "Palavra comum".

# -> OBS.: Uma palavra pode se encaixar em mais de uma categoria
#    (ex.: "abacaxi" começa com A e é comum).

# Parte 4 - Ao final, o programa deve exibir um resumo:
# -> Quantas palavras começam com A
# -> Quantas são palíndromos.
# -> Quantas são longas.
# -> Quantas são comuns.

# ============= Resolução =============

# Parte 1:
palavras = input("Digite varias palavras separadas por espaços: ")

# Parte 2:
lista_palavras = palavras.split()

# Parte 3:

for palavra in lista_palavras:
    print(f"Características da palavra: '{palavra}'")
    
    if palavra.lower()[0] == 'a':
        print("Começa com A")
    
    if palavra.lower() == palavra.lower()[::-1]:
        print("É palíndromo")

    if len(palavra) >= 7:
        print("Palavra longa")
    else:
        print("Palavra comum")
        
    print("\n")

# Parte 4:

contador_comecam_a = 0
contador_palindromos = 0
contador_palavras_longas = 0 
# Não criei um contador para palavras comuns pelo fato de que,
# quantidade_total_de_palavras = quantidade_palavras_longas + quantidade_palavras_comuns
# Dessa forma, é possível calcular a quantidade de palavras comuns apenas subtraindo
# quantidade_total_de_palavras - quantidade_palavras_longas

for palavra in lista_palavras:
    if palavra.lower()[0] == 'a':
        contador_comecam_a += 1

    if palavra.lower() == palavra.lower()[::-1]:
        contador_palindromos += 1

    if len(palavra) >= 7:
        contador_palavras_longas += 1

quantidade_palavras_comuns = len(lista_palavras) - contador_palavras_longas

print("\nResumo:")
print(f"Palavras que começam com A: {contador_comecam_a}")
print(f"Palíndromos: {contador_palindromos}")
print(f"Palavras longas: {contador_palavras_longas}")
print(f"Palavras comuns: {quantidade_palavras_comuns}")