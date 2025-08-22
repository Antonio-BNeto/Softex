# 💻 Exercício – Cálculo de Salário com Desconto

Este exercício faz parte das atividades de **Lógica de Programação em Python** e tem como objetivo praticar entrada de dados, cálculos matemáticos e formatação de saída.

---

## 📌 Enunciado

Escreva um programa em Python que:

### Parte 1 – Solicite ao usuário:
- O valor recebido por **hora trabalhada**;
- A quantidade de **horas trabalhadas no mês**.

### Parte 2 – Calcule:
- **Salário Bruto** = valor da hora × horas trabalhadas  
- **Desconto do Imposto de Renda (IR)** = 11% do salário bruto  
- **Desconto do INSS** = 9% do salário bruto  
- **Desconto do Sindicato** = 4% do salário bruto  
- **Salário Líquido** = salário bruto – (soma dos descontos)  

### Parte 3 – Mostre o resultado no seguinte formato:

- +Salário Bruto: R$ xxxx.xx
- -IR (11%): R$ xxxx.xx
- -INSS (9%): R$ xxxx.xx
- -Sindicato (4%): R$ xxxx.xx
- =Salário Líquido: R$ xxxx.xx

## 📖 O que foi aprendido

Ao implementar este exercício, foram trabalhados os seguintes conceitos:

- ✅ **Entrada de dados com `input()`**  
      Permite interagir com o usuário para receber informações numéricas.

- ✅ **Conversão de tipos (`float`)**  
      Necessário para lidar com valores decimais em cálculos monetários.

- ✅ **Operações matemáticas básicas**  
      Multiplicação e porcentagem para calcular descontos sobre o salário.

- ✅ **Uso de variáveis intermediárias**  
      Melhor organização e clareza no código ao criar variáveis para cada desconto.

- ✅ **Formatação de saída (`f-strings`)**  
      Exibição dos valores com duas casas decimais, no formato monetário.
