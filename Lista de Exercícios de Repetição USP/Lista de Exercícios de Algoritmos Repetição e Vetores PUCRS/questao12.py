n = []
qntd_valores = 20
for vez in range(qntd_valores):
    numero = int(input("Digite o número: "))
    n.append(numero)


for num in n:
    for i in range(1, num+1):
        calculo = i*num
        print(f"{i}x{num} = {calculo}")