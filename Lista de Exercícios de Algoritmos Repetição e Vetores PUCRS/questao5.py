soma_numero = 0
qntd_numeros = 0

while True:
    numero = int(input('Digite o número: '))
    if numero <0:
        break
    else:
        soma_numero += numero
        qntd_numeros +=1
        

media = soma_numero/qntd_numeros
print(f"A média dos números é de: {media}")
