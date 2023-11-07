def menu():
    print("""
    Menu  de opções:
    1. Novo Salário
    2. Férias
    3. Décimo terceiro
    4. Sair
    """)
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 4:
        exit()
    else:
        if opcao == 1:
            calcular_novo_salario()
        elif opcao == 2:
            calcular_ferias()
        elif opcao == 3:
            calcular_decimo_terceiro()
        else:
            print("Insira uma opção válida")


def calcular_novo_salario():
    salario_funcionario = float(input("Digite o salário do funcionário: "))
    percentagem_de_aumento = 0
    if salario_funcionario < 350:
        percentagem_de_aumento = 15/100
    elif salario_funcionario >= 350 and salario_funcionario <= 600:
        percentagem_de_aumento = 10/100
    else:
        percentagem_de_aumento = 5/100

    novo_salario = salario_funcionario * (1+percentagem_de_aumento)
    print(f"O Novo salário: R${format(novo_salario, '.2f')}")


def calcular_ferias():
    salario_funcionario = float(input("Digite o salário do funcionário: "))
    ferias = salario_funcionario + salario_funcionario/3
    print(f"O salário das férias será de: R${format(ferias, '.2f')}")

def calcular_decimo_terceiro():
    salario_funcionario = float(input("Digite o salário do funcionário: "))
    numero_meses = int(input("Digite o número de meses: "))
    if numero_meses <=0 or numero_meses >= 12:
        print("Digite um mês válido")
    else:
        decimo_terceiro = (salario_funcionario*numero_meses)/12
        print(f"O valor do décimo terceiro é de: R${format(decimo_terceiro, '.2f')}")
    

while True:
    menu()