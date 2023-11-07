
nomes_clientes = []
bonuses = []


for i in range(1, 151):
    nome_cliente = input(f"Digite o nome do Cliente {i}: ")
    valor_compras = float(input(f"Digite o valor das compras no ano passado para {nome_cliente}: R$ "))

    if valor_compras < 500000:
        bonus = valor_compras * 0.10
    else:
        bonus = valor_compras * 0.15

  
    nomes_clientes.append(nome_cliente)
    bonuses.append(bonus)


print("\nBônus dos Clientes:")
for i in range(len(nomes_clientes)):
    print(f"{nomes_clientes[i]}: R$ {bonuses[i]:.2f}")
