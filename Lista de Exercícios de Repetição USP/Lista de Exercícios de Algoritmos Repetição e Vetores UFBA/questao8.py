lista_numero_par = []
lista_numero_impar = []
tam_vetor = 5

while True:
    num = int(input("Digite o número: "))
    if num % 2 == 0:
        lista_numero_par.append(num)
    else:
        lista_numero_impar.append(num)

    if len(lista_numero_par) == tam_vetor:
        print(lista_numero_par)
    
    if len(lista_numero_impar) == tam_vetor:
        print(lista_numero_impar)
    
    
    resp = str(input("Quer continuar? [S/N]: ")).upper()
    if resp == "N":
        break
    
print(f"Lista números pares: {lista_numero_par}")
print(f"Lista números impares: {lista_numero_impar}")
