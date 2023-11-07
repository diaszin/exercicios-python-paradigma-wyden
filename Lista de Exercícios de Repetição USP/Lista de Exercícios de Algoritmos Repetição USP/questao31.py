def cadastrar_acao():
    global acao

    tipo_acao = str(input("Digite o tipo da ação: ")).upper()[0]
    if (tipo_acao == "F"):
        return False
    else:
        preco_compra = float(input("Digite o preço de compra da ação: "))
        preco_venda = float(input("Digite o preço de venda da ação: "))
        lucro = preco_venda=preco_compra

        acoes.append({
            "tipo": tipo_acao,
            "preco_compra": preco_compra,
            "preco_venda": preco_venda,
            "lucro": lucro
        })
        
        return True


def listar_lucro_por_acao():
    global acoes
    for acao in acoes:
        print(f"A ação {acao['tipo']} teve o lucro de: {acao['lucro']}")


def calcular_quantidade_lucro_acao_maior_que_1000():
    global acoes
    quantidade = 0
    for acao in acoes:
        if acao["lucro"] > 1000:
            quantidade += 1
    return quantidade


def calcular_quantidade_lucro_acao_menor_que_200():
    global acoes
    quantidade = 0
    for acao in acoes:
        if acao["lucro"] < 200:
            quantidade += 1
    return quantidade


def calcular_lucro_total_empresa() -> float:
    global acoes
    lucro_total = 0
    for acao in acoes:
        lucro_total += acao["lucro"]

    return lucro_total


acoes = []

while True:
    if cadastrar_acao() == False:
        break
    
listar_lucro_por_acao()
quantidade_acao_maior_1000 = calcular_quantidade_lucro_acao_maior_que_1000()
quantidade_acao_menor_200 = calcular_quantidade_lucro_acao_menor_que_200()
lucro_total_empresa = calcular_lucro_total_empresa()


print(f"""
Quantidade de ação maior que R$ 1000: {quantidade_acao_maior_1000}
Quantidade de ação menor que R$ 200: {quantidade_acao_menor_200}
Lucro total da empresa: {lucro_total_empresa}
""")