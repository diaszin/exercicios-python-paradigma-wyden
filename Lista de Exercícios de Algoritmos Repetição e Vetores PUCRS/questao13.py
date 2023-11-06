def fatorial(num: int):
    resultado = 1
    for c in range(1, num+1):
        resultado *= c

    return resultado


def inserir_numero(lista: list):
    n = int(input("Quantos valores dever ser lidos: "))
    for i in range(n):
        num = int(input("--> "))
        lista.append(num)


lista = []

inserir_numero(lista)

for num in lista:
    resultado_fatorial = fatorial(num)
    print(f"O número {num} tem como o fatorial: {resultado_fatorial}")
