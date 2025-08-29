notas_disciplina = {
	("Ana", "Matemática") : 9,
	("Matheus", "Matemática"): 6,
	("Ana", "História"): 7
}

nome_aluno = input("Digite o nome do aluno: ")

nome_aluno = nome_aluno.strip()

soma_notas = 0
conta_disciplina = 0

for nome, materia in notas_disciplina.keys():
	if nome == nome_aluno:
		nota = notas_disciplina[(nome, materia)]
		print(materia, nota)
		soma_notas += nota
		conta_disciplina += 1 

media = soma_notas/conta_disciplina

print(f"A média geral do aluno: {nome_aluno} foi {media:.2f}")