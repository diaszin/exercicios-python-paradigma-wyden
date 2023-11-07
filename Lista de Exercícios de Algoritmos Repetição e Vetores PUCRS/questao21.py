m = 0
produtorio = 1

while True:
    m = int(input("Digite um numero inteiro positivo (Ou digite 0 para encerrar! )"))
    if m % 2 == 0 and m > 0 :
        produtorio *= m

    if m == 0:
        break

print(f"O produtorio entre os numeros pares foi de {produtorio} ")
