lista_clientes = []

while len(lista_clientes) <= 5:
    nome_cliente = str(input("Digite o nome do cliente: "))
    valor_gasto_cliente = float(input("Digite o valor gasto do cliente do ano passado: "))
    lista_clientes.append({
        "nome": nome_cliente,
        "valor_gasto": valor_gasto_cliente
    })
    

for cliente in lista_clientes:
    valor_gasto_por_cliente = cliente.get("valor_gasto")
    nome_do_cliente = cliente.get("nome")
    if valor_gasto_por_cliente <= 1000:
        valor_bonus = (10*valor_gasto_por_cliente)/100
        print(f"O Cliente {nome_do_cliente} terá o bônus de {valor_bonus}")
    else:    
        valor_bonus = (15*valor_gasto_por_cliente)/100
        print(f"O Cliente {nome_do_cliente} terá o bônus de {valor_bonus}")
