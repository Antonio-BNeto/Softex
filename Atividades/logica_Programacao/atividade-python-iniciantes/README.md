# 🐍 Exercícios de Python – Strings, Lógica e Laços

Este conjunto de exercícios tem como objetivo praticar **manipulação de strings**, **lógica de programação** e **laços (for/while)**.  
As atividades devem ser resolvidas em arquivos separados e versionadas no **GitHub**.

---

## 📌 Questões

### Questão 1 – Contar Vogais e Consoantes
- Leia uma frase do usuário e mostre quantas vogais e consoantes há.  
- Ignore espaços, números e pontuação.  
- Exemplo:  

```
Entrada: Programar é divertido!
Saída: Vogais: 8 | Consoantes: 10
```

---

### Questão 2 – Verificar Palíndromo
- Leia uma palavra ou frase e diga se é palíndromo (mesma leitura ao contrário).  
- Ignore espaços e diferenças entre maiúsculas e minúsculas.  
- Exemplo:  

```
Entrada: Socorram me subino onibus em marrocos
Saída: É palíndromo
```


---

### Questão 3 – Frequência de Palavras
- Leia uma frase e mostre quantas vezes cada palavra aparece.  
- Exemplo:  
```
Entrada: eu gosto de python e eu gosto de programar
Saída:
eu: 2
gosto: 2
de: 2
python: 1
e: 1
programar: 1
```

---

### Questão 4 – Verificador de Senha Forte
- Leia uma senha e verifique se ela é considerada **forte**.  
- Defina como forte se tiver:
- Pelo menos 8 caracteres.  
- Letra minúscula.  
- Letra maiúscula.  
- Número.  
- Exemplo:  

```
Entrada: C0digoLegal → Saída: Senha forte
Entrada: codigo → Saída: Senha fraca
```
---

## 📂 Estrutura do Diretório
```
atividade-python-iniciantes/
├─ questao1.py
├─ questao2.py
├─ questao3.py
├─ questao4.py
├─ questao5.py
├─ README.md
└─ .gitignore (opcional)
```
---

### Questão 5 – Gerar Acrônimo
- Leia o nome de um curso/expressão e gere o acrônimo (iniciais em maiúsculo).  
- Ignore palavras comuns como: **de, da, do, das, dos, e**.  
- Exemplo:  
```
Entrada: linguagens de programação e estruturas de dados
Saída: LPED
```

---

## 🚀 Como Executar

No terminal, execute cada arquivo separadamente:

```bash
python questao1.py
python questao2.py
python questao3.py
python questao4.py
python questao5.py
```

---

## 📖 O que foi aprendido

Ao implementar este conjunto de exercícios, foram trabalhados os seguintes conceitos:

- ✅ **Manipulação de strings** – uso de `.lower()`, `.upper()`, `.replace()`, fatiamento `[::-1]` e `split()`.  
- ✅ **Laços (for/while)** – percorrer caracteres, listas e palavras em frases.  
- ✅ **Lógica condicional** – verificação de palíndromos, senha forte e filtros de caracteres.  
- ✅ **Contagem e dicionários** – uso de dicionários para armazenar frequências de palavras.  
- ✅ **Expressões booleanas** – verificação de letras maiúsculas, minúsculas, números e tamanho de strings.  
- ✅ **Construção de acrônimos** – manipulação de listas, filtragem de stopwords e uso de `.join()`.  