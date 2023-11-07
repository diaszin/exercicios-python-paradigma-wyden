def mostrar_tabela(numeros: list):
    cabecalho = "NÚMERO\tRAIZ QUADRADA\tAO CUBO\tAO QUADRADO"
    corpo = ""
    print(cabecalho)
    for numero in numeros:
        raiz_quadrada = numero ** 1/2
        cubo = numero **3
        quadrado = numero **2
        corpo += f"{numero}\t{raiz_quadrada}\t{cubo}\t{quadrado}\n"
    
    print(corpo)

numeros = []
contagem_linhas = 0

while True:
    num = int(input("Digite o número: "))
    if num == 0:
        break
    else:
        contagem_linhas +=1
        numeros.append(num)
        if contagem_linhas == 20:
            mostrar_tabela(numeros)
            contagem_linhas = 0
        