valor_total_vista = 0.0
valor_total_a_prazo = 0.0

for num in range(15):
    codigo_transacao = str(input("Digite o código para a transação [V/P]: ")).upper()
    valor_transacao = float(input("Digite o valor da transação: "))
    if codigo_transacao == "V":
        valor_total_vista += valor_transacao
    elif codigo_transacao == "P":
        valor_total_a_prazo += valor_transacao
    else:
        print("Código inválido !")
    
print(f"O valor total das compras à vista: R$ {format(valor_total_vista, '.2f')}")
print(f"O valor total das compras a prazo: R$ {format(valor_total_a_prazo, '.2f')}")
print(f"O valor total das compras efetuadas: R$ {format(valor_total_vista+valor_total_a_prazo, '.2f')}")
print(f"O valor da primeira prestação da compra a prazo é: R${format(valor_total_a_prazo/3, '.2f')}")
