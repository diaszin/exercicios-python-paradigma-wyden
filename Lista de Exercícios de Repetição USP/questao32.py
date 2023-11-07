def cadastrar_numero():
    global numeros
    numero = int(input("Digite o número: "))
    numeros.append(numero)


def calcular_quantidade_numeros_inferiores_35():
    global numeros
    quantidade = 0
    for numero in numeros:
        if numero < 35:
            quantidade += 1
    return quantidade


def calcular_media_numeros_positivos():
    global numeros
    soma_numeros_positivos = 0
    quantidade_numeros_positivos = 0

    for numero in numeros:
        if numero >= 0:
            soma_numeros_positivos += numero
            quantidade_numeros_positivos += 1

    media = soma_numeros_positivos/quantidade_numeros_positivos
    return media


def calcular_porcentagem_de_numeros_entre_50_e_100():
    global numeros
    quantidade_numeros_entre_50_e_100 = 0
    for numero in numeros:
        if numero >= 50 and numero <= 100:
            quantidade_numeros_entre_50_e_100 += 1

    percentagem = (quantidade_numeros_entre_50_e_100/len(numeros)) * 100
    return percentagem


def calcular_porcentagem_de_numeros_entre_10_20_menores_que_50():
    global numeros
    quantidade_numeros_inferiores_50 = 0
    quantidade_numeros_entre_10_20 = 0
    for numero in numeros:
        if (numero < 50):
            quantidade_numeros_inferiores_50 += 1
        if (numero >= 10 and numero <= 20):
            quantidade_numeros_entre_10_20 += 1

    if (quantidade_numeros_inferiores_50 > 0):
        percentagem = (quantidade_numeros_entre_10_20 /
                       quantidade_numeros_inferiores_50)*100
        return percentagem


numeros = []
resp = "S"
while resp == "S":
    cadastrar_numero()
    resp = str(input("Deseja continuar? [S/N]: ")).upper()[0]


quantidade_numeros_inferiores_35 = calcular_quantidade_numeros_inferiores_35()
media_numeros_positivos = calcular_media_numeros_positivos()
percentagem_entre_50_e_100 = calcular_porcentagem_de_numeros_entre_50_e_100()
percentagem_entre_10_e_20 = calcular_porcentagem_de_numeros_entre_10_20_menores_que_50()

print(f"""
Dentre os números, existem essa quantidade de números inferiores a 35: {quantidade_numeros_inferiores_35}
Dentre o números, essa é a média dos números positivos: {media_numeros_positivos}
Dentre o números, essa é porcentagem de números dentre 50 e 100: {percentagem_entre_50_e_100}
Dentre o números, essa é porcentagem de números dentre 10 e 20, e que são menores que 50: {percentagem_entre_10_e_20}
""")
