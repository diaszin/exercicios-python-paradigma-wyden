def media_elementos(lista: list):
    soma_numeros = 0
    for num in lista:
        soma_numeros +=  num
    
    media = soma_numeros/len(lista)
    return media

def maior_e_menor_elementos(lista: list):
    maior_numero = None
    menor_numero = None
    for num in lista:
        if maior_numero == None or maior_numero < num:
            maior_numero = num
        if menor_numero == None or menor_numero > num:
            menor_numero = num
            
    return maior_numero, menor_numero


def numeros_positivos_e_negativos(lista: list):
    numeros_positivos = 0
    numeros_negativos = 0
    
    for num in lista:
        if num >= 0:
            numeros_positivos +=1
        else:
            numeros_negativos +=1
    
    return numeros_positivos, numeros_negativos
        


lista = []
qntd_vezes = 10

for vezes in range(qntd_vezes):
    numero  = int(input("Digite o número: "))
    lista.append(numero)


media = media_elementos(lista)
maior, menor = maior_e_menor_elementos(lista)
numeros_positivos, numeros_negativos = numeros_positivos_e_negativos(lista)

print(f"""
Média dos números: {media}
Maior número: {maior}
Menor número: {menor}
Quantidade de números positivos: {numeros_positivos}
Quantidade de números negativos: {numeros_negativos}
""")