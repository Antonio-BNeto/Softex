# 📝 Exercício – Gerenciador de Palavras

Este exercício faz parte das atividades de **Lógica de Programação em Python** e tem como objetivo praticar manipulação de strings, listas e estruturas de repetição.

---

## 📌 Enunciado

Escreva um programa em Python que:

### Parte 1 – Solicite ao usuário:
- Digitar várias palavras (separadas por espaços).

### Parte 2 – Armazene:
- Todas as palavras em uma **lista**.

### Parte 3 – Para cada palavra da lista:
- Mostrar **"Começa com A"** se a palavra começar com a letra `A` ou `a`.  
- Mostrar **"É palíndromo"** se a palavra for igual quando lida de trás para frente (ex.: `ana`, `ovo`).  
- Mostrar **"Palavra longa"** se tiver **7 ou mais caracteres**.  
- Mostrar **"Palavra comum"** caso contrário.  
- ⚠️ Importante: uma palavra pode se encaixar em mais de uma categoria.

### Parte 4 – Ao final, exiba um resumo:
- Quantas palavras **começam com A**.  
- Quantas são **palíndromos**.  
- Quantas são **longas**.  
- Quantas são **comuns**.  

---

## 📖 O que foi aprendido

Ao implementar este exercício, foram trabalhados os seguintes conceitos:

- ✅ **Entrada de dados com `input()`**  
      Capturar várias palavras digitadas pelo usuário em uma única linha.

- ✅ **Manipulação de strings**  
      Uso de métodos como `.lower()` e slicing `[::-1]` para verificar letras e palíndromos.

- ✅ **Listas e o método `.split()`**  
      Separar palavras de uma string e armazenar em uma lista.

- ✅ **Laços de repetição (`for`)**  
      Percorrer cada palavra da lista para verificar suas características.

- ✅ **Condicionais (`if/else`)**  
      Aplicar regras diferentes dependendo da palavra analisada.

- ✅ **Contadores**  
      Incrementar variáveis para contabilizar categorias de palavras.

- ✅ **Resumo final**  
      Impressão de um relatório com a quantidade de palavras em cada categoria.
