cadastra_aluno = {}

def cadastrar_aluno():
    print("\nCADASTRAR NOVO ALUNO")
    nome = input("Nome do aluno: ").strip().title()
    disciplina = input("Disciplina: ").strip().title()
    
    chave = (nome, disciplina)
    
    if chave not in cadastra_aluno:
        try:
            nota1 =  float(input("Nota 1: "))
            nota2 =  float(input("Nota 2: "))
            nota3 =  float(input("Nota 3: "))
            
            cadastra_aluno[chave] = (nota1, nota2, nota3)
            print("Aluno cadastrao com sucesso!")
            
        except ValueError:
            print("Erro: digite notas válidas (números)")
    else:
        print("Aluno já tem essa discipla anexado")
    
def consultar_notas():
    print("\nCONSULTAR NOTAS")
    nome = input("Nome do aluno: ").strip().title()
    
    encontrados = False
    for (nome_aluno, disciplina), notas in cadastra_aluno.items():
        if nome_aluno == nome:
            encontrados = True
            print(f"\nDisciplina: {disciplina}")
            print(f"\nNotas: {notas}")
            print(f"\nMédia: {sum(notas)/len(notas):.2f}")
    
    if not encontrados:
        print("Nenhum aluno encontrado com o nome pesquisado")

def calcular_media_geral():
    print("\nMÉDIA GERAL DO ALUNO")
    nome = input("Nome do aluno: ").strip().title()
    
    todas_notas_aluno = []
    quant_disciplinas = 0
    
    for (nome_aluno, disciplina), notas in cadastra_aluno.items():
        if nome_aluno == nome:
            disciplina += 1
            todas_notas_aluno.extend(notas)
            media_disciplina = sum(notas)/len(notas)
            print(f"{disciplina}: {media_disciplina:.2f}")
            
    if disciplina > 0:
        media_geral = sum(todas_notas_aluno)/ len(todas_notas_aluno)
        print(f"\nMédia geral de {nome}: {media_geral}")
    else:
        print("Nenhum aluno encontrado com esse nome")             

while True:
    print("\n" + "="*50)
    print("SISTEMA DE CADASTRO DE ALUNOS")
    print("="*50)
    print("1. Cadastrar novo aluno")
    print("2. Consultar notas de um aluno")
    print("3. Calcular média geral do aluno")
    print("4. Sair")
    
    opcao = input("\nEscolha uma opção: ")
    
    if opcao == "1":
        cadastrar_aluno()
    elif opcao == "2":
        consultar_notas()
    elif opcao == "3":
        calcular_media_geral()
    elif opcao == "4":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida! Digite 1, 2, 3 ou 4.")