alunos = ["Maria", "Jose", "Carla", "Sol"]
notas = [35, 50, 20, 80]
aprovados = []

verificacao = [aprovados.append(alunos[i]) for i in range(len(notas)) if notas[i] >= 60]
print(aprovados)
