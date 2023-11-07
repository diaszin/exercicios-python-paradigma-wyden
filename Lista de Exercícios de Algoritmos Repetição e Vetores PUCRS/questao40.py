

def fatorial(num):
    if num == 0:
        return 1
    resultado = 1
    for i in range(1, num + 1):
        resultado *= i
    return resultado

n = int(input("Digite o número de valores a serem lidos: "))

print("{:<10} {:<15} {:<10}".format("Valor", "Somatório", "Fatorial"))

for _ in range(n):
    m = int(input("Digite um valor inteiro e positivo (m): "))
    
    somatorio = sum(range(1, m + 1))
    fatorial_m = fatorial(m)
    
    print("{:<10} {:<15} {:<10}".format(m, somatorio, fatorial_m))
