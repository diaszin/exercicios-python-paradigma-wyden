
medias_ponderadas = []


media_geral_turma = 0


for i in range(1, 51):
    print(f"Informações do Aluno {i}:")
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    
  
    media_ponderada = (n1 * 2 + n2 * 4 + n3 * 3) / 10
  
    medias_ponderadas.append(media_ponderada)
    
    
    media_geral_turma += media_ponderada


print("\nMédias Ponderadas dos Alunos:")
for i, media in enumerate(medias_ponderadas):
    print(f"Aluno {i+1}: {media:.2f}")
    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")


media_geral_turma /= 50
print(f"\nMédia Geral da Turma: {media_geral_turma:.2f}")