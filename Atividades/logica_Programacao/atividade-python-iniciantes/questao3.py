# Frequência de palavras

import unicodedata

frase = input("Digite uma frase: ")

frase_sem_acentos = unicodedata.normalize('NFD', frase).encode('ascii', 'ignore').decode('utf-8')
palavras = frase_sem_acentos.split()

frequencia = {}
for palavra in palavras:
    palavra = palavra.lower()
    if palavra in frequencia:
        frequencia[palavra] += 1
    else:
        frequencia[palavra] = 1


for palavra, contagem in dict(sorted(frequencia.items())).items():
    print(f"{palavra}: {contagem}") 