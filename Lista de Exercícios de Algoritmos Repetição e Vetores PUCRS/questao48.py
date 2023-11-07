
conceitos = []


for i in range(1, 76):
    matricula = input(f"Digite o número de matrícula do Aluno {i}: ")
    nota = float(input(f"Digite a nota numérica final para o Aluno {i}: "))

  
    if 0.0 <= nota <= 4.9:
        conceito = "D"
    elif 5.0 <= nota <= 6.9:
        conceito = "C"
    elif 7.0 <= nota <= 8.9:
        conceito = "B"
    elif 9.0 <= nota <= 10.0:
        conceito = "A"
    else:
        conceito = "Nota inválida"

    conceitos.append((matricula, conceito))


print("\nConceitos Finais dos Alunos:")
for matricula, conceito in conceitos:
    print(f"Aluno {matricula}: Conceito {conceito}")
