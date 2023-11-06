lista =[]
frase = ""
qtnd_vezes = 10

for num in range(qtnd_vezes):
    numero = int(input("Digite o número: "))
    lista.append(numero)
    

for num in lista:
    frase += f"{num} "


print(frase)