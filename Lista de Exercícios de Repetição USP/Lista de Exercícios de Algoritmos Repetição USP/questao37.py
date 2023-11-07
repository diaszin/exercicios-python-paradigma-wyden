def menu():
    print("""
    1 - Adição
    2 - Subtração
    3 - Multiplicação
    4 - Divisão
    5 - Sair
    """)
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 5:
        exit()
    else:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        if opcao == 1:
            calculo = adicao(num1, num2)
            print("-"*10)
            print(f"{num1}+{num2}={calculo}")
            print("-"*10)
        elif opcao == 2:
            calculo = subtracao(num1, num2)
            print("-"*10)
            print(f"{num1}-{num2}={calculo}")
            print("-"*10)
        elif opcao == 3:
            calculo = multiplicacao(num1, num2)
            print("-"*10)
            print(f"{num1}x{num2}={calculo}")
            print("-"*10)
        elif opcao == 4:
            calculo = divisao(num1, num2)
            if type(calculo) == float:
                print("-"*10)
                print(f"{num1}/{num2}={calculo}")
                print("-"*10)
            else:
                print("-"*10)
                print(calculo)
                print("-"*10)
        else:
            print("Insira uma opcao válida")


def adicao(num1, num2):
    soma = num1+num2
    return soma


def subtracao(num1, num2):
    subtracao = num1+num2
    return subtracao


def multiplicacao(num1, num2):
    multi = num1*num2
    return multi


def divisao(num1, num2):
    if num2 > 0:
        div = num1/num2
        return div
    else:
        return "Não pode dividir por zero "


while True:
    menu()
