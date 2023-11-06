def cadastrar_votos():
    global votos
    voto = int(input("Insira seu voto: "))
    if voto == 0:
        return False
    elif voto in [1, 2, 3, 4, 5, 6]:
        quantidade_voto = votos.get(voto)
        if quantidade_voto is None:
            votos[voto] = 1
        else:
            votos[voto] = quantidade_voto+1
    else:
        print("Insira um número correto !")


def calcular_total_de_votos_por_candidato():
    global votos
    votos_por_candidato = [0, 0, 0]
    for voto in votos.keys():
        if voto in [1, 2, 3]:
            votos_por_candidato[voto-1] = votos[voto]

    return votos_por_candidato


def calcular_total_votos_nulos():
    global votos
    total_votos = votos.get(5)
    if total_votos is not None:
        return total_votos


def calcular_total_votos_brancos():
    global votos
    total_votos = votos.get(6)
    if total_votos is not None:
        return total_votos


def calcular_percentagem_votos_nulos_total_votos():
    global votos
    soma_votos = 0
    for numero in votos.keys():
        soma_votos += votos[numero]
    votos_nulos = votos.get(5)
    if votos_nulos is not None:
        percentagem = (votos_nulos/soma_votos)*100
        return percentagem


def calcular_percentagem_votos_brancos_total_votos():
    global votos
    soma_votos = 0
    for numero in votos.keys():
        soma_votos += votos[numero]

    votos_em_branco = votos.get(6)
    if votos_em_branco is not None:
        percentagem = (votos_em_branco/soma_votos)*100
        return percentagem


votos = {}
while True:
    if cadastrar_votos() == False:
        break


candidato1, candidato2, candidato3 = calcular_total_de_votos_por_candidato()
total_votos_nulo = calcular_total_votos_nulos()
total_votos_brancos = calcular_total_votos_brancos()
percentagem_votos_nulos = calcular_percentagem_votos_nulos_total_votos()
percentagem_votos_brancos = calcular_percentagem_votos_brancos_total_votos()


print(f"""
O Candidato com o número 1, Obteve {candidato1}      
O Candidato com o número 2, Obteve {candidato2}      
O Candidato com o número 3, Obteve {candidato3}
Total de votos nulos são de: {total_votos_nulo}
Total de votos brancos são de: {total_votos_brancos}
Percentagem de votos nulos: {format(percentagem_votos_nulos, '.2f')}
Percentagem de votos brancos: {format(percentagem_votos_brancos,  '.2f')}
""")
