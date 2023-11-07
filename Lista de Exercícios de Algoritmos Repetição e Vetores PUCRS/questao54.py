
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))


if numero1 == numero2:
    print("Os extremos não podem ser iguais. Por favor, insira números diferentes.")
else:
   
    intervalo = abs(numero2 - numero1)

    terco = intervalo / 3

    ponto1 = numero1 + terco
    ponto2 = ponto1 + terco
    print(f"O intervalo entre {numero1} e {numero2} foi dividido em três partes iguais:")
    print(f"Ponto 1: {ponto1}")
    print(f"Ponto 2: {ponto2}")
