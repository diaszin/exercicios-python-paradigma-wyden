for i in range (20):
    n = int(input("Escreva um valor para que seja calculado a tabuada! ->  "))

    print()

    for l in range (1, n +1):
        valor = l * n
        print(f"{l} x {n} = {valor}")