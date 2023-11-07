n = int(input("Digite o número: "))

if n > 0 :
    soma = 1
    for num in range(n):
        if(num > 1):
            soma += (1/num)
    
    print("A soma é:",soma)
else:
    print("algoritmo só permite número positivo e maior que 1")
    print("rode o programa novamente")