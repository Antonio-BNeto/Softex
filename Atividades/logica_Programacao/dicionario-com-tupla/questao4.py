notas_alunos = {
	"Thiago": (6, 7, 9)
}

for key in notas_alunos.keys():
	media = sum(notas_alunos[key]) / len(notas_alunos[key])

	print(f"O aluno: {key}, possui média igual a {media:.2f}")
