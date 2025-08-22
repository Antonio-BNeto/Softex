# Exercício - Calculo de Salário com Desconto

# Escreva um Programa em Python que:

# Parte 1 - Solicie ao Usuário:
# -> O valor recebido por hora trabalhada;
# -> A quantidade de horas trabalhadas no mês.

# Parte 2 - Calcule:
# -> Salário Bruto (valor da hora x horas trabalhadas);
# -> Desconto do Imposto de Renda (11%)
# -> Desconto do INSS (9%)
# -> Desconto do Sindicato (4%)
# -> Salário Líquido (Salário Bruto - Soma dos descontos)

#  Parte 3 - Apresente o resultado no seguinte formato:
# + Salário Bruto: R$ xxxx.xx
# - IR (11%): R$ xxxx.xx
# - INSS (9%): R$ xxxx.xx
# - Sindicado (4%): R$ xxxx.xx
# = Salário Líquido: R$ xxxx.xx

# ============ Resolução ============

# Parte 1:

valor_por_hora_trabalhada = float(input("Digite o valor recebido por hora trabalhada: "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

# Parte 2:

salario_bruto = valor_por_hora_trabalhada * horas_trabalhadas
desconto_ir = salario_bruto * 0.11
desconto_inss = salario_bruto * 0.09
desconto_sindicato = salario_bruto * 0.04
salario_liquido = salario_bruto - (desconto_ir + desconto_inss + desconto_sindicato)

# Parte 3:

print(f"+ Salário Bruto: R$ {salario_bruto:.2f}")
print(f"- IR (11%): R$ {desconto_ir:.2f}")
print(f"- INSS (9%): R$ {desconto_inss:.2f}")
print(f"- Sindicado (4%): R$ {desconto_sindicato:.2f}")
print(f"= Salário Líquido: R$ {salario_liquido:.2f}")