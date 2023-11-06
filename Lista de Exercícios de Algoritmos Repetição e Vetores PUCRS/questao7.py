aluno = {}

while True:
    codigo_aluno = int(input("Digite o código do aluno: "))
    if codigo_aluno == 0:
        break
    else:
        nota1 = float(input("Digite a nota 1 do aluno: "))
        nota2 = float(input("Digite a nota 2 do aluno: "))
        nota3 = float(input("Digite a nota 3 do aluno: "))
        
        media = (nota1+nota2+nota3)/3
        aluno[codigo_aluno] = media



for cod in aluno.keys():
    media_aluno = aluno[cod]
    print(f"O Aluno com o código: {cod} tem a média de: {format(media_aluno, '.1f')}")