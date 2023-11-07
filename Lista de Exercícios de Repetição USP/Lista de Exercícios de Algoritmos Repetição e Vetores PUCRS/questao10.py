def calcular_media_ponderada(notas: list):
    soma_pontos = 0
    soma_notas_com_pontos = 0
    posicao_nota_maior = None
    for posicao in range(0, len(notas)):
        if posicao_nota_maior is None or notas[posicao] > notas[posicao_nota_maior]:
            posicao_nota_maior = posicao
    
    for posicao in range(0, len(notas)):
        pontos = 0
        if posicao == posicao_nota_maior:
            pontos = 4
        else:
            pontos = 3
        soma_pontos +=pontos
        soma_notas_com_pontos += notas[posicao]*pontos
    
    media_ponderada = soma_notas_com_pontos/soma_pontos
    return media_ponderada

alunos = []

while True:
    codigo = int(input("Digite o código do aluno: "))
    if codigo == 0:
        break
    else:
        nota1 = float(input("Digite a nota 1 do aluno: "))
        nota2 = float(input("Digite a nota 2 do aluno: "))
        nota3 = float(input("Digite a nota 3 do aluno: "))
        notas = [nota1, nota2, nota3]
        alunos.append({
            "codigo": codigo,
            "nota1": nota1,
            "nota2": nota2,
            "nota3": nota3,
            "media": calcular_media_ponderada(notas)
        })



for aluno in alunos:
    media = aluno['media']
    print(f"""
Código do aluno: {aluno['codigo']}
Nota 1: {aluno['nota1']}
Nota 2: {aluno['nota2']}
Nota 3: {aluno['nota3']}
Media: {media}
""") 
    if media >=5:
        print("APROVADO")
    else:
        print("REPROVADO")