numero = None
maior_numero = None
menor_numero = None
while numero != 0 or numero == None:
    numero = int(input("Digite o número escolhido: "))
    if (numero < 0):
        print("Digite novamente !, não é permitido número negativo !")
    else:
        if (maior_numero == None or numero > maior_numero) and numero != 0:
            maior_numero = numero
        if (menor_numero == None or numero < menor_numero) and numero != 0:
            menor_numero = numero


print(f"O maior número é {maior_numero}\nO menor número é  {menor_numero}")