
X = int(input("Digite o valor de X: "))


contador = 0


for i in range(20):
    if contador < 10:
        termo = 1
    else:
        termo = X ** (contador - 9)
    print(termo, end=" ")
    contador += 1