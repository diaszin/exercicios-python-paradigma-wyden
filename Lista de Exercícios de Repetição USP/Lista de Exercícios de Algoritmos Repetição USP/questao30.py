def cadastrar_produto():
    global produtos_sem_aumento

    codigo_produto = int(input("Digite o código do produto: "))
    if (codigo_produto < 0):
        return False
    else:
        preco_produto = float(input("Digite o preço do produto: "))
        produto = {
            "codigo": codigo_produto,
            "preco": preco_produto
        }
        produtos_sem_aumento.append(produto)
        cadastrar_com_aumento(produto)
        return True


def cadastrar_com_aumento(produto: dict):
    global produtos_com_aumento

    if type(produto) == dict:
        codigo = produto.get("codigo")
        preco = float(produto.get("preco"))
        if codigo != None and preco != None:
            valor_aumento = (20/100)*preco
            preco_com_acrescimo = preco + valor_aumento
            produtos_com_aumento.append({
                "codigo": codigo,
                "preco": preco_com_acrescimo
            })


def media_preco_sem_aumento():
    global produtos_sem_aumento
    soma_salario = 0
    for produto in produtos_sem_aumento:
        soma_salario += produto["preco"]

    media = soma_salario/len(produtos_sem_aumento)
    return media


def media_preco_com_aumento():
    global produtos_com_aumento
    soma_salario = 0
    for produto in produtos_com_aumento:
        soma_salario += produto["preco"]

    media = soma_salario/len(produtos_com_aumento)
    return media


produtos_sem_aumento = []
produtos_com_aumento = []

while True:
    if cadastrar_produto() == False:
        break

print("Tabela com os novos valores")
for produto in produtos_com_aumento:
    codigo = produto["codigo"]
    preco = produto["preco"]

    print(f"{codigo} ===== R${format(preco, '.2f')}")

media_produto_sem_aumento = media_preco_sem_aumento()
media_produto_com_aumento = media_preco_com_aumento()

print(f"""
Média do produto sem aumento: {format(media_produto_sem_aumento, '.2f')}
Média do produto com aumento: {format(media_produto_com_aumento, '.2f')}
""")
