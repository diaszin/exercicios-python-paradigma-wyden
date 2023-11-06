soma_numeros_pares = 0
qntd_numeros_pares = 0

while True:
    numero = int(input("Digite o número: "))
    if numero == 0:
        break
    else:    
        if numero % 2 == 0:
            soma_numeros_pares += numero
            qntd_numeros_pares +=1


media = soma_numeros_pares/qntd_numeros_pares
print(f"A Média dos números pares é de: {media}")
