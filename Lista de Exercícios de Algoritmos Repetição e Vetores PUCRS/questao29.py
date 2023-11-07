media_aritmetica = 0
valor_min = 13
valor_maximo = 73
contador = 0

for i in range(valor_min , valor_maximo + 1):
    print(i)
    media_aritmetica += i
    contador += 1
    print(media_aritmetica)

media_aritmetica = media_aritmetica / contador

print(f"A media aritimetica entre os valores de {valor_min} e {valor_maximo} foi de {media_aritmetica:.2f}")

