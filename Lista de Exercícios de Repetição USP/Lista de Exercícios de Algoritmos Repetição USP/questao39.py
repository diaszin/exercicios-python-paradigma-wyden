def cadastrar_cliente():
    global clientes
    codigo_cliente = int(input("Digite o código do cliente: "))
    if codigo_cliente <=0:
        return False
    else:
        tipo_conta = int(input("Digite o tipo da conta: "))
        valor_investido = float(input("Digite o valor investido: "))
        clientes.append({
            "codigo": codigo_cliente,
            "valor": valor_investido,
            "tipo": tipo_conta,
            "rendimento_mensal": calcular_rendimento_mensal(tipo_conta, valor_investido)
        })


def calcular_rendimento_mensal(tipo_conta: int, valor_investido: float):
    rendimento_mensal = 0
    if tipo_conta == 1:
        rendimento_mensal = 1.5
    elif tipo_conta == 2:
        rendimento_mensal = 2
    elif tipo_conta == 3:
        rendimento_mensal = 4
    else:
        print("Tipo de conta inválido")
    
    calculo = valor_investido*(rendimento_mensal/100)
    print(f"O rendimento mensal será de: R${format(calculo, '.2f')}")
    return calculo


def mostrar_total_investido():
    global clientes
    total_investido = 0
    for cliente in clientes:
        valor_investido = cliente.get("valor")
        if valor_investido is not None:
            total_investido += valor_investido
    
    print(f"O Total investido foi de: R${format(total_investido, '.2f')}")


def mostrar_total_juros():
    global clientes
    total_juros_pagos = 0
    for cliente in clientes:
        juros = cliente.get("rendimento_mensal")
        if juros is not None:
            total_juros_pagos += juros
    
    print(f'O total de juros pagos é de: R${format(total_juros_pagos, ".2f")}')
        

clientes = []
while True:
    if cadastrar_cliente() == False:
        break
    
mostrar_total_investido()
mostrar_total_juros()