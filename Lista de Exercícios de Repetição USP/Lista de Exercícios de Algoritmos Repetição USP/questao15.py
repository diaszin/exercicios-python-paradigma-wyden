quantidade_de_numeros_entre_30_e_90 = 0
quantidade_de_numeros = 10

for num in range(quantidade_de_numeros):
    numero = input("Digite o número: ")
    if numero >= 30 and numero <= 90:
        quantidade_de_numeros_entre_30_e_90 +=1


print(f"Existem {quantidade_de_numeros_entre_30_e_90} que está entre 30 e 90")
