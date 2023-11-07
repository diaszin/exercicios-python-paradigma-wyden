maior_valor = -1
menor_valor = 99999
media_valores = 0
qtd_valores = 500

for i in range(qtd_valores):
    numero = int(input("Digite qualquer numero ->  "))
    media_valores += numero
    if numero > maior_valor:
        maior_valor = numero
    if numero < menor_valor:
        menor_valor = numero

media_valores = media_valores/qtd_valores
print(f"O maior valor foi {maior_valor}\nO menor valor foi {menor_valor}\nA media dos valores foi {media_valores:.2f}")
    
