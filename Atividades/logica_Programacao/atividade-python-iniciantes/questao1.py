# Contar vogais e consoantes

import unicodedata

frase = input("Digite uma frase: ")

# Função criada para remover acentos
def remover_acentos(caractere):
    return unicodedata.normalize('NFD', caractere).encode('ascii', 'ignore').decode('utf-8')

num_vogais = 0
num_consoantes = 0

for letra in frase:
    
    letra_sem_acento = remover_acentos(letra).lower()
    
    if letra_sem_acento.isalpha():    
        if letra_sem_acento in "aeiou":
            num_vogais += 1
        elif letra_sem_acento not in "aeiou":
            num_consoantes += 1

print(f"Vogais: {num_vogais} | Consoantes: {num_consoantes}")