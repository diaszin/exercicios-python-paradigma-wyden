def cadastrar_aluno(aluno: list):
    nome = str(input("Digite o nome do aluno: "))
    r = str(
        input("Digite as respostas do aluno [Separe por vírgula]: ")).upper().split(",")

    aluno.append({
        "nome": nome,
        "respostas": r,
    })


def quantidade_respostas_certas(aluno, g):
    nota_final = 0
    for num_questao in range(len(aluno["respostas"])):
        if aluno["respostas"][num_questao] == g[num_questao]:
            nota_final += 0.5

    return nota_final


g = []
num_questoes = 20
for questao in range(num_questoes):
    letra = str(
        input("Insira o gabarito da prova [Separe por vírgulas]: ")).upper()
    g.append(letra)
num_alunos = 50

alunos = []
for qntd_aluno in range(num_alunos):
    cadastrar_aluno(alunos)
    
for aluno in alunos:
    nota_final = quantidade_respostas_certas(aluno,  g)
    if nota_final >= 6:
        print(f"{format(nota_final, '.1f')} - Aluno Aprovado")
    else:
        print("Aluno Reprovado")
