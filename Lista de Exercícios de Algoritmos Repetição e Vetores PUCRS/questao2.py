def calcular_numero():
    numero = int(input("Digite o valor: "))
    if numero >= 0:
        resultado = E(numero)
        print(resultado)

    else:
        print("Insira um número positivo")


def E(numero: int):
    resultado = 1 
    termo = 1

    for i in range(1, numero + 1):
        termo *= i  
        resultado += 1 / termo 

    return resultado




calcular_numero()
