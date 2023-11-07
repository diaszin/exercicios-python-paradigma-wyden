def menu():
    texto_menu = """
    Menu de opções:
    1 - Média aritmética
    2 - Média ponderada
    3 - Sair
    """
    print(texto_menu)
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        media_aritmetica = calcular_media_aritmetica()
        print(f"A média é: {media_aritmetica}")
    elif opcao == 2:
        media_ponderada = calcular_media_ponderada()
        print(f"A média é: {media_ponderada}")
    elif opcao == 3:
        exit()
    else:
        print("Insira uma opção válida !")


def calcular_media_aritmetica():
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    media = (nota1+nota2)/2

    return media


def calcular_media_ponderada():
    qntd_nota = 3
    soma_nota_e_peso = 0
    soma_pesos = 0
    for num in range(qntd_nota):
        nota = float(input("Digite a nota: "))
        peso = float(input("Digite o peso: "))
        soma = nota+peso
        soma_nota_e_peso += soma
        soma_pesos += peso
    
    media_ponderada = soma_nota_e_peso/soma_pesos
    return media_ponderada 
        
while True:
    menu()