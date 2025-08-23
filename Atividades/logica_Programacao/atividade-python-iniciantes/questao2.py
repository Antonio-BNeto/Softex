# Verificar palíndromo (ignorando espaços, maiúsculas/minúsculas e acentos)

import unicodedata

# Função criada para remover acentos
def remover_acentos(caractere):
    return unicodedata.normalize('NFD', caractere).encode('ascii', 'ignore').decode('utf-8')

frase = input("Digite uma frase: ")
frase_sem_acentos = remover_acentos(frase).replace(" ", "").lower()
if frase_sem_acentos == frase_sem_acentos[::-1]:
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")