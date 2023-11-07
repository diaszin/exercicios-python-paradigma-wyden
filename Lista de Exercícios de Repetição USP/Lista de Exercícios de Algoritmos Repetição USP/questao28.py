def cadastrar_pessoa():
    global dados, pessoas
    salario = float(input("Digite o valor do salário: "))
    if salario < 0:
        return False
    else:
        qntd_filhos = int(input("Digite a quantidade de filhos: "))
        dados.append({
            "salario": salario,
            "qntd_filhos": qntd_filhos
        })

        inserir_salario_maior(salario)
        if (salario <= 150.00):
            pessoas_com_150_reais += 1

        pessoas += 1

        return True


def inserir_salario_maior(salario: float):
    global salario_maior
    if salario_maior == None or salario > salario_maior:
        salario_maior = salario


def pegar_media_salario():
    global pessoas, dados
    soma_salario = 0
    for pessoa in dados:
        soma_salario += pessoa["salario"]

    media = soma_salario / pessoas
    return media


def pegar_media_filhos():
    global pessoas, dados
    soma_filhos = 0
    for pessoa in dados:
        soma_filhos += pessoa["qntd_filhos"]

    media = soma_filhos/pessoas
    return round(media)


def percentagem_pessoas_salario_150():
    global pessoas, pessoas_com_150_reais
    percentagem = (pessoas_com_150_reais / pessoas)*100
    return percentagem


dados = []
salario_maior = None
pessoas = 0
pessoas_com_150_reais = 0

while True:
    if (cadastrar_pessoa() == False):
        break


media_filhos = pegar_media_filhos()
media_salario = pegar_media_salario()
percentagem_150_reais = percentagem_pessoas_salario_150()

print(f"""
Essa é a média salarial: {format(media_salario, '.2f')}
Essa é a média de filhos: {media_filhos}
Essa é a percentagem de pessoas que recebem até de 150 reais: {format(percentagem_150_reais, '.2f')}
Esse é o maior salário: {salario_maior}
""")
