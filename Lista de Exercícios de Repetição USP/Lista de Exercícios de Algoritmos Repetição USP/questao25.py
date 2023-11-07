global cad_alunos, maior_nota, menor_nota, total_aluno_reprovados
cad_alunos = []
maior_nota = None
menor_nota = None
total_aluno_reprovados = 0
qntd_aluno = 10

def cadastrar_aluno():
    matricula_aluno = str(input("Digite a matricula do aluno: "))
    nota_final = cadastrar_notas()
    frequencia_aluno = int(input("Digite a frequência do aluno: "))
    return {
        "matricula": matricula_aluno,
        "nota_final": nota_final,
        "frequencia_aluno": frequencia_aluno
    }

def cadastrar_notas():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    
    nota_final = nota1 + nota2 + nota3/3
    
    return nota_final


def calcular_mostrar():
    resultado = ""
    for aluno in cad_alunos:
        matricula_aluno = aluno["matricula"]
        nota_final_aluno = aluno["nota_final"]
        frequencia_aluno = aluno["frequencia_aluno"]
        resultado += f"Matricula aluno: {matricula_aluno} - Nota final: {nota_final_aluno}"
        if nota_final_aluno >= 6 and frequencia_aluno >= 40:
            resultado += f"- Situação: Aprovado"
        else:
            resultado += f"- Situação: Reprovado"
            total_aluno_reprovados +=1
        
        if maior_nota == None or maior_nota < nota_final_aluno:
            maior_nota = nota_final_aluno
        if menor_nota == None or menor_nota > nota_final_aluno:
            menor_nota = nota_final_aluno
    
    print(f"A maior nota da turma é: {maior_nota}")
    print(f"A menor nota da turma é: {menor_nota}")
    print(f"Total de alunos reprovados: {total_aluno_reprovados}")
    print(f"Porcentagem de alunos reprovado com a frequência mínima: {total_aluno_reprovados/qntd_aluno*100}")


for aluno in range(qntd_aluno):
    dados_aluno = cadastrar_aluno()
    cad_alunos.append(dados_aluno)


calcular_mostrar()