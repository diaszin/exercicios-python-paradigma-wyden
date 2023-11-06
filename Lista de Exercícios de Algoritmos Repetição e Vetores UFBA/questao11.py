print("0 - Sair do programa \n 1 - Exibe lista na ordem normal \n 2 - Exibe lista na ordem inversa")
resp = int(input(": "))

lista = [0.9, 1.2, 3.4, 5.6, 6.7, 7.8, 8.9,
         9.0, 10.7, 10.1, 10.2, 10.4, 10.8, 14.2]

if resp == 0:
    exit()
elif resp == 1:
    print(lista)
elif resp == 2:
    lista.reverse()
    print(lista)
else:
    print("Resposta inválida, tente novamente !")
