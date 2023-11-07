media_valor_custo = 0
media_valor_final = 0
contador = 0
preco_final = 0


while True:

    codigo = int(input("Insira o codigo do produto (Ou um codigo negativo para encerrar...)  "))
    if codigo < 0: 
        break

    contador += 1
    preco_de_custo = float(input("Digite aqui o preco de custo do roduto desejado: "))
    media_valor_custo += preco_de_custo
    preco_final = preco_de_custo + (preco_de_custo * 0.20)
    media_valor_final += preco_final

    print(f"O codigo do produto -> {codigo} valor atualizado de R$ {preco_final}")


media_valor_custo = media_valor_custo/contador
media_valor_final = media_valor_final/contador

print(f"A media de valores de custo foi de {media_valor_custo:.2f}\nA media de valores atualizados foi de {media_valor_final:.2f}")



