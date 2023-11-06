def calcular_norma(vetor: list):
    soma = 0
    for numero in vetor:
        soma += numero

    resultado = soma ** (1/2)
    return resultado


def maior_norma_vetor(vetor: list):
    maior = None
    posicao_vetor = None
    for posicao in range(len(vetor)):
        if maior == None or maior < vetor[posicao]:
            maior = vetor[posicao]
            posicao_vetor = posicao

    return (maior, posicao_vetor,)


def soma_vetores(vetores: list):
    soma = 0
    for vetor in vetores:
        soma_vetor = 0
        for numero in vetor:
            soma_vetor += numero
        soma += soma_vetor
    return soma


vetor1 = [1, 2, 3, 4, 5]
vetor2 = [1, 2, 3, 8, 5]
vetor3 = [1, 2, 3, 4, 5]

norma_vetor_1 = calcular_norma(vetor1)
norma_vetor_2 = calcular_norma(vetor2)
norma_vetor_3 = calcular_norma(vetor3)

norma_dos_vetores = [norma_vetor_1, norma_vetor_2, norma_vetor_3]
numero_maior, posicao_vetor = maior_norma_vetor(norma_dos_vetores)
resultado_soma_vetores = soma_vetores([vetor1, vetor2, vetor3])

print(f"""
Essa é a norma maior: {numero_maior}
O vetor com maior norma é o vetor {posicao_vetor+1}
Soma dos vetores: {resultado_soma_vetores}
""")
