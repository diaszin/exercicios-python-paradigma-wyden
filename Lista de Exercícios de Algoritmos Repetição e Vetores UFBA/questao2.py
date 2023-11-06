lista = []
qntd_vezes = 10

for vez in range(qntd_vezes):
    numero = int(input("Digite o número: "))
    lista.append(numero)

numero_escolhido = int(input("Digite o número no qual deseja verificar: "))

if numero_escolhido in lista:
    print("Esse número existe na lista")
else:
    print("Esse número não existe na lista")
    
