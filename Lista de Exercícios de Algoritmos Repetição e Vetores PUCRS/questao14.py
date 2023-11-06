soma_valores = 0
qntd_valores = 0
qntd_valores_positivos = 0
qntd_valores_negativos = 0


while True:
    num = int(input("Digite o número: "))
    if num == 0:
        break
    else:
        soma_valores += num
        qntd_valores += 1
        if num > 0:
            qntd_valores_positivos += 1
        else:
            qntd_valores_negativos += 1

media_valores = soma_valores / qntd_valores
percentagem_valores_positivos = qntd_valores_positivos / qntd_valores * 100
percentagem_valores_negativos = qntd_valores_negativos / qntd_valores * 100

print(f"""
A média dos valores é de: {media_valores}
Quantidade de valores positivos: {qntd_valores_positivos}
Quantidade de valores negativos: {qntd_valores_negativos}
Os números positivos representam: {format(percentagem_valores_positivos, '.2f')}%
Os números negativos representam: {format(percentagem_valores_negativos, '.2f')}%
""")