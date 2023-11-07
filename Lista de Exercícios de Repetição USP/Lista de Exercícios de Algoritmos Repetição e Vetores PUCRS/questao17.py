soma_total = 0


while True:
    
        m = int(input("Digite o valor de m:  "))
        if m < 0:
            break 

        n = int(input("Digite o valor de n: "))

        
        soma = 0
        for i in range(n):
            soma += m + i

        soma_total += soma

        print(f"A soma dos {n} inteiros consecutivos a partir de {m} é {soma}")

# Apresenta a soma total
print(f"A soma total de todas as somas parciais é {soma_total}")