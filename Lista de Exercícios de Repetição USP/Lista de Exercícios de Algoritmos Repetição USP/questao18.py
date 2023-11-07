preco_final = None
quantidade_parcelas = None
valor_parcela = None
menu_escolhar_parcela = "Escolha a quantidade de parcela \n"
parcelas_disponiveis = []

valor_carro = float(input("Digite o valor do carro: "))

preco_final_vista = valor_carro * 20/100

for num in range(6, 66, 6):
    percentual_de_acrescimo = num / 2
    menu_escolhar_parcela += f"{num}x - {int(percentual_de_acrescimo)}% \n"
    parcelas_disponiveis.append(num)

menu_escolhar_parcela += "Digite a sua opção: "
while quantidade_parcelas not in parcelas_disponiveis:
    quantidade_parcelas = int(input(menu_escolhar_parcela))
    if (quantidade_parcelas not in parcelas_disponiveis):
        print("Número de parcelas incorreto, tente novamente !")

preco_fina_com_acrescimo = valor_carro + (valor_carro * percentual_de_acrescimo/100)

print(f"""
O preço final da compra vista é de {format(preco_final_vista, ".2f")}
O percentual de acréscimo é de {percentual_de_acrescimo}
O preço final com acréscimo é de {format(preco_fina_com_acrescimo, ".2f")}
      """)
