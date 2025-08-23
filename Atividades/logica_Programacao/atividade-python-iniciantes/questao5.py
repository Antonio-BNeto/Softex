# Gerar acrônimo

frase = input("Digite uma frase: ")
stopwords_input = input("Digite as stopwords separadas por vírgula (ou Enter para padrão): ")

stopwords_padrao = ["de", "da", "do", "das", "dos", "e"]

if stopwords_input:
    stopwords = [palavra.strip() for palavra in stopwords_input.split(",")]
else:
    stopwords = stopwords_padrao

palavras = frase.split()
acronimo = ""
for palavra in palavras:
    if palavra not in stopwords:
        acronimo += palavra[0].upper()
        
print(f"{acronimo}")
