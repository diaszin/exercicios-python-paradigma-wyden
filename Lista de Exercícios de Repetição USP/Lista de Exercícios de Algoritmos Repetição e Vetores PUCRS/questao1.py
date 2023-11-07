qntd_numeros_negativos = 0

for ind in range(5):
    num = int(input("Digite o número: "))
    if num < 0:
        qntd_numeros_negativos +=1


print(f"Nessa sequência de números tem {qntd_numeros_negativos} numeros negativos")
