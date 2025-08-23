# Gerar acrônimo

frase = input("Digite uma frase: ")
palavras = frase.split()
acronimo = ""
for palavra in palavras:
    if palavra not in ["de", "da", "do", "das", "dos", "e"]:
        acronimo += palavra[0].upper()
        
print(f"{acronimo}")
