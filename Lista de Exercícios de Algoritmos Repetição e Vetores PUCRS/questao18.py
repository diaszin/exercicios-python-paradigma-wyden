m = 0
fatorial = 0
ndivisores = 0
soma = 0


while True:
    m = int(input("digite um numero inteiro qualquer: "))

    if m <= 0:
        print("digite um numero positivo")

    if m % 2 == 0:
        ndivisores = 0

        for i in range(1, m + 1):
            if m % i == 0:
                ndivisores +=1
        print(f"O numero {m} tem {ndivisores} como divisores!")

    elif m % 2 != 0 and m < 10:
        fatorial = 1
        for i in range(1, m + 1):
            fatorial *= i
        
        print(f"O resultado fatorial de {m} é igual a {fatorial}")

    else:
        soma = 0
        for i in range(1, m + 1):
            soma += i
        print(f"A soma dos numeros inteiros de 1 ate {m} é igual a {soma}")



