def calcular_fatorial(m):
    if m == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, m + 1):
            fatorial *= i
        return fatorial


while True:
    
        m = int(input("Digite um valor inteiro positivo: "))
        if m < 0:
            break  # Encerra o loop se um valor negativo for digitado

        if m % 2 == 0:
            # Verifica e escreve o número de divisores se m for par
            divisores = [i for i in range(1, m + 1) if m % i == 0]
            print(f"{m} é um número par e possui {len(divisores)} divisores: {divisores}")
        elif m < 10:
            # Calcula e escreve o fatorial de m se m for ímpar e menor que 10
            fatorial = calcular_fatorial(m)
            print(f"O fatorial de {m} é {fatorial}")
        else:
            # Calcula e escreve a soma dos inteiros de 1 até m se m for ímpar e maior ou igual a 10
            soma = sum(range(1, m + 1))
            print(f"A soma dos inteiros de 1 até {m} é {soma}")